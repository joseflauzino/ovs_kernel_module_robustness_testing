from util import *
import subprocess
import argparse

SCRIPTS_FOLDER = "scripts/"
DEFAULT_IGNORE_LIST = "tests_to_ignore.txt"

logger = None

def execute_pre_tests(id, file_name, gnl_family_name):
    Logger(gnl_family_name).log_request_type(id, PRE_TEST, file_name)
    script_path = SCRIPTS_FOLDER + gnl_family_name + "_pre_tests.sh"

    try:
        subprocess.run(["sudo", script_path], check=True, capture_output=True, text=True)
        print("Pre-tests successfuly executed for test case",file_name)
    except subprocess.CalledProcessError as e:
        print("Error executing pre-tests script:")
        print("Return Code:", e.returncode)
        print("Error Output:\n", e.stderr)

def execute_gnl_cmd(test_type, test_case_name, gnl_command:GenericNetlinkCommand):
    # Get Generic Netlink Family Object
    gnl_family_obj = get_family_from_name(gnl_command.gnl_family_name)

    # Execute
    command = gnl_command.command
    attrs = gnl_command.get_gnl_attrs()
    request_msg, nl_error_code, nl_error_msg, reply_msg = gnl_family_obj.send_msg(
        command, attrs)
    
    Logger(gnl_command.gnl_family_name).log_request_message(request_msg)
    Logger(gnl_command.gnl_family_name).log_results(nl_error_code, nl_error_msg, reply_msg)    

def reset_ovs_module(script_file_name="reset_ovs_kernel_module.sh"):
    """
    Run as script that disable and enable the Open vSwitch kernel module.
    """
    script_path = SCRIPTS_FOLDER + script_file_name

    try:
        subprocess.run(["sudo", script_path], check=True, capture_output=True, text=True)
        print("Open vSwitch kernel module successfully reset!\n")
    except subprocess.CalledProcessError as e:
        print("Error executing script:")
        print("Return Code:", e.returncode)
        print("Error Output:\n", e.stderr)

def main():
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional arguments
    parser.add_argument("-f", "--family", help = "Name of the Generic Netlink Family to test. Default: ovs_datapath.")
    parser.add_argument("-t", "--test-case", help = "The name of the test case YAML file to perform. If not specified, all test cases of the family are performed.")
    parser.add_argument("-i", "--ignore-test", help = "The name of a test case YAML file to ignore.")
    parser.add_argument("-I", "--ignore-list", help = "The name of .txt file containing a list of test cases to ignore. Default: tests_to_ignore.txt.")
    parser.add_argument("-r", "--reset-module", help = "Reset the kernel module (true or false). Default: true.")

    # Read arguments from command line
    args = parser.parse_args()

    # Default Generic Netlink Family to test
    gnl_family_name = "ovs_datapath"

    test_case_arg = None
    list_of_tests_to_ignore = []
    reset_module = True

    # Get arguments
    if args.family:
        gnl_family_name = args.family
    if args.test_case:
        test_case_arg = args.test_case
    if args.ignore_test:
        list_of_tests_to_ignore.append(args.ignore_test)
    else:
        with open(DEFAULT_IGNORE_LIST) as file:
            for line in file:
                list_of_tests_to_ignore.append(line.strip())
    if args.reset_module and args.reset_module.lower() == "false":
        reset_module = False

    files = find_test_cases(gnl_family_name, "./input/test_cases/")
    id = 1
    skipped_tests = 0

    for file_name in files:
        if test_case_arg is not None: # a specific test case was given
            if test_case_arg != file_name:
                skipped_tests += 1
                continue # skip the test case because it is not the requested one (via argument)
        else: # no specific test case was given, then we can check the ignore list
            if file_name in list_of_tests_to_ignore:
                skipped_tests += 1
                continue # skip the test case

        test_case = load_test_case(gnl_family_name, file_name)

        # Check if there are pre-tests
        if PRE_TEST.lower() in test_case.keys() and test_case[PRE_TEST.lower()]:
            # Execute the pre-test commands of a test case
            execute_pre_tests(id, file_name, gnl_family_name)

        # Execute test of a given test case
        print("Performing test case:",file_name)
        Logger(gnl_family_name).log_request_type(id, TEST, file_name)
        execute_gnl_cmd(TEST, file_name, GenericNetlinkCommand.from_dict(test_case["test"]))

        id+=1

        # Reset the Open vSwitch kernel module
        if reset_module:
            reset_ovs_module()
    if skipped_tests > 0:
        Logger(gnl_family_name).log_skipped_tests(skipped_tests)
    print(f"Tests completed for family {gnl_family_name}.")

if __name__ == "__main__":
    main()
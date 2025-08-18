# Source Code Documentation

> **Note:** For detailed instructions on how to reproduce the experiments in the paper, please refer to the README.md file in the ["experiments/"](experiments/) directory.

## Directory structure

The contents of this directory are organized as follows.

```
..
├── input                  # input files
    ├── rules              # Generic Netlink attribute descriptors
    ├── test_cases         # test case descriptors
├── output                 # raw data files of the results
├── scripts                # shell scripts to configure the kernel module before/after each test
├── .gitignore             # lists files that should be ignored by git
├── README.md              # (this) instructions
├── __init__.py            # defines the directory as a Python package
├── data_type_limits.py    # functions to generate values according to data type limits
├── generate_test_cases.py # utility (CLI) to generate test cases from descriptors
├── main.py                # utility (CLI) to perform test cases from descriptors
├── requeriments.txt       # Python depedencies
├── tests_to_ignore.txt    # (filenames of) test cases to ignore - use as needed
├── util.py                # useful functions
```
Next, we describe the main code files and descriptors.

## File generate_test_cases.py

This file is used to generate test cases from descriptors (YAML) files.

The `rules` directory contain the descriptors of all Generic Netlink families implemented by the Open vSwitch kernel module. Each descriptor define all available command, Netlink attributes, and their respective data types.

From this files, you can generate test cases by using the following syntax:

```
python3 generate_test_cases.py -f <family>
```

For example, for the `ovs_flow` family, you can run the following command:
```
python3 generate_test_cases.py -f ovs_flow
```

The test cases (also YAML files) will be generated in the respective `test_cases/<family>/` directory. These files are used as input by the main.py file, described below.

## File main.py

This file is used to perform the robustness tests. To list all available parameters and the syntax used, please run the following command: `sudo python3 main.py -h`.

The output is as follows:

```
usage: main.py [-h] [-f FAMILY] [-t TEST_CASE] [-i IGNORE_TEST] [-I IGNORE_LIST] [-r RESET_MODULE]

optional arguments:
  -h, --help            show this help message and exit
  -f FAMILY, --family FAMILY
                        Name of the Generic Netlink Family to test. Default: ovs_datapath.
  -t TEST_CASE, --test-case TEST_CASE
                        The name of the test case YAML file to perform. If not specified, all test cases of the family are performed.
  -i IGNORE_TEST, --ignore-test IGNORE_TEST
                        The name of a test case YAML file to ignore.
  -I IGNORE_LIST, --ignore-list IGNORE_LIST
                        The name of .txt file containing a list of test cases to ignore. Default: tests_to_ignore.txt.
  -r RESET_MODULE, --reset-module RESET_MODULE
                        Reset the kernel module after each test (true or false). Default: true.
```

Usage example:
```
sudo python3 main.py -f ovs_datapath
```
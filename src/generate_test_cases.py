import yaml
from util import *
import argparse

class GenericNetlinkFamily:
    class Attribute:
        def __init__(self, name, type, supported_by=None):
            self.name = name
            self.type = type
            self.supported_by = supported_by if supported_by is not None else []

        def __repr__(self):
            return (f"Attribute(name={self.name}, type={self.type}, "
                    f"supported_by={self.supported_by})")

    def __init__(self, name, cmd_min, cmd_max, cmd_requires_pre_test):
        self.name = name
        self.cmd_range = {"min": cmd_min, "max": cmd_max}
        self.cmd_requires_pre_test = cmd_requires_pre_test
        self.attributes = []

    def add_attribute(self, name, type, supported_by=None):
        attribute = self.Attribute(name, type, supported_by)
        self.attributes.append(attribute)

    @classmethod
    def from_yaml(cls, yaml_data):
        family_data = yaml_data.get("generic_netlink_family", {})
        name = family_data.get("name", "unknown")
        cmd_range = family_data.get("cmd_range", {})
        cmd_min = cmd_range.get("min", 0)
        cmd_max = cmd_range.get("max", 0)
        cmd_requires_pre_test = family_data.get("cmd_requires_pre_test", [])

        gnl_family = cls(name, cmd_min, cmd_max, cmd_requires_pre_test)

        for attr in family_data.get("attributes", []):
            gnl_family.add_attribute(
                attr["name"],
                attr["type"],
                attr.get("supported_by", [])
            )

        return gnl_family

    def __repr__(self):
        return (f"GenericNetlinkFamily(name={self.name}, cmd_range={self.cmd_range}, "
                f"cmd_requires_pre_test={self.cmd_requires_pre_test}, attributes={self.attributes})")

def get_supported_attrs(cmd:int, gnl_family:GenericNetlinkFamily):
    supported_attrs = []
    for attr in gnl_family.attributes:
        if cmd in attr.supported_by:
            supported_attrs.append(attr)
    return supported_attrs

def main():
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional arguments
    parser.add_argument("-f", "--family", help = "Name of the Generic Netlink Family to generate tests")

    # Read arguments from command line
    args = parser.parse_args()

     # Default Generic Netlink Family to generate test
    gnl_family_name = "ovs_datapath"

    # Get arguments
    if args.family:
        gnl_family_name = args.family

    input_file_name = gnl_family_name + ".yaml"
    full_path = 'input/rules/' + input_file_name
    try:
        with open(full_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
            gnl_family = GenericNetlinkFamily.from_yaml(yaml_data)
            min = gnl_family.cmd_range["min"]
            max = gnl_family.cmd_range["max"]
            for cmd in range(min, max + 1):
                print("Command:",cmd)
                supported_attrs = get_supported_attrs(cmd, gnl_family)
                for attr in supported_attrs:
                    print(" ",attr.name)
                    rules_list = get_rules(attr.type)
                    for rule in rules_list:
                        test_case = {}
                        if cmd in gnl_family.cmd_requires_pre_test:
                            test_case["pre_test"] = {
                                    "script_name": gnl_family.name + "_pre_tests.sh"
                                }
                        test_case["test"] = {
                                "gnl_family_name": gnl_family.name,
                                "command": cmd,
                                "gnl_atts": [{attr.name:rule}]
                            }
                        test_case_name = attr.name + "[" + rule + "]-" + "CMD[" + str(cmd) + "].yaml"
                        save_test_case(test_case, gnl_family.name, test_case_name)
                    
    except FileNotFoundError:
        print("The specified YAML file could not be found.")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")

if __name__ == "__main__":
    main()
from ovs import OvsDatapath, OvsFlow, OvsPacket, OvsVport, OvsMeter, OvsCtLimit
import lorem
import yaml
import os

PRE_TEST = "PRE_TEST"
TEST = "TEST"
POST_TEST = "POST_TEST"

def load_test_case(nl_family:str, test_case_name:str, base_path="./input/test_cases/"):
    """
        Read a robustness test case (a YAML file) and return the corresponding dictionary.
    """
    file_path = base_path + nl_family.lower() + "/" + test_case_name
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except Exception as e:
        print(f"Error reading test case file: {e}")
        return None

def save_test_case(data: dict, nl_family:str, test_case_name:str, base_path="./input/test_cases/"):
    """
        Write a dictionary in a YAML file that corresponds to a robustness test case.
    """
    file_path = base_path + nl_family.lower() + "/" + test_case_name
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False, indent=4)
        print(f"Dictionary successfully written to {file_path}")
    except Exception as e:
        print(f"Error writing YAML file: {e}")

def find_test_cases(nl_family:str, base_path="./input/test_cases/"):
    """
        Find the test cases for a given Generic Netlink Family.
        Returns a list of file names.
    """
    directory_path = base_path + nl_family + "/"
    try:
        # Get all files and directories in the given directory
        entries = os.listdir(directory_path)
        
        # Filter out directories, leaving only files
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory_path, entry))]
        
        return files
    except Exception as e:
        print(f"Error reading directory {directory_path}: {e}")
        return []

def get_family_from_name(family_name):
    if family_name == "ovs_datapath":
        return OvsDatapath()
    elif family_name == "ovs_flow":
        return OvsFlow()
    elif family_name == "ovs_packet":
        return OvsPacket()
    elif family_name == "ovs_vport":
        return OvsVport()
    elif family_name == "ovs_meter":
        return OvsMeter()
    elif family_name == "ovs_ct_limit":
        return OvsCtLimit()
    else:
        return None

def _signed_int_limits(bits):
    """
        Generate limits for signed integer types (e.g., int, short, long)
    """
    min_value = -(2 ** (bits - 1))
    max_value = 2 ** (bits - 1) - 1
    return min_value, max_value

def _unsigned_int_limits(bits):
    """
        Generate limits for unsigned integer types (e.g., unsigned int, unsigned short)
    """
    max_value = 2 ** bits - 1
    return 0, max_value

def _get_attr_name(index):
    """
        Get the attribute name based on index.
    """
    if index == 1:
        return "OVS_DP_ATTR_NAME"
    return None

def get_attr_value(attr):
    VALUE_TO_EXCEED = 1000

    if attr != None:
        # Common
        if attr == "Null":
            return None
        # Strings
        if attr == "StrEmpty":
            return ""
        if attr == "StrNonPrintable":
            return "ab\ncd\t"
        if attr == "StrNonAscii":
            return "dp-test-çáãËÆ"
        if attr == "StrOverflow":
            return lorem.paragraph()
        
        # Numbers
        if attr == "NumMinInt8": # Minimum signed 8-bit number
            return _signed_int_limits(8)[0]
        if attr == "NumMaxInt8": # Maximum signed 8-bit number
            return _signed_int_limits(8)[1]
        if attr == "NumUnderflowInt8": # Underflow for a 8-bit number
            return _signed_int_limits(8)[0] - VALUE_TO_EXCEED
        if attr == "NumOverflowInt8": # Overflow for a 8-bit number
            return _signed_int_limits(8)[1] + VALUE_TO_EXCEED
        
        if attr == "NumMinUint8": # Minimum unsigned 8-bit number
            return _unsigned_int_limits(8)[0]
        if attr == "NumMaxUint8": # Maximum unsigned 8-bit number
            return _unsigned_int_limits(8)[1]
        if attr == "NumUnderflowUint8": # Underflow for an unsigned 8-bit number
            return _unsigned_int_limits(8)[0] - VALUE_TO_EXCEED
        if attr == "NumOverflowUint8": # Overflow for an unsigned 8-bit number
            return _unsigned_int_limits(8)[1] + VALUE_TO_EXCEED
        
        if attr == "NumMinShort": # Minimum signed short (16-bit)
            return _signed_int_limits(16)[0]
        if attr == "NumMaxShort": # Maximum signed short (16-bit)
            return _signed_int_limits(16)[1]
        if attr == "NumUnderflowShort": # Underflow for a signed short (16-bit)
            return _signed_int_limits(16)[0] - VALUE_TO_EXCEED
        if attr == "NumOverflowShort": # Overflow for a signed short (16-bit)
            return _signed_int_limits(16)[1] + VALUE_TO_EXCEED
        
        if attr == "NumMinUshort": # Minimum unsigned short (16-bit)
            return _unsigned_int_limits(16)[0]
        if attr == "NumMaxUshort": # Maximum unsigned short (16-bit)
            return _unsigned_int_limits(16)[1]
        if attr == "NumUnderflowUshort": # Underflow for an unsigned short (16-bit)
            return _unsigned_int_limits(16)[0] - VALUE_TO_EXCEED
        if attr == "NumOverflowUshort": # Overflow for an unsigned short (16-bit)
            return _unsigned_int_limits(16)[1] + VALUE_TO_EXCEED

        if attr == "NumMinInt": # Minimum signed int (32-bit)
            return _signed_int_limits(32)[0]
        if attr == "NumMaxInt": # Maximum signed int (32-bit)
            return _signed_int_limits(32)[1]
        if attr == "NumUnderflowInt": # Underflow for a signed int (32-bit)
            return _signed_int_limits(32)[0] - VALUE_TO_EXCEED
        if attr == "NumOverflowInt": # Overflow for a signed int (32-bit)
            return _signed_int_limits(32)[1] + VALUE_TO_EXCEED
        
        if attr == "NumMinUint": # Minimum unsigned int (32-bit)
            return _unsigned_int_limits(32)[0]
        if attr == "NumMaxUint": # Maximum unsigned int (32-bit)
            return _unsigned_int_limits(32)[1]
        if attr == "NumUnderflowUint": # Underflow for an unsigned int (32-bit)
            return _unsigned_int_limits(32)[0] - VALUE_TO_EXCEED
        if attr == "NumOverflowUint": # Overflow for an unsigned int (32-bit)
            return _unsigned_int_limits(32)[1] + VALUE_TO_EXCEED
        
        if attr == "NumMinLong": # Minimum signed long (64-bit)
            return _signed_int_limits(64)[0]
        if attr == "NumMaxLong": # Maximum signed long (64-bit)
            return _signed_int_limits(64)[1]
        if attr == "NumUnderflowLong": # Underflow for a signed long (64-bit)
            return _signed_int_limits(64)[0] - VALUE_TO_EXCEED
        if attr == "NumOverflowLong": # Overflow for a signed long (64-bit)
            return _signed_int_limits(64)[1] + VALUE_TO_EXCEED
        
        if attr == "NumMinUlong": # Minimum unsigned long (64-bit)
            return _unsigned_int_limits(64)[0]
        if attr == "NumMaxUlong": # Maximum unsigned long (64-bit)
            return _unsigned_int_limits(64)[1]
        if attr == "NumUnderflowUlong": # Underflow for an unsigned long (64-bit)
            return _unsigned_int_limits(64)[0] - VALUE_TO_EXCEED
        if attr == "NumOverflowUlong": # Overflow for an unsigned long (64-bit)
            return _unsigned_int_limits(64)[1] + VALUE_TO_EXCEED
        
        # Objects
        if attr == "ObjEmptyCorrectClass":
            return None #TODO: generate an empty object with correct class 
        if attr == "ObjPrimitive":
            return int(100) # return an integer
        if attr == "ObjCommon":
            return list() # return a List as a common data type
    # It is not a keyword, so just return the value of attr 
    return attr

def get_command(value:list):
    cmd = None
    try:
        cmd = int(value)
    except:
        cmd = get_attr_value(value)
    return cmd

def isValid(test_case):
    return True

def get_rules(attr_type):
    rules_list = ["Null"]

    if attr_type == "string":
        rules_list.append("StrEmpty")
        rules_list.append("StrNonPrintable")
        rules_list.append("StrNonAscii")
        rules_list.append("StrOverflow")
    
    elif attr_type == "int8":
        rules_list.append("NumMinInt8") # NumMinType
        rules_list.append("NumMaxInt8") # NumMaxType
        rules_list.append("NumUnderflowInt8") # NumUnderflow
        rules_list.append("NumOverflowInt8") # NumOverflow
    elif attr_type == "uint8":
        rules_list.append("NumMinUint8") # NumMinType
        rules_list.append("NumMaxUint8") # NumMaxType
        rules_list.append("NumUnderflowUint8") # NumUnderflow
        rules_list.append("NumOverflowUint8") # NumOverflow
    elif attr_type == "short":
        rules_list.append("NumMinShort") # NumMinType
        rules_list.append("NumMaxShort") # NumMaxType
        rules_list.append("NumUnderflowShort") # NumUnderflow
        rules_list.append("NumOverflowShort") # NumOverflow
    elif attr_type == "ushort":
        rules_list.append("NumMinUshort") # NumMinType
        rules_list.append("NumMaxUshort") # NumMaxType
        rules_list.append("NumUnderflowUshort") # NumUnderflow
        rules_list.append("NumOverflowUshort") # NumOverflow
    elif attr_type == "int":
        rules_list.append("NumMinInt") # NumMinType
        rules_list.append("NumMaxInt") # NumMaxType
        rules_list.append("NumUnderflowInt") # NumUnderflow
        rules_list.append("NumOverflowInt") # NumOverflow
    elif attr_type == "uint":
        rules_list.append("NumMinUint") # NumMinType
        rules_list.append("NumMaxUint") # NumMaxType
        rules_list.append("NumUnderflowUint") # NumUnderflow
        rules_list.append("NumOverflowUint") # NumOverflow
    elif attr_type == "long":
        rules_list.append("NumMinLong") # NumMinType
        rules_list.append("NumMaxLong") # NumMaxType
        rules_list.append("NumUnderflowLong") # NumUnderflow
        rules_list.append("NumOverflowLong") # NumOverflow
    elif attr_type == "ulong":
        rules_list.append("NumMinUlong") # NumMinType
        rules_list.append("NumMaxUlong") # NumMaxType
        rules_list.append("NumUnderflowUlong") # NumUnderflow
        rules_list.append("NumOverflowUlong") # NumOverflow

    elif attr_type == "object":
        rules_list.append("ObjPrimitive")
        rules_list.append("ObjCommon")

    return rules_list

class Logger:
    def __init__(self, family, output_dir="output/", format="txt"):
        self.file_name = output_dir + family + "_log" + "." + format
        # Ensure the file exists and is ready for writing
        with open(self.file_name, "a") as file:
            pass  # Just create the file if it doesn't exist

    def _write_to_file(self, message:str):
        with open(self.file_name, "a") as file:
            file.write(message)

    def log_request_type(self, id, test_type, test_case):
        self._write_to_file("\n\nID: "+str(id)+" === Executing "+ test_type + " of the test case: "+ test_case +"===\n")

    def log_request_message(self, message_obj):
        self._write_to_file("\nMessage sent: "+ str(message_obj))

    def log_results(self, nl_error_code, nl_error_msg, reply_msg):
        """
        Logs the results of a test into a file.
        """

        with open(self.file_name, "a") as file:
            file.write("\n"+"Netlink Error Code: "+str(nl_error_code)+"\n")
            file.write("Netlink Error Message: "+str(nl_error_msg)+"\n")
            file.write("Reply Message: "+str(reply_msg)+"\n")

    def log_skipped_tests(self, number_of_tests):
        self._write_to_file("\n\n"+str(number_of_tests)+" skipped.\n")

class GenericNetlinkCommand:
    def __init__(self, **kwargs):
        # Define the expected fields
        self.expected_fields = {"gnl_family_name", "command", "gnl_atts"}
        
        # Validate the input fields
        for key in kwargs:
            if key not in self.expected_fields:
                raise ValueError(f"Unexpected field: {key}")
        
        # Set attributes for each expected field
        for field in self.expected_fields:
            setattr(self, field, kwargs.get(field, None))

    @classmethod
    def from_dict(cls, data: dict):
        if not isinstance(data, dict):
            raise TypeError("Input data must be a dictionary.")
        return cls(**data)

    def to_dict(self):
        return {field: getattr(self, field) for field in self.expected_fields}
    
    def get_gnl_attrs(self):
        attr_list = []
        if self.gnl_atts and self.gnl_atts != None:
            for attr in self.gnl_atts:
                attr_keys = list(attr.keys())
                key = attr_keys[0]
                value = attr[key]
                attr_list.append([key, get_attr_value(value)])
        return attr_list
    

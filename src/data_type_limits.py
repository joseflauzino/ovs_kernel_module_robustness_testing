# Generate limits for signed integer types (e.g., int, short, long)
def signed_int_limits(bits):
    min_value = -(2 ** (bits - 1))
    max_value = 2 ** (bits - 1) - 1
    return min_value, max_value

# Generate limits for unsigned integer types (e.g., unsigned int, unsigned short)
def unsigned_int_limits(bits):
    max_value = 2 ** bits - 1
    return 0, max_value

# Generate limits for signed int (32-bit)
signed_int_32 = signed_int_limits(32)
print(f"Signed int (32-bit): Min = {signed_int_32[0]}, Max = {signed_int_32[1]}")

# Generate limits for unsigned int (32-bit)
unsigned_int_32 = unsigned_int_limits(32)
print(f"Unsigned int (32-bit): Min = {unsigned_int_32[0]}, Max = {unsigned_int_32[1]}")

# Generate limits for signed short (16-bit)
signed_short_16 = signed_int_limits(16)
print(f"Signed short (16-bit): Min = {signed_short_16[0]}, Max = {signed_short_16[1]}")

# Generate limits for unsigned short (16-bit)
unsigned_short_16 = unsigned_int_limits(16)
print(f"Unsigned short (16-bit): Min = {unsigned_short_16[0]}, Max = {unsigned_short_16[1]}")

# Generate limits for signed long (64-bit, assuming 64-bit long)
signed_long_64 = signed_int_limits(64)
print(f"Signed long (64-bit): Min = {signed_long_64[0]}, Max = {signed_long_64[1]}")

# Generate limits for unsigned long (64-bit, assuming 64-bit unsigned long)
unsigned_long_64 = unsigned_int_limits(64)
print(f"Unsigned long (64-bit): Min = {unsigned_long_64[0]}, Max = {unsigned_long_64[1]}")

# Limits for char (8-bit signed)
char_8 = signed_int_limits(8)
print(f"Signed char (8-bit): Min = {char_8[0]}, Max = {char_8[1]}")

# Limits for unsigned char (8-bit)
unsigned_char_8 = unsigned_int_limits(8)
print(f"Unsigned char (8-bit): Min = {unsigned_char_8[0]}, Max = {unsigned_char_8[1]}")

# Limits for float (32-bit, IEEE 754 standard)
import math
print(f"Float (32-bit): Min = {-math.pow(2, 128)}, Max = {math.pow(2, 128) - 1}, Precision ~ 7 digits")

# Limits for double (64-bit, IEEE 754 standard)
print(f"Double (64-bit): Min = {-math.pow(2, 1024)}, Max = {math.pow(2, 1024) - 1}, Precision ~ 15 digits")

"""exercise 2 week 2 on signle precision rapresentation"""
# Write a function that converts a 32 bit word into a single precision
# floating point (i.e. interprets the various bits as sign, mantissa and
# exponent)

hex_bin_conversion = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111",
}


def hex_to_bin(x):
    "convertion from hexadeciaml to binary integers"
    bin_number = ""
    for i in x:
        bin_number += hex_bin_conversion[i]
    return bin_number


def bin_to_dec(x):
    """convertion from binary to decimal rapresentation"""
    s = str(x)
    number = 0
    count = 0
    for i in reversed(s.lower()):
        a = int(i)
        number += pow(2, count) * a
        count += 1
    return number


to_convert = input(
    "insert the value in binary or hexadecimal rapresantation to convert: ")

# check if in hex, in this case go to binary
if len(to_convert) == 8:
    to_convert = hex_to_bin(to_convert)

# compute the exponent
exp_bin = to_convert[1:9]
print("exponential binary: ", exp_bin)
exp = bin_to_dec(exp_bin)
print("exponential decimal: ", exp)

# computer the mantissa
mantissa_bin = to_convert[9:len(to_convert)]
print("mantissa binary: ", mantissa_bin)
decimal_part = 1
count = 1
for i in mantissa_bin:
    i = int(i)
    decimal_part += pow(2, (-1) * count) * i
    count += 1
print("mantissa decimal: ", decimal_part)

print("value: ",
      pow(-1, int(to_convert[0])) * decimal_part * pow(2, exp - 127))

"""exercise 1 week 2"""
# Write a function that converts number representation (bin<->dec<->hex)

# conversion from bin to dec done
# conversion from hex to dec
# conversion from dec to bin
# conversion from hex to bin

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

hex_dec_conversion = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
}

dec_hex_conversion = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
}


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


def dec_to_bin(x):
    """convertion from decimal to binary rapresentation"""
    number = int(x)
    s = ""
    while number >= 1:
        s += str(number % 2)
        number = number // 2
    return s[::-1]


def hex_to_bin(x):
    "convertion from hexadeciaml to binary integers"
    bin_number = ""
    for i in x:
        bin_number += hex_bin_conversion[i]
    # erase first 0 characters to be coherent with binary notation
    count = 0
    for i in bin_number:
        if i == "1":
            break
        count += 1
    temp = ""
    for i in range(count, len(bin_number)):
        temp += bin_number[i]
    return temp


def hex_to_dec(x):
    """convert an hexadecimal to decimal number"""
    s = str(x)
    number = 0
    count = 0
    for i in reversed(s.lower()):
        number += hex_dec_conversion[i] * pow(16, count)
        count += 1
    return number


def dec_to_hex(x):
    """convert decimal to hexadecimal number"""
    number = int(x)
    s = ""
    while number > 0:
        s += dec_hex_conversion[number % 16]
        number = number // 16
    return s[::-1]


print("Would you like to convert a decimal a binary or an hexagesimal number?")
type_of_number = input("Type dec/bin/hex: ")
number_to_convert = input("what number do you want to convert? ")

if type_of_number == "bin":
    print("decimal: ", bin_to_dec(number_to_convert))
    print("binary: ", number_to_convert)
    print("hexadecimal: ", dec_to_hex(bin_to_dec(number_to_convert)))

if type_of_number == "dec":
    print("decimal: ", number_to_convert)
    print("binary: ", dec_to_bin(number_to_convert))
    print("hexadecimal: ", dec_to_hex(number_to_convert))

if type_of_number == "hex":
    print("decimal: ", hex_to_dec(number_to_convert))
    print("binary: ", hex_to_bin(number_to_convert))
    print("hexadecimal: ", number_to_convert)

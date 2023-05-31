import re

from bitstring import BitArray


def logical_xor(s, a):
    print(f"{s} ^ {a} = {s ^ a}")


def left_shift(s, d):
    print(f"{s} ^ {d} = {s << d}\n" + "{0:b}".format(s << d))


def is_number(s: str):
    regex = re.compile(r"^([+-]?[1-9]\d*|0)$")
    if re.fullmatch(regex, s) is None:
        return False
    return True


def is_hex(s: str):
    s_split = s.split("0x")
    if len(s_split) > 1:
        return True
    return False


def is_binary(s: str):
    if len(s.split("0b")) > 1:
        return True
    return False


def to_uint(s: str):
    if is_hex(s):
        print(f"Uint: {int(s, 16)}")
    if is_binary(s):
        b = BitArray(bin=s)
        print(f"Uint: {b.uint}")
    if is_number(s):
        scale = 10
        res = bin(int(s, scale))[2:]
        b = BitArray(bin=res)
        print(f"Uint: {b.uint}")


def to_ascii(s: str):
    pass


def to_int(s: str):
    if is_hex(s):

        print(f"Int: {int(s, 16)}")
    if is_binary(s):
        b = BitArray(bin=s)
        print(f"Int: {b.int}")
    if is_number(s):
        scale = 10
        res = bin(int(s, scale))[2:]
        b = BitArray(bin=res)
        print(f"Int: {b.int}")


def to_hex(s: str):
    if is_binary(s):
        print(f"Hex: {hex(int(s, 2))}")
    if is_number(s):
        print(f"Hex: {hex(int(s, 10))}")


def to_bin(s: str):
    if is_hex(s):
        s = s.split("0x")[1]
        num_of_bits = 4 * len(s)
        print(f"Binary: {bin(int(s, 16))[2:].zfill(num_of_bits)}")
        print(f"num_bits: {num_of_bits}")
    elif is_number(s):
        res = bin(int(s, 10))[2:]
        print(f"Binary: {res}")
        print(f"num_bits: {len(res)}")


def decode(s: str):
    if is_hex(s):
        print('From Hex:')
        to_bin(s)
        to_int(s)
        to_uint(s)
        print("\n")
    if is_binary(s):
        print('From Binary:')
        to_uint(s)
        to_int(s)
        to_ascii(s)
        to_hex(s)
        print("\n")
    if is_number(s):
        print('From Number:')
        to_bin(s)
        to_hex(s)
        to_int(s)
        to_uint(s)
        print("\n")


if __name__ == '__main__':
    while True:
        inp = input("Enter a string to convert: ")
        decode(inp.strip())

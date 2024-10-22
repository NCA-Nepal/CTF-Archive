import binascii

flag = open('flag.txt').read()

def encode_base_777(string):
    base = 777
    encoded_value = 0

    for char in string:
        encoded_value = encoded_value * 256 + ord(char)

    encoded_string = ""
    while encoded_value > 0:
        encoded_string = chr(encoded_value % base) + encoded_string
        encoded_value //= base

    return encoded_string

encoded_string = encode_base_777(flag)
hex_encoded = binascii.hexlify(encoded_string.encode())

with open('output.txt', 'wb') as f:
    f.write(hex_encoded)

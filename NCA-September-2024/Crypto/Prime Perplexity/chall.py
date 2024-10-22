#!/bin/python3

from Crypto.Util.number import *
from sympy.ntheory import nextprime
from random import randint
from tqdm import tqdm
from Crypto.PublicKey import RSA

e = 65537
p = getPrime(1024)
q = nextprime(p)

iterations = randint(2, 2**12)

for _ in tqdm(range(iterations), desc="Finding Prime Number For Encryption"):
    q = nextprime(q)

n = p * q 
key = RSA.construct((n, e)).export_key().decode()

# Write N and E values to the pubkey file
with open("pubkey", "w") as pubkey:
    pubkey.write(key)

msg = bytes_to_long(b'nca{REDUCTED}')
cipher = pow(msg, e, n)

# Write the values to the message.txt file
with open('message.txt', 'w') as message:
    message.write(f'cipher={str(cipher)}')

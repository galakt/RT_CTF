#!/usr/bin/env python3
import os, binascii, struct
from Crypto.Cipher import AES

pad = lambda m: m + bytes([16 - len(m) % 16] * (16 - len(m) % 16))
def haggis(m):
    crypt0r = AES.new(bytes(0x10), AES.MODE_CBC, bytes(0x10))
    return crypt0r.encrypt(len(m).to_bytes(0x10, 'big') + pad(m))[-0x10:]

#print(bytes(0x10)) # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
target = os.urandom(0x10)
print(target)

a = binascii.b2a_hex(target)
#print(a)

#b = binascii.unhexlify(a)
# b = binascii.a2b_hex(a)
#print(b)


print(haggis(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'))
print('finished')
# msg = binascii.unhexlify(input())

# if msg.startswith(b'I solemnly swear that I am up to no good.\0') \
#         and haggis(msg) == target:
#     print(open('flag.txt', 'r').read().strip())
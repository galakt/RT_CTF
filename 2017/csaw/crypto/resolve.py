import hashlib
import string
import sys

def xor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

plaintext = 'hello'
plain_md5 = hashlib.md5(plaintext).hexdigest()
plain_md5_hex = plain_md5.encode('hex')

plaintext_len = len(plaintext)
plain_md5_len = len(plain_md5)
plain_md5_hex_len = len(plain_md5_hex)
print ('end')

f = open('encrypted', 'r')
cipher_hex = f.read().strip('\n')
cipher_hex_len = len(cipher_hex)

ciphet_unhex = cipher_hex.decode('hex')
ciphet_unhex_len = len(ciphet_unhex)

known_part = 'flag{'
key = ''

for i in range(0, len(known_part)):
    for c in string.printable:
        if (xor(c,ciphet_unhex[i]) == known_part[i]):
            key += c
            break

test = xor(known_part, key)
key = 'A qua'
test2 = xor(ciphet_unhex, key)
print ('end2')
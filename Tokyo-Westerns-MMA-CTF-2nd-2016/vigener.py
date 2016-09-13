# Python 3 Source Code
import string
import base64
from base64 import b64encode, b64decode
import sys
import os
import random
import functools
import math
import itertools
import fractions

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/'
crypted_base64 = 'a7TFeCShtf94+t5quSA5ZBn4+3tqLTl0EvoMsNxeeCm50Xoet+1fvy821r6Fe4fpeAw1ZB+as3Tphe8xZXQ/s3tbJy8BDzX4vN5svYqIZ96rt35dKuz0DfCPf4nfKe300fM9utiauTe5tgs5utLpLTh0FzYx0O1sJYKgJvul0OfiuTl00BCks+aaJZm8Kwb4u+LtLCqbZ96lv3bieCahtegx+7nzqyO6YCb4b9LovCELZ9Pe0L5rLSaBDzXaftxseAw1JzCF0MGjeCacKb69u9TlgCudZT6Os3ojhcWxD914vNHfeCuaJvH4s4aarBKlGdsT8G4UKZhfJB+y0LbjqCOnZT6baF1WiZeNtfsNtuoo+c=='
message = 'TWCTF{'
key0 = 'rCQcv+5m'
key = 'rCQcv+5m'

# Kasiski test
def kasiski_test(s, l):
    dists = []
    for i in range(len(s) - l):
        word = s[i : i+l]
        j = s[i + l : ].find(word)
        if j != -1:
            dist = (i+l+j) - i
            dists += [ dist ]
    dist = functools.reduce(fractions.gcd, dists)
    return dist


def bruteforce(charset, minlength, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(minlength, maxlength + 1)))


def shift(char, key, rev = False):
    if not char in chars:
        return char
    if rev:
        return chars[(chars.index(char) - chars.index(key)) % len(chars)]
    else:
        return chars[(chars.index(char) + chars.index(key)) % len(chars)]


def encrypt(message, key):
    encrypted = b64encode(message.encode('ascii')).decode('ascii')
    return ''.join([shift(encrypted[i], key[i % len(key)]) for i in range(len(encrypted))])

def decrypt(encrypted, key):
    return base64.b64decode(''.join([shift(c, key[i % len(key)], True) for i, c in enumerate(encrypted)]))
# def decrypt(encrypted, key):
#     encrypted = ''.join([shift(encrypted[i], key[i % len(key)], True) for i in range(len(encrypted))])
#     return b64decode(encrypted.encode('ascii')).decode('ascii')


def generate_random_key(length = 5):
    return ''.join(map(lambda a : chars[a % len(chars)], os.urandom(length)))

print (sys.version)
print(crypted_base64)
dist = kasiski_test(crypted_base64, 3) 
print(dist)

isascii = lambda s: all([ c < 128 for c in s ])
chunk = lambda s, l: [s[i:i+l] for i in range(0, len(s), l)]

def is_valid_key_block(key, k, restrict=3):
    key += 'A' * (4 - len(key))
    plaintext = decrypt(crypted_base64, key)
    for s in chunk(plaintext, 3)[ k :: dist // 4]:
        if not isascii(s[ : restrict]):
            return False
    return True

# for k in range(dist // 4):
#     for i in bruteforce(chars, 4, 4):

for k in range(dist // 4):
    for x in chars:
        for y in chars:
            if not is_valid_key_block(x + y, k, restrict=1):
                continue
            for z in chars:
                if not is_valid_key_block(x + y + z, k, restrict=2):
                    continue
                for w in chars:
                    if is_valid_key_block(x + y + z + w, k):
                        key = x + y + z + w
                        plaintext = decrypt(crypted_base64, key)
                        print('%s %s %s' % (k, key, b'  '.join(chunk(plaintext, 3)[ k :: dist // 4])))

key = 'shA6I8HUXLFY'
print(key)
print(decrypt(crypted_base64, key))


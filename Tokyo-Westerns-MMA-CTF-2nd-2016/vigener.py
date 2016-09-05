# Python 3 Source Code
import string
from base64 import b64encode, b64decode
import sys
import os
import random

import itertools

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/'
crypted_base64 = 'a7TFeCShtf94+t5quSA5ZBn4+3tqLTl0EvoMsNxeeCm50Xoet+1fvy821r6Fe4fpeAw1ZB+as3Tphe8xZXQ/s3tbJy8BDzX4vN5svYqIZ96rt35dKuz0DfCPf4nfKe300fM9utiauTe5tgs5utLpLTh0FzYx0O1sJYKgJvul0OfiuTl00BCks+aaJZm8Kwb4u+LtLCqbZ96lv3bieCahtegx+7nzqyO6YCb4b9LovCELZ9Pe0L5rLSaBDzXaftxseAw1JzCF0MGjeCacKb69u9TlgCudZT6Os3ojhcWxD914vNHfeCuaJvH4s4aarBKlGdsT8G4UKZhfJB+y0LbjqCOnZT6baF1WiZeNtfsNtuoo+c=='
message = 'TWCTF{'
key0 = 'rCQcv+5m'
key = 'rCQcv+5m'


def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(6, maxlength + 1)))


def try_guess_vi_key():
    for attempt in bruteforce(chars, 6):
        attempt = key + attempt
        try:
            decrypted_by_attempt = decrypt(crypted_base64, attempt)
            print('OUU SHIT!')
            print(attempt)
            print(decrypted_by_attempt)
        except:
            a=1


def look_for_key():
    for attempt in bruteforce(chars, 1):
        attempt = key + attempt
        crypted_by_attempt = encrypt(message, attempt)
        print(crypted_by_attempt)
        if crypted_by_attempt.startswith('a7TFeCSh'):
            print('OK!')
            print(attempt)
            print(crypted_by_attempt)
            break
        #if len(attempt) <= 5:
        #    continue
        # print(len(attempt))
        # if crypt(attempt) == etalon:
        #     print('found!')
        #     print(attempt)
        #     break


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
    encrypted = ''.join([shift(encrypted[i], key[i % len(key)], True) for i in range(len(encrypted))])
    return b64decode(encrypted.encode('ascii')).decode('ascii')


def generate_random_key(length = 5):
    return ''.join(map(lambda a : chars[a % len(chars)], os.urandom(length)))

try_guess_vi_key()
#print(encrypt(message, key))
#print(decrypt('a7TFeCSh', key))

#print(len(crypted_base64)) #368
#look_for_key()
#print('\n')
#print(decrypt('a7TFeCSh', key))
#key 5-14

##print(random.randint(5,14))


# if len(sys.argv) == 4 and sys.argv[1] == 'encrypt':
#     f = open(sys.argv[3])
#     plain = f.read()
#     f.close()
#
#     key = generate_random_key(random.randint(5,14))
#
#     print(encrypt(plain, key))
#
#     f = open(sys.argv[2], 'w')
#     f.write(key)
#     f.close()
#
# elif len(sys.argv) == 4 and sys.argv[1] == 'decrypt':
#     f = open(sys.argv[3])
#     encrypted = f.read()
#     f.close()
#
#     f = open(sys.argv[2])
#     key = f.read()
#     f.close()
#
#     print(decrypt(encrypted, key), end = '')
#
# else:
#     print("Usage: python %s encrypt|decrypt (key-file) (input-file)" % sys.argv[0])

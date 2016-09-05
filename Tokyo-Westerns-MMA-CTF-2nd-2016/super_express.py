#!/usr/bin/env python3
import string
import sys
import itertools

cool_key = '0B1i'

flag = 'TWCTF{}'
etalon = '805eed80cbbcf9'
crypted = ['80', '5e', 'ed', '80', 'cb', 'bc', 'cb', '94', 'c3', '64', '13', '27', '57', '80', 'ec', '94', 'a8', '57', 'df', 'ec', '8d', 'a8',
           'ca', '94', 'a8', 'c3', '13', 'a8', 'cc', 'f9']


def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))


def crypt(key):
    if len(key) % 2 == 1:
        print("Key Length Error")
        sys.exit(1)

    n = len(key) // 2
    encrypted = ''
    for c in flag:
        c = ord(c)
        for a, b in zip(key[0:n], key[n:2*n]):
            c = (ord(a) * c + ord(b)) % 251
        encrypted += '%02x' % c
    return encrypted


def look_for_key():
    for attempt in bruteforce(string.printable, 6):
        if len(attempt) % 2 == 1:
            continue
        print(len(attempt))
        if crypt(attempt) == etalon:
            print('found!')
            print(attempt)
            break



def try_decrypt():
    result = ' '
    for i in crypted:
        print(i)
        for c in string.printable:
            hc = c
            n = len(cool_key) // 2
            encrypted = ''
            c = ord(c)
            for a, b in zip(cool_key[0:n], cool_key[n:2 * n]):
                c = (ord(a) * c + ord(b)) % 251
            encrypted += '%02x' % c
            if(encrypted == i):
                result = result + hc
                break
    print(result)


#print("finished")

try_decrypt()

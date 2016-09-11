import pwn
import itertools
import string
import hashlib
import sympy # perfect_power
from Crypto.Util.number import isPrime


#import Crypto.Util as Cr
#import isPrime from Crypto.Util.number

r = pwn.remote('secuprim.asis-ctf.ir',42738)

print(r.recvline())
print(r.recvline())
bot_task = r.recvline()
print(bot_task)
print(r.recvline())

def bruteforce(charset, minlength, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(minlength, maxlength + 1)))

key_part_2 = bot_task[12:34]
print('part2=')
print(key_part_2)

sha_key = bot_task[52:84]
print('sha_key_starts with')
print(sha_key)

ans = ''
for i in bruteforce(string.ascii_letters, 4,4):
    if(hashlib.sha256('%s%s'%(i,key_part_2)).hexdigest().startswith(sha_key)):
        ans = i
        print('FOUND')
        break

r.sendline(ans)
print(r.recvline())
print(r.recvline())

def get_primes_and_pp(number_from, number_to):
    result = 0
    print('======================================')
    print(number_from)
    print(number_to)
    print('======================================')
    while number_from <= number_to:
        if(sympy.perfect_power(number_from)):
            result += 1
        if(isPrime(number_from)):
            result += 1
        number_from += 1
    return result

while True:
    print(r.recvline())
    task = r.recvline()
    print(task)
    num1=long(task.split(' ')[12])
    num2=long(task.split(' ')[16])
    res = str(get_primes_and_pp(num1, num2))
    print('RESULT FOUND %s'%(res))
    r.sendline(res)
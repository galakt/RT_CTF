import hashlib
import pwn
import itertools
import string

def solve():
    r = pwn.remote('shopping.ctf.site', 21111)
    #while True:
    l = r.recvline().strip('\n')
    print(l)
    if(l.startswith('Enter a raw string (max. 32 bytes) that meets the following condition: hex(sha1(input))[0:6] ==')):
        hexedval = l.replace('Enter a raw string (max. 32 bytes) that meets the following condition: hex(sha1(input))[0:6] == ', '')
        payload = brute_sha1hex(hexedval)
        print ('Found payload={}'.format(payload))
        r.writeline(payload)
    r.interactive()

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

def brute_sha1hex(startdigits):
    for attempt in bruteforce(string.printable, 6):
        sha1hex = hashlib.sha1(attempt).hexdigest()
        if(sha1hex.startswith(startdigits)):
            return attempt
    return ''

solve()
#sha1 = hashlib.sha1('1').hexdigest()
#print (sha1)
#print (sha1.encode('hex'))
#print (sha1.decode('hex'))
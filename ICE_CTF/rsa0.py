import gmpy2
from Crypto.PublicKey import RSA
#d = lambda p, q, e: int(gmpy2.invert(e, (p-1)*(q-1)))
#key = RSA.construct((n, e, d(p,q,e)))
import binascii

c=0x4963654354467b66616c6c735f61706172745f736f5f656173696c795f616e645f7265617373656d626c65645f736f5f63727564656c797d

print(binascii.unhexlify(hex(c)[2:]).decode())
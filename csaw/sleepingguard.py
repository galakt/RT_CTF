import pwn
import base64
import os

print "Started!"
r = pwn.remote("crypto.chal.csaw.io", 8000)

l1 = r.recvall(timeout = 5)
print(l1)

print('START DECODING')
decoded_str = base64.b64decode(l1)
decoded_str2 = base64.b64decode(l1[::-1])
print ('DECODE FINISHED')
# print(decoded_str)

print('CREATING FILE')
f = open('/root/Desktop/github/RT_CTF/csaw/sleeping_guard.png', 'wb')
f.write(decoded_str)
f.close()

f = open('/root/Desktop/github/RT_CTF/csaw/sleeping_guard2.png', 'wb')
f.write(decoded_str2)
f.close()
import pwn
import base64
import os

print "Started!"
r = pwn.remote("pwn.chal.csaw.io", 8001)
print(r.recvline())

print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())


print('GETTING HELP')
r.sendline('help')
print(r.recvline())
print('RECV HELP')
l2 = r.recvuntil(', \'exit\', or \'help\'.', timeout=2)
print(l2)

print('CREATING FILE')
f = open('/root/Desktop/github/RT_CTF/csaw/aui', 'wb')
f.write(l2)
f.close()
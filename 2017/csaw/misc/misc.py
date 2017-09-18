import pwn

def solve():
    r = pwn.remote('misc.chal.csaw.io',4239)
    print(r.recvline())
    result_string1 = '';
    result_string2 = '';
    while True:
        l1 = r.recvline().strip('\n')
        l2 = l1[1:10]
        parity = bit_xor(l2)
        print('InitialMessage={} WithoutStartStop={} Parity={}'.format(l1, l2, parity))
        if(parity == 0):
            l3 = l2[0:8]
            unb = pwn.unbits(l3)
            print('Parity! Without parity bit={} unb={}'.format(l3, unb))
            result_string1 = result_string1 + unb
            print(result_string1)
            result_string2 = result_string2 + l3;
            print(pwn.unbits(result_string2))
            r.writeline('1')
        else:
            r.writeline('0')

def bit_xor(x):
    result = 0
    for bit in x:
        result = result ^ int(bit)
    return result
#print(parity_brute_force(00110011001))
#print(pwn.unbits('01100110'))
solve()
#print(pwn.unbits('00110011001'[1:8]))
#print(int('00110011001'))
#print(bit_xor('10011'))

print 'Finished'


import pwn
import math, operator, shlex

def parse_bill(bill):
    bill = bill.replace(',', '')
    return int(shlex.split(bill)[0][1:]) * 100

def find_change(coins, value):
    coins = sorted(coins, reverse=True)
    coin_dict = {}
    for c in coins:
        if value % c == 0:
            coin_dict[c] = value / c
            return coin_dict
        else:
            coin_dict[c] = math.trunc(value/ float(c))
            value -= (c * coin_dict[c])

coins = [1, 5, 10, 25, 50, 100, 500, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000]

print ('Started')
r = pwn.remote("misc.chal.csaw.io", 8000)

iteration_count = 0
while True:
    iteration_count += 1
    print ('ROUND # %s'%(iteration_count))
    l1 = r.recvline(timeout=2)
    print(l1)

    amount = int(round(float(str(l1.rstrip()[1:])) * 100))
    print "Coins needed: " + str(amount)
    answer =  find_change(coins, amount)

    for coin in sorted(coins, reverse=True):
        l2 = r.recvuntil(':', timeout=2)
        print(l2)
        ans = '0'
        if(answer.has_key(coin)):
            ans = str(answer[coin])
        print(ans)
        r.sendline(ans)
    print(r.recvline(timeout = 2))
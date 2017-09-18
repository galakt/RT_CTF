import pwn
import random
import credit_card_numbers_generator as cg

def solve():
    r = pwn.remote('misc.chal.csaw.io', 8308)
    generator = random.Random()
    generator.seed()  # Seed from current time
    while True:
        l = r.recvline().strip('\n')
        print(l)
        if(l == 'I need a new Visa!'):
            r.writeline(cg.credit_card_number(generator, cg.visaPrefixList, 16, 1)[0])
            continue
        if(l == 'I need a new Discover!'):
            r.writeline(cg.credit_card_number(generator, cg.discoverPrefixList, 16, 1)[0])
            continue
        if(l == 'I need a new MasterCard!'):
            r.writeline(cg.credit_card_number(generator, cg.mastercardPrefixList, 16, 1)[0])
            continue
        if(l == 'I need a new American Express!'):
            r.writeline(cg.credit_card_number(generator, cg.amexPrefixList, 15, 1)[0])
            continue
        if(l.startswith('I need a new card that starts with')):
            numberpart = l.replace('I need a new card that starts with ','').replace('!','')
            result = ''
            if(numberpart.startswith('2')
               or numberpart.startswith('3')
               or numberpart.startswith('4')
               or numberpart.startswith('5')
               or numberpart.startswith('7')
               or numberpart.startswith('8')
               or numberpart.startswith('9')):
                result = cg.completed_number(list(numberpart), 16)
            if(numberpart.startswith('6')
               or numberpart.startswith('1')):
                result = cg.completed_number(list(numberpart), 15)
            print('NumberPart = {}, result={}'.format(numberpart, result))
            r.writeline(result)
            continue
        if(l.startswith('I need a new card which ends with')):
            numberpart = l.replace('I need a new card which ends with ', '').replace('!', '')
            if(len(numberpart) == 1):
                cards = cg.credit_card_number(generator, cg.mastercardPrefixList, 16, 100)
                card = next((x for x in cards if x.endswith(numberpart)), None)
                print('NumberPart = {}, card={}'.format(numberpart, card))
                r.writeline(card)
                continue
            while True:
                part_without_last = numberpart[0:len(numberpart)-1]
                tcard = cg.completed_number_behind(list(part_without_last), 16)
                print('NumberPart = {}, card={}'.format(numberpart, tcard))
                if(tcard.startswith('0')):
                    continue
                if(tcard.endswith(numberpart)):
                    r.writeline(tcard)
                    break
            continue
        if(l.startswith('I need to know if')):
            numberpart = l.replace('I need to know if ', '').replace(' is valid! (0 = No, 1 = Yes)', '')
            print (numberpart)
            answer = is_valid(numberpart)
            print ('NumberPart = {}, is_valid = {}'.format(numberpart, answer))
            r.writeline(answer)
            continue
        if(l == 'Thanks!'):
            continue
        if(l == 'True'):
            continue
        if(l == 'False'):
            continue
        if(l == "Hmmmmm that doesn't seem correct..."):
            continue
        raise Exception('Unknown command')

def is_valid(x):
    xlen = len(x)
    if(x.startswith('6') or x.startswith('1')):
        #if(xlen != 15):
        #    return '0'
        generated_number = cg.completed_number(list(x[0:xlen-1]), xlen)
        if(generated_number == x):
            return '1'
    else:
        #if(xlen != 16):
        #    return '0'
        generated_number = cg.completed_number(list(x[0:xlen-1]), xlen)
        if(generated_number == x):
            return '1'
    return '0'


def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """

    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )

solve()

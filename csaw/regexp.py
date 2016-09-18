import rstr, pwn, re, string

print "Started!"
r = pwn.remote("misc.chal.csaw.io", 8001)

def parse(parseInput):
    re.compile(parseInput) #try to parse to see if it is a valid RE
    retval = ""
    stack = list(parseInput)
    lastelement = ""
    while stack:
        element = stack.pop(0) #Read from front
        if element == "\\":
            element = stack.pop(0)
            element = element.replace("\\d", "0").replace("\\D", "a").replace("\\w", "a").replace("\\W", "@")
        elif element in ["?", "*"]:
            lastelement = ""
            element = ""
        elif element == ".":
            element = "a"
        elif element == "+":
            element = ""
        elif element == "{":
            arg = _consumeTo(stack, "}")
            arg = arg[:-1] #dump the }     
            arg = arg.split(",")[0] #dump the possible ,
            lastelement = lastelement * int(arg)
            element = ""
        elif element == "[":
            element = _consumeTo(stack, "]")[0] # just use the first char in set
            if element == "]": #this is the odd case of []<something>]
                _consumeTo(stack, "]") # throw rest away and use ] as first element
        elif element == "|":
            break # you get to an | an you have all you need to match
        elif element == "(":
            arg = _consumeTo(stack, ")")
            element = parse( arg[:-1] )

        retval += lastelement
        lastelement = element
    retval += lastelement #Complete the string with the last char

    return retval

def _consumeTo(stackToConsume, endElement ):
    retval = ""
    while not retval.endswith(endElement):
        retval += stackToConsume.pop(0)
    return retval

line1 = r.recvline(timeout=2)
print "INTRO: {}".format(line1)
# r.sendline(answer)
# line3 = r.recvline(timeout=2)
# print "LINE: {}".format(line3)

count = 0
looping = True;
while looping:
    count += 1
    print "ROUND # {}".format(count)
    chall = r.recvline(timeout=2).rstrip()
    print "CHALL: {}".format(chall)
    if(chall != "Irregular"):
        fix_str = chall.rstrip().replace("\\d", "0").replace("\\D", "a").replace("\\w", "a").replace("\\W", "@")
        answer = parse(fix_str)
        print "ANSWER: {}".format(answer)
        r.sendline(answer)
    else:
        looping = False;
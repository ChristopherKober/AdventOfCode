password = ['h','e','p','x','c','r','r','q']

password = ['a','b','c','d','e','f','g','h']

password = ['g','h','i','j','k','l','m','n']

password = ['g','h','j','a','a','b','c','c']

password = ['h','e','p','x','c','r','r','q']

password = ['h','e','p','x','x','z','a','a']

def incr(s):
    changedVal = False
    for i in range(len(s)):
        if changedVal:
            s[i] = 'a'
        if s[i] == 'i' or s[i] == 'o' or s[i] == 'l':
            changedVal = True
            s[i] = chr(ord(s[i])+1)
    if changedVal:
        return s

    s[-1] = chr(ord(s[-1]) + 1)
    return balance(s)


def balance(s):
    index = len(s) - 1
    while index >= 0:
        if ord(s[index]) > ord('z'):
            s[index] = 'a'
            if index > 0:
                s[index-1] = chr(ord(s[index-1]) + 1)
        index = index - 1
    return s
        


while True:
    prevprev = ''
    prev = ''
    doublePrev = ''
    hasTriple = False
    hasDouble = False
    hasSecondDouble = False
    hasBadLetters = False
    for i in password:
        if prevprev != '' and prev != '' and ord(prevprev) + 1 == ord(prev) and ord(prev) + 1 == ord(i):
            hasTriple = True
        if not hasDouble and doublePrev == i:
            hasDouble = True
            doublePrev = ''
        elif hasDouble and doublePrev == i:
            hasSecondDouble = True
            doublePrev = ''
        else:
            doublePrev = i
        if i == 'i' or i == 'o' or i == 'l':
            hasBadLetters = True
        prevprev = prev
        prev = i
    if hasTriple and hasSecondDouble and not hasBadLetters:
        break
    else:
        password = incr(password)


for i in password:
    print(i,end='')
print()

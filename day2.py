def isValid(num):
    n = str(num)
    return not n[:len(n) // 2] == n[len(n) // 2:]

def isRepeatingPattern(num):
    n = str(num)
    substr = ""
    i = 0

    while len(substr) <= len(n) // 2:
        substr += n[i]
        i += 1

        if len(substr) == len(n):
            return False
        
        r = len(n) // len(substr)
        newStr = substr * r

        if newStr == n:
            return True
    return False


res = 0
with open('input2', 'r') as f:
    i = f.readline()
    r = i.split(',')

    ranges = []
    for i in r:
        ranges.append(tuple(i.split('-')))

    for r in ranges:
        for i in range(int(r[0]), int(r[1]) + 1, 1):
            if not isValid(i) or isRepeatingPattern(i):
                res += i

#nums = [101, 11, 22, 99, 1010, 1188511885, 2222, 446446, 38593859]
#for n in nums:
#    print(f"{n} is: {isValid(n)}")

print(res)

substr = "hola"
s2 = substr * 2

print(s2)

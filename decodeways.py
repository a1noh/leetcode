string = "12330"

def numDecodings(string):
    print(string)
    dp = [0 for i in range(len(string))]

    if string[0] is not '0':
        dp[0] = 1

    for i in range(1, len(string)):
        x = int(string[i])
        y = int(string[i-1: i+1])
        if x != 0:
            dp[i] += dp[i-1]
        if 10 <= y <= 26:
            if i-2 >= 0:
                dp[i] += dp[i - 2]
            else:
                dp[i] += 1

    print(dp)
    print(dp[len(dp)-1])

numDecodings(string)








# 1 2 3 1 2


def decodeWys(string):
    l = [0 for i in range(len(string))]
    if string[0] is not '0':
        l[0] = 1
    print(string)
    for i in range(1, len(string)):
        one = int(string[i])
        two = int(string[i-1: i + 1])
        print(one, two)
        if one is not 0:
            l[i] += l[i-1]
        if 10 <= two <= 26:
            if i-2 >= 0:
                l[i] += l[i-2]
            else:
                l[i] += 1
    print(l)
    print(l[len(l)-1])

#decodeWys("12312")

def fibo(n):
    l = [0, 1]
    if n == 1:
        return 0
    count = 2
    while count < n:
        temp = l[0]
        l[0] = l[1]
        l[1] = temp + l[0]
        count+=1

    return l[-1]
# 0 1 1 2 3
print(fibo(5))

# 1 2 3 1 2 1
# 1 2 3 3 6
def decodeWays(string):
    sum = 0


string = "12312"

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
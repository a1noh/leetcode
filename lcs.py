# Python3 implementation of Finding
# Length of Longest Common Substring

# Returns length of longest common
# substring of X[0..m-1] and Y[0..n-1]


def LCSubStr(X, Y, m, n):

    # LCSuff is the table with zero
    # value initially in each cell
    LCSuff = [[0 for k in range(n + 1)] for l in range(m + 1)]

    # To store the length of
    # longest common substring
    result = 0

    # Following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    s = ""
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i - 1] == Y[j - 1]):
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                if LCSuff[i][j] > result:
                    result = LCSuff[i][j]
                    s = X[i-result:i]
            else:
                LCSuff[i][j] = 0
    print(s)

    return result


# Driver Code
X = 'Austin'
Y = 'Ausnoht'

m = len(X)
n = len(Y)

print('Length of Longest Common Substring is',
      LCSubStr(X, Y, m, n))
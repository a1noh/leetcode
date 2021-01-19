
def numSteps(s):
    s, res = int(s, 2), 0
   # print(s)
    while s != 0:
        print(s)
        if s & 1:
            s = s - 1
        else:
            s = s >> 1
        res += 1
    print(res)

numSteps("1011")

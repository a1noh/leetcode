

f = open("sample_input2.txt", "r")

T = f.readline()


def runCombinations(s):
    # find length of char array
    l = len(s);
    combis = []
    for i in range(pow(2, l - 1)):

        k = i
        x = 0

        comb = []
        temp = ""
        temp += s[x]

        x += 1

        for j in range(len(s) - 1):
            if (k & 1):
                comb.append(temp)
                temp = ""
            k = k >> 1

            temp += s[x]
            x += 1

        comb.append(temp)
        temp = ""
        if (len(comb) != 1):
            mult = 1
            for i in comb:
                mult *= int(i)

            combis.append(str(mult))


    #print(combis)
    return combis


def dfs(num, depth, depthList):
    num = str(num)
    l = runCombinations(num)
    if depth > depthList[0]:
        depthList.pop()
        depthList.append(depth)
    depth += 1

    for i in l:
        if len(i) ==0:
            break
        dfs(i, depth, depthList)

    return depthList


for test in range(1,int(T)+1):               # 6 79 243
    num = f.readline()
    l = [0]
    #ans =dfs(int(num),0,l)
    #print(ans)







l = [0]
print(runCombinations("99999"))

l =dfs("99999", 0, l)
print(l)
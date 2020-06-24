x=input()
l = input()
l.strip()
l = list(map(int, l.split(" ")))

twosum = 0
numofcards = len(l)
i = 0
while (len(l)!=0):
    twosum = l[0] + l[1]
    if twosum % 2 == 0:
        l.pop(0)
        l.pop(0)
        numofcards-=2
    else:
        l.pop(0)

print(numofcards)

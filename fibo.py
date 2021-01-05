def fibo(n):
    l = [0, 1]
    count = 2
    if n == 1:
        print(0)
    while count < len(range(n)):
        temp = l[0]
        l[0] = l[1]
        l[1] = l[0] + temp
        count+=1
    print(l[1])

fibo(6)
# 0 1 1 2 3 5
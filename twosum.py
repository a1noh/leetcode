def twosum(nums, target):
    d = {}
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in d:
            print(i, d[temp])
        else:
            d[nums[i]] = i

twosum([2,7,11,15],9)
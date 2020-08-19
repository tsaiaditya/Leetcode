def func(nums):
    d = {i:0 for i in nums}
    for i,j in enumerate(nums):
        # print(i,j)
        # d[j] += 1
        if d[j]:
            nums.pop(i)
            continue
        else:
            d[j]=1
    print(nums)
    return len(nums)

print(func(nums=[0,0,1,1,1,2,2,3,3,4]))
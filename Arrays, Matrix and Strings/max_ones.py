'''
Returns maximum contiguous count of 1's in a given array
'''
def maxcount(nums):
    counts = []
    count = 0
    for i in nums:
        if(i == 1):
            count = count + 1
        else:
            counts.append(count)
            count = 0
    counts.append(count)
    return max(counts)

nums = list(map(int,input().split(',')))
print(maxcount(nums))
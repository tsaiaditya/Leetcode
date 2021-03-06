'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
#using dictionary
class Solution:
    def twoSum(self, numbers, target):
        dic = {}
        for i,n in enumerate(numbers):
            if n in dic:
                return [dic[n], i]
            dic[target-n] = i

s = Solution()
print(s.twoSum([2,7,11,15],9))
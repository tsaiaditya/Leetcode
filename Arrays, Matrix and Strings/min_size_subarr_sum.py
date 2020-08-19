import collections
class Solution:
    def minSubArrayLen(self, s, nums):
        q = collections.deque()
        dist = float("inf")
        if(len(nums) == 0):
            return 0
        for i in range(len(nums)):
            while(sum(q)>=s):
                dist = min(len(q),dist)
                q.popleft()
            q.append(nums[i])
        while(sum(q)>=s):
            dist = min(len(q),dist)
            q.popleft()
        
        return 0 if dist == float("inf") else dist

s = Solution()
print(s.minSubArrayLen(7,[2,3,1,2,4,3]))
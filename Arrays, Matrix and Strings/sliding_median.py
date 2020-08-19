import numpy as np
import collections
class Solution:
    def medianSlidingWindow(self, nums, k):
        temp = collections.deque()
        med = []
        for i in nums:
            if len(temp)<k:
                temp.append(i)
            else:
                med.append('%.5f'%np.median(temp))
                temp.popleft()
                temp.append(i)
        if temp:
            med.append('%.5f'%np.median(temp))
        return med

s = Solution()
print(s.medianSlidingWindow([1,3,-1,-3,5,3,6],3))
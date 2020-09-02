'''
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        queue,ans,fin = [],[],[]
        for i in nums:
            if len(queue) == 0:
                queue.append(i)
            else:
                if max(queue)<i and i-max(queue) == 1:
                    queue.append(i)
                else:
                    ans.append(queue)
                    queue = [i]
        ans.append(queue)
        for i in ans:
            if len(i) == 1:
                fin.append(str(i[0]))
            else:
                fin.append(str(i[0])+"->"+str(i[len(i)-1]))
        return fin
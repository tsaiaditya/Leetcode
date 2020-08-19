'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
'''
class Solution:
    def candy(self, r):
        s = 0  
        c = 0  
        last_peak = 0  
        for i, x in enumerate(r):
            if i == 0:
                c = 1
            elif r[i] > r[i-1]:  
                if c < 0:
                    c = 2
                else:
                    c += 1
            elif r[i] == r[i-1]:  
                c = 1
            else:  
                if c > 0:
                    last_peak = c
                    c = -1
                else:
                    c -= 1
                if -c >= last_peak:
                    s += 1
            s += abs(c)
            print(f'{r[i]=}, {c=:+d}, {last_peak=}, {s=}') # only supported in python 3.8, use py candy.py for compiling....
        return s

x = Solution()
print(x.candy([1,2,0,3,4,8,2]))
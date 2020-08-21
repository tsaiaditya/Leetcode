'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:

1 <= n <= 19
'''

class Solution:
    def numTrees(self, n: int) -> int:
        g_array = [1,1]
        
        for j in range(2,n+1):
            sum_g = 0
            for i in range(1,j+1):
                f_i = g_array[i-1]*g_array[j-i]
                sum_g += f_i
            g_array.append(sum_g)
                        
        return g_array[n]
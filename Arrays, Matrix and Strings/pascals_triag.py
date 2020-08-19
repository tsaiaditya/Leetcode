'''
Generates pascal's Triangle based on given number of rows
'''

class Solution:
    def generate(self, numRows):
        fin = []
        if numRows == 0:
            return fin
        fin.append([1])
        if numRows == 1:
            return fin
        for i in range(1,numRows):
            fin.append([])
            fin[i].append(1)
            for j in range(1,i):
                fin[i].append(fin[i-1][j-1]+fin[i-1][j])
            if(numRows!=0):
                fin[i].append(1)
        return fin

print("Enter a number: ")
n = int(input())
s = Solution()
print(s.generate(n))
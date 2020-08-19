'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
'''
class Solution:
    def updateMatrix(self, matrix):
        #check if matrix is empty
        if(len(matrix) == 0):
            return matrix
        #dp 2d array with inf values with the range of matrix rows and cols.
        dp = [[float("inf") for i in range(len(matrix[0]))] for j in range(len(matrix))]
        #check for left and top
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i>0:
                        dp[i][j] = min(dp[i][j],dp[i-1][j]+1)
                    if j>0:
                        dp[i][j] = min(dp[i][j],dp[i][j-1]+1)
        #check for bottom and right
        x = len(matrix)-1
        while(x>=0):
            y = len(matrix[x])-1
            while(y>=0):
                if(x < len(matrix)-1):
                    dp[x][y] = min(dp[x][y],dp[x+1][y]+1)
                if(y<len(matrix[x])-1):
                    dp[x][y] = min(dp[x][y],dp[x][y+1]+1)
                y-=1
            x-=1
                
        return dp
st,image = "",[]
for i in input():
    # temp = []
    if(i == '['):
        st = ""
    elif(i == ']'):  
        temp = list(map(int,st.split(',')))
        image.append(temp)
    else:
        st+=i
image = image[:len(image)-1]
s = Solution()
print(s.updateMatrix(image))
'''
Snake like traversal for a given matrix.
'''
class Solution:
    def findDiagonalOrder(self, matrix):
        if len(matrix)==0:
            return []
        if len(matrix)==1:
            return matrix[-1]
        m=len(matrix)
        n=len(matrix[0])
        x,y=[0,0],[0,0]
        ans=[]
        ans.append([matrix[0][0]])
        a,b=[1,0],[0,1]
        while x!=[m-1,n-1] and y!=[m-1,n-1]:
            if y[1]+1>n-1:
                y[0],y[1]=y[0]+1,y[1]
            else:
                y[0],y[1]=y[0],y[1]+1
            if x[0]+1>m-1:
                x[0],x[1]=x[0],x[1]+1
            else:
                x[0],x[1]=x[0]+1,x[1]
            a,b=x[:],y[:]
            ans.append([])
            ans[-1].append(matrix[b[0]][b[1]])  
            while a!=b: 
                b[0],b[1]=b[0]+1,b[1]-1
                ans[-1].append(matrix[b[0]][b[1]])
        final=[]
        for i in range(len(ans)):
            if i%2==0:
                final+=ans[i][::-1]
            else:
                final+=ans[i]
        return final

mat = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9],
    [10,11,12]
]
# mat = [[i] for i in range(10000)]

s = Solution()
print(s.findDiagonalOrder(mat))
class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return matrix
        fin = []
        m = len(matrix)
        n = len(matrix[0])
        k = 0
        l = 0
        while(k<m and l<n):
            for i in range(l,n):
                fin.append(matrix[k][i])
            k+=1
            for i in range(k,m):
                fin.append(matrix[i][n-1])
            n-=1
            if(k<m):
                for i in range(n-1,l-1,-1):
                    fin.append(matrix[m-1][i])
                m-=1
            if(l<n):
                for i in range(m-1,k-1,-1):
                    fin.append(matrix[i][l])
                l+=1
        return fin

mat = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
s = Solution()
s.spiralOrder(mat)
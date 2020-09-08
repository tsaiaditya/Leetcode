class Solution:
    def spiralOrder(self, matrix):
        #Method 1:
        '''
        07/27/2020 16:20	Accepted	32 ms	14 MB	python3
        '''
        '''
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
        print(fin)
        '''
        #Method 2:
        '''
        Runtime: 24 ms, faster than 94.79% of Python3 online submissions for Spiral Matrix.
        Memory Usage: 13.7 MB, less than 85.85% of Python3 online submissions for Spiral Matrix.
        '''
        out = []
        while len(matrix):
            out += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1] # Rotate
        print(out)

mat = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
s = Solution()
s.spiralOrder(mat)
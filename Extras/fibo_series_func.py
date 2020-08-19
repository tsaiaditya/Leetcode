'''
returns sum of fibonacci numbers for a given range x,y
'''
class Solution:
    def fib(self, N):
        if(N == 0):
            return 0
        if(N == 1):
            return 1
        if(N == 2):
            return 1
        d = [0]*(N+1)
        d[1] = 1
        for i in range(2,N+1):
            d[i] += d[i-1]+d[i-2]
        # print(*d)
        return d
    def fib_func(self,x,y):
        series = self.fib(y)
        # print(series)
        temp = []
        for i in range(x,y+1):
            for j in series:
                if j>=i:
                    temp.append(j)
                    break
        print(sum(temp))

s = Solution()
x = int(input())
y = int(input())
s.fib_func(x,y)
import math
class Solution:
    def fib(self, N: int) -> int:
        '''
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
        return d[N]
        '''
        phi = (1 + math.sqrt(5)) / 2
        return round(pow(phi, N) / math.sqrt(5))

s = Solution()
print(s.fib(int(input())))
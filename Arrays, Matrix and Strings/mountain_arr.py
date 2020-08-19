def arraySorted(arr, n): 
    if (n == 0 or n == 1): 
        return True
    for i in range(1, n): 
        if (arr[i-1] > arr[i]): 
            return False
    return True

def arraySortedRev(arr, n): 
    if (n == 0 or n == 1): 
        return True
    for i in range(1, n): 
        if (arr[i-1] < arr[i]): 
            return False
    return True

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if(len(A)>=3):
            x = A.index(max(A))
            if(x == 0 or x == len(A)-1):
                return False
            l1 = []
            for i in range(0,x):
                l1.append(A[i])
                if(A[i]>=A[x]):
                    return False
            if(not arraySorted(l1,len(l1))):
                return False
            if(len(l1)!=len(set(l1))):
                return False
            l1 = []
            for i in range(x+1,len(A)):
                l1.append(A[i])
                if(A[i]>=A[x]):
                    return False
            if(not arraySortedRev(l1,len(l1))):
                return False
            if(len(l1)!=len(set(l1))):
                return False
            return True
        else:
            return False
a=[0,3,2,1]
s = Solution()
print(s.validMountainArray(a))
'''
Longest subArray with no more than two distinct values that differ by no more than 1 [closed]
input : [1,2,1,1,2,3,4]
output : 5 because len([1,2,1,1,2]) = 5 which is the max sub array available.
Dynamic Porgramming solution
'''

def f(A):
    if (len(A) < 2):
        return len(A)

    best = 1
    bestLower = 1
    bestHigher = 1
  
    for i in range(1,len(A)):
        if (A[i] == A[i-1]):
            bestLower = bestLower + 1
            bestHigher = bestHigher + 1
        
        elif (A[i] - 1 == A[i-1]):
            bestLower = 1 + bestHigher
            bestHigher = 1
        
        elif (A[i] + 1 == A[i-1]):
            bestHigher = 1 + bestLower
            bestLower = 1
        
        else:
            bestLower = 1
            bestHigher = 1
        best = max(best, bestLower, bestHigher)
    
    return best


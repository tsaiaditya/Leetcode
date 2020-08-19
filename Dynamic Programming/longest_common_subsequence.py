def lcs(X , Y): 
    m = len(X) 
    n = len(Y)

    if(m>n):
        X,Y = Y,X
        m,n = n,m
    
    L = [[None]*(n+1) for i in range(m+1)] 
  
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
    y = list(Y)
    y.insert(0,' ')
    print(*y,sep = " ")
    for i in range(m+1):
        print(*L[i])
    seq = ''
    i = m
    j = n
    while(i>=0 and j>=0):
        if(L[i][j]>max(L[i-1][j],L[i][j-1])):
            seq += Y[j-1]
            i -= 1
            j -= 1
        elif(L[i][j] == 1 and L[i-1][j] == L[i][j-1]):
            j -= 1
        elif(L[i][j] == 1 and L[i-1][j] != L[i][j-1]):
            seq += Y[j-1]
            j-=1
        else:
            j -= 1
    print("Longest common subsequence string: ",seq[::-1])
    '''
    seq = ''
    count = [0]
    for i in range(m+1): 
        for j in range(n+1): 
            if L[i][j] not in count:
                count.append(L[i][j])
                print(i,j)
                seq += Y[j-1]
    print("Longest common subsequence string: ",seq)
    '''
    return L[m][n] 
  
# X = "AGGTAB"
# Y = "GXTXAYB"
X = "lokesh"
Y = "sai"
print("Length of Longest common subsequence is ", lcs(X, Y))
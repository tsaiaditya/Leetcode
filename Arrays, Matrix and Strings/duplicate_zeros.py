'''
Adding 0's in mid of array and shifting array to left
'''
a = [1,0,2,3,0,4,5,0]
zeros = [i+1 for i,j in enumerate(a) if j == 0]
print(zeros)
for i,j in enumerate(zeros):
    print(i,j)
    a.insert(i+j,0)
    a.pop()
    print(a)
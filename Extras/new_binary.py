'''
Any binary value having '11' should be removed and then for a given number, we need to give the value in our new binary list
for the given index as query
'''
m = [(i,bin(i)[2:]) for i in range(10**7) if '11' not in bin(i)]
# print(m)
# print([i for i,j in enumerate(m) if j[1] == '10100100'][0])
print(len(n))
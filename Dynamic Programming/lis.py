def lis(arr):
    ans = [1 for i in range(len(arr))]
    # print(ans)
    order = []
    for i in range(1,len(arr)):
        temp = []
        for j in range(0,i):
            if(arr[i]>arr[j] and ans[i]<ans[j]+1):
                ans[i]+=1
                temp.append(arr[j])
        temp.append(arr[i])
        order.append(temp)
    
    print("Longest Increasing Subsequence length: "+str(ans[len(arr)-1]))
    print("Elements in the order: ")
    print(*order[len(order)-1],end=' ')
print("Enter the number of elements: ")
n=int(input())
# arr = []
print("Enter the elements: ")
s = input().strip()
arr = list(map(int,s.split(' ')))
lis(arr)
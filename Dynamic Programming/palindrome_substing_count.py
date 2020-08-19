'''
count the number of palindromic substrings in a given string and lists the substrings

'''
def palindrome_count(s):
    arr = [[0 for i in range(len(s))] for j in range(len(s))]
    count = 0
    substrings = list(s)
    for i in range(len(s)):
        arr[i][i] = 1
        count += 1
    for cols in range(1,len(s)):
        for rows in range(0,cols):
            if(rows == cols-1 and s[rows] == s[cols]):
                arr[cols][rows] = 1
                count += 1
                substrings.append(s[rows:cols+1])
            elif(s[rows] == s[cols] and arr[rows+1][cols-1] == 1):
                arr[cols][rows] = 1
                count += 1
                substrings.append(s[rows:cols+1])
    
    print("Number of Palindromic substrings: "+str(count))
    print("List of substrings: ")
    print(*substrings,sep=',')

print("Enter a string : ")
s = input()
palindrome_count(s)
def common(strs):
    com = ""
    for i in list(zip(*strs)):
        if(len(set(i)) == 1):
            com += i[0]
    return com
strs = ["flower","flow","flight"]
print(common(strs))
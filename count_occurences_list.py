Input=[1, 2, 2, 3, 3, 3,4]
dict={ }
count=0
for i in Input:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

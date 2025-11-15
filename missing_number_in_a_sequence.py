#Input: [1,2,4,5]

list=[1,2,4,5]

for i in range(1,len(list)):
    if i in list:
        continue
    else:
        print(i)
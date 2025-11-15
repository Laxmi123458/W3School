from collections import Counter
str1="listen"
str2="silent"

if len(str1)!=len(str2):
    print("No")
else:
    if Counter(str1)==Counter(str2):
        print("yes")
    else:
        print("no")
str="Madam"
rev_str=""
for i in str:
    rev_str=i+rev_str
print(rev_str)
if str.lower() == rev_str.lower():
        print("word is palindrome")
else:
        print("word is not palindrome")
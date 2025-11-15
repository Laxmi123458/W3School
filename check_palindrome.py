original_word=input("Enter a word").strip()
revered_word= original_word[ : : -1]
print(revered_word)
if original_word.lower() == revered_word.lower():
    print("The word is palindrome")
else:
    print("The word is not palindrome")



str = "Welcome"

vowels = ""
consonants = ""
for x in str:
    if x.isalpha():
        if x.lower() in 'aeiou':
            vowels += x
        else:
            consonants += x
print("Vowels:", vowels)
print("Consonants:", consonants)
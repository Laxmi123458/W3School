"""
Enter operation:
1. Divide
2. Add
3. Sub
4. Multiply

2

Enter 1st number>

6

Enter 2nd number

8

Result>

14
"""

n = int(input('Enter operation options:'))

for i in range(0,n):

    print('Enter 1 for choice 1: add\n')

    print('Enter 2 for choice 2: subtraction\n')

    print('Enter 3 for choice 3: multiplication\n')

    print('Enter 4 for choice 3:divison\n')

    choice = int(input('Enter your choice:'))

    first_num = int(input("Enter 1st number"))
    sec_num = int(input("Enter 2nd number"))

    if (choice == 1):
        add = first_num + sec_num
        print(f"{first_num}+{sec_num}:{add}")
    elif (choice == 2):
        sub = first_num - sec_num
        print(f"{first_num}+{sec_num}:{sub}")
    elif (choice == 3):
        mul = first_num * sec_num
        print(f"{first_num}+{sec_num}:{mul}")
    elif (choice == 4):
        div = first_num / sec_num
        print(f"{first_num}+{sec_num}:{div}")
    else:
        print('Invalid choice')




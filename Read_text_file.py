c=0
with open("output.txt", 'r') as file:
    data=file.read()
    w=data.split()
    c+=len(w)
print(c)


#want to specify the data type of a variable, this can be done with casting.
x=str(3)
y=int(9)
z=float(4)
print(x,y,z)

# get the data type of a variable with the type() function.
x=10
c=6.8
print(type(x))
print(type(c))

#variable names are case sensitive
a=10
A=11
print(a)
print(A)

#variable names are case sensitive
#allowed A-Z, a-z, _
#Notallowed - to start with a number and contain any special character
my_vari=10 #snake cae
MyVari=11 #Pascal case
myVari=4 #camel case
print(my_vari)
print(MyVari)
print(my_vari)

#Python allows you to assign values to multiple variables in one line:
x,y,z="apple ","bannana ", "orange"
print(x,y,z)
print(x + y + z) #notice space character after "apple " and "bannana ", without them the result would be "applebannanaorange".
print(x)
print(y)
print(z)

# can assign the same value to multiple variables in one line
x=y=z=34
print(x)
print(y)
print(z)

#Unpack a Collection:If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits=["apple","bannana", "orange"]
x,y,z=fruits
print(x)
print(y)
print(z)


#print() function, when you try to combine a string and a number with the + operator, Python will give you an error
x = 5
y = "John"
print(x + y)

#best way to output multiple variables in the print() function is to separate them with commas, which even support different data types
x = 5
y = "John"
print(x,y)

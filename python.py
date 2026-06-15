#First Python program
print("Hello, World!")

#Variable assignment(first method)
name="Sam"
age=30
price=19.99
print(name)
print(age)
print(price)

#Variable assignment(second method)
name="Sam"
age=30
price=19.99
print("My name is :",name)
print("My age is :",age)
print("The price is :",price)

#Variable
name="Sam"
age=30  
age2=age
print(age2)

#Variables type
name="Sam"
age=30
price=19.99
print(type(name))
print(type(age))
print(type(price))

#Data types
#String(double quotes)
name="Sam"
print(name)

#String(single quotes)
name='Sam'
print(name)

#String(triple quotes)
name="""Sam"""
print(name) 

#String
name1='Sam'
name2="Smith"
name3='''Sam'''
print(name1)
print(name2)
print(name3)

#Float & None
age=23
old=False
a=None
print(type(age))
print(type(old))
print(type(a))

#Print Sum
a=10
b=20
sum=a+b
print(sum)

#Print Difference
a=100
b=50
diff=a-b
print(diff)

#Comments in Python
#This is a single line comment
'''
Single line comments
'''

#This is a multi-line comment
print("Hello World")
"""
Multi-line 
comments
"""

#Types of operators
#Arithmetic operators
a=10
b=5
print(a+b) #Addition
print(a-b) #Subtraction
print(a*b) #Multiplication
print(a/b) #Division
print(a//b) #Floor Division(Quotient without remainder)
print(a%b) #Modulus(Remainder)
print(a**b) #Exponentiation(a^b)

#Comparison/Relational operators(gives a boolean output)
a=50
b=20
print(a==b) #Equal to
print(a!=b) #Not equal to
print(a>b) #Greater than
print(a<b) #Less than
print(a>=b) #Greater than or equal to
print(a<=b) #Less than or equal to

#Assignment operators
#method 1
num=10
num=num+10
print(num)

#method 2
num=10
num+=10
print(num)

#Logical operators
a=10
b=20
print(a>5 and b>15) #Logical AND(both conditions must be true)
print(a>15 or b>15) #Logical OR(at least one condition must be true)
print(not(a>5 and b>15)) #Logical NOT(negates the condition)

#method 1
print(not False) #True
print(not True) #False

#method 2
a=10
b=20
print(not False) #True
print(not(a>b)) #True

#method 3
val1=True
val2=False
print("ans operator:",val1 and val2) #False

#method 4
val1=True
val2=False
print("ans AND operator:",val1 and val2) #False
print("ans OR operator:",val1 or val2) #True
print("ans NOT operator:",not val1) #False

#method 5
a=10
b=20
print("ans AND operator:",(a==b) and (a>b)) #False
print("ans OR operator:",(a==b) or (a>b)) #False
print("ans NOT operator:",not(a==b)) #True


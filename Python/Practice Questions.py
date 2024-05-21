#Calculator
x=int(input('Enter 1st value: '))
y=int(input('Enter 2nd value: '))
s=input( 'Enter +,-,*,/ : ')
if  s=='+':
    print(x+y)
elif s=='-':
    print( x-y)
elif s=='*':
    print( x*y)
else:
    print( x/y)

#Check if the number is Prime or Not
n=int(input('Enter a number: '))
x=False
for i in  range(2,n):
    if  n%i==0:
        x=True
        break
if  x:
    print("Not Prime")
else:
    print("Prime")

#Print Pattern
for num in range(6):
    for i in range(num):
        print (num, end="")
    print("\n")
for  num in range(4,0,-1):
    for  i in range(num):
        print( num, end="")
    print("\n")

#Check Palindrome or Not    
n=int(input( 'Enter a number: '))
comp=n
temp=0
while n>0:
    r = n % 10
    temp = (temp * 10) + r
    n = n // 10
if temp==comp:
    print("Palindrome")
else:
    print("Not Palindrome")

#Multiplication table
t=int(input("Enter number: "))
for i in range(1,11):
    print( t, "x", i, "=", t*i)









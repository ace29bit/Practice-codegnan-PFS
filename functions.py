#funtions
'''def calculate(a,b):
    print("Sum ",a+b)
    print("diff ",a-b)
    print("product ",a*b)
calculate(10,20)'''
#//,**,%
'''def calc(a,b):
    print("Int div",a//b)
    print("Exponents",a**b)
    print("Division",a%b)
calc(12,3)'''

'''def fullname():
    fname=input("Fname ")
    lname=input("Lname ")
    print((fname+" "+lname).title())
fullname()'''
#difference between print & return
#print just shows the human user output in a console
#return will terminate the function and gives back a value from the function
'''def mul(a,b):
    print(a*b)
mul(10,3)
'''
#using return
'''
def mul(a,b):
    return a*b
print(mul(10,7))
'''
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
print(cal(10,5))'''
#
'''def cal():
    a=int(input("Enter value "))
    b=int(input("Enter value "))
    op=int(input("Options 1.add\n2.sub\n3.mul"))
    if op==1: c=a+b
    elif op==2: c=a-b
    elif op==3: c=a*b
    return c
print(cal())'''
#using def in another def
def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("Enter value "))
    b=int(input("Enter value "))
    op=int(input("Options \n1.add\n2.sub\n3.mul"))
    if op==1: add()
    elif op==2: sub()
    elif op==3: mul()














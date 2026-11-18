#split bill
'''def split_bill():
    a=int(input("Number of persons: "))
    b=int(input("Total bill: "))
    print("Perhead amount: {}".format(b//a))
    print(f"Perhead amount: {b//a}")
split_bill()'''
#
'''def bakery():
    cake=input("Enter the cake name: ")
    qty=int(input("Weight of the cake: "))
    print("Your cake:{} \nWeight of cake:{} \nAmount Pay:{}".format(cake,qty,qty*150))
bakery()'''
#
# * arguements->* is used unpack the element
'''a=(2,3,4,5,6,7)
print(a)
print(*a)'''

'''a="codegnan"
print(*a)'''

'''d=[5+6j]
print(*d)'''

'''a,b,c=2,3,4,5,6,7,8,9,11,12,
print(a)
print(b)
print(c)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''a,b,c='cod'
print(a)
print(b)
print(c)'''

'''*a,b,c="codegnan"
print(*a)
print(b)
print(c)'''

#variable length argument
#definition
'''a variable-length argument uses a star(*)before the parameters name (commonly written
as *args) to accept any number of positional input
and automatically store them in a tuple'''

def check1(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        if type(i)in (int, float):
            d=d+1
            print(d)
check1()
check1(2,3,4,5,6,7)
check1(2,3,4,5,2.3,4.3)
check1(1,2,3,4,2.3,4.3,"venkat")





























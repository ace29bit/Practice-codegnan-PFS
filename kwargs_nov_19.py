#kwargs(**)
'''def Details(**a):
    print(a)
    print(type(a))
Details()
d={"id":[1,2,3],"names":["durga","venkat","sai"],"status":['p','a','p']}
Details(**d)'''

#return only keys
#return only values
#return both key and values
'''def marks(**a):
    print(a.values())
    print(a.keys())
    print(a.items())
b={'venkat':100,'durga':100}
marks(**b)'''
'''def marks(**a):
    for i in a:#for keys
        print(i)
    for i in a:#for values
        print(a[i])
    for i in a:#for both key & values
        print(i,a[i])
b={'venkat':100,'durga':100}
marks(**b)'''

#both * & **
'''def both(*a,**b):
    print(a)
    print(b)
z={'venkat':100,'durga':100}
both(1,2,3,5,**z)'''
#
'''def final(*a,**b):
    print(a)
    print(type(a))
    print(b)
    print(type(b))
    d=3
    for i in a:
        d+=i
        print(d)
    for i,j in b.items():
        print("Keys ",i)
        print("values ",j)
info={'names':['durga','venkata','sai','sivayya'],'city':['vij','rjm','vzg']}
final(2,3,4,5,2.3,4.5,**info)'''

#task Railway ticket
#railway ticket
def railway():
    print("WELCOME TO INDIAN RAILWAY")
    name=input("enter your name: ").title()
    age=int(input("Enter your age:"))
    gender=input("Male/Female TYPE: [M/F]: ").upper()
    print(f"Name: {name}\nAge: {age}\nGender: {"Male" if gender=='M' else "Female"}")
    ticket=1000
    if age>=60:
        if gender=='F':
            ticket-=500
            print('Ticket Amount: ',ticket)
        else:
            ticket-=300
            print('Ticket Amount: ',ticket)
    else:
        if gender=='F':
            ticket-300
            print('Ticket Amount: ',ticket)
        else:
            print('Ticket Amount: ',ticket)
    print("HAPPY JOURNEY")
railway()
    



















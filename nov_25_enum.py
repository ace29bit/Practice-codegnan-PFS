#enumerate: we can give counter to the collection
'''names=['durga','venkata','sai','sivayya']
for i in range(len(names)):
    print(i,names[i])'''

'''names=['durga','venkata','sai','sivayya']
b=list(enumerate(names))
print(b)
e=tuple(enumerate(names,1))
print(e)
f=set(enumerate(names,100))
print(f)
d=dict(enumerate(names,7))
print(d)'''

#anonymous functions(nameless functions)
#anonymous functions are nameless function and we use a keyword called as lambda
#to create anonymous function

#write a function to calculate 2*x+5 where x=5
'''def cal(x):
    a=2*x+5
    print(a)
cal(5)'''

#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''n=int(input("value 1 "))
cal=lambda x:2*x+5
print(cal(n))'''

'''n1=int(input())
n2=int(input())
cal=lambda x,y:2*(x+y)+5
print(cal(n1,n2))'''

'''a="codegnan"
up=lambda x:x.upper()
print(up(a))'''

'''up=lambda x:x.upper()
print(up("codegnan"))'''

'''a="hello python"
t=lambda x:a.title()
print(t(a))'''

'''fname=input()
lname=input()
f=lambda y,z:y+" "+z
print(f(fname,lname))'''

'''fname,lname=[i for i in input().split(",")]
full=lambda fname,lname:(fname+" "+lname).title()
print(full(fname,lname))'''

'''a,b=input().split(" ")
full=lambda fname,lname:(fname+" "+lname).title()
print(full(a,b))'''

#ASCII
#chr(),ord()
'''print(chr(65))
print(chr(71))
#ord()
print(ord('a'))'''

'''for i in range(97,123):
    print(chr(i),end=" ")'''

'''for i in range(ord('a'),ord('z')+1):
    print(chr(i),end=" ")'''

st=input()
d={}
for i in st:
    d[i]=ord(i)
print(d)



















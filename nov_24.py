#built-in functions
#dir()
#print(dir("__builtins__"))
#fromkeys()
'''a="venkat"
print(list(a))
print(tuple(a))
print(set(a))
d=dict.fromkeys(a)
e=dict.fromkeys(a,"sai")
print(e)
print(d)'''

#eval(): using in runtime input can accept any datatype without rising error
#note for string you have to give quotes " " or ' '
'''a=eval(input("a value "))
b=eval(input("b value "))
print(a+b)'''

#zip() combines multiple collections into single collections
a=[1,2,3,4,5,6]
name=["Durga","venakata","sai","sivayya"]
b=zip(a,name)
d=dict(zip(a,name))
e=list(zip(a,name))
f=set(zip(a,name))
print(f)
print(d)
#print(*b)






















#filter()is used to select only the elements
#from an iterable that satisfy a given condition.

#even
'''a=[2,4,5,7,8,10,12,14,16,25,30,100]
eve=list(filter(lambda x:x%2==0,a))
print(eve)'''

'''a=[]
print(type(a))
b=()
print(type(b))
c=set()
print(type(c))
d={}
print(type(d))'''

#map()is used to apply a function to
#every element in an iterable and return the modified results.

'''a=[2,5,7,10,20,40,60]
b=[1,3,4,11,15,35,70]
big=list(map(max,a,b))
print(big)
smal=list(map(min,a,b))
print(smal)'''

#print(ord('+'))

'''a=["c","c++","ml","java","python"]
b=["html","css","js","bs","react"]
n=list(map(max,a,b))
print(n)'''

'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=input("Data").split(",")
print(a+" "+b)'''

'''a,b=[int(x) for x in input("Data").split(",")]
print(a+b)'''

'''a,b=(int(x) for x in input("enter the value").split(","))
print(a+b)'''

'''a,b=int(input("Value: ")).split(",")
print(a+b)'''

#using map() for run time values
'''a,b=map(int,input("enter the values").split(","))
print(a+b)'''

#in list []
'''a=list(map(int,input("Enter the values").split(",")))
print(a)'''

#in tuple()
'''b=tuple(map(int,input("values ").split(",")))
print(b)'''

#in set()
c=set(map(int,input("Values ").split(" ")))
print(c)








































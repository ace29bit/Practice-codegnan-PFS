#generator
#list comprehension
'''a=[i for i in range(16)]
print(a)'''

#generator
'''a=(i for i in range(16))
print(a)
print(*a)
print(list(a))
print(set(a))'''

#addition using list comprehension
'''a,b=[int(x) for x in input("enter the value: ").split(",")]
print(a+b)'''

#using yield
'''a,b=[int(x) for x in input("enter the numbers ").split(" ")]
def check(a,b):
    while a<b:
        yield a
        a+=1
        yield a
print(*check(a,b))'''
#using return
'''a,b=[int(x) for x in input("Enter the numbers ").split(",")]
def check(a,b):
    while a<=b:
        a+=1
    return a
print(check(a,b))'''

#return v/s yield
#return : return terminates the program
'''def demo():
    return 'vij'
    return 'hyd'
    return 'viz'
    return 'vij','hyd','viz'
print(*demo())'''

#yield : yield is opposite to return it runs the program untill any condition met
'''def demo():
    yield 'vij'
    yield 'hyd'
    yield 'viz'
print(*demo())
#output vij hyd viz
# if you want to print the above output in line by line
#use next() funtion it allow the yield to print one by one as below
d=demo()
print(next(d))
print(next(d))
print(next(d))'''

#max() min() sum()

print(max(1,2,3,4,6,7))
print(min(1,2,3,4,5,6,8))
#sum() for this function we can not give the values directly
#sum() can be done in two approaches as follows
a=1,2,3,4,5,6
print(sum(a))
#by giving in a list or tuple 
print(sum([2,3,4,5,6,8,8,9]))








































     


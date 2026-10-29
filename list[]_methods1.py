Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list[]
a=[2,8.5,"Python",8+6j,True,False]
print(a)
[2, 8.5, 'Python', (8+6j), True, False]
type(a)
<class 'list'>
#append()- It's used to add a value into the list
#Note: append() can only add single value
b=["python","Java","c","c++"]
b.append("R")
print(b)
['python', 'Java', 'c', 'c++', 'R']
b.append("AI","ML")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b.append("AI","ML")
TypeError: list.append() takes exactly one argument (2 given)
>>> b.append(["AL","ML"])
>>> print(b)
['python', 'Java', 'c', 'c++', 'R', ['AL', 'ML']]
>>> #extend()
>>> #extend() :- It is used to add multiple values into the list
>>> #Note:- append() can only add single value while extend() can add multiple values
>>> c=[10,20,30,40]
>>> c.extend(50,60)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    c.extend(50,60)
TypeError: list.extend() takes exactly one argument (2 given)
>>> c.extend([50,60])
>>> print(c)
[10, 20, 30, 40, 50, 60]
>>> c.extend([70,80])
>>> print(c)
[10, 20, 30, 40, 50, 60, 70, 80]
>>> #insert() :- used to add a value at a particular index in list
>>> d=[1,2,3,4]
>>> d.insert(0,5)
>>> print(d)
[5, 1, 2, 3, 4]
>>> #index() - is used to know the index of a value in list
>>> d.index(5)
0
>>> e=["Mango","banana","grape"]
>>> f=e.copy()
>>> print(f)
['Mango', 'banana', 'grape']
>>> #copy() - is used to copy the values of a variables

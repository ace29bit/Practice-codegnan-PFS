Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=["vij","viz","hyd"]
a.pop()
'hyd'
print(a)
['vij', 'viz']
a.pop(1)
'viz'
print(a)
['vij']
a.pop("vij")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.pop("vij")
TypeError: 'str' object cannot be interpreted as an integer
print(a)
['vij']
#pop() - is used to delete the value in the list
#remove(): - it's also used to delete the value in the list
#note:- pop() remove the value using index while remove() delete the value directly
a=["Hey","Hello","hi"]
a.remove("Hey")
print(a)
['Hello', 'hi']
#clear() is used to delete entire list
b=["hai","bye"]
b.clear()
print(b)
[]
b.append("Welcome")
print(b)
['Welcome']
a=["banana","apple","grapes","sapota"]
a.sort()
print(a)
['apple', 'banana', 'grapes', 'sapota']
>>> #sort() - used to arrange the values in list in an ascending order
>>> #note - complex, combination list cannot sort
>>> a=[True,False]
>>> a.sort()
a
>>> 
>>> print(a)
[False, True]
>>> #reverse() - its reverse the list
>>> a=[1,2,3,4,5,6,7,8]
>>> a.reverse()
>>> print(a)
[8, 7, 6, 5, 4, 3, 2, 1]
>>> colors=["white","black","green"]
>>> colors.reverse()
>>> print(colors)
['green', 'black', 'white']
>>> #len() - shows the length of the list
>>> a=[1,2,3,45]
>>> a.len()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.len()
AttributeError: 'list' object has no attribute 'len'
>>> len(a)
4
>>> b=["a","b","apple"]
>>> b.count("a")
1
>>> b.count("apple")
1
>>> #count() - it tells a word or value appears in a list value

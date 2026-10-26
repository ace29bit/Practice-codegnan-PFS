Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a='Venkat'
>>> print(a[4])
a
>>> print(a[0]-a[4])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(a[0]-a[4])
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> print(a[0-4])
n
>>> print(a[0]+a[1]+a[2]+a[3])
Venk
>>> a='I am in class'
>>> print(a[0]+a[1]+a[2])
I a
>>> #add plus (+) to combine the index values
>>> a="I am learning python full stack"
>>> b-"Time is very precious"
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b-"Time is very precious"
NameError: name 'b' is not defined
>>> b="Time is very precious"
>>> print(a[1])
 
>>> print(a[0])
I

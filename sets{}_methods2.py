Python 3.14.8 (tags/v3.14.8:8e6e75d, Sep 30 2026, 18:19:33) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#symmetric_difference_update():- works like symmetric_difference() but modifies the orginal set instead of creating newset
a={1,2,3,4}
b={2,3,4,5}
a.symmetric_difference_update(b)
print(a)
{1, 5}
a
{1, 5}
#pop():- removes and return a arbitrary(random) element
a={1,2,3,4}
a.pop()
1
a.pop(3)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.pop(3)
TypeError: set.pop() takes no arguments (1 given)
#remove():- Remove element x. Raises key error if x is missing
a={5,6,78,8,9}
a.remove(78)
print(a)
{5, 6, 8, 9}
a.remove(78)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.remove(78)
KeyError: 78

#discard():- Remove element x. Does nothing if x is missing
b={"hi","Byee","Hello")
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
b={"hi","Byee","Hello"}
b.discard("Hai")
print(b)
{'Hello', 'Byee', 'hi'}
b.discard("hi")
print(b)
{'Hello', 'Byee'}
#copy() :- it create the shallow copy of the set(orginal)
a={1,2,3,4,5,6,7}
a.copy()
{1, 2, 3, 4, 5, 6, 7}
b=a.copy()
print(b)
{1, 2, 3, 4, 5, 6, 7}
#clear():- removes all the elements and leaving set empty
a={1,2,3,4,5}
a.clear()
print(a)
set()
a=set()
a.add("Hello World!")
print(a)
{'Hello World!'}
type(a)
<class 'set'>
>>> a={1,2,3,4,5,6,7}
>>> print(len(a))
7
>>> #isdisjoint():- Returns True if both sets does'nt intersect(No commom elements)
>>> a={1,2,3,4,5}
>>> b={6,7,8,9,0}
>>> a.isdisjoint(b)
True
>>> b.update(1)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    b.update(1)
TypeError: 'int' object is not iterable
>>> b.update({1})
>>> print(b)
{0, 1, 6, 7, 8, 9}
>>> print(a)
{1, 2, 3, 4, 5}
>>> a.isdisjoint(b)
False

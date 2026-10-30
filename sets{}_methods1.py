Python 3.14.8 (tags/v3.14.8:8e6e75d, Sep 30 2026, 18:19:33) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a={29,5.6,"python",10+9j,True,False}
print(a)
{False, True, 5.6, (10+9j), 'python', 29}
type(a)
<class 'set'>
b={1,2,3,4,6,7,8}
print(b)
{1, 2, 3, 4, 6, 7, 8}
type(b)
<class 'set'>
#add :- add a single element to the set
a={1,2}
a.add(3)
print(a)
{1, 2, 3}
a.add(22)
print(a)
{1, 2, 3, 22}
#subset():-Returns 'True' if all elements of the set are contained in another specified set.
a={1,2,3,4,5,6}
b={2,4,6}
a.issubset(a)
True
c={9,1,7}
c.issubset(a)
False
#superset():- Returns 'True' if the set contains all elements of another specified set
a={10,20,30,40}
b={10,20}
a.issuperset(b)
True
b.isuperset(a)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    b.isuperset(a)
AttributeError: 'set' object has no attribute 'isuperset'. Did you mean: 'issuperset'?
b.issuperset(a)
False
a.issuperset(b)
True
a.issubset(b)
False
b.issubset(a)
True
#union:- Returns all unique elements from both sets.
a={1,2,3,4}
b={2,3,4,5}
a|b
{1, 2, 3, 4, 5}
c=a|b
print(c)
{1, 2, 3, 4, 5}
#intersection():- Returns only the elements presents in both sets
class_1={"durga","venkat","sai","sivayya"}
class_2={"venkat","sai"}
class_1&class_2
{'sai', 'venkat'}
class_1 | class_2
{'sai', 'venkat', 'durga', 'sivayya'}
#update():-add multiple elements from list,tuple or another set
a={1,2,3}
a.update([4,5,7,8])
print(a)
{1, 2, 3, 4, 5, 7, 8}
Details={"venkat","BCA",310}
address={"Benz circle","Vijayawada"}
Details.update(address)
print(Details)
{'venkat', 'Vijayawada', 'BCA', 310, 'Benz circle'}
#difference():- Returns elements in the first set but not from the second set
a={1,2,3,4}
b={3,4,5,6}
a.difference(b)
{1, 2}
fruits={"apple","Banana","Grapes"}
fruits2{"Kiwi","Banana","Grapes"}
SyntaxError: invalid syntax
fruits2={"Kiwi","Banana","Grapes"}
a.difference(b)
{1, 2}
fruits.difference(fruits2)
{'apple'}
fruits2.difference(fruits)
{'Kiwi'}
#symmetric_difference():- Returns elements in either set, but'not' in both
a={1,2}
b={2,3}
>>> a.symmetric_difference(b)
{1, 3}
>>> a={1,2}
>>> b={1,2}
>>> a.symmetric_difference(b)
set()
>>> #difference_update():- removes all elements of another set from the original set
>>> #note:- note itsn't creating newset and only modifies the orginal set low memory usage comapare to difference()
>>> closet={"shirt","Jacket","hat","jeans"}
>>> Pack={"Jacket","hat","jeans"}
>>> closet.difference_update(pack)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    closet.difference_update(pack)
NameError: name 'pack' is not defined. Did you mean: 'Pack'?
>>> closet.difference_update(Pack)
>>> print(closet)
{'shirt'}
>>> closet.difference(Pack)
{'shirt'}

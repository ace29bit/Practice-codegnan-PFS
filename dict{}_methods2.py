Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a={"year":2026,"month":11}
#update()- add the elements into the dictionary(1 or more)
a.update({"time":10})
print(a)
{'year': 2026, 'month': 11, 'time': 10}
#for more values elements should pass only in single arguement
a.update({"hour":1},{"min":30})
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.update({"hour":1},{"min":30})
TypeError: update expected at most 1 argument, got 2
#see it throws an error
a.update({"hour":1,"min":30})
print(a)
{'year': 2026, 'month': 11, 'time': 10, 'hour': 1, 'min': 30}
#setdefault()- in set the given two value tunrns into dict value means it automatically creates fist value as key and second value as a value
#Note: set default only takes 2 value not more than two
a={"color":"black","food":"veg","desert":"cake"}
a.setdefault("place","vij")
'vij'
print(a)
{'color': 'black', 'food': 'veg', 'desert': 'cake', 'place': 'vij'}
#pop() - deletes the value using key and returns value
a.pop("color")
'black'
#popitem() - automatically deletes the last key:value
a.popitem()
('place', 'vij')
>>> #returns the key:value
>>> #note- In pop() the must give 1 arguement or else throw error
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> b=a.copy() #returns the copy another data
>>> print(b)
{'food': 'veg', 'desert': 'cake'}
>>> b.clear() # clears the dictionary and returns empty dictionary {}
>>> print(b)
{}
>>> # dict{} does'nt allow duplicates
>>> a={"name":"Venkat","wish":"welcome","name","venkat","name":"venkat"}
SyntaxError: ':' expected after dictionary key
>>> a={"name":"Venkat","wish":"welcome","name":"venkat","name":"venkat"}
>>> print(a)
{'name': 'venkat', 'wish': 'welcome'}
>>> a={"name":"Venkat","wish":"welcome","name":"venkat","Name":"venkat"}
>>> print(a)
{'name': 'venkat', 'wish': 'welcome', 'Name': 'venkat'}
>>> #in dict{} repeated keys, it only prints the last key

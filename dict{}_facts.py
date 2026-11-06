Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # dict{} does'nt allow duplicates
>>> a={"name":"Venkat","wish":"welcome","name":"venkat","name":"venkat"}
>>> print(a)
... {'name': 'venkat', 'wish': 'welcome'}
SyntaxError: multiple statements found while compiling a single statement
>>> a={"name":"Venkat","wish":"welcome","name":"venkat","Name":"venkat"}
>>> print(a)
{'name': 'venkat', 'wish': 'welcome', 'Name': 'venkat'}
>>> #in dict{} repeated keys, it only prints the last key
>>> #if you want to give repeated  values the keys should be different
>>> #to pass more values to a key
>>> a={"id_no:":[10,20,30],"names":["venkat","durga","sai"],"marks":[50,60,70]}
>>> print(a)
{'id_no:': [10, 20, 30], 'names': ['venkat', 'durga', 'sai'], 'marks': [50, 60, 70]}
>>> a.keys()
dict_keys(['id_no:', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['venkat', 'durga', 'sai'], [50, 60, 70]])
>>> type(a)
<class 'dict'>

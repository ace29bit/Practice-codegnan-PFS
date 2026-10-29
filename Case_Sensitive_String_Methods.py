Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#String_methods
#upper_case
a="code"
a.upper()
'CODE'
b="python"
b.upper()
'PYTHON'
#lower_case
a="HAI"
a.lower()
'hai'
#capitalize() is used to capital the fisrt letter in the word
a="what's your name?"
a.capitalize()
"What's your name?"
b="my name is venkat"
b.capitalize()
'My name is venkat'
#title() is used to make capital the first letter of every word
a="there is a car"
a.title()
'There Is A Car'
b="he's playing cricket"
b.title()
"He'S Playing Cricket"
a="hello"
a.isupper()
False
a.islower()
True
b="VENKAT"
b.isupper()
True
#isalpha() to check weather the variable contains alphabatics
a="Haii"
a.isalpha()
True
#isdigit() to check the following variable contains number
a=123
a.isdigit()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
a="123"
a.digit()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.digit()
AttributeError: 'str' object has no attribute 'digit'. Did you mean: 'isdigit'?
>>> a.isdigit()
True
>>> #startswith() is to check the following string starts with given substring
>>> a="Python"
>>> a.isstartswith("P")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.isstartswith("P")
AttributeError: 'str' object has no attribute 'isstartswith'. Did you mean: 'startswith'?
>>> a.startswith("P")
True
>>> a="Hello"
>>> a.startswith("O")
False
>>> #endswith() just like startswith() but checks end substring
>>> a="Something"
>>> a.endwith("g")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.endwith("g")
AttributeError: 'str' object has no attribute 'endwith'. Did you mean: 'endswith'?
>>> a.endswith("g")
True
>>> #isalnum()
>>> #is used to check the variable contain alphanumerical
>>> c="Venkat77"
>>> c.isalnum()
True
>>> c="Venkat1344@#"
>>> c.isalnum()
False

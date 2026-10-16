Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#int()
int(4)
4
int(9.8)
9
int("hi")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(4+5j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(4+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(true)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(True)
1
int(False)
0
#float
float(5)
5.0
float(4.1)
4.1
float("Bye")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("Bye")
ValueError: could not convert string to float: 'Bye'
float(8+3j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(8+3j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
str(7)
'7'
str(8.0)
'8.0'
str("Hello")
'Hello'
str(6+5j)
'(6+5j)'
str(True)
'True'
str(False)
'False'
complex(2)
(2+0j)
complex(8.0)
(8+0j)
complex("Hai)
...         
SyntaxError: unterminated string literal (detected at line 1)
>>> complex("Bye")
...         
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    complex("Bye")
ValueError: complex() arg is a malformed string
>>> complex(True)
...         
(1+0j)
>>> complex(False)
...         
0j
>>> bool(2)
...         
True
>>> bool(6.8)
...         
True
>>> bool("hai")
...         
True
>>> bool(5+7j)
...         
True
>>> bool(True)
...         
True
>>> bool(False)
...         
False

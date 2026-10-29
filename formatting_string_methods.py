Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #formatting means adding additional data to the string
>>> a=10
>>> b=20
>>> print("The sum is",a+b)
The sum is 30
>>> city="Vij"
>>> print("My city is",city)
My city is Vij
>>> #format() is used to place the varibles in string as we like
>>> name="Venkat"
>>> city="vij"
>>> print("Hello Everyone I name is {} and I came from {}".format(name,city))
Hello Everyone I name is Venkat and I came from vij
>>> f1=motu
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    f1=motu
NameError: name 'motu' is not defined
>>> f1="motu"
>>> f2="pathlu"
>>> print("say hello to {} {}".format(f1,f2))
say hello to motu pathlu
>>> print("Hello {} Hello {}".format(f1,f2))
Hello motu Hello pathlu
>>> #fstring
>>> a="Venkat"
>>> b="sai"
>>> print(f"my middle name is {a} {b}")
my middle name is Venkat sai

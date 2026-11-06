Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #methods
>>> a={"name":"venkat","year":2026,"month":"oct"}
>>> a.keys() #retrives only keys
dict_keys(['name', 'year', 'month'])
>>> a.values() #retrives only values
dict_values(['venkat', 2026, 'oct'])
>>> a.items() #retrives both keys&values in tuple
dict_items([('name', 'venkat'), ('year', 2026), ('month', 'oct')])
>>> a.["name"]
SyntaxError: invalid syntax
>>> a["name"]
'venkat'
>>> #above method is used to accessing
>>> #only keys must pass, if value pass error will rise
>>> a["venkat"] #example
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a["venkat"] #example
KeyError: 'venkat'
>>> #get() : returns the value if exist, if not it does'nt rise any error like accessing
>>> a.get("year")
2026
>>> a.get("dec")
>>> #see it is'nt throw any error

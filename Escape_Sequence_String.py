Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #escape_Sequence
>>> #\n -> new Line
>>> #\t -> tab space
>>> a="Name Venkat\ncity Vijayawada\n
SyntaxError: unterminated string literal (detected at line 1)
>>> a="name Venkat\ncity Vijayawada\n"
>>> print(a)
name Venkat
city Vijayawada

>>> b="Name\tVenkat\tCity\tVijayawada"
>>> print(b)
Name	Venkat	City	Vijayawada
>>> b.replace("Venkat","Durga")
'Name\tDurga\tCity\tVijayawada'
>>> #replace
>>> c="What's your hobbies"
>>> c.replace("hobbies","habits")
"What's your habits"
>>> c.replace("h","H")
"WHat's your Hobbies"

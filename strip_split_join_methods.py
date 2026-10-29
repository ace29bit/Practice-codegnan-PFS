Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #strip() is used for removing the white spaces or empty spaces
>>> #rstrip()
>>> #lstrip()
>>> a="   Hai   "
>>> a.lstrip()
'Hai   '
>>> a.rstrip()
'   Hai'
>>> a.strip()
'Hai'
>>> #split() is used to seperate the sentence
>>> a="my name is venkat"
>>> a.split()
['my', 'name', 'is', 'venkat']
>>> b="I'm from vijayawada"
>>> b.split()
["I'm", 'from', 'vijayawada']
>>> b[2].capitalize()
'M'
>>> c=b.split()
>>> c[2].capitalize()
'Vijayawada'
>>> #join() is used to combine the strings
>>> a="rain","winter","summer"
>>> "".join(a)
'rainwintersummer'
>>> " ".join(a)
'rain winter summer'
>>> "V".join(a)
'rainVwinterVsummer'
>>> ":)".join(a)
'rain:)winter:)summer'

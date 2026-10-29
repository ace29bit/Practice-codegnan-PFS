Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #tuple() - values in tuple cannot change
>>> a=(2,6.5,"python",3+7j,True,False)
>>> print(a)
(2, 6.5, 'python', (3+7j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.index(3+7j)
3
>>> a.count(True)
1
>>> a.count(False)
1
>>> len(a)
6

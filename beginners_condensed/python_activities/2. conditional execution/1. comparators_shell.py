Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # comparators demo
>>> 
>>> 5 > 3
True
>>> 5 < 3
False
>>> 5 == 3
False
>>> 5 != 3
True
>>> 
>>> 'apple' == 'orange'
False
>>> 'apple' != 'orange'
True
>>> 'apple' > 3
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    'apple' > 3
TypeError: '>' not supported between instances of 'str' and 'int'
>>>
>>> a = 10
>>> b = 27
>>> a > b
False
>>> a < b
True
>>> a >= b
False
>>> a <= b
True
>>> a == b
False
>>> 
>>> 
>>> a > 20 and b > 20
False
>>> a > 20 or b > 20
True
>>> a == 27 and b == 27
False
>>> a == 27 or b == 27
True
>>>
>>> 

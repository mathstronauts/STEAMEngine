Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Lists and Indexing
>>> list = ['mouse', 'keyboard', 'monitor']
>>> print(list)
['mouse', 'keyboard', 'monitor']
>>> 
>>> print(list[0])
mouse
>>> print(list[1])
keyboard
>>> print(list[2])
monitor
>>> print(list[-1])
monitor
>>> # negative indexing: index -1 refers to the last item, -2 is second last
>>> 
>>> veggies = ['lettuce', 'tomato', 'onions', 'cucumber', 'carrots', 'peppers', 'beets', 'broccoli', 'spinach']
>>> print(veggies)
['lettuce', 'tomato', 'onions', 'cucumber', 'carrots', 'peppers', 'beets', 'broccoli', 'spinach']
>>> print(veggies[2:5])
['onions', 'cucumber', 'carrots']
>>> # the range [2:5] returns the third, fourth, and fifth items [2 included: 5 not included]
>>> 
>>> len(veggies)
9
>>> veggies[3] = 'pickles'
>>> print(veggies)
['lettuce', 'tomato', 'onions', 'pickles', 'carrots', 'peppers', 'beets', 'broccoli', 'spinach']
>>> veggies.append('cauliflower')
>>> print(veggies)
['lettuce', 'tomato', 'onions', 'pickles', 'carrots', 'peppers', 'beets', 'broccoli', 'spinach', 'cauliflower']
>>> veggies.insert(2, 'cucumber')
>>> print(veggies)
['lettuce', 'tomato', 'cucumber', 'onions', 'pickles', 'carrots', 'peppers', 'beets', 'broccoli', 'spinach', 'cauliflower']
>>> veggies.remove('beets')
>>> print(veggies)
['lettuce', 'tomato', 'cucumber', 'onions', 'pickles', 'carrots', 'peppers', 'broccoli', 'spinach', 'cauliflower']
>>> 

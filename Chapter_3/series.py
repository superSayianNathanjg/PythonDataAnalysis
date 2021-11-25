""" Pandas series
Python list designed for containing information.
Pandas Series designed for math operations etc.
Pandas uses numpy behind the scenes.

list * 2 = copies contents and doubles size.
Series * 2 = multiples each element in list by 2. MUCH quicker than using list.

s = Series
To return only values that are greater than 6.
s[ s > 6]
=> Returns values that are greater than 6.

2 series can be operated on.
s1 - s2 etc.
"""

from pandas import Series

s = Series([14, 7, 3, -7, 8], index=["a", "b", "c", "d", "e"])

# print(s["e"])  # Print specific index.

my_list = Series([3, 6, 8])
my_list = my_list * 2
print(my_list[my_list > 6])
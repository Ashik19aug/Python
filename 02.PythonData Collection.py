# mylist = ["apple", "banana", "cherry"]
# Lists are used to store multiple items in a single variable. Like Array

# Lists are one of 4 built-in data types in Python used to store collections of data,
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)  # "apple", "banana", "cherry", "apple", "cherry"
print (thislist[1])  # banana <Print second item on the list>
print(thislist[-1])  # cherry <Print last item on the list>
print(thislist[2:5])
print(len(thislist))  # print list length

# It is also possible to use the list() constructor when creating a new list.
thislist2 = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist2)

# ===================================Python Tuples===============================================
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
thistuple = ("tuple1", "tuple2", "tuple3")
print(thistuple)
print(thistuple[1])
print(len(thistuple))
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1]
# we cannot change, add or remove items after the tuple has been created.
# A tuple with strings, integers and boolean values

# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))  # note the double round-brackets
print(thistuple)
print(thistuple[2:5])  # [index_number : Length_number]
# tuple is unchangeable but if we want to change tuple we need to change variable tuple to list.
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple


# we are also allowed to extract the values back into variables. This is called "unpacking"
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
# If the number of variables is less than the number of values, you can add an * to the variable name and
# the values will be assigned to the variable as a list
mnb = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *asd) = mnb

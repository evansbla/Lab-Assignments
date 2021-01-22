import numpy as np
import matplotlib as plt
import itertools as it

#  Problem 1
L = 1,2,3,4,5,6,7,8,9

def max_min():
    return print("Min:", min(L), "Max:", max(L), "Average:", sum(L)/len(L))

max_min()


#  Problem 2
list1 = list(("apple", "banana", "cherry"))
list2 = list1
list2.append("pineapple")
print("list 1:", list1)
print("list 2:", list2)
print(list1 == list2)
# List is a mutable object (True)

str1 = str('abc')
str2 = str1
str2 += ("de")
print("string 1:", str1)
print("string 2:", str2)
print(str1 == str2)
# String is an immutable object (False)

tuple1 = tuple((1,2))
tuple2 = tuple1
tuple2 += (3,)
print("tuple 1:", tuple1)
print("tuple 2:", tuple2)
print(tuple1 == tuple2)
# Tuple is an immutable object (False)

int1 = int(17.6)
int2 = int1
int2 = int(24.3)
print(int1 == int2)
# Int is an immutable object (False)

set1 = set(("apple", "banana", "cherry"))
set2 = set1
set2.add('1')
print("Set 1:", set1)
print("Set 2:", set2)
print(set1 == set1)
# Set is a mutable object (True)


#  Problem 3
def Calculator():
    want = input("Select One: Add, Multiply: ")
    if want == "Add":
        num1 = input("Enter First Number: ")
        num2 = input("Enter Second Number: ")
        return print("Answer:", int(num1)+int(num2))
    else:
        num3 = input("Enter First Number: ")
        num4 = input("Enter Second Number: ")
        return print("Answer:", int(num3)*int(num4))

Calculator()


# Problem 4
l = input("Enter list (no space/comma): ")
def powerset(iterable):
    s = list(iterable)
    return it.chain.from_iterable(it.combinations(s, r) for r in range(len(s)+1))

print(list(powerset(l)))

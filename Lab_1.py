import numpy as np
import matplotlib as plt

#  Problem 1
if __name__ == "__main__":
    print('Hello World')

#  Problem 2
r = np.arange(0,2*np.pi)

def sphere_volume(r):
    return 4/3*(3.14159)*r**3

if __name__ == "__main__":
    print(sphere_volume(r))

#  Problem 3
def isolate(x,y,z,a,b):
    return print(x,"     ",y,"     ",z," ",a," ",b)

isolate(1,2,3,4,5)

#  Problem 4
def first_half(x):
    return print(x[:len(x)//2])

def backwards(x):
    return print(x[len(x):0:-1]+x[0])

first_half('Hello World')
backwards('Hello World')

#  Problem 5
x = "bear"
y = "ant"
z = "cat"
a = "dog"

def list_ops(x,y,z,a):
    # 1: Just the List
    list = [x,y,z,a]
    print(list)
    # 2: Append "eagle"
    list.append("eagle")
    print(list)
    # 3: Replace index 2 with "fox"
    list.insert(2,"fox")
    list.remove("cat")
    print(list)
    # 4: Remove index 1
    list.remove("ant")
    print(list)
    # 5: Sort in reverse alphabetical
    list.sort(reverse=True)
    print(list)
    # 6: Add string "hunter" to last entry
    list.append("hunter")
    return print(list)

list_ops(x,y,z,a)

# Problem 6
def pig_latin(word):
    if word[0] in ("a","e","i","o","u","y"): #sometimes y
        return print(word+"hay")
    else:
        return print(word[1:]+word[0]+"ay")

pig_latin("hello")

# Problem 7
def palindrome():
    n = 0
    for a in range(999,100,-1):
        for b in range(a,100,-1):
            x = a*b
            if x>n:
                s = str(a*b)
                if s == s[::-1]:
                    n = a*b
    return n

print(palindrome())

# Problem 8
def alt_harmonic(n):
    sum = 0
    for i in range(1,n):
        sum += (-1)**(i+1)/(i)
    return sum

print(alt_harmonic(500000))

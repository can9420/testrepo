# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x = 1
y=2.8
z=1j

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print("-----------------")

import random
print(random.randrange(1,20))

print("-----------------")

thisturple = ("apple", "banana", "orange", "melon", "pink")
print (thisturple[1:6])

alist = ["apple", "banana", "melon", "cherry"]
#alist.pop(0)
#alist.clear()
print(alist)

print("-----------------")

adict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1963
        }
#print(adict)

#m = adict["model"]
#m = adict.get("model")
#adict["year"] = 1998
#print(adict)

for x in adict:
    print(x, adict[x])
    print("_")

for x in adict.values():
    print(x)

for x, y in adict.items():
    print(x, y)
    
print("-----------------")

aset = {"apple", "banana", "cherry"}
print(aset)

for x in aset:
    print (x)
    
#check if an item is present in the set
#print("banna" in aset)

#add a single item use add()
aset.add("orange")
print(aset)

#add multiple item use update()
aset.update(["mango", "grapes"])
print(aset)

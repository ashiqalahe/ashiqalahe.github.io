''' syntax of python'''
#to print a strings
print("hello world")

#or
b="Bangladesh"
print(b)

#indentation

if 2<5:
    print("2 is smallest then 5")


'''variable of python'''
x=5
y="jhon"
print(x)
print(y)

x=5 #x is type of int
x="jhon" #now x is type of string
print(x)

x='awesome'
print("python is  "+x)

x="python is"
y=" awesome"
z= x+y
print(z)

x=5
y=7
print(x+y)


x=5
y="html"
n=str(x)
print(y+n)

'''python numbers'''
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

#intizer
x=2
y=-1234
print(type(x))
print(type(y))

#foat
x=2.02
y=1.0
z=-21.102
#scientific float
a = 35e5
b = 12E4
c = -87.7e10
print(type(a))
print(type(b))
print(type(c))

#complex numbers
a=2+3j
b=5j
c=-32j
print(type(a))
print(type(b))
print(type(c))

'''python casting'''
x = int(1)
y = int(2.8) # 2.8 is a foalt num but it will be int 2
z = int("3")
print(x,y,z)

#float Casting
x=float(2)
y=float("3")
z=float(2.4)
print(x,y,z)

#String casting
x = str("a1")
y = str(2)
z = str(3.0)

print(x,y,z)

'''Python string'''
a="Hello world!"
print(a)

a="Hello world!"
print(a[0])

a="Hello world!"
print(a[2:7])

b="Hello world!"
print(b.lower())

c="Hello world!"
print(c.upper())

a="Hello world!  "
print(a.strip())

a="Hello world!"
print(a.split(" "))
'''x = input("Enter your name: ")
print("Hello, " + x)
'''

'''Python operator'''
#assignment operator
'''x=5
y=3
print(x+y)
print(x-y)
print(x/y)
print(x*y)
print(x//y)
print(x**y)
print(x%y)
'''
a=5
a +=3
print("the balue of a+=3:",a)

a=5
a -=3
print("the balue of a-=3:",a)

a=5
a /=3
print("the balue of a/=3:",a)

a=5
a *=3
print("the balue of a*=3:",a)

a=5
a //=3
print("the balue of a//=3:",a)

a=5
a **=3
print("the balue of a**=3:",a)

a=5
a %=3
print("the balue of a%=3:",a)

#comparisom operator
x = 5
y = 3

print(x == y)


x = 5
y = 3

print(x != y)

x = 5
y = 3

print(x < y)

x = 5
y = 3

print(x > y)


x = 5
y = 3

print(x >= y)


x = 5
y = 3

print(x <= y)

a=7
print(a>5 and a<10)

a=7
print(a>5 or a<10)

a=7
print(not(a>5 and a<6))

'''python list'''


thislist = ["apple", "banana", "cherry"]
print(thislist[1])


thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = list(("apple", "banana", "cherry",))
print(thislist)

'''Python Tuples'''
thistuple = ("apple", "banana", "tomato",1)
print(thistuple)

thistuple = ("apple", "banana", "tomato")
print(thistuple[1])

thistuple = ("apple", "banana", "tomato")
print(thistuple[1])


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

'''thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)
'''

'''Python sets'''
thisset = {"apple", "pototo", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

'''thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)'''

thisset = set(("apple", "banana", "cherry"))
print(thisset)

'''Python Dictionary'''

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)



thisdict =	{
  "brand": "Ford",
  "model": "land cruser",
  "year": 1964
}
x = thisdict["model"]
print(x)


thisdict =	{
  "brand": "Ford",
  "model": "land rover",
  "year": 1960
}
x = thisdict.get("model")
print(x)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)


#if
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

'''if elif else'''

a = 33
b = 200
if b > a:
  print("b is greater than a")
#elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#else

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

a=20
b=13
if a > b: print("a is greater than b")

a=7
b=9
print("A") if a > b else print("B")

a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

'''while looping'''
i = 1
while i < 6:
  print(i)
  i += 1


i = 0
while i < 6:

  if i == 3:
    break
  i=i+1
print(i)

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


'''for looping'''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for i in "banana":
    print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

'''python function'''
def my_function():
  print("Hello from a function")

my_function()


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
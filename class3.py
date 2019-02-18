astring="shakib"
print( " +is a good boy and i=%d"%astring.count("i"))

name="ashiq"
hight=5.6
weight=65
old=24
print("%s is %d years old and his hight is %.1f ft and weight %dkg "%(name,old,hight,weight))

astring="hellow dhaka"
print("a single quat are ''")
print(len(astring))

astring="hello uganda"
print(astring.index("u"))
print(astring.count("a"))


astring="hello Bangladesh"
print(astring.upper())
print(astring.lower())

astring="hellow Bangladesh"
new=astring.split(" ")
print(new)

#slicing

astring="hellow world"
print(astring[ :])
print(astring[ :6])
print(astring[ 2:9])
print(astring[ 7:])
print(astring[::2])
print(astring[0:12:2])
print(astring[-1])
print(astring[:-1])
print(astring[::-1])

amy="hellow canada"
print(amy.startswith("hello"))
print(amy.endswith("can"))

a="fire traack servic is very faster in our society"
print("the leght of a=%d"%len(a))

a="fire traack servic is very faster in our society"
print("the string should a in 8 number line a=%d" %a.index("a"))
print("a accurce 2 times %d"%a.count("a"))

a="fire traack servic is very faster in our society"
print("the first five charecter is'%s'"%a[:6])
print("the next five charecter is'%s'"%a[5:11])
print("the thirteenth number'%s'"%a[14])
print("the split of string by space %s"%a.split(" "))


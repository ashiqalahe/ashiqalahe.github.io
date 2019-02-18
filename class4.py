'''name=input("inter your number here: ")
name=int(name)
print(name)
print(type(name))
name=input("input yous name here: ")
print(name.split(" "))
for i in range(10):
    print(i)

name="apple"
for i in name:
    print(i)
name=["banana","orange","tomato"]
for i in name:
    print(i)

name=["abc","adf","fine"]
for i in name:
    print(i)
name="ashiq"
for i in name:
    print(name[1])

name=["abc","dfg","cfg",]
for i in name:
    if i=="dfg":
        print("i am here")

for i in range(0,7,2):
    print(i)

flag=True
while flag:
    print("hello")
    flag=False

new=1
while new<6:

    print(new)

    if new==3:
        break
    new = new + 1'''

a=input()
def lopin(par):
    for i in range (int(par)):
        if i%2!=0:
            print(i)
        else:
            print(i)
lopin(a)

x=[]
for x in range(1500,2710):
    if(x%7==0) and (x%5==0):
        print (x)
'''car=["tmss", "python", "django"]
print(len(car))

mylist=["a","b","c","a"]
new=mylist.count("a")
print(new)

count=0
mylist=["a","b","c","a"]
for i in mylist:
    if i=="b":
        count=count+1
print(count)



list=[]
list1=[]
count=0
count1=0
mylist=["a","b","c","a","b"]
for i in mylist:
    if i=="b":

        list.append(i)
    elif i=="a":

        list1.append(i)
print(list,list1)


numlist=[]
for i in range(20,40,1):
    numlist.append(i)
print(numlist)
'''
'''
numlist=[]
numlist1=[]
for i in range(20,41):
    if i%2==0:
        numlist.append(i)
    else:
        numlist1.append(i)
print(numlist,numlist1)

'''
'''num=int(input())
num1=int(input())
list=[]
list1=[]
for i in range(num,num1):
    if i%2==0:
        list.append(i)
    else:
        list1.append(i)
print(list,list1)'''

als=["a","b","c","a","c","b","z","a","b","c","a","c","b","z"]
count=0
for i in als:
    if i=="a" or i=="b" or i=="z":
        count +=1
print(count)

new=0
new1=0
mylist=["a","b","c","a"]
for i in mylist:
    if i=="b":
        new=new+1
    if i=="a":
        new1=new1+1
print("a:%d,b:%d"%(new,new1))
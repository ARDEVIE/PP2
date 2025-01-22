mylist = ['apple', 'banana', 'cherry']
print(mylist[1]) #output banana

mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2]) #output banana

# True or False 
# List items cannot be removed after the list has been created
# answer is false

thislist = ['apple', 'banana', 'cherry']
print(len(thislist))

mylist = ['apple', 'banana', 'cherry']
print(mylist[-1]) #output cherry

fruits = ["apple", "banana", "cherry"]
print(fruits[1]) #second in list

mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4]) # ['banana', 'cherry', 'orange']

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi" 

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2]) # mango

fruits = ["apple", "banana", "cherry"]
fruits.insert(0, "orange") 
print(mylist[1]) #apple

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
fruits.extend(tropical)

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist) #['apple', 'cherry']

fruits = ['apple', 'banana', 'cherry']
fruits.clear()

mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1

fruits = ["apple", "banana", "cherry"]
newlist = [x 
for x in fruits]

fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits] #['apple', 'apple', 'apple']

list1 = ['a', 'b' , 'c']
list2 = [1, 2, 3]
for x in list2:
  list1.append(x) # ['a', 'b', 'c', 1, 2, 3]
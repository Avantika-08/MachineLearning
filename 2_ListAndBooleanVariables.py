#Boolean
print(bool())     #False

my_str="Hello World"
print(my_str.isalnum())      #False
print(my_str.isalpha())      #False -> it checks if all the characters are alphabets. In our case there is a space in b/w Hello and World
print(my_str.isdigit())      #False
print(my_str.istitle())      #True
print(my_str.startswith("H"))      #True
print(my_str.endswith('a'))        #False


#Boolean and Logical Operators
print(True and True)         #False
print(True or False)         #True

print(my_str.isalnum() or my_str.isalpha())    #False


#Lists -> collection of same or different types of objects. Mutable(Changeable)
lst=[]
print(type(lst))
print(bool(lst))        #False

lst=list()
type(lst)

lst=['Apple',100,'Mango',10.5]
print(lst)

print(len(lst))

lst.append(200)       #Add elements at the last
print(lst)

#Indexing in list -> starts with 0
print(lst[3])
print(lst[:])         #Prints all the elements
print(lst[1:4])

lst.insert(1,"Ava")   #Adds at 1st index
print(lst)

lst=[1,2,3,4,5,6]
lst.extend([8,9])
print(lst)


print(sum(lst))

print(lst.pop())
print(lst.pop(0))

lst=[1,2,2,3,4,1,1,5,6]
print(lst.count(1))

print(lst.index(1))      #return the index of first occurence of the element
print(lst.index(1,1,len(lst))) 
print(min(lst))

print(lst*5)

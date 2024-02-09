# #Boolean
# print(bool())     #False

# my_str="Hello World"
# print(my_str.isalnum())      #False
# print(my_str.isalpha())      #False -> it checks if all the characters are alphabets. In our case there is a space in b/w Hello and World
# print(my_str.isdigit())      #False
# print(my_str.istitle())      #True
# print(my_str.startswith("H"))      #True
# print(my_str.endswith('a'))        #False


# #Boolean and Logical Operators
# print(True and True)         #False
# print(True or False)         #True

# print(my_str.isalnum() or my_str.isalpha())    #False


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
print(lst[5])











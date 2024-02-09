# #Sets -> unordered collection of data types. Mutable. No Duplicate Elements
# set_var=set()        #Empty set
# print(type(set_var))

# set_var={1,2,3,4,3}
# print(set_var)

# #print(set_var[0])   #Does'nt support indexing

# set_var.add(20)
# print(set_var)

# set1={"Apple","Banana","Orange"}
# set2={"Apple","Banana","Orange","Pineapple"}
# print(set2.difference(set1))     #Pineapple
# print(set1.difference(set2))     #set()

# print(set2.intersection(set1))

# set2.difference_update(set1)     #updates the set after difference
# print(set2)


#Dictionary -> unordered collection. Mutable. Contains key value pair
# dic={}            #Empty Dictionary

# my_dict={1:"Apple",2:"Banana"}
# print(my_dict)

# print(my_dict[2])  #Accessing Value using Key

# for x in my_dict:
#     print(x)       #Print the keys
    
# for x in my_dict.values():
#     print(x)       #Print the values
    
# for x in my_dict.items():
#     print(x)       #Print key:value
    
# my_dict[3]="Capybara"   #Add new key value pair
# print(my_dict)

# my_dict[2]="Book"       #Data gets overwritten
# print(my_dict)


#Nested Dictionary
car1_model={'Mercedes':1960}
car2_model={'Audi':1970}
car3_model={'Ambassador':1980}

car_type={'car1':car1_model,'car2':car2_model,'car3':car3_model}
print(car_type)

print(car_type['car1'])
print(car_type['car1']['Mercedes'])


#Tuples -> Immutable. Used where definition of program is required one time
tup=tuple()

tup=('A','B','C')
print(tup)

#tup[0]=['D']    #Error because tuples are immutable

print(tup.count('A'))

print(tup.index('C'))




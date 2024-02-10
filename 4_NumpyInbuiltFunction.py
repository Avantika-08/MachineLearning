#Numpy -> used for creating multidimensional array(data structure that stores values of same datatype)

import numpy as np

# my_lst=[1,2,3,4,5]
# arr=np.array(my_lst)
# print(arr)

# print(type(arr))
# print(arr.shape)

# lst1=[1,2,3,4,5]
# lst2=[2,3,4,5,6]
# lst3=[3,4,5,6,7]
# arr=np.array([lst1,lst2,lst3])
# print(arr)
# print(arr.shape)

# arr=arr.reshape(5,3)
# print(arr)

# print(arr.reshape(1,15))

# print(my_lst[1])
# print(arr[1][2])
# print(arr[:,:])         #Retrieves all the column
# print(arr[0:2,0:2])     #Retrieves first two rows and columns
# print(arr[1:,3:])
# print(arr[1:,2:4])
# print(arr[1:2,1:4])

arr=np.arange(0,10,1)       #Start-Stop-Steps
# print(arr)

#print(np.linspace(1,10,50)) #Start-stop-No. of points

# arr[3:]=100                 #Copy function and broadcasting
# print(arr)                  #[  0   1   2 100 100 100 100 100 100 100]

# arr1=arr                   #Shares same memory location. any change in one array will reflects to others also
# arr1[:5]=500
# print(arr1)                #[500 500 500 500 500 100 100 100 100 100]
# print(arr)                 #[500 500 500 500 500 100 100 100 100 100]
#                            #This is called Reference type. Arrays are reference type(sharing same memory)
#In order to prevent this we have copy() fn.
# arr1=arr.copy()              #Creates different memory for arr1
# arr1[:2]=500
# print(arr1)                  #[500 500   2   3   4   5   6   7   8   9]
# print(arr)                   #[0 1 2 3 4 5 6 7 8 9]

# #Some conditions very useful in EDA
# val=2
# print(arr<2)                 #Gives array with boolean values
# print(arr*2)
# print(arr/2)
               
# print(arr[arr<5])            #Gives the array of elements which are less than 5

print(np.ones(2,dtype=int))    #Returns an array filled with ones
print(np.ones((2,5),dtype=float))

print(np.random.rand(3,3))     #All the elements are selected between 0 and 1(Uniform Distribution)
arr_ex=print(np.random.randn(3,3))    #Selects random variable based on Standard normal distribution

print(np.random.randint(1,100,8).reshape(2,4))  #Random numbers b/w a given range
print(np.random.random_sample((1,5)))
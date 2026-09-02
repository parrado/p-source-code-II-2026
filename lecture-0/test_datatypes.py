# Import required modules
from math import sqrt
from array import array

# Declare integer variable
var1=2
# Declare floating point variable
var2=2.0

# Perform operation with two variables
var3=var1*sqrt(var2)

# Print type of variable
print(var3,' is of type ',type(var3))

# Integer literal in binary
bin1=0b01010111  

print(bin1)
      
##################################
# var4 is boolean
var4=type(var3) is int
print(var4)

#######################################
str1=f'var3 value is: {var3}'
str2=f"var4 value is: {var4}"
str3=str1+str2
print(str3)
print(len(str3))

########################################
# Declare empty list
list1=[]

# Append elements to list
list1.append(5.0)
list1.append(4)

# Create list of strings
list2=["alex","juan","rigo"]
list2.pop(1)

# Create list initiliazed with zeroes
nData=20000000
list3=[0.0]*nData
list3.append(3.141592654)
print(list3[0])
print(list3[-1])



# Print some elements in declared lists
print(list1[1])
#print(list2[2])
print(list3[10000])
print(list3[20000000])
print(list3[20000001])

list4=[]
list4.append([0,1,2,3])
list4.append('Hello world')
list4.append(2.5)
print(list4[0][3],list4[1][2],list4[1][3],list4[2])


##############################################

array0=array('i',[1,2,3,4,5,6,7,8,9,10])
array1=array('d',[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])


print("array0 elements are ",array0.itemsize, "bytes")
print("array1 elements are ",array1.itemsize, "bytes")

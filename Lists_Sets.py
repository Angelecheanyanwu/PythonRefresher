# Lists and Sets Problem Statement below 

############Fill up a list using user input#

healty_food =[]

for i in range(10):
    x= input('Enter list of healthy foods :')
    healty_food.append(x)

print(healty_food)

############ List Comprehension to fill up list using user input

nothealthyfood=[input('enter food') for i in range(10) ]

print(nothealthyfood)



#######remove elements in a list using a loop
lista = ['angel', 'mary', 'gaberiel', 'mark', 'matthew', 'luke', 'angel', 'mary', 'gaberiel', 'mark', 'matthew', 'luke'
         'angel', 'mary', 'gaberiel', 'mark', 'matthew', 'luke','angel', 'mary', 'gaberiel', 'mark', 'matthew', 'luke']

newlist=[]

for i in lista:
    if lista.count('angel')!=0:
        lista.remove('angel')
    else:
        newlist.append(i)

print(newlist)

#####OR
lista = ['angel', 'mary', 'gaberiel', 'mark', 'matthew', 'luke', 'angel', 'mary', 'gaberiel', 'mark', 'matthew', 'luke'
         'angel', 'mary', 'gaberiel', 'mark', 'matthew', 'luke','angel', 'mary', 'gaberiel', 'mark', 'matthew', 'luke']

newlist=[]

for i in lista:
    if i =="angel":
        lista.remove('angel')
    else:
        newlist.append(i)

print(newlist)


############ Checking membership

food=['rice','beans', 'fanta', 'chicken', 'grapes']

print('x' in food)
print('beans'not in food)  #evalutes to true or false 

# ############ Sorting 
food=['rice','beans', 'fanta', 'chicken', 'grapes']

print('x' in food)
print('beans'not in food)  #evalutes to true or false 

############ Sorting 
food.sort() # ascending order
food.reverse()# descending order
print(food)

########### More List Comprehension
music=['kendrick', 'masego','drake','sza', 'summer','davido']

goodmusictaste=['sza','kendrick','summer','masego']

badmusictaste =  [i for i in music if i not in goodmusictaste]
print(badmusictaste)
 

###################  SETS ##################################

# Problem Statement:

# You are given two lists of integers, list_a and list_b. Write a Python program that performs the following tasks:

# Convert both lists into sets to remove duplicates.
# Find:

# The union of the two sets (all unique elements from both lists).
# The intersection of the two sets (common elements in both lists).
# The symmetric difference of the two sets (elements in either set but not both).
# Sort each of the resulting sets (union, intersection, symmetric difference) and convert them back into lists.
# Return a dictionary containing the sorted results with the following keys:
# "union"
# "intersection"
# "symmetric_difference"


list_a = [1, 2, 3, 4, 5, 5, 6]
list_b = [4, 5, 6, 7, 8, 8, 9]


set_a = set(list_a)
set_b= set(list_b)

# Perform set operations
union_set = set_a | set_b  # Union of two sets
intersection_set = set_a & set_b  # Intersection of two sets
symmetric_difference_set = set_a ^ set_b  # Symmetric difference of two sets

# Convert results to sorted lists
results = {
    "union": sorted(list(union_set)),
    "intersection": sorted(list(intersection_set)),
    "symmetric_difference": sorted(list(symmetric_difference_set))
}

# Print the final results
print(results)




################ SWAP AND REVERSE ALGORITHIMS##############


data =['a', 'b', 'c', 'd', 'e','f', 'g', 'h']

for index in range(len(data)//2):
    data[index], data[-index-1]= data[-index-1],data[index]
print(data)


####### Using the Reverse Iterator #############

data =['a', 'b', 'c', 'd', 'e','f', 'g', 'h']

data_reversed=[]

for i in reversed(data):
    data_reversed.append(i)

print(data)
print(data_reversed)


######## Reverse Using Slicing #############

data =['a', 'b', 'c', 'd', 'e','f', 'g', 'h']

data[:] = data[::-1]

print(data)

############## Sorting Algorithims ############# 

data =[1,32,54,38,65,11,100,-1,3]

data.sort()

print(data)


for i in range(len(data) //2):
    data[i],data[-i-1] = data[-i-1],data[i]
print(data)


####### Another Variation ######

print(sorted(data), reversed= True)

print(data)


######### SORTING 2D LIST ###########



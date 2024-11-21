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

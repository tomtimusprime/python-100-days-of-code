################################ Lists #########################################
# Lists: ordered, mutable, allows duplicate elements
my_list = ["bannana", "apple", "pineapple", "pear"]
print(my_list)

# List function
my_list2 = list()
print(my_list2)

# Lists in python can contain different types and can contain duplicate elements
my_list2 = [5, True, "Hi", "Hi"]

# -1 and -2, etc. are the last item, second to last item, etc.
item = my_list2[-2]

# see how many elements are in the list using the len() function
print(f"There are {len(my_list2)} items in the list.")

# Append items, specify where to place the item, and remove item(s)
my_list2.append("lemon")
my_list2.insert(1, "guava") # specify where to insert the item with the index as the first argument.

my_list2.pop() #returns the last item and also removes it. 

my_list2.remove("Hi") # can also remove a specific item

my_list2.clear() # removes everything from the list.

my_list.reverse()
my_list.sort() #changes the original list
new_list = sorted(my_list2) #if you want a whole new list and preserve the orginal

# Adding multiple items at once
my_list3 = [0] * 5 # output [0, 0, 0, 0, 0]

# concatenating lists
newest_list = my_list + my_list2
print(newest_list)

# slicing a list
numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = numberList[1:5] # start slicing at index 1 and stop at index 2 - the last index item is excluded
# if you don't specify a start index it'll start from the beginning and if you don't 
# specif an ending index, it'll go all the way to the end.
# You can also add a step index so if you want to do every other item, or every third item you can do that. 
a = numberList[::-1] # This will reverse your items
a = numberList[::2] # This will get every other item in your list - output 1, 3, 5, 7, 9 in this case.
print(a)

# If you are trying to copy a list and are simply assigning an old list to a new list it will point to the same place in memory and modify the original list
# as well as the new list. To avoid this, use the .copy() method.
list_copy = numberList.copy()
list_copy = list(numberList) # also accomplishes a copy
list_copy = numberList[:] # also accomplishes a copy

# an advanced way to create a new list with a modification to each item in the original list
b = [i*i for i in numberList]
print(b)




################################ Tuples #########################################
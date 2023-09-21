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
a = numberList[1:5] # start slicing at index 1 and stop at index 2
print(a)
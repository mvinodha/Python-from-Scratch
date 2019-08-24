# To remove elements or the entire list

marvel = ["Iron Man", "Captain America", "Hulk", "Black Panther", "Thor"]

# Using remove()

'''

marvel.remove("Hulk")

print(marvel)

'''

# Using pop()

"""

# Remove's the last element

'''
marvel.pop()

print(marvel)
'''

# Remove's the indexed element

marvel.pop(2)

print(marvel)

"""

# Using del()

"""

# To delete a particular element

'''

del marvel [1]

print(marvel)

'''

# To delete the entire list
# No traces of it will be present

del marvel

print(marvel)

"""

# Using clear()
# Only the elements will be deleted, not the list
# Output will be an empty list

marvel.clear()

print(marvel)

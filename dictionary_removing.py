series = {"Name": "Game of Thrones",
          "Network": "HBO",
          "Genre": "Drama",
          "Awards": 80}

# Using pop()


# Remove's the last element

'''
series.popitem()

print(series)

'''
# Remove's the indexed element using key

series.pop("Awards")

print(series)



# Using del()

"""
# To delete a particular element using the key
'''
del series ["Network"]

print(series)
'''

# To delete the entire dictionary
# No traces of it will be present
'''
del series

print(series)
'''
"""

# Using clear()
# Only the elements will be deleted, not the dictionary
# Output will be an empty set
'''

series.clear()

print(series)

'''

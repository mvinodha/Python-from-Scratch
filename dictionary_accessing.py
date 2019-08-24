series = {"Name": "Game of Thrones",
          "Network": "HBO",
          "Genre": "Drama",
          "Awards": 80}

# Using slice operator

'''
print(series["Network"])
'''

# Using get()

'''
net=series.get("Network")
print(net)
'''

#Using for

# To get the keys

'''
for x in series:
    print(x)
'''

# To get the values
'''
for x in series.values():
    print(x)
'''
# To get both the key and values

for x,y in series.items():
    print(x,y)

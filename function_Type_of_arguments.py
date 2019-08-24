'''
# Required argument

def add(a,b):
    c = a+b
    print(c)

add(10,20)



# Keyword argument

def songs(name, artist):
    print("Name:", name, "Artist:", artist)

songs(name="Bohemian Rhapsody", artist="Freddie Mercury")



# Default argument

def songs(artist,name="Bohemian Rhapsody"):
    print("Name:", name, "Artist:", artist)

songs(artist="Freddie Mercury")

'''

# Variable Length argument

def songs(* details):
    for x in details:
        print(x)

songs("Freddie Mercury", "Bohemian Rhapsody", "Queen", "Rock and roll", "Lead Singer")

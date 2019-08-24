#This program is used to build a star pattern using for loop

#To print "*" in ascending order

print("\t This program builds a pattern")

limit = int ( input ("Enter the number of lines you want to print the pattern"))
'''
for X in range(0 , limit+1 ):
    
    for Y in range(X):
        
        print("*",end="")

    print("\n")

'''
#To print "*" in descending order

'''
for X in range(0 , limit ):
    
    for Y in range(X,limit):
        
        print("*",end="")

    print("\n")
'''

#To print "numbers" in ascending order

for X in range(0 , limit+1 ):
    
    for Y in range(1,X+1):
        
        print(Y,end="")

    print("\n")

    
    
        

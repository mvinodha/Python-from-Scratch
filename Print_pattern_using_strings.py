limit = int ( input ("Enter the number of lines you want to print the pattern"))

#Using while loop

'''
i=0

while i<=limit:
    print("*" * i)
    i+=1
'''

#Using for loop

for x in range(0, limit+1):
    print("*" * x)

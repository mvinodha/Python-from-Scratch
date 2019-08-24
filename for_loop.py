
#Simple for loop Collection Iteration

'''
my_list = ["Marvel Cinematic universe", 4 ,
           "Captain America", "Hulk",
           "Iron Man", "Black Widow" ]

for x in my_list:
    print(x)
'''

#Simple for loop for String iteration

'''
for x in "Hawk eye":
    print(x)
'''

#For with else
'''
my_list = ["Marvel Cinematic universe", 4 ,
           "Captain America", "Hulk",
           "Iron Man", "Black Widow" ]

for x in my_list:
    print(x)
else:
    print("You have reached the end")
'''

#For with break
'''
my_list = ["Marvel Cinematic universe", 4 ,
           "Captain America", "Hulk",
           "Iron Man", "Black Widow" ]

for x in my_list:
    if x=="Hulk":   #Stops printing with hulk
        break
    print(x)
'''

#For with continue
'''
my_list = ["Marvel Cinematic universe", 4 ,
           "Captain America", "Hulk",
           "Iron Man", "Black Widow" ]

for x in my_list:
    if x=="Hulk":   #Prints excluding Hulk
        continue
    print(x)
'''

#Range using - Single parameter
'''
for x in range(5):   #Prints till 4 starting from 0
    print(x)
'''

#Range using - Two parameters
'''
for x in range(5,10):  #Prints till 9 starting from 5
    print(x)
'''

#Range using - Three parameters
'''
for x in range(5,50,3): #Increments by 3 starting from 5
    print(x)
'''

#Nested for loop

my_list1 = ["Marvel Cinematic Universe" ]

my_list2 = ["Captain America", "Hawkeye",
           "Iron Man", "Black Widow" ]

my_list3 = ["Chris Evans", "Jeremy","Robert Jr." , "Scarlet"]

for x in my_list1:
    print(x)
    for y in my_list2:
        print(y)
        for z in my_list3:
            print(z)





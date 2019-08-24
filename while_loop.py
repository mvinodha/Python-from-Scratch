#A program making using of the while loop


'''
i=1
while i<10:
	print(i)
	i+=1
'''


#Using while else
'''
i=0
while i<10:
	i+=1
	print(i)

else:
	print("The loop has been exhausted")
'''


#Using while with break

'''
i=1
while i<10:
	print(i)
	if i== 5:      #Prints till 5 excluding even the else block
		break
	i+=1
	 
else:
	print("The loop has been exhausted")
'''

#Using continue instead of break(infinite loop)
'''
i=1
while i<10:
	print(i)
	if i== 5:
		continue    #Causes an infinte loop
	i+=1
	 
else:
	print("The loop has been exhausted")
'''


i=0
while i<10:
	i+=1
	if i== 5:
		continue    # Prints excluding 5

	print(i)
else:
	print("The loop has been exhausted")

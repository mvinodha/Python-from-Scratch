#Program to print multiplication table


print("Program to build the desired multiplication table")

number= int(input("Enter the number whose table you would like to print:"))

range_no= int(input("Specify the range in which you want the number to be printed:"))

print("Multiplication table of: ", number)

'''
i=1

while i <= range_no:
    pdt=number*i
    print(number, "*" , i, "=" , pdt)
    i+=1
    
'''

#Using for loop instead of while


for i in range(1,range_no+1):
    pdt=number*i
    print(number, "*" , i, "=" , pdt)

#Program to print multiplication table using string formating


print("Program to build the desired multiplication table")

number= int(input("Enter the number whose table you would like to print:"))

range_no= int(input("Specify the range in which you want the number to be printed:"))

print("Multiplication table of: ", number)

for i in range(1,range_no+1):
    pdt=number*i
    print("{1} * {0} = {2} " .format (i, number, pdt))
   


def add(a,b):
    c=a+b
    print(c)

def sub(a,b):
    c=a-b
    print(c)

def mul(a,b):
    c=a*b
    print(c)

def div(a,b):
    c=a/b
    print(c)

print("This is a calculator")
choice=int(input("Specify the operation you have to perform: 1. Addition \n 2. Subtraction \n 3. Multiplication\n 4.Division"))
print("Enter any two numbers")
a=int(input("a:"))
b=int(input("b:"))

if(choice==1):
    add(a,b)

elif(choice==2):
    sub(a,b)

elif(choice==3):
    mul(a,b)

elif(choice==4):
    div(a,b)

else:
    print("Select a valid option")


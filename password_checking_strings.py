#Program to validate username and password
#Check for length, it need not be case sensitive, remove white spaces

username= "batman"
password= "batman"

string_name=input("Enter the user name: ")
string_password=input("Enter the password: ")

name = string_name.strip()
pswrd = string_password.strip()

if len(name)>=6 and len(pswrd)>=6:

    if username==name.lower() and password==pswrd.lower():
        print("Valid user")
    else:
        print("Invalid user")

else:
    print("Make sure your password and username's length is greater than 6")
    

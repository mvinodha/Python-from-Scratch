#Simple program making use of identity operator
username= "batman"
password= "batman"


name=input("Enter the user name: ")
pswrd=input("Enter the password: ")

print(name)
print(name is "superman")

if name is "batman":
    print("Valid user")
else:
    print("Invalid user")


#Simple program making use of identity operator
username= "batman"
password= "batman"

name="superman"
pswd="ironman"

print(name is "superman" and pswd is "ironman")

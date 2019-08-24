 #A simple prOgram to validate a user

'''
username= False
password= False

if username or not password :
    print("It is a valid user")
else:
    print("Not a valid user")
'''

username= "batman"
password= "batman"

name=input("Enter the user name: ")
pswrd=input("Enter the password: ")

if username!=name and password!=pswrd:
    print("Invalid user")

else:
    print("Valid user")



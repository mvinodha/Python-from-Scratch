
username= "batman"
password= "batman"

while True:
    str_name=input("Enter the user name: ")
    if username == str_name:
        while True:
            str_pswrd=input("Enter the Password: ")
            if password == str_pswrd:
                print("Login Successful")
                break
            else:
                print("Your password is incorrect")
        break
    else:
        print("Your username is incorrect")
      
    
        
        





# A car game using looping and decision making

print("Welcome Champion!")

print("Press 'Help' to know the control or you can proceed directly")

while True:

    command_one =input("Enter the command to begin:")

    if command_one == "help":
        print("This is how the game works")
        print("Start --> to start your car")
        print("Run --> to get your car moving")
        print("Stop --> to stop your car")

    elif command_one == "start":

        print("Your car is ready to move")

        command_two = input("Enter the command")

        if command_two == "run":

            print("Your car is moving")

            command_three = input("Enter the command")

            if command_three == "stop":

                print("Congrats! You have completed the race")

            else:

                 print("Oops! You have to press stop")

        else:

            print("Oops! You have to press run")
    
    




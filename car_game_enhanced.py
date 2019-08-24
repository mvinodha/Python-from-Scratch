
while True:

    command_one =input("Enter the command: ")

    if command_one == "help":
        print("This is how the game works")
        print("Start --> to start your car")
        print("Run --> to get your car moving")
        print("Stop --> to stop your car")

    elif command_one == "start":

        print("Your car is started")

        continue

    elif command_one == "run":

        print("Your car is moving")


    elif command_one == "stop":

         print("Your car is stopped")

         break

    else:

        print("Try again!")

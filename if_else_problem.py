print("First Semester Marks Calculator")

name=input("Enter the name: ")


department=input("Enter the department in which the student is enrolled: ")



print("Enter the marks scored in the following subjects:")

mark_1= int(input("English: "))

mark_2= int(input("Maths: "))

mark_3= int(input("Physics: "))

mark_4= int(input("Chemistry: "))

mark_5= int(input("C programming: "))

check=input("If the above entered marks are correct press 'y' else press 'n' ")



if check == "y":

    print("Your marks have been updated succesfully\n")

    total = mark_1 + mark_2 + mark_3 + mark_4 + mark_5

    print("The total marks secured by the student for the first semester is: " , total)

    average = total/5

    print ("The average result of the marks scored is: " , average)

    if mark_1 >= 50 and mark_2 >= 50 and mark_3 >= 50 and mark_4 >= 50 and mark_5 >= 50:

        print ("Result: Pass")

    else:

        print ("Result: Fail")

else:

    print("Please re-enter your marks correctly")


student_name=input("Enter the name:")
student_number=int(input("Enter the rollnumber:"))
student_class=input("Enter the class in which the student studies:")
student_email=input("Enter the mail id:")
mail=student_email+"@xyz.com"
'''The below format
It is for multiplestatements in single line'''
'''This is for the user defined input
mark1,mark2,mark3,mark4,mark5=100,55,95,30,74'''
print("Enter the marks scored continuously for 5 subjects")
mark1=int(input("Mark1:"))
mark2=int(input("Mark2:"))
mark3=int(input("Mark3:"))
mark4=int(input("Mark4:"))
mark5=int(input("Mark5:"))
sports=input("Enter the games as played by the student:")
#The below format is for multiline expressions
sum=mark1+\
    mark2+\
    mark3+\
    mark4+\
    mark5
average=sum/5
print('\t \tReport card for the student',student_name)
print("\n\tName:",student_name)
print("\n\tRollnumber:",student_number)
print("\n\tClass: "+student_class)
print("\n\tMail id:",mail)
print("\n\tSports:",sports)
print("\n\tMarks scored in the last exam:",sum)
print("\n\tThe average marks scored:",average)

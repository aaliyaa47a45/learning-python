print("Student Result Analyser")

name = input("Enter student name:")

physics = int(input("Enter Physics marks:"))
chemistry = int(input("Enter Chemistry marks:"))
maths = int(input("Enter Maths marks:"))

average = (physics+chemistry+maths)/3

print("Average marks:",average)

if average>=90:
    grade = "A+"
elif average>=75:
    grade="A"
elif average>=60:
    grade="B"
elif average>=40:
    grade="C"
else:
    grade= "Fail"

print("Grade:",grade)



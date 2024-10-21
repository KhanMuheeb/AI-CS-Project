Physics = int(input("Enter Marks in Physics"))
Chemistry = int(input("Enter Marks in Chemistry"))
Bio = int(input("Enter Marks in Biology"))
Maths = int(input("Enter Marks in Maths"))
Computer = int(input("Enter Marks in Computer"))
total_Marks = Physics+Chemistry+Bio+Maths+Computer
percentage = (total_Marks/500)*100
if percentage >= 90 :
    grade = "A"
elif percentage >= 80 :
    grade = "B"
elif percentage >= 70 :
    grade = "C"
elif percentage >= 60 :
    grade = "D"
elif percentage >= 50 :
    grade= "E"
else :
    grade = "F" 
print(percentage,"percentage")
print(grade,"grade")
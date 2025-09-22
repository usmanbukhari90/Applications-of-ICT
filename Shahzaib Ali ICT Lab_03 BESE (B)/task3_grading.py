marks = int(input("enter your marks here :"))

if marks>=90 and marks<=100 :
    grade = "A"
elif marks>=75 :
    grade = "B"
elif marks>=60 :
    grade = "c"
elif marks>=40 :
    grade = "F" 
elif marks>100 :
    grade = "Your marks are not valid , incorrect numbers"       
    print("Your Grade is ;", grade)       
else:
    print("You are badly Fail , BASTARD")
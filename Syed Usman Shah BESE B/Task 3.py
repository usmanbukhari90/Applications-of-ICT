marks = int(input("Enter Your Marks: "))

if marks>=90 and marks<=100:
    grade = "A"
elif marks>=75 and marks<=89:
    grade = "B"
elif marks>=60 and marks<=74:
    grade = "C"
elif marks>=50 and marks<=59:
    grade = "D"
elif marks<50:
    grade="F"
else:
    print("Invalid Input")
    exit()
print("Your Grade is:",grade)
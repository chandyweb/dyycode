score = int(input("input your score:"))
if (score >= 90):
    print(" Grade A")
elif ( score >=80 and score <=89):
    print (" Grade B")
elif ( score >=70 and score <=79):
    print("Grade C")
elif ( score >=60 and  score <= 69):
    print("Grade D")
else:
    print("Grade F")


num1 = int(input("Num1 : "))
num2 = int(input("Num2 : "))
operation = str(input("Operation = "))

if operation == "+":
    print("Result = ", num1 + num2)
elif operation == "-":
    print("Result = ", num1 - num2)
elif operation == "*":
    print("Result = ", num1 * num2)
elif operation == "/":
    print("Result = ", num1 / num2)
else:
    print("I'm Sorry for my mistake")

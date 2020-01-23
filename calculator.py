number1= input("Enter first number")
if not number1.isdigit():
    number1 = Input("wrong input try again")

number2= input("Enter second number")
if not number2.isdigit():
    number2 = Input("wrong input try again")

operation= input("Choose the operation")

number1 = int(number1)
number2= int(number2)
if operation == '+':
    answer = number1+number2

elif operation == '-':
    answer = number1-number2
elif operation == '*':
    answer = number1*number2

elif operation == '/':
    answer = number1/number2

print("The answer is %d" %answer)


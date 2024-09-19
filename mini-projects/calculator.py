operator = input("enter an operator (+ - * /): ")
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))

if operator == "+":
	result = num1 + num2
elif operator == "-":
	result = num1 - num2
elif operator == "*":
	result = num1*num2
elif operator == "/":
	result = num1/num2
else:
	print(f"{operator} is not a valid operator")
	break
print(round(result,3))
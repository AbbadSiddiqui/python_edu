#Projects#

#Python Calculator V1#
num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))
operator = input("Choose your operator (+,-,*./.%): ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "%":
    print(num1 % num2)
else:
    print("Invalid operator")
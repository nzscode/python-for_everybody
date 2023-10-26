num1 = int(input("enter num1"))
num2 = int(input("enter num2"))
operand = input("enter  +, - , * ,  /")

if operand  == "+":
    print(num1 + num2)
elif operand == "-":
    print(num1 - num2)
elif operand == "*":
    print(num1 * num2)
else:
    print(float(num1) / float(num2))
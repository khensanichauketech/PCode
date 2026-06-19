def values():
    operator = input("Enter operator ( + - * /): ")
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    calculate(operator, num1, num2)

def calculate(operator, num1, num2):
    if operator == "+":
        results = num1 + num2
        print(results)
        values()
    elif operator == "-":
        results = num1 - num2
        print(results)
        values()
    elif operator == "*":
        results = num1 * num2
        print(results)
        values()
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by 0")
            num2 = float(input("Enter a number again: "))
            calculate(operator, num1, num2)
        else:
            results = num1 / num2
            print(results)
            values()
    else:
        print("Invalid operator!")
        operator = input("Enter operator ( + - * /): ")
        calculate(operator, num1, num2)
        


if __name__ == "__main__":
    values()
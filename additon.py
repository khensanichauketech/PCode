print("We are learning maths")
lower = int(input("Lower number: "))
upper = int(input("Upper number: "))
counter = 0

while lower <= upper:
    counter += lower
    lower += 1

print(f"The sum is: {counter}")
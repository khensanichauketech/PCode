import random

name = input("Your name: ")
passcode = int(input("Passcode: "))
counter = 0

num = random.randint(1000, 99999)

while num != passcode:
    num = random.randint(1000, 99999)  # regenerate number
    counter += 1

print(f"Matched after {counter} tries")
print("Number:", num)
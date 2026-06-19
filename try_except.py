hours_worked = input("Enter hours: ")
rate = input("Pay rate: ")


#Function
def computepay(x, y):
    if x > 40:
        base_hours = 40
        overtime = (x - base_hours) * 15
        pay = float((base_hours * y) + overtime)
        return pay
    else: 
        pay = float(x * y)
        return pay


#Try and Except
try:
    x = int(hours_worked)
    y = int(rate)
    
except:
    x = -1
    y = -1


#If statement
if x > 0 and y > 0:
    print("Captured")
    salary = computepay(x, y)
    print(f"R {salary}") 
else:
    print("Error, please enter numeric values")





name=input("Enter your name:")
print(name)
print("Select the operation you want:")
print("1. Addition (a)")
print("2. Subtraction (s)")
print("3. Multiplication (m)")
print("4. Division (d)")
operation_used = input("Enter the option number for the input value:")
 
if operation_used == "1":
    x = float(input("Enter addition num1 (a):"))
    y = float(input("Enter addition num2 (b):"))
    z = x + y
    print(f"Addition (a) = {z}")

elif operation_used == "2":
    x = float(input("Enter subtraction num1 (a):"))
    y = float(input("Enter subtraction num2 (b):"))
    z = x - y 
    print(f"Subtraction (s) = {z}") 

elif operation_used == "3":
    x = float(input("Enter multiplication num1 (a):"))
    y = float(input("Enter multiplication num2 (b):"))
    z = x * y  
    print(f"Multiplication (m) = {z}")

elif operation_used == "4":
    x = float(input("Enter division num1 (a):"))
    y = float(input("Enter division num2 (b):"))
    z =  x / y 
    print(f"Division (d) = {z}")

else:
    print("Invalid option selected for the operation used")

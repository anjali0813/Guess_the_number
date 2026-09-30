#CALCULATOR

a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))

sum = a + b
difference = a - b
product = a * b
divide = a / b
remainder = a % b
power = a ** b

print("------------START OPERATION-------------")

print("Choice of operations :\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus/Remainder\n6. Power")
choice = input("Enter your choice of operation - ('1','2','3','4','5','6') : ")

if (choice == '1'):
    print("Sum of the numbers = ",sum)
    
elif (choice == '2'):
    print("Difference of the numbers = ",difference)

elif (choice == '3'):
    print("Product of the numbers = ",product)

elif (choice == '4'):
    print("Quotient of the numbers after division = ",divide)

elif (choice == '5'):
    print("Remainder after division = ",remainder)

elif (choice == '6'):
    print("a to the power b = ",power)

else:
    print("INVALID OPERATION")

print("------------OPERATION COMPLETED-------------")
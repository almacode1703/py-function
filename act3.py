# Add
def add(x,y):
    return x+y

#sub
def subtract(x,y):
    return x-y

#mul
def multiply(x,y):
    return x*y

#div
def division(x,y):
    return x/y

# We will ask user to provide inputs
print("Please select operation")
print("a. Add")
print("b. Subtract")
print("c. Multiplication")
print("d. Division")

choice = input("Please enter your choice (a/b/c/d) : ")

num1 = int(input("Please  entner first number : "))
num2 = int(input("Please  entner second number : "))

if(choice == 'a'):
    print("Result of Addition is : ", add(num1, num2))

elif(choice == 'b'):
    print("Result of Division is : ", subtract(num1, num2))

elif(choice == 'c'):
    print("Result of Multiplication is : ", multiply(num1, num2))

elif(choice == 'd'):
    print("Result of Division is : ", division(num1, num2))

else:
    print("Enter valid option")

# --Take a user's name and greet them.
n=input("Enter a name:")
print("Hello, " + n)

# --Add two numbers entered by the user.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=a+b
print("The sum is:", c)

# --Find the area of a rectangle.
length=int(input("Enter the length of the rectangle:"))
width=int(input("Enter the width of the rectangle:"))
area=length*width
print("The area of the rectangle is:", area)    

# --Convert Celsius to Fahrenheit.
celsius=float(input("Enter temperature in Celsius:"))
fahrenheit=(celsius*9/5)+32
print("Temperature in Fahrenheit:", fahrenheit)

# --Swap two variables without a third variable.
a = 10
b = 20
a, b = b, a
print("a =", a)
print("b =", b)

# --Find whether a number is even or odd.
num=int(input("Enter a number:"))
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")

# --Find the largest of three numbers.
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))
if (x > y) and (x > z):
    print(x, "is the largest number.")
elif (y > x) and (y > z):
    print(y, "is the largest number.")
else:
    print(z, "is the largest number.")  

# --Calculate simple interest.
principal=float(input("Enter the principal amount:"))
rate=float(input("Enter the rate of interest:"))
time=float(input("Enter the time in years:"))
simple_interest=(principal * rate * time) / 100
print("The simple interest is:", simple_interest)

# --Generate a multiplication table.
num=int(input("Enter a number to generate its multiplication table:"))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)
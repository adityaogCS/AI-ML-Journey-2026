# --Sum of digits
num = int(input("Enter a number: "))
total = 0
while num > 0:
    digit = num % 10
    total = total + digit
    num =num // 10

print("Sum of digits:", total)

# --Reverse a number
num=int(input("Enter a number:"))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print("Reversed number:", reverse)

# --Armstrong number
num = int(input("Enter a number: "))
original = num

digits = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total += digit ** digits
    num //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# --Prime number
num=int(input("Enter a number:"))
if num>1:
    for i in range(2, num):
        if (num % i == 0):
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

# --Factorial of a number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("The factorial of", num, "is:", factorial)

# --Fibonacci series
n_terms=int(input("Enter the number of terms: "))
n1, n2 = 0, 1
count = 0
if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci sequence up to", n_terms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# --GCD and LCM
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b

while y != 0:
    x, y = y, x % y

gcd = x
lcm = (a * b) // gcd

print("GCD =", gcd)
print("LCM =", lcm)

# --Number guessing game
import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number: "))

    if guess == number:
        print("Correct!")
        break

    print("Try again")

# --Password validator
password=input("Enter a password:")
if len(str(password)) < 8:
    print("Password must be at least 8 characters long.")
elif not any(char.isdigit() for char in str(password)):
    print("Password must contain at least one digit.")
elif not any(char.isupper() for char in str(password)):
    print("Password must contain at least one uppercase letter.")
elif not any(char.islower() for char in str(password)):
    print("Password must contain at least one lowercase letter.")
elif not any(not char.isalnum() for char in password):
    print("Password must contain at least one special character.")
else:
    print("Password is valid.")

# --Basic ATM menu (deposit, withdraw, balance)
balance = 1000

while True:
    print("\n----- ATM MENU -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Deposit Successful")
        print("Current Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful")
            print("Current Balance:", balance)
        else:
            print("Insufficient Balance")
            print("Current Balance:", balance)

    elif choice == "3":
        print("Current Balance:", balance)

    elif choice == "4":
        print("Thank you for using ATM!")
        print("Total Balance:", balance)
        break

    else:
        print("Invalid Choice")

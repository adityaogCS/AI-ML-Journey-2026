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

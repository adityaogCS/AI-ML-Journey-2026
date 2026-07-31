# ----------------------------WHILE LOOP QUESTIONS (PHASE 1)---------------------------------------
# print all number from 1 to 10 using loop
# i=1
# while i<=10:
#     print(i)
#     i+=1

#  print all numbers from 10 down to 1 in reverse order
# i=10
# while i>= 1:
#     print(i)
#     i-=1

# print all even numbers from 1 to 100
# num = 1
# while num <= 100:
#     if num % 2 == 0:
#         print(num)
#     num += 1

# print all odd numbers between 1 to 100
# num=1
# while num <=100:
#     if num %2!=0:
#         print(num)
#     num+=1

# print the multiplication number of a table n from n*1 to n*10
# n=int(input("enter a table:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

# calculate and print the sum of first n natural numbers
# n= int(input("Enter a number:"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i+=1
# print(sum)

# calculate the sum of all even numbers from 1 up to n
# n=int(input("enter a Number:"))
# i=1
# sum=0
# while i<=n:
#     if i%2==0:
#         sum=sum+i
#     i+=1
# print("the sum of even integers is :",sum)

# Calculate the sum of all odd numbers from 1 to n
# n=int(input("enter the number:"))
# sum=0
# i=1
# while i<=n:
#     if i%2!=0:
#         sum=sum+i
#     i+=1
# print("The sum of all odd numbers is:", sum)

# calculate and print the factorial of a given number
# n = int(input("Enter a number: "))
# factorial = 1
# i = 1
# while i <= n:
#     factorial = factorial * i
#     i += 1
# print("Factorial =", factorial)

# find and print the product of all digits of a given number
# n=int(input("Enter a number"))
# product=1
# while n > 0:
#     digit = n % 10        # Get the last digit
#     product = product * digit
#     n = n // 10           # Remove the last digit

# print("Product of digits =", product)

# count and print the total number of digits in a given number
# n = int(input("Enter a number: "))

# count = 0

# while n > 0:
#     digit = n % 10
#     print(digit)
#     count += 1
#     n = n // 10

# print("Total number of digits =", count)

#  reverse the given value and print the reversed value
# Take input from the user
# n = int(input("Enter a number: "))

# reverse = 0

# while n > 0:
#     digit = n % 10           # Get the last digit
#     reverse = reverse * 10 + digit
#     n = n // 10              # Remove the last digit

# print("Reversed number =", reverse)

# check weather the given number is a palindrome
# n=int(input("Enter a number:"))
# original=n
# reverse=0
# while n>0:
#     digit = n%10
#     reverse = reverse * 10 + digit
#     n = n //10
# if original == reverse:
#     print("the number is Palindrome")
# else:
#     print("the number is not a palindrome")

# find and print the sum of digits of the given number
# n=int(input("Enter the number:"))
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# print(sum)
# check weathewr the number is a armstrong number or not
# n=int(input("Enter a number:"))
# original=n
# count=0
# temp=n
# while temp >0:
#     count+=1
#     temp= temp//10

# sum=0
# temp=n
# while temp >0:
#     digit=temp%10
#     sum=sum+(digit**count)
#     temp=temp//10
# if original == sum:
#     print("Armstrong")
# else:
#     print("not armstrong")

# check weather the given number is a perfect number or not
# n=int(input("Enter a number:"))
# i=1
# sum=0
# while i<n:
#     if n%i ==0:
#         sum= sum+i
#     i+=1
# if sum == n:
#     print(n, "is a perfect number")
# else:
#     print(n, "is not a perfect number")

# print all prime numbers between 1 to 100
# for num in range(2, 101):
#     is_prime=True

#     for i in range(2, num):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(num)
# import random
# pin=random.randint(1000,9999)
# print("Generated Pin:", pin)

# for num in range(2,num):
#     if num>1:
#         for i in range(2, num):
#             if num%i==0:
#                 break
#             else:
#                 print(num)

# n=int(input("Enter a number"))
# sum_even=0
# for i in range(1, n+1):
#     if i%2 ==0:
#         sum_even= sum_even+i
#         i+=1
# print(sum_even)

# n=int(input("Enter a table number:"))
# for i in range(1, 11):
#     if i==5:
#         continue
#     print(n*i)

# while True:
#     n= int(input("Enter a number: "))
#     if 1<=n<=10:
#         print("Thanks")
#         break
#     else:
#         print("Enter the number again: ")
# numbers= [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# positive_number_count=0
# for i in numbers:
#     print(i)
#     if i>0:
#         positive_number_count+=1
# print("Final number count is:", positive_number_count)    
# n=int(input("Enter a number:"))
# sum=0
# for i in range(0, n+1):
#     if i%2==0:
#         sum=sum+i
#         i+=1
# print("sum of even number upto the given number",sum)
# n=int(input("Enter a number:"))
# for i in range(1,11):
#     table=i*n
#     if i==5:
#         continue
#     print(table)   
# str="Aditya"
# reversed_str=""
# for char in str:
#     reversed_str= char+ reversed_str
# print(reversed_str)

# input_str="teteer"
# for char in input_str:
#     print(char)
#     if input_str.count(char)==1:
#         print("non repeating first element in the string is:", char)
#         break
# n=int(input("Enter a number:"))
# factorial=1
# while n>0:
#     factorial=factorial*n
#     n-=1
# print("factorial is:",factorial)        
# for i in range(4):
#     n=int(input("enter a number from 1 to 10:"))
#     if 1<n<10:
#         print("valid input, well done!")
#     else:
#         print("invalid input")
# else:
#     print("you have exceeded all 4 attempts!")
# num=int(input("Enter a number:"))

# for i in range(2,num):
#     if num%i ==0:
#         print("it is not a prime number")
#         break
# else:
#     print(" it is a prime number")
# item=['apple', 'banana', 'orange', 'apple', 'mango']
# count=[]
# for i in item:
#     list.count(item)
#     print(count)
# import time
# max_retries=5
# attempts=0
# wait_time=1
# while attempts<max_retries:
#     print("Attempts:",attempts+1,"wait time:",wait_time)
#     time.sleep(wait_time)
#     wait_time*=2
#     attempts+=1
def is_pallindrome(num):
        original=num
        reverse=0
        while num>0:
            digit=num%10
            reverse=reverse*10+digit
            num=num//10
            return original==reverse
            num=int(input("Enter a number:"))
            if is_palindrome(num):
                print("True")
            else:
                print("False")

# --------------------------------PRINT FUNCTION-----------------------------------
print("hey, I am a \"good boy\"\n and this viewer is also a good boy")
print("hey",6,7,sep="-")
print("hey",6,7,sep="-",end=" 009\n")
# -------------------------------TYPECASTING-----------------------------------
old_age = input("Enter your old age:")
new_age = int(old_age) + 2
print(new_age)
# ---------------------------------------STRING SLICING-----------------------------------
str="Aditya_Kumar"
print(str[-len(str):-2]) #slicing very important topic
# --------------------------------------STRING ENDS WITH-----------------------------------
str="Aditya_Kumar"
print(str.endswith("ar")) #endswith is a function which checks whether the string ends with the given substring or not
# -------------------------------------STRING STARTS WITH-----------------------------------
str="Aditya_Kumar"
print(str.startswith("Adi")) #startswith is a function which checks whether the string starts with the given substring or not
# ------------------------------------STRING CAPITALIZE-----------------------------------
str="my name is aditya kumar"
str=str.capitalize()            #capitalize is a function which converts the first character of the string to uppercase and the rest to lowercase  
print(str)
# ------------------------------------STRING REPLACE-----------------------------------
str="I am studying python from last 2 months"
str = str.replace("python","java") #replace is a function which replaces the old substring with the new substring in the given string
print(str)
# -----------------------------------STRING CONCATENATION-----------------------------------
first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
print("Your full name is: " + first_name + " " + last_name)
print("Length of your full name is:", len(first_name + " " + last_name)) #len is a function which returns the length of the given string
# -------------------------------------------------------------AGE CALCULATOR-----------------------------------
age = int(input("Enter your age: "))
if age <= 12:
    print("You are a childhood")
elif age > 12 and age <= 19:
    print("You are a teenager")
elif age > 19 and age <= 35:
    print("Younge adulthood")
elif age > 35 and age <= 50:
    print("Middle adulthood")
elif age > 51 and age <= 65:
    print("Senior citizenship")
else:
    print("You are in old age")
# --------------------------------GRADE CALCULATOR-----------------------------------
marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
elif marks >= 35 and marks < 70:
    print("Grade D")
elif marks >= 0 and marks < 35:
    print("Grade F")
else:
    print("Invalid marks")
# --------------------------------EVEN OR ODD-----------------------------------
number= int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even")
else:    print("The number is odd") 
# --------------------------------GREATEST NUMBER-----------------------------------
first_number= int(input("Enter the first number: "))
second_number= int(input("Enter the second number: "))
third_number= int(input("Enter the third number: "))
if first_number > second_number and first_number > third_number:
    print("The greatest number is:", first_number)
elif second_number > first_number and second_number > third_number:
    print("The greatest number is:", second_number)
else:    print("The greatest number is:", third_number)
#-------------------------------TYPECASTING-----------------------------------
number= int(input("Enter a number: "))
if number % 7 == 0:
     print("The number is multiple of 7")
else:    print("The number is not multiple of 7")
# --------------------------------ARMSTRONG NUMBER-----------------------------------
n = int(input())
s = 0
t = n
while n > 0:
     digit = n % 10
     s += digit ** 3
     n //= 10
if s == t:
     print("Armstrong number")
else:
     print("Not an Armstrong number")
# --------------------------------LISTS-----------------------------------
marks=[90,80,70,60,50]
print(marks[1:3]) #list indexing
# -------------------------------LISTS-----------------------------------
movie1 = input("Enter the name of the first movie: ")
movie2 = input("Enter the name of the second movie: ")
movie3 = input("Enter the name of the third movie: ")

movies = [movie1, movie2, movie3]
print(movies)
# -----------------------------------PALINDROME CHECKING-----------------------------------
Lists = [1,2,3,2,1]
copy_Lists = Lists.copy()
copy_Lists.reverse() #reverse is a function which reverses the list
if Lists == copy_Lists:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")
# -----------------------------------LIST METHODS-----------------------------------
numbers = [1, 2, 3, 4, 5]
numbers.append(6) #append is a function which adds an element at the end of the list
print(numbers)
numbers.insert(0, 0) #insert is a function which adds an element at the specified index of the list
print(numbers)
numbers.remove(3) #remove is a function which removes the first occurrence of the specified element from the list
print(numbers)
numbers.pop() #pop is a function which removes the last element from the list
print(numbers)
numbers.pop(0) #pop is a function which removes the element at the specified index from the list
print(numbers)
numbers.clear() #clear is a function which removes all the elements from the list
print(numbers)
numbers = [1, 2, 3, 4, 5]
numbers.sort() #sort is a function which sorts the elements of the list in ascending order
print(numbers)
numbers.sort(reverse=True) #sort is a function which sorts the elements of the list in descending order
print(numbers)
numbers.reverse() #reverse is a function which reverses the order of the elements in the list
print(numbers)
numbers = [1, 2, 3, 4, 5]
print(numbers.index(3)) #index is a function which returns the index of the firstoccurrence of the specified element in the list
print(numbers.count(2)) #count is a function which returns the number of occurrences of the specified element in the list
# --------------------------------TUPLES-----------------------------------
Tup = ("A", "B", "C", "D", "A", "A", "B", "C", "A", "A", "B", "C", "A")
print(Tup.count("A"))
List = ["A", "B", "C", "D", "A", "A", "B", "C", "A", "A", "B", "C", "A"]
print(List.sort())
print(List) 
# --------------------------------TUPLE METHODS-----------------------------------
sup = (1,2,3,4,5,6,7,8,9,7,7,7)
print(sup.count(6)) #count is a function which returns the number of occurrences of the specified element in the tuple
print(sup.index(5)) #index is a function which returns the index of the first occurrence of the specified element in the tuple
print(sup.count(7)) #count is a function which returns the number of occurrences of the specified element in the tuple
print(sup.index(7)) #index is a function which returns the index of the first occurrence of the specified element in the tuple
#-------------------------------DICTIONARY-----------------------------------
dictionary={
    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat" : "a small animal",    
}
print(dictionary)
#-------------------------------SET -----------------------------------
Subjects = {
    "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c",
}
print(Subjects) #set is a collection which is unordered, unchangeable*, and unindexed. In Python sets are written with curly brackets.
print(len(Subjects)) #len is a function which returns the number of elements in the set
#-------------------------------SET METHODS-----------------------------------
Nums = {9,"9.0"}
print(Nums)
print(type(Nums)) #type is a function which returns the type of the specified object
#-------------------------------DICTIONARY METHODS-----------------------------------
marks ={}
marks["Physics"] = int(input("Enter your Physics marks: "))
marks["Chemistry"] = int(input("Enter your Chemistry marks: "))
marks["Maths"] = int(input("Enter your Maths marks: "))
print(marks)
# -------------------------------DICTIONARY METHODS-----------------------------------
marks ={}
x = int(input("Enter your Physics marks: "))
marks.update({"Physics": x})
x = int(input("Enter your Chemistry marks: "))
marks.update({"Chemistry": x})
x = int(input("Enter your Maths marks: "))
marks.update({"Maths": x})
print(marks)

# wap to take a number from the user and print the table of that number 
n=int(input("Enter the number: "))
i=1
while i<=10:
    i+=1
    print(n*i)
# --------------------------------CONTINUE STATEMENT-----------------------------------
i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
# --------------------------------BREAK STATEMENT-----------------------------------
i = 0
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1
# --------------------------------FOR LOOP-----------------------------------
list = [1, 2, 3, 4, 5]
for el in list:
    print(el)
# --------------------------------FOR LOOP WITH ELSE-----------------------------------
List = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = int(input("Enter a number: "))
for el in List:
    if el == x:
        print("The number is present in the list", el, List.index(el))
        break
else:
    print("The number is not present in the list")
# --------------------------------SUM OF FIRST N NUMBERS USING RANGE-----------------------------------
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("The sum of first", n, "numbers is:", sum)
# -------------------------------SUM OF FIRST N NUMBERS USING WHILE LOOP-----------------------------------
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("The sum of first", n, "numbers is:", sum)
# -------------------------------FACTORIAL OF A NUMBER USING FOR LOOP-----------------------------------
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("The factorial of", n, "is:", factorial)
# --------------------------------EVEN OR ODD USING FUNCTION-----------------------------------
n = int(input("Enter a number: "))
def number(n):
    if n%2 == 0:
        print("EVEN")
    else:
        print("ODD")
result = number(n)
print(result)
print(type(result)) #type is a function which returns the type of the specified object
# --------------------------------EVEN OR ODD USING FUNCTION WITH RETURN STATEMENT-----------------------------------
n = int(input("Enter a number: "))

def number(n):
    return "EVEN" if n % 2 == 0 else "ODD"

print(number(n))
#--------------------------------RECURSION----------------------------------- 
def show(n):
    if n == 0:
        return 
    print(n, end=" ")
    show(n-1)
show(5)     
#--------------------------------RECURSION-----------------------------------
def fact(n):
    if( n==0 or n==1):
        return 1
    return n*fact(n-1)
print(fact(5))
#---------------------------------------------------------------RECURSION-----------------------------------
def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)
print(sum(5))
#---------------------------------------------------------------RECURSION-----------------------------------
def print_list(list, index=0):
    if index == len(list):
        return
    print(list[index])
    print_list(list, index + 1)
fruits = ["mango", "banana", "grapes", "apple"]
print_list(fruits)
# ----------------------square of a number using function-----------------------------------
def calc_square(n):
    square = n * n
    return square
print(calc_square(10))
# -------larger number using function-----------------------------------
def calc_larger(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
print(calc_larger(10,20,30))
#----------------------area of circle using function-----------------------------------
def calc_area_of_circle(radius):
    area = 3.14 * radius * radius
    return area
print(calc_area_of_circle(7))

# ----------------------count vowels in a string using function-----------------------------------
def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"

    for char in text:
        if char in vowels:
            count += 1

    return count
string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))
#---------------------------------------------------------------REVERSE STRING USING FUNCTION----------------------------------- 
def reverse_str(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text
string = input("Enter a string: ")
print("Reversed string:", reverse_str(string))
# -------------------prime number using function-----------------------------------
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")

def sum_numbers(a, b):
    return a + b
print(sum_numbers(5, 10))
# ---------------------------FAbonacci series using recursion-----------------------------------
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter the number of terms: "))

for i in range(terms):
    print(fibonacci(i))
# -----------second largest number in a list using function-----------------------------------
def second_largest(list):
    list.sort()
    return list[-2]

x = [10, 20, 50, 40, 30]
print("Second Largest:", second_largest(x))
# -------------reverse a string without using built-in functions-----------------------------------
str = ("aditya")
reversed_str = ("")      
for char in str:
    reversed_str = char + reversed_str
print("Reversed string:", reversed_str)
#-----------frequency of all elements in a string-------------
string=" My name is Aditya Kumar"
for char in string:
    if char != " ":
        print(char, ":", string.count(char))

n = int(input("Enter a number: "))
if n%2 == 0:
    print("EVEN")
else:
    print("ODD")
# -------------function to check whether a number is palindrome-------------
def is_palindrome(n):
    original = n
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return original == reversed_num
num = int(input("Enter a number: "))
if is_palindrome(num):
    print("Palindrome")
else:
    print("Not a Palindrome")


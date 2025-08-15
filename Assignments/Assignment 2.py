"""
#Part 1: Decision-Making Structures
#Task 1
#Write a program that checks if a given number is positive, negative or zero.

number = float(input("Enter a number: "))

if number > 0:
    print("the number is positive")
elif number < 0:
    print("the number is negative")
else:
    print("the number is zero")
    

#Task 2
#Write a program to find the larger of the two numbers.

number1 = float(input("enter first number:"))
number2 = float(input("enter second number:"))

if number1 > number2 :
    print(f"the greater number is{number1}")
elif number2 > number1:
    print(f"the greater number is {number2}")
else:
    print("both numbers are equal")
    

#Task 3
#Write a program to find the largest of the three numbers.

number1 = float(input("enter first number:"))
number2 = float(input("enter second number:"))
number3 = float(input("enter third number:"))

if number1 >= number2 and number1 >= number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = nubmer2
else:
    largest = number3

print(f"the largest number is {largest}")


#Task 4
#Write a program to check if the given string “Mass” is present in the string “Saylani Mass IT”.
#If the string is present then display the message “string found”.

main = "Saylani Mass It Training"
sub = "Mass"

if sub in main.split():
    print("String found")
else:
    print("String not found")
    

#Task 5
#Write a program to take user’s age as input and display whether he is minor, adult or senior citizen:
#a. Minor age is less than 18. b. Adult age is greater than 18 and less than 60 c. Senior citizen age is greater than 60

user_age = int(input("Enter the age: "))

if user_age <= 18:
    print("User is a Minor")
elif user_age >=18 and user_age <= 60:
    print("User is a Adult")
else:
    print("User is a Senior Citizen")
    

#Task 6
#Write a program to take integer as input and check if it is even or odd.

even_odd = int(input("Enter the Number: "))

if even_odd % 2 == 0:
    print(f"{even_odd} is even number ")
else:
    print(f"{even_odd} is odd number")


#Task 7
#Write a program to take two numbers and an operator (/,x,+,-) as input and perform the corresponding operation.

num1 = float(input("enter the number 1"))
operator = input("enter operator /,*,+,- : ")
num2 = float(input("enter the number 2"))

if operator == '+':
    result = num1 + num2
    print(f"{num1}+{num2}={result}")
elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == 'x':
    result = num1 * num2
    print(f"{num1} x {num2} = {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operator! Please use one of: /, x, +, -")


#Task 8
# Program to check if a number is between 20 (inclusive) and 40 (exclusive)

num = float(input("Enter a number: "))

if 20 <= num < 40:
    print(f"{num} is in the range [20, 40)")
else:
    print(f"{num} is NOT in the range [20, 40)")
    

#Task 9
# Program to check divisibility by 2, 3, or both

num = int(input("Enter an integer: "))

divisible_by_2 = num % 2 == 0
divisible_by_3 = num % 3 == 0

if divisible_by_2 and divisible_by_3:
    print(f"{num} is divisible by both 2 and 3")
elif divisible_by_2:
    print(f"{num} is divisible by 2")
elif divisible_by_3:
    print(f"{num} is divisible by 3")
else:
    print(f"{num} is not divisible by 2 or 3")
    

#Task 10
#Write a program to take user’s score as input and determine if they pass or fail (pass if score is above 60, otherwise fails.)

user_score = int(input("Enter the score: "))

if user_score >=60:
    print("You are Pass With a Great Score")
else:
    print("You are fail need more improvements")
    

#Task 11
#Write a program that takes a temperature in Celsius and checks if it is freezing, moderate or hot. a. Freezing temperature is below 0.
#b. Moderate temperature is greater than 0 and less than 26. c. Hot temperature is above 26.

temp = int(input("Enter temperature in Celsius: "))

if temp < 0:
    print(f"{temp}°C is FREEZING temperature")
elif 0 <= temp < 26:
    print(f"{temp}°C is MODERATE temperature")
else:
    print(f"{temp}°C is HOT temperature")


#Part-2: Loops

#Task 1
#Write a program to print numbers from 1 to 30 using for loop.

for number in range(1, 31):
    print(number)

#Task 2
#Write a program to print even numbers from 1 to 50 using while loop.

num = 2 

while num <= 50:
    print(num)
    num += 2  

#Task 3
#Write a program to print multiplication table of a given number.

num = int(input("Enter a number: "))
print(f"\nMultiplication Table of {num}:")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Task 4
#Write a program to print odd numbers from 1 to 50 using while loop.

num = 1 

print("Odd numbers from 1 to 50:")
while num <= 50:
    print(num)
    num += 2 

#Task 5
#Write a program to calculate the sum of all numbers from 1 to 50 using for loop.

total = 0  

for number in range(1, 51):  
    total += number 

print("The sum of numbers from 1 to 50 is:", total)


#Task 6
#Write a program to print each character of a string.

word = input("Enter the string: ")

print("Characters in the string")

for character in word :
    print(character)


#Task 7
#Write a program to compute the factorial of a number using while loop.


#Task 8
#Write a program to print numbers from 10 down to 1. [Hint: first check the sequence generated by range function on IDLE using this command i.e. list(range(10, 0, -1))]

for number in range(10, 0, -1):
    print(number)

#Task 9
#Write a program that continues to ask user to input password until the correct password is entered.

correct_password = "secret123"  

while True:
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")

#Task 10
#Write a program to print the square of each number from 1 to 10 using for loop.

print("Number\tSquare")  

for num in range(1, 11):  
    square = num ** 2     
    print(f"{num}\t{square}")

#Task 11
#Write a program to calculate the sum of even and odd numbers and print them. (numbers from 1 to 50)

even_sum = 0
odd_sum = 0

for num in range(1, 51):
    if num % 2 == 0:  
        even_sum += num
    else:             
        odd_sum += num

print(f"Sum of even numbers (1-50): {even_sum}")
print(f"Sum of odd numbers (1-50): {odd_sum}")

#Bonus Task
#Bonus Challenge: Write a program to print the first 10 Fibonacci numbers using for loop. Hint: First 10 Fibanacci numbers are  0,1,1,2,3,5,8,13,21,34

n = 10  
a, b = 0, 1  

print("First 10 Fibonacci numbers:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b

"""

# Part 1: Function 

'''# Write a function named “Greetings” that takes user’s name and print greeting.

def Greetings(name):
    print(f"Hello, {name} Welcome!")

user_name = input("Enter Your Name: ")
Greetings(user_name)

# Write a function that takes a number as argument and check if a given number is positive, negative or zero.



def number_check(num):
    if num > 0:
        print(f"{num} is Positive")
    elif num < 0:
        print(f"{num} is Negative")
    else:
        print(f"{num} is Zero")

number = int(input("Enter the Number: "))
number_check (number)


# Write a function to take two numbers as arguments and return the larger number.

def large_num(num1,num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        print("both are same")

check = large_num(10,20)
print("Larger Number", check)


# Write a function to take three numbers as argument and return the largest number.

def three_num(num1, num2, num3):
            if num1 >= num2 and num1 >= num3:
              return num1
            elif num2 >= num1 and num2 >= num3:
              return num2
            else:
                return num3


largest_num = three_num(22,35,65)
print("Largest Number: ", largest_num)



# Write a function to take user’s age as argument and return the message from the function whether he is minor, adult or senior citizen:
a. Minor age is less than 18.
b. Adult age is greater than 18 and less than 60
c. Senior citizen age is greater than 60

def user_age(age):
    if age <= 18:
        print("You are a Minor")
    elif age <= 60:
        print("You are Adult")
    else:
        print("You are a senior Citizen")

users_age = int(input("Enter your age"))
user_age(users_age)


# Write a function to take integer as argument and check if it is even or odd.

even_odd = int(input("Enter the Number: "))

if even_odd % 2 == 0:
    print(f"{even_odd} is even number ")
else:
    print(f"{even_odd} is odd number")


# Write a function to take number as argument and return the square of that number.

def sq_num(number):
    return number ** 2

numbers = int(input("Enter the Number"))
result = sq_num(numbers)
print(f"The square of {numbers} is {result}")


# Write a function to compute the area and circumference of the circle and return the computed results.

def my_fun (radius):
    area = 3.14 * radius**2
    circumference = 2*3.142*radius
    return area,circumference
print (my_fun(5))

#Write a function to take user’s score as argument and determine if they pass or fail (pass if score is above 60, otherwise fails.)

def user_score(score):
    if score >= 60:
        print("You are Passed")
    else:
        print("You are failed")

result = int(input("Enter the Score"))
user_score(result)



# Write a function to compute factorial of a given number using recursion technique.

n = int(input("Enter number"))

def fact (n):
    if n>0:
        result = n*fact(n-1)
        print(result)
    else:
        result = 1

    return result

factorial = fact(n)
print(factorial)

# Part-2: Data Structures (List)

# 1.	Create a list to store student data i.e. name, age, course and is_attending. Display each element of list using for loop.

student = ["Toufeeq Ahmed",18, "AI and Data Science", True]

for item in student:
    print(item)

# Write a code to separate strings, numbers and Boolean data from the above list into separate lists.

student = ["Toufeeq Ahmed",18, "AI and Data Science", True]

strings = []
numbers = []
booleans = []

for item in student:
    if type(item)==str:
        strings.append(item)
    elif type(item)==int:
        numbers.append(item)
    elif type(item)==bool:
        booleans.append(item)

print("Strings List:", strings)
print("Numbers List:", numbers)
print("Booleans List:", booleans)


# Create a list [“apple”, “raspberry”, “pineapple”, “cherry”]. 
a. How can you check if apple is present in the list and get the index of the element (if present)
b. Now replace the raspberry and pineapple with orange.
c. Insert “apricot” at index 2.
d. Extend the resulting list with items “car”, “bike”, “aeroplane”.
'''

list = ["apple", "raspberry", "pineapple", "cherry"]

# a)

if "raspberry" in list:
    print("Yes it is in list")
else:
    print("Not in list")

# b)

list = ["apple", "raspberry", "pineapple", "cherry"]

list[1:3]= ["orange"]
print(list)

# c)

list[1:2]=["apricot"]
print(list)

list.extend(["Mango","Grapes","Peach"])
print(list)

Si

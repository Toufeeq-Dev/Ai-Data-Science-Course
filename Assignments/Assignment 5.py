#                     # ==> Encapsulation Practice      

#           # task 1 Bank Account
    
# class BankAccount:

#     # Constructor
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number
#         self.__balance = balance

#     # Methods
#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#         else:
#             print("Insufficient balance")

#     def get_balance(self):
#         return self.__balance

# acc1 = BankAccount("543543453", 8000) # object

# acc1.deposit(2000) # deposit method

# acc1.withdraw(5000)  # withdraw method

# acc1.get_balance()  # get balance method


#                 # task 2  Student Marks Validation

# class Student:
#     def __init__(self, name, roll_no, marks):
#         self.__name = name
#         self.__roll_no = roll_no
#         self.__marks = marks
#     # getter methods
#     def  get_name(self):
#         return self.__name

#     def get_roll_no(self):
#         return self.__roll_no

#     def get_marks(self):
#         return self.__marks

#     # setter methods
#     def set_name(self, name):
#         self.__name = name

#     def set_roll_no(self, roll_no):
#         self.__roll_no = roll_no

#     def set_marks(self, marks):
#         self.__marks = marks

# std1 = Student("Toufeeq Ahmed", 74538, 89)

# print(std1.set_marks(70))

# print(std1.get_marks())

#                 # Task 3 Password Manager

# class PasswordManager():
#   def __init__(self, username, password):
#     self.username = username
#     self.__password = password

#   def set_password(self, new_password):
#     self.__password = new_password

#   def check_username(self):
#     return self.username

#   def check_password(self):
#     return self.__password

# user1 = PasswordManager("Toufeeq", "12345")

# # Username check karna
# print(user1.check_username())

# # Password check karna
# print(user1.check_password())


# # Password change karna
# user1.set_password("new 123")
# print(user1.check_password())

#                 # Task 4  Employee salery protection 
# class Employee():
#   def __init__(self,name,age,salary,gender):
#     self.__name = name
#     self.age = age
#     self.__salary = salary
#     self.gender = gender

# # getter method
#   def get_name(self):
#     return self.__name

#   def get_age(self):
#     return self.age

#   def get_salary(self):
#     return self.__salary

#   def get_gender(self):
#     return self.gender

# # setter method
#   def set_name(self,name):
#     self.__name = name

#   def set_age(self,age):
#     self.age = age

#   def set_salary(self,salary):
#     self.__salary = salary

#   def set_gender(self,gender):
#     self.gender = gender

#   def show_employee_details(self):
#     print("Name: ",self.__name)
#     print("Age: ",self.age)
#     print("Salary: ",self.__salary)
#     print("Gender: ",self.gender)

# emp1 = Employee("Toufeeq",18,50000,"Male")

# emp1.set_salary(80000)

# print(emp1.get_salary())


#                     # Task 5 Shopping Cart

# class ShoppingCart:
  
#   def __init__(self, item):
#     self.__item = item

#   def add_item(self):
#     product = input("What would you like to add? ")
#     self.__item.append(product)
#     print(f"{product} added to cart.")

#   def remove_item(self):
#     product = input("What would you like to remove? ")
#     if product in self.__item:
#       self.__item.remove(product)
#       print(f"{product} removed from cart.")
#     else:
#       print(f"{product} not found in cart.")

#   def view_cart(self):
#     print("Your cart:", self.__item)

# cart1 = ShoppingCart([])

# cart1.add_item()
# cart1.view_cart()

# cart1.remove_item()
# cart1.view_cart()



                        # ==> Inheritance Practice

            # Task 1 Single_level Animal

# Parent class
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

# Child class
class Dog(Animal):
    def make_sound(self):
        print("Bark! Bark!")  # Overriding  method


a = Animal()
a.make_sound()   

d = Dog()
d.make_sound()   

                # Task 2 Single_level Vehicle

# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Child class
class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Seats: {self.seats}")

my_car = Car("Toyota", "Corolla", 5)
my_car.display_details()




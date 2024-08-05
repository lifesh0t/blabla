# import random

# def get_random_number():
#     print(random.randint(0, 10))

# get_random_number()


# def find_sum(num1, num2):
#     sum_nums = num1 + num2  # Finds the sum of num1 and num2
#     return sum_nums  # Returns the sum of the numbers
# num1 = 100
# num2 = 200
# print(find_sum(num1, num2))

# num3 = 400
# num4 = 500
# print(find_sum(num3, num4))


# from itertools import product

# def get_pins(observed):
#     # Define adjacency map
#     adjacency_map = {
#         '1': ['1', '2', '4'],
#         '2': ['1', '2', '3', '5'],
#         '3': ['2', '3', '6'],
#         '4': ['1', '4', '5', '7'],
#         '5': ['2', '4', '5', '6', '8'],
#         '6': ['3', '5', '6', '9'],
#         '7': ['4', '7', '8'],
#         '8': ['5', '7', '8', '9', '0'],
#         '9': ['6', '8', '9'],
#         '0': ['8', '0']
#     }
    
#     # Generate list of possible digits for each digit in observed PIN
#     possible_digits = [adjacency_map[digit] for digit in observed]
    
#     # Compute all possible combinations of these digits
#     all_combinations = [''.join(p) for p in product(*possible_digits)]
    
#     return all_combinations

# # Example usage
# print(get_pins('1357'))

# def math(a: int, b:int) -> tuple[int, int, float, float]:
#     sum_result = a + b
#     subtraction = a - b
#     division = a / b 
#     multiplication = a * b
#     return sum_result, subtraction, division, multiplication

# def get_user_number() -> int:
#     while True:
#         user_input = input("your number: ")
#         if not user_input1.isdigit():
#             print("try another")
#             continue
#         else:
#             user_input1 = int(user_input)
#             break
#     return user_input

# user_input1 = get_user_number()
# user_input2 = get_user_number()

# result = math(user_input1, user_input2)
# print(result)

# def math(a: int, b: int) -> tuple[int, int, float, float]:
#     sum_result = a + b
#     subtraction = a - b
#     division = a / b if b != 0 else float('inf')  # Using float('inf') to denote division by zero
#     multiplication = a * b
#     return sum_result, subtraction, division, multiplication

# def get_user_number() -> int:
#     while True:
#         user_input = input("your number: ")
#         if not user_input.isdigit():
#             print("try another")
#             continue
#         user_input1 = int(user_input)
#         break
#     return user_input1

# user_input1 = get_user_number()
# user_input2 = get_user_number()

# result = math(user_input1, user_input2)
# print(result)

# from typing import List

# def get_mail(text: str) -> List[str]:
#     text_list = text.split()
#     contains_at = [word for word in text_list if '@' in word]
#     contains_point = [word for word in contains_at if '.' in word.split ('@', 1)[1]]
#     return contains_point
# text = input("Insert mails: ")
# answer = get_mail(text)
# print(answer)

# Find all of the numbers from 1-1000 that are divisible by 6.

# divisible_6 = [i for i in range(1, 1000) if i % 6 == 0]
# print(divisible_6)

# Find all number from 1-1000 that have 9 in them.

# find9 = [i for i in range(1, 1001) if '9' in str(i)]
# print(find9)
# all9 = len(find9)
# print(f"Total: {all9}")

# Given string: text = 'In this lecture we will review some additional functionalities of python built-in data structures.' calculate how many words have letter e in it.
# text = ["In this lecture we will review some additional functionalities of python built-in data structures."]
# print([letter for letter in text if text.startwith("E") in text])

# text = ["In this lecture we will review some additional functionalities of python built-in data structures."]
# words_with_E = ([word for sentence in text for word in sentence.split() if word.startswith("E") or "e" in word])
# count = len(words_with_E)
# print(count)
# print(words_with_E)

# Given the same string as in previous exercise: calculate count of words that have more than 5 characters.
# text = "In this lecture we will review some additional functionalities of python built-in data structures."
# words = text.split()
# count = sum(1 for word in words if len(word) > 5)
# print(count)

# Given the same string calculate the occurrence of each letter in the string. (HINT: store everything in dictionary)

# Given the same string calculate the occurrence of each letter in the string. (HINT: store everything in dictionary)

# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
# my_list = list(text)

# print(f"my_list:\n{my_list}")

# occurences = {letter: my_list.count(letter) for letter in my_list if letter != " " and letter != "-" and letter != "."}

# print(occurences)



# inp_str = "GeeksforGeeks"
# out = {x: inp_str.count(x) for x in set(inp_str)}
# print("Kiekvienos raidės pasikartojimai GeeksforGeeks yra:\n" + str(out))

# Write a program that checks if given number is a perfect square.

# import math

# def is_square(i: int) -> bool:
#     return i == math.isqrt(i) ** 2

# num = int(input("Number: "))
# if is_square(num):
#     print(f"{num} is a perfect square.")
# else:
#     print(f"{num} is not a perfect square.")

# a=int(input('enter any number'))
# flag=0
# for i in range(1,a):
#     if a==i*i:
#         print(a,'is perfect square number')
#         flag=1
#         break
# if flag==1:
#     pass
# else:
#     print(a,'is not perfect square number')

#     def is_square(n):
#     return int(n**0.5) ** 2 == n

# user_input = int(input("Please insert a number "))
# print(is_square(user_input))

# Weekdays in codewars

# def whatday(num):
#     weekdays = {
#     1: "Sunday",
#     2: "Monday",
#     3: "Tuesday",
#     4: "Wednesday",
#     5: "Thursday",
#     6: "Friday",
#     7: "Saturday"
# }
#     if num in weekdays:
#         return weekdays[num]
#     else:
#         return "Wrong, please enter a number between 1 and 7"
    
# user_input = int(input("enter number: "))
# print(whatday(user_input))

# class Person:
#     def __init__(self, name: str, location: str, age: int = 0) -> None:
#         self.name = name
#         self.age = age
#         self.location = location
#     def travel(self):
#         print(f"{self.name} is walking....")
#     def say_hello(self) -> None:
#         print(f"{self.name} hellooo!")

# class Driver(Person):
#     def __init__(self, name: str, location: str, car: str,  age: int = 0) -> None:
#         super().__init__(name, location, age)
#         self.car = car

#     def travel(self):
#         print(f"{self.name} is driving a car {self.car} much faster then walking")

# person1 = Person("Tom", 40, "Germany")
# person2 = Driver("John", 39, "Opel", "England")

# print(person1.name, person1.age, person1.location)
# print(person2.name, person2.age, person2.location)
# person1.travel()
# person2.travel()
# print(person1.say_hello(), person2.say_hello())

# Create a Calculator class with main functionality: add, divide, multiply, subtract , etc.. Initiate class and show up some calculations.
# class Calculator:

#     def add(self, userinput1: int, userinput3: int) -> int:
#             return userinput1 + userinput3
#     def divide(self, userinput1: int, userinput3: int) -> float:
#             return userinput1 / userinput3
#     def multiply(self, userinput1: int, userinput3: int) -> int:
#            return userinput1 * userinput3
#     def deduct(self, userinput1: int, userinput3: int) -> int:
#             return userinput1 - userinput3
       
# userinput1 = int(input("Enter your number: "))
# userinput2 = input("Enter your move (add, deduct, multiply, divide): ")
# userinput3 = int(input("Enter your next number: "))
# calc = Calculator() 
# if userinput2 == '+':
#        print(calc.add(userinput1, userinput3))
# elif userinput2 == '-':
#        print(calc.deduct(userinput1, userinput3))
# elif userinput2 == '/':
#        print(calc.divide(userinput1, userinput3))
# elif userinput2 == '*':
#        print(calc.multiply(userinput1, userinput3))

# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:
# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.

# class Employee:
#     def __init__(self, name, surname) -> None:
#         self.name = name
#         self.surname = surname
#         self.email = f"{name.lower()}.{surname.lower()}@company.com"

#     def __str__(self) -> str:
#         return f"{self.name} {self.surname}, Email: {self.email}"
    
# empl = Employee("John", "Wick")
# print(empl)

# Create a Book class that has two attributes:
# title
# author
# and two methods:
# A method named .get_title() that returns: "Title: " + the instance title.
# A method named .get_author() that returns: "Author: " + the instance author.
# and instantiate this class by creating 3 new books:
# Pride and Prejudice - Jane Austen (PP)
# Hamlet - William Shakespeare (H)
# War and Peace - Leo Tolstoy (WP)
# The name of the new instances should be pride_and_prejudice, hamlet, and war_and_peace, respectively. For instance, if I instantiated the following book using this Book class:
# Harry Potter - J.K. Rowling (harry_potter)
# I would get the following attributes and methods:
# harry_potter.title ➞ "Harry Potter"
# harry_potter.author ➞ "J.K. Rowling"
# harry_potter.get_title() ➞ "Title: Harry Potter"
# harry_potter.get_author() ➞ "Author: J.K. Rowling"

# class Book:
#     def __init__(self, title: str, author: str) -> None:
#         self.title = title
#         self.author = author
#     def get_title(self) -> str:
#         return f"Title: {self.title}"
#     def get_author(self) -> str:
#         return f"Author: {self.author}"

# pride_and_prejudice = Book("Pride and Prejudice", "Jane Austen")
# hamlet = Book("Hamlet", "William Shakespeare")
# war_and_peace = Book("War and peace", "Leo Tolstoy")

# print(pride_and_prejudice.get_author())
# print(pride_and_prejudice.get_title())
# print(hamlet.get_author())
# print(hamlet.get_title())
# print(war_and_peace.get_author())
# print(war_and_peace.get_title())



# A country can be said as being big if it is:
# Big in terms of population.
# Big in terms of area.
# Add to the Country class so that it contains the attribute is_big. Set it to True if either criteria are met:

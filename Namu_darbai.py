# Excercises:
# Lesson 1:
# Create a program that allows user to enter his/her name and age
# Calculate the year user was born
# # Print the answer to the terminal
# from datetime import datetime
# def calculate_birth_year():
#     current_year = datetime.now().year
#     name = input("Your name?: ")
#     age = int(input("Your age?: "))
#     birth_year = current_year - age
#     print(f"Your name {name}, You were born {birth_year}, and you are {age} old.")
# calculate_birth_year()

# Create a program that allows user to enter a full sentence
# Print the sentence backwards, then all capital letters.
# Print every second letter in the sentence
# sentence = input("Enter you words: ")
# print(sentence[::-1])
# print(sentence.upper())
# for i in range (len(sentence)):
#     if i % 2 == 1:
#         print(sentence[i] + " ", end="")

# Create a program that expects a user to enter two numbers
# Multiply those numbers and print the answer
# Create similar programs with other signs.
# number1 = int(input("Your number?: "))
# number2 = int(input("Your number another number?: "))
# result = number2 * number1
# print(f"Rezultatas: {result}")

# Create program that allows user to enter text
# Convert that text to Leet speak 1337
# Print outcome
# def to_leet_speak(text):
#     leet_dict = {
#         'A': '4', 'a': '4',
#         'E': '3', 'e': '3',
#         'G': '6', 'g': '6',
#         'I': '1', 'i': '1',
#         'O': '0', 'o': '0',
#         'S': '5', 's': '5',
#         'T': '7', 't': '7'
#     }
#     leet_text = ""
#     for char in text:
#         leet_text += leet_dict.get(char, char)
#     return leet_text
# user_input = input("Ivesk teksta: ")
# leet_output = to_leet_speak(user_input)
# print(f"Leet kalba: {leet_output}")
# Lesson 2:

# nera


# Lesson 3:

# Write python program that asks user to enter name, surname, age. Put these values into a dictionary and print it.
# name = input("Name: ")
# surname = input("Surname: ")
# age = input("Age: ")
# user_info = {
#     'Name': name,
#     'Surname': surname,
#     'Age': age,
# }
# print(user_info)

# Try creating nested dict structure which would use all data types and structures you already know.
# name = input("Name: ")
# surname = input("Surname: ")
# age = int(input("Age: "))
# role = str(input("Job: "))
# workplace = str(input("Company: "))
# degree = str(input("Degree: "))
# languages = str(input("Languages can speak: "))
# user_info = {
#     'name': name,
#     'surname': surname,
#     'age': age,
#     'role': role,   
#     'workplace': workplace,
#     'degree': degree,
#     'languages': languages,
# }
# print(user_info)

# Create a program, that would take sentences from the input and create a dictionary where they keys represents letters and values the frequency 
# those letters appeared in those sentence. The program must demand that user should enter 3 or more sentences.

# nera


# Create a dictionary of student names and their grades:
# Store student names as keys and their grades as values in a dictionary.
# Calculate the average grade of all students:
# Use sum() and len() functions to calculate the total and number of grades, respectively, and then divide the total by the number to get the average.
# Remove students with grades below 80 from the dictionary:
# Create a set of student names with grades below 80.
# Check if a specific student exists in the dictionary:
# Input a student name from the user.
# Use the in operator to check if the student name exists in the dictionary.
# Print a message indicating whether the student name is found or not.

# student_grades = {
#     'name': "Donatas" 'grades': '80',
#     "Eimantas": 75,
#     "Ieva": 99,
#     "Karolis": 77,
#     "Rimvydas": 88,
#     "Mante": 95,
#     "Aurelija": 80,
#     "Gintare": 90
#     }
# total_grades = sum(student_grades.values())
# for i in range(len(student_grades)):
#         while student_grades[i]['grades']:
#             sum(value['grades'] for value in student_grades)




# number_one = 500
# number_two = 500
# if number_one == number_two:
#     print("geras")
# elif number_one == number_two:
#     print("Numbers are equal !")
# else: 
#     print("nieko gero")

# score = int(input("Score: "))
 
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

# number1 = input(int)("tavo skaicius: ")
# number2 = input(int)("tavo antras skaicius: ")

# if number1 == number2:
#     print("lygus")
# elif number

# while True:
#     user_input = input("Enter your name: ")
#     if len(user_input) != 0:
#         break
# print(f"You entered {user_input }")


# while True:
#     user_input = input(int)("enter your nr: ")
#     if user_input == int:
# print("geras")

# Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.
# name = input("Name: ")
# surname = input("Surname: ")
# age = int(input("Age: "))
# if age >= 21:
#     print(f"Welcome {name} , {surname} !")
# else:
#     print(f"Uzauk {name} , {surname}")

# Create a database (list of privileged users), print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"
# user = input("name: ")

# privileged_users = ["Eimantas" , "Donatas" , "Ieva"]

# if user in privileged_users:
#     print(f"welcome {user}")
# else:
#     print("von lauk!")

# user = "Johnny"
# privileged_users = ["Tom", "Albert", "Stephen"]
# if user in privileged_users:
#     print(f"Welcome home {user}")
# else:
#     print("INTRUDER ALLERT. Silently calling police...")

# Allow user to enter two numbers, print out which one is higher than the other, or equal.
# number1 = int(input("Skaicius: "))
# number2 = int(input("2 skaicius: "))
# if number1 > number2:
#     print(f"number1 {number1} daugiau uz {number2}")
# elif number1 < number2:
#     print(f"number2 {number2} daugiau uz {number1} ")
# else:
#     print(f"number1 {number1} lygu number2 {number2}")

# Write a small calculator application, that allows user to enter two numbers and a symbol, do the operation and print the answer.
# number1 = int(input("1 skaicius: "))
# step = input("koks veiksmas bus +, -, *, /,: ")
# number2 = int(input("2 skaicius: "))
# if step == "+":
#     result = number1 + number2
#     print(f"Atsakymas: {result}")
# elif step == "-":
#     result = number1 + number2
#     print(f"Atsakymas: {result}")
# elif step == "*":
#     result = number1 * number2
#     print(f"Atsakymas {result}")
# elif step == "/":
#     result = number1 / number2
#     print(f"Atsakymas: {result}")
    
# kitas variantas

# number1 = int(input("Please insert first number "))
# number2 = int(input("Please insert second number "))
# operator = input("Please insert an operator for the equation (+, -, * or /) ")
 
# if operator == '+':
#     result = number1 + number2
# elif operator == '-':
#     result = number1 - number2
# elif operator == '*':
#     result = number1 * number2
# else:
#     result = number1 / number2
# print(f"{number1} {operator} {number2} = {result}"


# Create a number guessing game from 1-10.

# import random
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# number = random.choice(list)
 
# while True:
#     user_guess = int(input("Insert a number between 1 and 10 - "))
#     if user_guess != number:
#         print("You guessed the number incorrectly, try again ")
#     else:
#         break
# print(f"Congratulations you've guessed the number! The number is {number}")
 


# Create a variables containing strings for username and password. Start endless loop allowing to enter username 
# and password. If credentials are correct stop endless loop and print greeting message.
# good_username = "spokas"
# good_password = "spokas"
# while True:
#     username = input("username: ")
#     password = input("password: ")
#     if username == good_username and password == good_username: 
#         print(f"privet: {username}")
#         break 
#     else:
#         print("dink lauk, nedraugas")

# Allow user to enter 10 integers, and then print the sum and average of those entered numbers.
# um_list = []
# i = 0
# print("Iveskite 10 sveiku skaiciu: ")
# while i < 10:
#   num_list.append(int(input()))
#   i += 1  
 
# print(f"Jus ivedete skaicius: {num_list}")
# num_sum = sum(num_list)
# print(f"Siu skaiciu suma lygi: {num_sum}")
# print(f"Siu skaiciu vidurkis yra: {num_sum/i}")

# Generate a dictionary of 10 keys (1,2,3...10). Each of them should store a value of random integer number from 1 to 100.

# import random
# random_dict = {i: random.randint(1, 100) for i in range(1, 11)}
# print(random_dict)

# import random
 
# num_dict = {i: random.randint(1,101)
#             for i in range(1,11)}
# print(num_dict)


# Create a pin code cracker. Let's say pin code consists of 4 random digits. You can store the value in variable. 
# Then create a loop going through all possible combinations until you find the one you entered.

# 1 PAVIZDYS

# from random import *
# import itertools
# guess = ""
# password = input("Password: ")
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# while (guess != password):
#     guess = ""
#     perm = ""
#     for letter in password:
#         guessletter = letters[randint(0, 25)]
#         guess = str(guessletter) + str(guess)

#         perm = itertools.permutations(guess)
        
#     for p in perm:                    
#         guess = "".join(p)
#         print(" ",guess,end="\r")
                     
# print(f"Password guessed! ==> {guess}")

# 2 PAVIZDYS

# input("")

# from random import *
# import itertools


# guess = ""
# password = input("Password: ")
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# while (guess != password):
#     guess = ""
#     perm = ""
#     for letter in password:
#         guessletter = letters[randint(0, 25)]
#         guess = str(guessletter) + str(guess)

#         perm = itertools.permutations(guess)
        
#     for p in perm:                    
#         guess = "".join(p)
#         print(" ",guess,end="\r")
            
            
# print(f"Password guessed! ==> {guess}")
# input("")

# 3 PAVIZDYS

# correct_pin = input("Enter your PIN: ") 

# found_pin = ""

# for i in range(1000):  
#     attempt = f"{i:04}"
    
   
#     if attempt == correct_pin:
#         found_pin = attempt
#         break

# print(f"The pin code is: {found_pin}")


# Create a program that allows a user to enter a series of numbers, and then calculates the average of all the numbers. 
# The program should also print the list of all the numbers, as well as the average.

# nera

# 10 Pamoka

# Create at least 5 different functions by your own and test it


# import random
# def get_name():
#     names = ["Ieva", "Rolandas", "Dzonis", "Eimantas" , "Karolis"]
#     return random.choice(names)
# print(get_name())

# import random
# def get_random_number():
#     return(random.randint(0, 10000))

# def multiply_results():
#     random_number = get_random_number()
#     mult_result = random_number * 2
#     print(mult_result)
# multiply_results()

# def divide_results():
#     div_result = multiply_results()
#     if div_result is not None:
#         div_r = div_result / 2
#         print(div_r)
# divide_results()

# def greet(name: str) -> str:
#     return f"Laba {name}"
# greeting = greet("Aru")
# print(greeting)


# Create a function that adds a string ending to each member in a list.

# def add_ending(lst, ending):
#     return [item + ending for item in lst]
# word = ["Apple", "Watermelon", "Melon"]
# suffix = "s"
# new_words = add_ending(word, suffix)
# print(new_words)

# Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication.

# def calculate(a: int, b: int): 
#     sum_result = a + b
#     subtraction = a - b
#     division = a / b if b != 0 else "Dalyba negalima"
#     multiplication = a * b

#     return { 
#         "sum": sum_result,
#         "subtraction": subtraction,
#         "division": division,
#         "multiplication": multiplication,
#     }
# num1 = float(input("your first number: "))
# num2 = float(input("your second number: "))
# results = calculate(num1, num2)
# for operation, result in results.items():
#     print(f"{operation}: {result}")


# Create a function that returns only strings with unique characters.

# def is_unique(s):
#     return len(set(s)) == len(s)
# while True:
#     user_input = input("Enter your word (or 'quit' to exit): ").strip()
#     if user_input.lower() == 'quit':
#         print("Thank you")
#         break
#     if is_unique(user_input):
#         print(f"'{user_input}'contains unique letters.")
#     else:
#         print(f"'{user_input}'not contains unique letters.")
#     print()


# Write a program that defines a function called extract_email_addresses() that takes a text as input and extracts all email addresses from the text.


# from typing import List

# def get_mail(text: str) -> List[str]:
#     text_list = text.split()
#     contains_at = [word for word in text_list if '@' in word]
#     contains_point = [word for word in contains_at if '.' in word.split ('@', 1)[1]]
#     return contains_point
# text = input("Insert mails: ")
# answer = get_mail(text)
# print(answer)



#  test = "hello world"
# print(test)

# Variable Declaration
# studentName = "Opeyemi"
# location = "Adegbayi"
# score = 97
# print(f"My name is {studentName} i stay at {location} and my total score is {str(score) } in Mathematics")

# Course = input ("What department are you?")
# testScore1 = input("CA Score")
# testScore2 = input ("Exam Score")
# TotalScore = (int(testScore1) + int(testScore2))
# print( "Department "+Course+ " Assessment "+testScore1+ " Exam Score "+testScore2+ " Final Score "+ str(TotalScore))

# Global and Local variables
# a = 20

# def addition():
# global a 
# b = 10
# a = 30
# score = a + b
# print("Addition is",score)
# print(a)
# addition()

# def division():
#     b = 10
#     score = a / b
#     print("Division is", score)
#     print(a)
# division()

# location = input("Where do you live")
# Name = input("What is your name")
# Age = input("How old are you")
# Sex = input("Gender")
# print(f"Location{location} Name{Name} Age{Age} Sex{Sex} ")

# x ="orange"
# y = "Banana"
# z = "Cherry"

# x, y, z = "Orange", "Banana", "Cherry"
# x = y = z = "Orange"

# print(x)
# print(y)
# print(z)

#Unpack a list
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# Assignment 1
# Name = input(" What is your name? ")
# Location = input(" Where do you live? ")
# Assessment = input(" What is your test score? ")
# Exam = input(" What is your exam score? ")
# TotalScore = ( int(Assessment) + int(Exam) )
# print( f"My name is {Name}, i am from {Location}, my total score is {TotalScore} ")

# OR
# student_name = input("enter your name:")
# location = input("enter your location:")
# score1 = float(input("enter your score1:"))
# score2 = float(input("enter your score2:"))
# total_score = score1 + score2
# print("My name is", student_name, "i am from", location, " my score is", str(total_score))

# Types of variables
# def name():
#     name = " Asiwaju Tinubu"
#     location = "Abuja"
#     print(location, name)
# name()


# a = 20
# b = 5

# def addition():
#         global a
#         b = 10
#         a = 30
#         score = a + b
#         print("addition is" ,score)
# addition()
# def substract():
#         global b
#         b = 10
#         # a = 30
#         score = a - b
#         print("substraction is" ,score)
# substract()

# def multiplication():
#         score = a * b
#         print("multiplication is" , score)
#     # addition()
#     # substract()
# multiplication() 

# print(a)
# print(b)

# x = 40
# y = 10.5
# z = 12j                                     
# print(type(x))
# print(type(y))
# print(type(z))

# student_info = { "name":"Ade", "school":"SQI", "Course":"Python"}
# print(student_info["Course"]) 
# print(student_info["school"])

# student_info =  dict{ "name" = "Ade" , "school" = "SQI", "course" = "Python" }
# print(student_info["name"]) 
# print(student_info["course"])

# name1 = ({1,2,3,4,5,6,7, "ade", "tade"})
# print (type(name1))

# x = True
# y = False
# print(type(x))
# print(type(y))

# x = 10
# y = float(x)
# print(type(y))
# print(y)

# convert boolean datatype to float
# x = False
# y = float(x)
# print(y)

# Array conversion
# list []
# tuple ()
# set {}
# dictionary {}

# list to tupple
# student_name = ["timi", "kunle", "sola", False, 23j, 142.8]
# print(type(student_name))
# student_name = tuple(student_name)
# print(type(student_name))


# # Tuple to list
# student_name = ["timi", "kunle", "sola", False, 23j, 142.8]
# # print(type(student_name))
# student_name = tuple(student_name)
# student_name = list(student_name)
# print(type(student_name))

# list to set
# student_name = ["timi", "kunle", "sola", False, 23j, 142.8]
# print(type(student_name))
# student_name = tuple(student_name)
# student_name = list(student_name)
# student_name = set(student_name)
# student_name = frozenset(student_name)
# print(type(student_name))

# name = ("Gbenga", "sola", "Tola", "Adanla")
# print(name)
# name1 = list(name)
# name1.append("Kola")
# print(name1)
# surname = tuple(name1)
# print(surname)

# Finding intersections in variables
# val1 = [1,2,3,4,5,6,7,8,9]
# val2 = [5,10,4,20,7,30,35,40,45]

# val1 = set(val1)
# val2 = set(val2)
# intersection = val1.intersection(val2)
# print(intersection)

# Assignment2

# write a program that will ask the user to supply 5 values using two variables,
# then find the intersection of the two variables.

# Correction
# val1 = set(input("enter 5 values separated with comma and space").split(", "))
# val2 = set(input("enter 5 values separated with comma and space").split(", "))
# intersection = val1.intersection(val2)
# print(intersection)


# PYTHON OPERATORS

# operators are used to perform operations on variables and values
# Types of Operators

# 1. Arithmetic operator: +, -, /, *, %, //, **
# Example:
# x = 10
# y = 5
# result = x + y

# # x = 10
# # y = 5
# # result = x / y

# x = 10
# y = 5
# result = x // y

# x = 10
# y = 5
# result = x ** y

# x = 10
# y = 5
# result = x % y

# print(result)


# 2. Assignment operator: =, +=, -=, /=, *=, //=, %=, **=, etc
# i.e
# x = 10
# print("before assigning", x)
# x += 6
# print("after assigning", x)
# x += 10
# print(x)
# x  *= 17
# print(x)
# x %= 23
# # % is what is left after division
# print(x)
# x = 2
# print(x)
# x **= 7
# print(x)

# 3. Comparison operator: ==, !=, >, <, <=, >=
# x = 10
# y = 5
# result = x == y
# print(result)

# x = 10
# y = 5
# result = x != y
# print(result)

# x = 10
# y = 5
# result = x <= y
# print(result)

# x = 10
# y = 5
# result = x >= y
# print(result)

# 4. Logical operator: and, or, not
# fval = 10
# sval = 5
# print(fval == sval and fval >= sval)
# print(fval == sval or fval >= sval)
# print (not (fval >= sval))
# print((fval == sval or fval >= sval) and (fval > sval and fval >= sval))

# day1 = "wednesday"
# day2 = " not christmas"
# time = "1pm"
# weather = "bright"
# if (day1 == "wednesday" and day2 == " not christmas") and time == "11am" and weather == "bright":
#     print("I WILL COME TO SQI")
# else:
#     print("I WILL STAY AT HOME")

# food = input("What type of meat do you have? ")
# if food == "Rice":
#         print("i will buy rice")
# elif food == "Beans":
#         print("i will buy beans")
# elif food == "Yam":
#         print("i will buy yam")
# else:
#         print("i will not buy any food")

# A     B     A and B     A or B     not A

# T     T        T           T         F

# T     F        F           T         F

# F     T        F           T         T

# F     F        F           F         T
# If you checking for more than one condition use elif

# Identity Operators "is" or "is not"
# fval = "5"
# sval = 5
# print(fval == sval)
# print(fval is not sval)
# print(fval is sval)

# # Membership Operator is "in" or is "not in"
# fval = ["sola", "tunde", "monday", "sunday"]
# comment = "this is a python class for iot and robotics"
# print("monday" in fval)
# print("python" not in comment)

# Bitwise Operators(converts numbers to binary) 
# fval = 20
# print(bin(fval))

# Python String Class
# name = 'sunday' #==['s', 'u', 'n', 'd', 'a', 'y']
# day = 'wednesday'
# print(name[2])
# print(name[-4])
# print(name[0:3])
# print(name[-4:-2])
# print(name[-6:-3])
# print(len(day))

# comment = """  commented this is python class. it was started last
# week and stiil continue through this week. the number of people in
# this class is  """

# # String Methods
# print(comment.startswith("commented"))
# print(comment.endswith(" "))

# Strip() function
# print('length before strip is ', len(comment))
# print('length after strip is ', len(comment.strip()))
# name = input("What is your name?")
# if name.strip() == "timi":
#     print("my name is timi")
# else:
#     print("my name is ade")

    # Lower() function
# name = 'SUNDAY'
# print(name.lower())
# value = "method"
# user = input("please enter value to continue")
# if value == user.lower().strip():
#         print(user)
# else:
#         print("invalid input")

    # Upper() function
# name = 'kayode'
# print(name.upper())
# value = "METHOD"
# user = input("please enter 'method' to continue")
# if value == user.lower().strip():
#         print(user)
# else:
#         print("invalid input")

# Assignment3
# 1) ADD 2) SUBTRACT 3) MULTIPLY 4) DIVIDE
# print(" select an operation to perform:")
# print(" 1. ADD")
# print(" 2. SUBTRACT")
# print(" 3. MULTIPLY")
# print(" 4. DIVIDE")
# print(" 5. PERC")


# operation = input()

# if operation == "1":
#  num1 = input("Enter first number")
#  num2 = input("Enter second number")
#  print("The sum is" + str(float(num1) + float(num2)))
# elif operation == "2":
#  num1 = input("Enter first number")
#  num2 = input("Enter second number")
#  print("The difference is" + str(float(num1) - float(num2)))
# #    # code for subtraction
# elif operation == "3":
#  num1 = input("Enter first number")
#  num2 = input("Enter second number")
#  print("The product is" + str(float(num1) * float(num2)))
# #    # code for multiplication
# elif operation == "4":
#  num1 = input("Enter first number")
#  num2 = input("Enter second number")
#  print("The result is" + str(float(num1) / float(num2)))
# #    # code for division
# elif operation == "5":
#  num1 = input("Enter first number")
#  num2 = input("Enter second number")
#  print("The result is" + str(float(num1) % float(num2)))
# #    # code for perc
# else:
#  print("Invalid Entry")


 # ASSIGNMENT 4
# Question1 = input("What is a noun? \n").strip().lower().capitalize()
# score = 0
# if ("name" and "person" and "animal" and "place" and "thing"  in Question1):
#     mark = 6
#     score += 6
#     print(f"mark: {int(mark)}")
#     print(f"CORRECT! Your score is {int(score)}" )
# # if  "Name".lower() or "person".lower or "animal".lower() or "place".lower or "thing".lower() in Question1:
# #     score += 10
# #     print(f"CORRECT! Your score is {int(score)}" )
# else:
#     print("INCORRECT!")

# Question2 = input("How many elements are in the periodic table? \n").strip().lower().capitalize()

# if Question2 == "118":
#     mark = 6
#     score += 6
#     print(f"mark: {int(mark)}")
#     print(f"CORRECT! Your score is {int(score)}" )
# # elif Question2 == "Name" and "person" or "animal" or "place" or "thing":
#     # score += 10
#     # print(f"CORRECT! Your score is {int(score)}" )
# else:
#     print("INCORRECT!")

# Question3 = input("Which animal lays the largest egg? \n").strip().lower().capitalize()

# if Question3 == "Ostrich":
#     mark = 0
#     score += 6
#     print(f"mark: {int(mark)}")
#     print(f"CORRECT! Your score is {int(score)}" )
# # elif Question3 == "Name" and "person" or "animal" or "place" or "thing":
#     # score += 10
#     # print(f"CORRECT! Your score is {int(score)}" )
# else:
#     print("INCORRECT!")

# Question4 = input("what is the most abundant gas in earth's atmosphere? \n").strip().lower().capitalize()

# if Question4 == "Nitrogen":
#     mark = 6
#     score += 6
#     print(f"mark: {int(score)}")
#     print(f"CORRECT! Your score is {int(score)}" )
# # elif Question4 == "Name" and "person" or "animal" or "place" or "thing":
#     # score += 10
#     # print(f"CORRECT! Your score is {int(score)}" )
# else:
#     print("INCORRECT!")

# Question5 = input("Which planet in the solar system is the hottest? \n").strip().lower().capitalize()

# if Question5 == "Venus":
#     mark = 6
#     score += 6
#     print(f"mark: {int(mark)}")
#     print(f"CORRECT! Your score is {int(score)}" )
# # elif Question5 == "Name" and "person" or "animal" or "place" or "thing":
#     # score += 10
#     # print(f"CORRECT! Your score is {int(score)}" )
# else:
#     print("INCORRECT!")



# questions = ( "How many elements are in the periodic table?: ", 
#               "Which animal lays the largest egg?: ",
#               "what is the most abundant gas in earth's atmosphere?: ",
#               "How many bones are in the human body?: ",
#               "Which planet in the solar system is the hottest?: ")

# options = (("A. 116",  "B. 117",  "C. 118",  "D. 119"),
#            ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
#            ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
#            ("A. 206", "B. 207", "C. 208", "D. 209"),
#            ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# answers = ("C", "D", "A", "A", "B")
# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("--------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)  

#     guess = input("ENTER (A, B, C, D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 6
#         print("CORRECT!")
#     else:
#         print("INCORRECT!")
#         print(f"{answers[question_num]} is the correct answer")       

#     question_num += 1

#     print("--------------------")
#     print("       RESULTS      ")
#     print("--------------------")

#     print("answers:", end = "")
#     for answer in answers:
#         # print(answer, end = " ")
#         print()

#     print("guesses:", end = "")
#     for guess in guesses:
#         print(guess, end = " ")
#         print()

#     # score = int( score / len(question) * 100 )
#     score = int(score)
#     print(f"Your score is: {score}")

# Replace Function
# comment = "commented that This is a python class. it was started last week and still continue through this week. the number of people in this class is "

# newval = comment.replace("this", "now")
# newval = comment.replace("through", "throughout")
# print(newval)

# Split() function
# print(len(comment.split()))
# print((comment.split('.')))
# print((comment.split('This'.lower().strip())))
# word_split = comment.split()
# print(word_split)


# # Join() function
# print(" ".join(word_split))
# value = ["rice", "beans", "yam", "banana"]
# print(" ".join(value))

# # Capitalize() function
# name = "tomiwa adio lagos"
# print(name.capitalize())
# print(comment.capitalize())

# # Center() function
# print(comment.center(100))
# # It creates space around

# # Count() function
# print(comment.count("week"))

# # Encode() function
# print(name.encode())

# # In Operator
# val = "week" in comment
# print(val)
# val = "week" not in comment
# print(val)

# # Concatenation
# name = "paul"
# print(name + comment)
# comment = """{} commented that This is a python class. it was started last
#           week and still continue through this week. the number of people
#           in this class is {}"""
# num = 6
# print(comment.format(name, num))
 
# # Escape character
# print('she\'s the owner')
# print('she is the\b owner')
# print('she is the\t owner')
# print('she is the\n owner')
# print('she is the\r owner')
# print('she is the\a owner')
# print('she is the\f owner')
# print('she is the\v owner')

# Class Work
# Write a program that;
# - Ask the user if they will want to replace a word in the article
# - Ask the user which word they will like to replace
# - Ask the user which word they will like as replacement
# - Print the new article with the new word
# solution
# essay = input("Write an article of 10words ")
# ammendment = input("Would you like to replace any word?")
# amend = input("Type the word you would like to replace")
# # thanks = ("Thank you for banking with us!")
# newword = input("Type the new word")
# if ammendment == "YES".lower():
#     print(amend)
# else:
#     print("Thank you for banking with us!")

# if amend in essay :
#  new_word = essay.replace(amend, newword)  
#  print(new_word) 

# correction
# article = input("Write a short article about yourself \n>>> ")
# reply = input("would you like to replace any word in the article? Press \n1. Yes \n2. No \n>>>> ")
# if reply == "1":
#    resp1 = input("which word would you like to replace \n>>> ")
#    resp2 = input("which word would you like to use as replacement \n>>> ")
#    print(article.replace(resp1, resp2))
# elif reply == '2':
#    print("You have made no corrections")
# else:
#    print("Invalid Choice!")


# ARRAY:
# list
# tuple
# set
# dictionary

# List: is a collection which ordered, changeable and allows duplicate values.
# A list is created with a square bracket [] or list() constructor.
# my_list = ["Shade", "energy", "Charse", "energy"]

# my_list = list(("Shade", "energy", "Charse", "energy"))
# append, extend, insert
# print(my_list)
# my_list.append("ope")
# print(my_list)

# my_list.append("ope")
# print(my_list)

# nlist = ["Jide", "Kola", "Tola"]
# my_list.extend(nlist)
# print(my_list)

# my_list.insert(2, "adeola")
# print(my_list)

# CLASSWORK
# Write a program that lists all numbers divisible by 3 between 0 and 100
# Solution
# numbers = []
# for x in range(0,101):
#     if x%3 == 0:
#      numbers.append(x)
# print(numbers)
# OR
# num = [x for x in range(0,101) if x%3==0]
# print(num)
# Replace doesn't work for list
# my_list.replace("energy" "solar")
# print(my_list)

# my_list2 = list((12, 14, "Sunday", "Charse", ["tomiwa", "ope", "tomisin"], "True", "False", 5 ))
# my_list3 = list((12, 14, "Sunday", "Charse", ["tomiwa", "ope", "tomisin"], ["True", "False", "None"], False, 5.08 ))
# print(my_list2[1:6])
# print(my_list2[-5])
# print(my_list2[-4:-1])
# print(my_list3[5][2])

# if "energy" in my_list:
#     print("present")
# else:
#     print("not available")

# my_list.remove("energy")
# print(my_list)

# my_list.pop()
# print(my_list)
    
# del my_list2
# print(my_list2)

# my_list2.clear()
# print(my_list2)

# my_list2 = list(("Sunday", "Charse", "True","True", "False", ))
# my_list2.sort(reverse = True)
# print(my_list2)

# my_list2.reverse()
# print(my_list2)

# llist = ["Sunday", "Charse", "tomiwa", "ope", "tomisin", "True", "False"]
# llist.sort(reverse=True, key=str.upper)
# print(llist)

# name = my_list2.copy()
# print(name)

# print(my_list2.count("True"))

# print(max(my_list2))
# print(min(my_list2))

# ASSIGNMENT 5
# Write a program called "grading system" by assigning marks from 0-100 to grades A-F
# Solution
# marks = int(input("Enter your score/n>>>>"))
# if marks >100:
#   grade = "Invalid score"
# elif marks >= 70:
#   grade = "A"
# elif marks >= 60:
#   grade = "B"
# elif marks >= 50:
#   grade = "C"
# elif marks >= 45:
#   grade = "D"
# elif marks >= 40:
#   grade = "E"
# elif marks >= 0 :
#   grade = "F"
# else:
#   grade = "null"
# print("Your grade is" grade)

# ASSIGNMENT 6
# Write a program that puts all odd numbers btw 1-100 as determined by the user in a list
# number = []
# start = int(input("enter the start range /n>>>"))
# end = int(input("enter the end range /n>>>"))
# for num in range(start,end+1):
#     if(num%2!=0):
#         number.append(num)
# print(number)

# TUPLE: A tuple is a collection that is ordered but not changeable
#  and allows duplicate values. A tuple is created using bracket i.e () or tuple()
# del join
# Unpacking values of a tuple
# item = ("Yam", "Sunday", "Lagos", 45, "adtomtom", "Data science")
# (Food, Name, Location, Age, Email, Course) = item
# print(Location)
# print(Age)
# print(Name)
# (*Location, Age) = item
# (Food, *Name, Location) = item
# print(Food, Name, Location, Age, Email, Course)
# print(Location)
# print(item)
# (Food, *Name) = item
# print(Name)

# # Joining tuples together
# name = ("Shade", "energy", "magnet", "Charse", "energy")
# name2 = (12, 14, "Sunday", "Charse", True, False, 5.08)
# new_name = name + name2
# print(new_name)

# new_name = name * 5
# print(new_name)

# name = ("ade", "sunday", "femi")

# name = list(name)

# name = (type(name))

# name.append(name)

# name.append("Tolu")
# print(name)

# name1 = ("ade", "sunday", "femi")

# name1.append("Tolu")

# name1.append("dammy")

# name1.append("ayo")
# print(name1)

# name2 = ["ade", "sunday", "femi"]

# name3 = ["tolu", "ayo", "dammy"]

# for i in name3:
#  print(i)

# for i in name3:
#   name2.append(i)
# print(name2)

# for i in name3:
#   name2.append(i)
# print(name2)

# student_name = ("tayo", "risi")
# new_name = ("ayo", "kunle")
# student_name = list(student_name)
# for i in new_name:
#  student_name.append(i)
# print(student_name)
# student_name = tuple(student_name)
# print(student_name)



# Set: A set is a collection which is unordered and unindexed, changeable and does not allow duplicate
# values. It is written using curly bracket
# set.update
# name = {"shade", "energy", "magnet", "charse", "energy", "charse"}
# nm = {"dammy", "femi", "ife", "ola", "emma"}
# name.update(nm)
# print(name)

# namee = {1,2,3,4,5,6}
# name.update(nm,namee)
# print(name)

# name.add("timi")
# print(name)

# # set.remove
# name.remove("timi")
# print(name)

# for i in namee:
#     name.remove(i)
#     print(name)

# name.discard("simi")
# print(name)

# for i in namee:
#     name.discard(i)
#     print(name)

#     # Set.pop
#     name.pop()

#     # set.clear
# print(nm)
# nm.clear()
# print(nm)

# # set.del
# del nm
# print(nm)

# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# set2 = {11, 12, 3, 14, 5, 2}
# set3 = {2, 4, 5, 7, 8}

# set.union
# set_union = set1.union(set2)
# print(set_union)

# # set.update
# set1.update(set2)
# print(set1)

# # set.intersection
# set5 = set1.intersection(set2)
# print(set5)

# set.intersection_update
# set1.intersection_update(set2)
# print(set1)

# set.symmetric_difference
# set4 = set1.symmetric_difference(set2)
# print(set4)

# set4 = set1.symmetric_difference(set3)
# print(set4)

# set.difference
# set4 = set1.difference(set3)
# print(set4)

# # set.difference_update
# set1.difference_update(set3)
# print(set1)

# # set.isdisjoint
# print(set1.isdisjoint(set3))
# print(set1.isdisjoint(set2))

# # set.issubset
# set4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
# print(set3.issubset(set4))
# print(set4.issuperset(set3))

# CLASSWORK
# Write a program that prompts the user to enter a sentence. Extract all the vowels
# (unique) from the sentence and store them in a set. Display the set of vowels.
# Solution
# result = set()
# sentence = input("write a sentence:").lower()
# vowels = ("a","e","i","o","u")
# for i in sentence:
#     if i in vowels:
#         result.add(i)
# print(result)

# Dictionary; is a collection which is ordered, changeable but does not allow duplicate and unindexed.
# Dictionary are used to store data in a key:value pairs.
# It is written using {key:value} or dict{key=value}
# car = {'Producer':'Toyota', 'model':'venza 2021', 'engine':'6 engine', 'color':'black', 'ok':'True'} 
# car = dict(Producer='Toyota', model ='venza 2021', engine ='6 engine', color='black', ok='True')
# student_record = dict(name="Tony Johnson", level= "300", deparment= "mechanical engineering", course= 10 )
# print(len(car))
# print(type(car))
# car["color"] = "red"
# print(car)

# print(car.get('Producer'))

# print(car["Producer"])


# print(car.keys())

# print(car.values())

# car["passenger"] = 4
# print(car)

# print(car.items())

# car.update({"year":2021, "tyre":"white"})
# print(car)

# car["tyre"] = "black"
# print(car) 

# car.pop("passenger")
# print(car)

# car.popitem()
# print(car)

# car.clear()
# print(car)

# del car["model"]

# del car
# print(car)
# for i in student_record.values():
#     print(i)

# for i in student_record:
#     student_record[i]
# print(student_record)

# for x in student_record.keys():
#     print(x)

# for x, y in student_record.items():
#     print(x, "=", y)

# new_record = car.copy()
# print(new_record)

# new_record = dict(student_record)
# print(new_record)

# Nested Dictionary: dictionary inside dictionary
# student_details = {
#     "Tony Johnson":{'name':'Tony Johnson', 'level':300, 'location':'Takie', 'dept':'math'},
#     "Micheal Chan":{'name':'Micheal Chan', 'level':200, 'location':'General', 'dept':'computer'},
#     "Timi Joy":{'name':'Timi Joy', 'level':400, 'location':'Apake', 'dept':'english'}
# }
# print(student_details["Tony Johnson"])
# print(student_details["Tony Johnson"]['level'])
# print(student_details["Tony Johnson"]['dept'])
# print(student_details["Tony Johnson"]['location'])
# print(student_details["Timi Joy"]['dept'])

# std1 = {'name':'Tony Johnson', 'level':300, 'location':'Takie', 'dept':'math'}
# std2 = {'name':'Micheal Chan', 'level':200, 'location':'General', 'dept':'computer'}
# student_details2 = {
#     'std_1':std1,
#     'std_2':std2,
# }
# print(student_details2['std_1']['level'])
# for record in student_details2.values():
#     print(record['name'])

# student_details = {
#     "Tony Johnson":{'name':'Tony Johnson', 'level':300, 'location':'Takie', 'dept':'math'},
#     "Micheal Chan":{'name':'Micheal Chan', 'level':200, 'location':'General', 'dept':'computer'},
#     "Timi Joy":{'name':'Timi Joy', 'level':400, 'location':'Apake', 'dept':'english'}
# }
# for record in student_details['Tony Johnson'].values():
#     print(record)

# # EXAMPLE
# student_record = {}
# for i in range(1,3):
#     # print(i)
#     print("Enter information for student", i)
#     id_ = input("Enter your id >")
#     name = input("Enter your full name >")
#     level = input("Enter your level >")
#     location = input("Enter your location >")
#     dept = input("Enter your department >")

#     student = {'id': id_, 'name':name, 'level':level, 'location':location, 'dept':dept}
#     student_record[id_]= student
# print(student_record)
    

# IF ELSE statement
# IF statement is used for conditional execution of code. It allows you to specify a block of code that should be executed only if a certain condition is true.
# if condition:
#     print('statement1')
# else:
#     print('statement2')

# x = 10
# if x == 10:
#     print('x is 10')
# else:
#     print('x is not 10')

# x = 10
# if x > 11:
#     print('x is greater than 11')
# else:
#     print('x is less than 11')

# food = input('Madam, what food is available')
# if food.lower().strip() == 'rice':
#     print('i will buy rice')
# elif food.lower().strip() == 'beans':
#     print('i will buy beans')
# elif food.lower().strip() == 'yam':
#     print('i will buy yam')
# elif food.lower().strip() == 'eba':
#     print('i will buy eba')
# else:
#     print('i will not buy anything')



# food = input('Madam, what food is available')
# if food.lower().strip() == 'rice':
#     print('i will buy rice')
# if food.lower().strip() == 'beans':
#     print('i will buy beans')
# if food.lower().strip() == 'yam':
#     print('i will buy yam')
# if food.lower().strip() == 'eba':
#     print('i will buy eba')
# else:
#     print('i will not buy anything')


# Nested IF ELSE
# food = input('Madam, what food is available')
# if food.lower() == 'rice':
#     meat = input('what meat is available')
#     if meat == 'beef' or meat == 'fish':
#         print('i will buy rice today')
#     else:
#         print('i will not buy')
# elif food == 'yam':
#         extras = input('what can i take with yam')
#         if extras == 'beans':
#             print('i will buy yam') 
#         else:
#              print('Thanks i will fast')
# else:
#     print('i will not buy anything')


# question = input('are you a student of SQI by registration?')
# if question.lower() == 'yes':
#     quest = input('which course did you register for?')
#     if quest.lower() =='data science':
#         que = input('what is the name of your instructor?')
#         if que.lower() == 'mr yemi':
#             print('you are welcome')
#         else:
#             print('you are not allowed here')
#     elif quest.lower() =='data analysis':
#         que = input('what is the name of your instructor?')
#         if que.lower() == 'mr paul':
#             print('you are welcome to data analysis class')
#         else:
#             print('you are not a member of this class')
#     elif quest.lower() =='web development':
#         que = input('what is the name of your instructor?')
#         if que.lower() == 'mr selim':
#             print('you are welcome to class')
#         else:
#             print('you do not belong here')
#     else:
#         print('go to the front desk and confirm the course you registered for')
# else:
#     print('Go back home')

# ASSIGNMENT
# Write a program that allows the user to manage a phone book using a dictionary array. Then implement functionalities to add contacts, search for contacts, and display the phonebook.
# SOLUTION
# storage = {}
# for i in range(1, 3):
#  print('save contact', i)
#  name = input('Enter name/n>>')
#  number = input('Enter phone number/n>>')
#  saved_contact = {name:number}
#  storage[name] = saved_contact
# print('continue phonebook operation')
# print('1. Search For Contacts')
# print('2. Display my Phonebook')
# operation = input('Enter valid code/n>>>')
# if operation =='1':
#  search = input('Type name/n>')
#  search = storage
#  for name in search:
#    print(storage[name])
# elif operation == '2':
#   print(storage)
# else:
#     print('Invalid code!')
# CORRECTION
# import time
# contact ={}
# print('***SAMSUNG***........')
# time.sleep(3)
# for i in range(1,100):
#     print('''press
#     1. Add contact
#     2. search contact
#     3. display contact
#     4. quit''')
#     ans = input('>>>')
#     if ans == '1':
#       name = input('Enter the name you want to add:')
#       number = input('Enter the number you want to add:')
#       contact[name] = number
#     elif ans == '2':
#       name = input('Enter the name you want to search:')
#       if name in contact:
#         print(name+':' + number)
#       else:
#          print('contact not found')
#     elif ans == '3':
#        for name, number in contact.items():
#           print('name:' + name)
#           print('number:' + number)
#     elif ans == '4':
#        break
# print(contact)
          
# score = float(input('What is your score?'))
# if score <= 39:
#     print('F')
# elif score <= 44:
#     print('E')
# elif score <= 49:
#     print('D')
# elif score <= 59:
#     print('C')
# elif score <= 69:
#     print('B')
# elif score <= 100:
#     print('A')
# else:
#     print('Score above range')

# USING MULTIPLE COMPARISON OPERATORS
# food = input('What food is available?')
# avail_meat = input('What meat is available?')
# meat_item = ('fish', 'egg', 'beef')
# if food == 'rice' and avail_meat in meat_item:
#     print('i will buy rice')
# else:
#     print('i will not buy anything')
       

# food = input('What food is available?')
# avail_meat = input('What meat is available?')
# meat_item = ('fish', 'egg', 'beef')
# meat = 'fish'
# if food == 'rice' and meat == avail_meat in meat_item:
#     print('i will buy rice')
# else:
#     print('i will not buy anything')
       
# food = input('What food is available?')
# meat = input('What meat is available?')
# if (food == 'rice' and (meat == 'fish' or meat == 'beef'))
#     print('i will buy rice')
# else:cd
#     print('i will not buy anything')
       

# PYTHON LOOP
# A loop is used to execute a block of code repeatedly
# A loop is used in a situation whereby you want to make use of a piece of code over and over but you do not want to write the same code multiple times

# TYPES
# FOR loop is used for iterating over a sequence
# WHILE loop is used to execute a statement as long as a condition is met

# there can be nested for and nested while lops.
# while loop is used when you do not know the number of iteration required
# a while loop evaluates condition if the condition evaluate to True, the code inside the while loop is executed
# the condition is evaluated again.
# This process continues until condition is false. 

# EXAMPLE
# x = 0
# while x <= 10:
#     print("You're welcome to class")
#     x += 1

# x = 1
# while x <= 10:
#     print("You're welcome to class", x)
#     x += 1

# the test condition is always True
# while True:
#  age = int(input('how old are you?'))
#  while age > 18:
#     print('You can vote!')
#     break
#  else:
#     print('You are not eligible to vote!')

# i = 1
# n = 5
# while i <= n:
#     print(i)
#     i = i + 1

# x = 0
# while x <= 10:
#     x+=1
#     if x == 5:
#         break
#     print('You are welcome', x)
# else:
#     print('The condition was successful')

# total = 0
# number = int(input('Enter a number:'))
# # add numbers until number is zero
# while number != 0:
#     total += number  #total = total + number
     
#     #  take integer input again
#     number = int(input('Enter a number:'))
# print('total =', total)

# counter = 0
# while counter < 3:
#     print('Inside loop')
#     counter = counter + 1
# else:
#     print('Inside else')

# For Loop
# name = ['Kayode', 'Akin', 'dammy', 'gbenga', 'shola', 'james', 'john']
# new_name = ['kayode', 'tunde', 'sunday', 'tuesday', 'friday', 'monday']
# for i in new_name:
#     name.append(i)
# print(name)

# my_ = ['shade', 'energy', 'magnet', 'charse', 'energy']
# for name in my_:
#     print(name)

# num = []
# for x in range(1, 20):
#     val = input('enter your number or q to quit')
#     if val == 'q':
#         break
#     num.append(val)
# print(num)

# for i in range(1, 13):
#     print(i, 'Times')
#     for j in range(1, 11):
#         print(str(i) + 'times' + str(j) + ' = ' + str(i*j))

# FUNCTION 
# Is a block of organized, reusable code that is used to perform some task it is usually call   by its name when its tasks needs execution 

# WHY DO WE USE FUNCTION
# To avoid repetition of code (DRY)
# For code to run faster and for easy readability
# For code reusability and easy debugging

# TYPES OF FUNCTION
# Built-in function
# User defined function

# 3 stages of function; function definition, function declaration, function invocation



# val1 = 50
# val2 = 20
# def addition():
#     result = val1 + val2
#     print("the result of this addition is", result)
#     substract()
# def substract():
#     result = val1 - val2
#     print(result)
# addition()


# val1 = 50
# val2 = 20
# def algebral():
#     global val1
#     val3 = 35
#     val1 = 25
#     res = val1 + val3 * 5
#     print(res)
#     substraction()
   
# def substraction():
#     val3 = 20
#     result = val1 - val3
#     print(result)
# algebral()


# def menu():
#     print(""" 
#          1. Daily plan
#          2. Weekly plan
#          3. Monthly plan
#          4. Two months plan
#          5. Three months plan 
#          6. Back
#          """)
# ussd = input("please enter your ussd\n")
# while ussd != "*131#":
#      reply = input("invalid input!!! please try again\n")
#      if reply == "*131#":
#         break
# menu()
 
# Parameterized and non-parameterized function
# parameterized function = input given to a function
# Required argument
# the number of argument should be the same in both f.call and f.def
# position should be followed
# EXAMPLE
# def display(a,b):
#     print(a,b)
# display(10, 20)

# def student_name(name,score):
#     print("my name is", name, "my score is",  str(score))
# student_name("kayode", 30)

# keyword argument - order/position is not required
# nitialization is done based on keyword(name)
# EXAMPLE
# def display(a,b):
#     print(a,b)
# display(b=20,a=10) 

# def student_name(name,score,department):
#     print("my name is" + name + "my dept is" + department + "and my score is"+ str(score))
# student_name(name ='kayode', score =30, department ='data science')

# Default Argument
# number of arguments need not to be matched with both f.call and f.def
# some of the arguments will be converted to default arguments
# EXAMPLE
# def display(name, course='Data analysis'):
#     print(name)
#     print(course)
# display(name= 'abc', course='Data science')
# display(name = 'pqr')

# Variable length argument
# arbitruary number of arguments done by placing * as prefix to the argument of f.def
# EXAMPLE
# def display(*courses):
#     for i in courses:
#         print(i)
# display('B.tech', 'M.tech', 'Mca')


# ASSIGNMENT
# 1) Write a to-do list
# Solution
# to_do = {}
# while True:
#     print("""
#           1. Add to-do list
#           2. Search to-do list
#           3. Display my to-do list
#           4. Close app
#           """)
#     option = input('select an option\n>')
#     if option == '1':
#        day = input('select a day\n>')
#        tym = input('what time\n>')
#        activity = input('what do you want to do\n>')
#        if day in to_do:
#            to_do[day].append((tym, activity))
#        else:
#            to_do[day] = [(tym, activity)]
#            print('No scheldule found for', day)         
#     elif option == '2':
#        day = input('choose a day/n>').lower().strip()
#        if day in to_do:
#           print('Scheldule for', day)
#           for time, activity in to_do[day]:
#               print(f'{time}: {activity}')
#        else:
#           print('to-do list not found for', day)
#     elif option == '3':
#           print(to_do)
#     elif option == '4':
#        break

       
    #2) Write a program that guesses a random number picked by computer
# import random
# number = random.randint(1, 1000)
# guess = 0
# while guess != number:
#         guess = int(input("Enter Guess:"))
#         if (guess < number):
#             print("Guess Higher!")
#         elif (guess > number):
#             print("Guess Lower!")
#         else:
#             print("You Have Won!!!")


# Return Function
# In python, the "return" statement is used within functions to specify the value that the function should send back or return to the caller. When a function is called , it executes its code and optionally produce a result. The result can be any python data type , such as an integer, string, list, dictionary, etc.

# def student_name():
#     return "timi"
# def subject():
#     print(student_name(), ", your score in mathematics is 90")
# subject()

# val1 = 50
# val2 = 20
# def subtract(a, b):
#     return a - b

# def addition(val3, val4):
#     res = val3 + val4 + subtract(10, 6)
#     return res
# val1 = 50
# val2 = 20
# def myName():
#     return "Yemi"

# def algebral():
#     add = addition(5, 10)
#     result = val1 + val2 * add
#     print("Welcome"+ myName()+ "your score is"+ str(result))
# algebral()



# ASSIGNMENT
# Write a calculator program with a login function
# import time
# import sys
# print('APEX CALCULATOR APP')
# time.sleep(2)
# print('Create an account')
# user_name = input('Enter a username of your choice\n>')
# passcode = input('Enter a preferred password\n>')
# def begin():
#     print('Log In Section')
#     # time.sleep(1)
#     login_user = input('Enter username\n>')
#     login_pass = input('Enter password\n>')
#     while user_name == login_user  and passcode == login_pass :  
#         task()
#     else:
#         print("invalid username or password!!!......input a valid username/password")
#         time.sleep(1)
#         begin()
# def task():         
#     print("""
#         Kindly select an option
#             1. ADDITION
#             2. SUBTRACTION
#             3. DIVISION
#             4. MULTIPLICATION
#             5. EXIT
#                 """) 
#     ops = input('Enter operation option\n>')
#     if ops == "1":
#         def addition():
#             a = float(input("enter a value"))
#             b = float(input("enter a value"))
#             result = a + b
#             print(result)
#         addition()
#     elif ops == '2':
#         def subtraction():
#             a = float(input("enter a value"))
#             b = float(input("enter a value"))
#             result = a - b
#             print(result)
#         subtraction()
#     elif ops == '3':
#         def division():
#             a = float(input("enter a value"))
#             b = float(input("enter a value"))
#             result = a / b
#             print(result)
#         division()
#     elif ops == '4':
#         def multiplication():
#             a = float(input("enter a value"))
#             b = float(input("enter a value"))
#             result = a * b
#             print(result)
#         multiplication()
#     elif ops == '5':
#         sys.exit()
#     else:
#         print('Incorrect code')
# begin()

# FUNCTION-------EXAMPLE

# import sys 
# func = ""
# def login():
#     user_name = input('Enter your username\n>')
#     password = input('Enter your password\n>')
#     if user_name.capitalize()=='Yemi' and password=='1234':
#         operation()
#     else:
#         print('Invalid user_name or password')
#         login()

# def operation():
#     global func
#     print("""Enter your operation:
#           1. Addition
#           2. Subtraction
#           3. Division
#           4. Quit""")
#     option = input(">>>")
#     if option== '1':
#         func = 'Addition'
#         addition()
#     elif option== '2':
#         func = 'Subtraction'
#         subtract()
#     elif option== '3':
#         func = 'Division'
#         division()
#     elif option== '4':
#         sys.exit()
#     else:
#         print('Invalid input')
#         operation()

# def tryAgain():
#     print('Enter 1. perform operation again, 2. go to menu')
#     user = input('>>>')
#     if user== '1':
#         if func=='Addition':
#             addition()
#         elif func=='Subtraction':
#             subtract()
#         elif func=='Division':
#             division()
#     elif user=='2':
#         operation()
#     else:
#         print('Invalid input')
#         tryAgain()

# def subtract():
#     val1 = int(input('Enter value 1 >'))
#     val2 = int(input('Enter value 2 >'))
#     print(val1 - val2)
#     tryAgain()

# def addition():
#     val1 = int(input('Enter value 1 >'))
#     val2 = int(input('Enter value 2  >'))
#     print(val1 + val2)
#     tryAgain()

# def division():
#     val1 = int(input('Enter value 1 >'))
#     val2 = int(input('Enter value 2 >'))
#     print(val1 / val2)
#     tryAgain()
# login()

# Python Object Oriented Programming (OOP)
# class is made up of two things: Data and function which a called class members
# this class members can be assessed by the object of the class
# A variable declared in a class outside a function in that class is called instance variable
# A funtion in a class must carry the ""(self)"" in it

# class student_name():
#     name ='Timi'
#     location ='ibadan'
#     def walk(self):
#         name = 'Ade'
#         print(name,'is walking')
#     def talk(self):
#         print('i am talking')
# rn = student_name()
# print(rn.location)
# print(rn.name)
# rn.talk()
# rn.walk()
# student_name.walk(" ")
# student_name.talk(" ")

# import time
# class car:
#     def __init__(self, owner, location):
#        self.owner = owner
#        self.location = location
#        self.name = 'Toyota'
#        self.color = 'Brown'
#        self.brand = '2019 model'
#        self.trafficator = 'Straight'
#        self.tyre = 4
#        self.stiring = 1
#        self.gear = 0
#        self.details()

#     def details(self):
#         print('This car is owned by' + self.owner + 'and is located in'+ self.location)
#         time.sleep(2)
#         self.startEngine()
    
#     def startEngine(self):
#         print('the engine is started')
#         self.gear = input('Enter gear 1 to take off')
#         if self.gear == "1":
#             self.moveCar()
#         else:
#             print('that is not the right gear to take off')
#             self.startEngine()

#     def moveCar(self):
#         print(self.name+'is in gear'+ self.gear +'and the car is moving'+ self.trafficator)
#         self.driver = input('Press Y to change gear or D to change direction or P to park')
#         if self.driver.upper() == 'Y':
#             self.changeSpeed()
#         elif self.driver.upper() == 'D':
#             self.direction()
#         elif self.driver.upper() == 'P':
#             self.park()
#         else:
#             self.moveCar()

#     def changeSpeed(self):
#          self.gear = input('Enter gera number')
#          if self.gear == '1':
#              self.moveCar()
#          elif self.gear == '2':
#              self.moveCar()
#          elif self.gear == '3':
#              self.moveCar()
#          elif self.gear == '4':
#              self.moveCar()

#     def direction(self):
#         self.trafficator = input('please enter your direction')
#         if self.trafficator.lower() == 'straight':
#             self.moveCar()
#         elif self.trafficator.lower() == 'left':
#             self.moveCar()
#         elif self.trafficator.lower() == 'right':
#             self.moveCar()

#     def park(self):
#         print('the car is parking now ...')
#         time.sleep(2)
#         print('The car has finished parking and application exited')

# cr = car('TIMI', 'Ibadan')

# Python Inheritance - means acquiring properties
# There are two classes - the base class(PARENT CLASS) and derived class(CHILD CLASS)
# Through the object of the derived class we can access the properties of both parent and child class

# TYPES OF INHERITANCE
# 1. Single inheritance and
# 2. Multi-level inheritance

# single inheritance - one base class and one derived class
# class parent:
#     name = "ade"
#     def display(self):
#         print("parent")
# class child(parent):
#     def show(self):
#         print("child")
# c2 = child()
# c2.display()
# c2.show()
# print(c2.name) 

# multi-level inheritance
# base class === derived class === base class === derived class
# grandparent === parent == child

# class grandparent:
#   def gdisplay(self):
#     print("grandparent")
# class parent(grandparent):
#   def pdisplay(self):
#     print("parent")
# class child(parent):
#   def cdisplay(self):
#     print("child")
# class grandchild(child):
#   def grdisplay(self):
#     print("grandchild")
# c3 = child()
# c4 = grandchild()
# c4.gdisplay()
# c4.grdisplay()
# c4.cdisplay()
# c3.gdisplay()
# c3.pdisplay()
# c3.cdisplay()

# class Father:
#   def __init__(self):
#       self.surname = "Adeowo"
#       self.name = "Owolabi"
#       self.skin_color = "dark skin"
#       self.height = "tall"
#       self.language = "Yoruba"
#       self.wlk = "slowly"
#       self.tlk = "loud"
#       self.slp = "snores"

#   def walk(self):
#       print(self.name + " " + self.surname+" is walking "  + self.wlk)
  
#   def talk(self):
#       print(self.name +' from '+self.surname+' talks ' + self.tlk)
  
#   def sleep(self):
#       print(self.name + " " + self.slp +' while sleeping')
    
# class Child(Father):
#     def __init__(self):
#         # Father.__init__(self)
#         super().__init__()
#         self.birth = "2003"
#         self.location = "Ibadan"
#         self.name = "Johnson"
#         self.wlk = "anyhow"

#     def run(self):
#         print(self.name+ " is running up and down")

# class GrandChild(Child):
#     def __init__(self):
#         super().__init__()
#         self.name = "Micheal"
#         self.wlk = "fast"
# ft = Father()
# ch = Child()
# gd = GrandChild()
# gd.walk()
# ch.walk()
# ft.walk()
# gd.sleep()
# ch = Child()
# ch.run()
# ch.sleep()
# print(ch.language)
# ch.walk()
# gd.run()
# gd.talk()
# gd.walk()

# PYTHON MODULE
# A module is considered to be the same as a code library
# i.e
# A file containing a set of functions you want to include in your application
# import pandas
# y = dir(pandas)
# print(y)

# How to Create a Module
# To create a module, save the code you want in a file with the file extension .py:
# import mine
# mine.student_name('Timi')

# EXAMPLE
# step1: Save the code below in a file named mine.py
# def student_name(name):
#     print("my name is" + name)

# step 2: Now we can use the module we just created, by using the import statement:
# import mine

# step 3: Import the module named mine, and call the student_name function:
# import mine
# mine.student_name("timi")
# Note: When using a function from a module, use the syntax: module_name.function_name.

# Variables in Module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

# Example
# Save this code in the file mymodule.py

# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }

# Import the module named mine, and access the person1 dictionary:
# import mine
# a = mine.person1["Age"]
# b = mine.person1["Country"]
# c = mine.person1["name"]
# print(a,b,c)

# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module
# You can create an alias when you import a module, by using the 'as' keyword:
# import mine as m
# a = m.person1["age"]
# b = m.person1["country"]
# c = m.person1["name"]
# print(a,b,c)

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.

# Example
# import sys
# x = dir(sys)
# print(x)

# Import and use the platform module:
# import numpy
# x = dir(numpy)
# print(x)

# import random
# x = dir(random)
# print(x)

# L = "PHONE"
# print(L)
# import platform
# import sys
# y = dir(sys)
# z = dir(platform.sys)
# print(y)
# print(z)
# y = platform.system()
# print(y)
# y = dir(platform)
# y = dir(platform.system())
# print(y)
# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

# Example
# List all the defined names belonging to the platform module:

# import platform

# x = dir(platform)
# print(x)
# Note: The dir() function can be used on all modules, also the ones you create yourself.

# Import From Module
# You can choose to import only parts from a module, by using the from keyword.

# Example
# The module named mymodule has one function and one dictionary:

# def greeting(name):
#   print("Hello, " + name)

# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }
# Example
# Import only the person1 dictionary from the module:

# from mine import person1
# print (person1["age"])
# print (person1["name"])
# print (person1["country"])

# from mine import student_name
# mine.student_name("timi")

# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. 
# Example:
# person1["age"], not mine.person1["age"]

# ASSIGNMENT
# Write a program that functions and operates like a mobile banking app

# SOLUTION

import mysql.connector
mycon = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="wonderkid92",
    database=" APEX_BANK"
    )
mycursor = mycon.cursor()
# mycursor.execute("CREATE DATABASE APEX_BANK")
# mycursor.execute("SHOW DATABASES")
# for i in mycursor:
#     print(i)
# mycursor.execute("CREATE TABLE CUSTOMER_DETAILS (Full_Name VARCHAR(30), Account_number VARCHAR(10), Account_Pin VARCHAR(4), Account_Balance VARCHAR(20))")
# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table)
# mycursor.execute('ALTER TABLE CUSTOMER_DETAILS CHANGE customer_id customer_id INT(4) PRIMARY KEY AUTO_INCREMENT')
# mycursor.execute("ALTER TABLE CUSTOMER_DETAILS ADD UNIQUE(Phone_No, Account_No);")
# myquery = "INSERT INTO CUSTOMER_DETAILS (Full_Name, Account_number, Account_Pin, Account_Balance) VALUES(%s, %s, %s, %s)"
# mycursor.execute(myquery)
# mycon.commit()
# sql = "DELETE FROM CUSTOMER_DETAILS WHERE Account_Balance= %s"
# val = ('1200',)
# mycursor.execute(sql, val)
# query = "SELECT * FROM CUSTOMER_DETAILS WHERE Account_Balance '255000000'"
# mycursor.execute(query)
# output = mycursor.fetchall()      
# print(output)
# for inf in output:
#     print(inf)
# mycon.commit()
# print(mycursor.rowcount, 'record deleted successfully')




import sys
import time
import random
class Bank:
    def __init__(self):
        self.bankname = 'APEX BANK'
        self.name = ""
        self.pin = ""
        self.acc_no = 0
        self.login = []
        self.acc_bal = 0
        self.acc_detail = []
class operation(Bank):
    def __init__(self):
        super().__init__()
        print(f"WELCOME TO {c1.bankname}!!!")
        print("""
              ........................................
              Please select an operation function below
              1. Account Registration
              2. Account Login
              3. Exit
              """)
        ops = input('Select an option\n>')
        if ops == '1':
            c3 = registration()
        elif ops == '2':
            c4 = login()
        elif ops == '3':
            sys.exit()
        else:
           print('Invalid selection! Please try again')
           c2 = operation()

class registration(Bank):
    def __init__(self):
        super().__init__()
        c1.name = input('Enter your name?\n>')
        c1.acc_no = random.randint(1000000000, 10000000000)
        c1.pin = input('Kindly enter a 4digits account pin of your choice\n>')
        while len(str(c1.pin)) == 4:
                c1.acc_detail.append({"Name": c1.name, "Account number": c1.acc_no, "Password": c1.pin})
                print(c1.acc_detail)
                c4 = login()
        else:
            print('PIN input invalid! Enter a 4digits pin\n>')
            c3 = registration()

class login(Bank):
    def __init__(self):
        super().__init__()
        acc_validation = input('Enter your account number\n>')
        password = input('Enter your pin\n>')
        while acc_validation == c1.acc_no or password == c1.pin:
            c5 = bank_app()
        else:
            print('Invalid account number\password! Enter valid details')
            c4 = login()
class bank_app(Bank):
    def __init__(self):
        super().__init__()
        print("""
            Welcome to APEX BANK what would you like to do today?
            1. Check Account Balance
            2. DEPOSIT
            3. WITHDRAW
            4. LOG-OUT
              """)
        option_choice = input('Kindly select an option of what you will like to do\n>')
        if option_choice == '1':
            print(f'Your account balance is: ${c1.acc_bal}')
            c5 = bank_app()
        elif option_choice == '2':
            depo = int(input('How much would you like to deposit?\n>'))
            c1.acc_bal += depo
            print(f'Your account balance is: ${c1.acc_bal}')
            c1.acc_detail.append({"Balance": c1.acc_bal})
        elif option_choice == '3':
            withdrawal = int(input('How much would you like to withdraw?\n>'))
            if withdrawal < c1.acc_bal:
                c1.acc_bal -= withdrawal
                print(f'Your account balance is: ${c1.acc_bal}')
                c1.acc_detail.append({"Balance": c1.acc_bal})
            else:
                print('Insufficient funds!')
                c5 = bank_app()
        elif option_choice == '4':
            c2 = operation()
        else:
            print('Invalid option! Kindly choose within the options provided\n>')
            c5 = bank_app()
        # myquery = "INSERT INTO CUSTOMER_DETAILS VALUES(%s, %s, %s, %s)"
        myquery = "INSERT CUSTOMER_DETAILS VALUES(%s, %s, %s, %s)"
        myvalues = (c1.name, c1.acc_no, c1.pin, c1.acc_bal)
        mycursor.execute(myquery, myvalues)
        mycon.commit()

    
c1 = Bank()
c2 = operation()
c3 = registration()
c4 = login()
c5 = bank_app()



                                        

# PYTHON DATABASE (Mysql) structured query language
# A database is a collection of data stored in a format that can be easily be accessed
# To manage database, we use a software called Database Management System DBMS
# TYPES OF DBMS
# Relational and non Relational(NOSQL)

# To download mysql connector user: pip install mysql_connector
# import mysql.connector
# mycon = mysql.connector.connect(host='127.0.0.1, user='root', passwd='', database='cbttest_db'')

# preparation: You create a connection to the database using a database using a database library appropriate for your programming language (e.g sqlite for python. mysqli for PHP. etc.).


# import mysql.connector
# mycon = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="wonderkid92",
#     database="sakila")   
# mycursor = mycon.cursor()
# mycursor.execute("show databases")
# for i in mycursor:
#     print(i)

# import mysql.connector
# mycon = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="wonderkid92",
#     database="classwork")
# mycursor = mycon.cursor()

# mycursor.execute("CREATE DATABASE classwork")
# mycursor.execute("show databases")
# for i in mycursor:
#     print(i)

# mycursor.execute("CREATE TABLE CLASS (student_id INT(4), Full_Name VARCHAR(20), Address VARCHAR(50), Phone_number VARCHAR(11), password VARCHAR(20))")
# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table)

# mycursor.execute("ALTER TABLE CLASS CHANGE student_id student_id INT(4) PRIMARY KEY AUTO_INCREMENT")
# mycursor.execute("ALTER TABLE CLASS ADD UNIQUE(Phone_number);")

# myquery = "INSERT INTO CLASS (Full_Name, Address, Phone_number, Password) VALUES(%s, %s, %s, %s)"
# val = (('Timi Adesola', 'Iwo road', '07069507760', '12345'), 
#     ('Jacob Timi', 'ui', '08060587394', '9946'),
#     ('John Amao', 'adenike', '09060587394', '9936'),
#     ('meg essien', 'Agbowo', '08165587394', '9926'),
#     ('Hannah uwana', 'sango', '07060585394', '1946'),
#     ('comfort odeh', 'Agodi', '08060357394', '9146'),
#     ('Frank Idoho', 'VGC', '08055555555', '9145'),
# )
# mycursor.executemany(myquery, val)  
# mycon.commit()

# ASSIGNMENT
# import sys
# import mysql.connector
# mycon = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="wonderkid92",
#     database="schooldata")

# mycursor = mycon.cursor()
# mycursor.execute("CREATE DATABASE schooldata")
# mycursor.execute("SHOW DATABASES")
# for i in mycursor:
#     print(i)

# mycursor.execute("CREATE TABLE REGISTER (student_details INT(4), Full_Name VARCHAR(20), Age VARCHAR(7), Gender VARCHAR(4), Exam_score VARCHAR(3))")
# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table)

# mycursor.execute("ALTER TABLE REGISTER CHANGE student_details student_details INT(4) PRIMARY KEY AUTO_INCREMENT")
# mycursor.execute("ALTER TABLE REGISTER ADD UNIQUE(Exam_score);")



# myquery = "INSERT INTO REGISTER(Full_name, Age, Gender, Exam_score) VALUES(%s, %s, %s, %s)"
# print("""
#     Menu
#     1. Register
#     2. Exit
#       """)
# menu = input('Kindly select a menu\n>')
# while menu == '1':
# Full_name = input('Input your name\n>')
# Age = input('Input your age\n>')
# Gender = input('Input your gender\n>')
# Exam_score = input('Input your score\n>')
# menu = input('Kindly select a menu\n>')
# if menu == '2':
#     sys.exit()

# val = (Full_name, Age, Gender, Exam_score)
# mycursor.execute(myquery, val)  
# mycon.commit()



# query = "SELECT * FROM class"
# # query = "SELECT Full_Name, Phone_number FROM class"
# mycursor.execute(query)
# output = mycursor.fetchall()   #fetches all rows from the last executed statement
# # print(output)
# for inf in output:
#     print(inf)

# query = "SELECT * FROM payment WHERE amount > '2'"
# query = "SELECT * FROM payment WHERE staff_id != '1'"
# query = "SELECT * FROM payment WHERE rental_id < '5000' AND payment_id > '200'"
# mycursor.execute(query)
# output = mycursor.fetchall()       #fetches all rows from the last executed statement
# print(output)
# for inf in output:
#     print(inf)

# query = "SELECT * FROM class WHERE Full_Name LIKE '%a'"
# query = "SELECT * FROM class WHERE Full_Name LIKE 'J%'"
# mycursor.execute(query)
# output = mycursor.fetchall()      
# print(output)
# for inf in output:
#     print(inf)


# query = "SELECT * FROM class WHERE Full_Name LIKE '_______O'"
# #This is the number of characters before "o"
# mycursor.execute(query)
# output = mycursor.fetchall()      
# print(output)
# for inf in output:
#     print(inf)

# query = "SELECT * FROM class WHERE Full_Name IS NULL"
# # where that specific row is vacant
# query = "SELECT * FROM class WHERE Full_Name IS NOT NULL"
# # where that specific row is not vacant
# mycursor.execute(query)
# output = mycursor.fetchall()      
# print(output)
# for inf in output:
#     print(inf)


#******SORTING
# query = "SELECT * FROM class ORDER BY Full_Name " #ascending order
# query = "SELECT * FROM class ORDER BY Full_Name DESC" #descending order
# mycursor.execute(query)
# output = mycursor.fetchall()      
# print(output)
# for inf in output:
#     print(inf)

# sql = "UPDATE CLASS SET student_id='8' WHERE Phone_number=%s"
# val =('08060587394',)
# mycursor.execute(sql, val)
# mycon.commit()
# print(mycursor.rowcount, 'record updated successfully')


# sql = "DELETE CLASS WHERE Phone_number=%s"
# val =('08060587394',)
# mycursor.execute(sql, val)
# mycon.commit()
# print(mycursor.rowcount, 'record deleted successfully')

# sql = "DROP TABLE CLASS"
# mycursor.execute(sql)


# FILE HANDLING
# A file is a container in computer storage devices used for storing data
# When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that resources that are tied with the file are freed.
# Python has several functions for creating, reading, updating, and deleting files.
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode
# There are four different methods (modes) for opening a file:
# myFile = open("filename", mode='r', 'a', 'w', 'x', encoding= 't', 'b')
# 'r' read only anf it is default for open function. Raise error if file does not exist
# 'a' Append new content to an existing file. Create new file with the specified name if file does not exist
# 'w' Open file for writing. Create new file with the specified name if file does not exist
# 'x' To create new file. Raise error if file already exist

# with open("filename", mode="rt") as myFile:

# myFile = open("C:\\Users\\YEMI\\Documents\\python code.txt", "rt")

# myFile = open("C:\\Users\\YADTECH\\anaconda3\\Lib\\site-packages\\mysql_connector-2.2.9.dist-info\\top_level.txt", "rt")
# print(myFile.read())

# print(myFile.readline())    #Reads the first line

# for text in myFile:
#     print(text)

# import docx2txt
# myFile = open("C:\\Users\\YADTECH\\Documents\\i am a believer.txt", "rt")
# print(myFile)
# # myFile = docx2txt.process("SWP.rtf")
# print(myFile.read())

# myFile = open("C:\\Users\\YADTECH\\Documents\\i am a believer.txt", "a")
# myFile.write("\n Jesus is Lord")
# # myFile.close()
# myFile = open("C:\\Users\\YADTECH\\Documents\\i am a believer.txt", "rt")
# print(myFile.read())
# myFile.close()


# myFile = open("infile.txt", 'w')
# myFile.write("\n this is a new content to append to the old file")

# myFile = open("infile.txt", 'rt')
# print(myFile.read())
# myFile.close()

# import os
# if os.path.exists("C:\\Users\\YADTECH\\Documents\\i am a believer.txt"):
#     with open("C:\\Users\\YADTECH\\Documents\\i am a believer.txt", mode="rt") as myfile:
#         print(myfile.read())
# else:
#     print("File does not exist")

# if os.path.exists("infile.txt"):
#     os.remove("infile.txt")
#     print("file deleted successfully")
# else:
#     print("File not available")

# os.mkdir("new folder")
# os.rmdir("new folder")
# # code to remove folder containing contents in it
# for root, dirs, files in os.walk("Documents"):
#     for file in files:
#         os.remove("Documents\\"+file)
# os.mkdir("Documents")

# code to get username of any System(pc)
# import os.path
# homedir = os.path.expanduser("~")
# print(homedir)

# # code to get system environment
# import os
# homedir = os.environ["PATH"]
# print(homedir)

# # code to get the path of a file on your device
# print(os.path.dirname(os.path.abspath("Excel tutorial.txt")))

# PYTHON ERROR HANDLING
# Two types of error in programming:
# compile time error and run time error
# try and except, finally

# def simpleCall():
#     for i in range(5):
#         a = int(input("enter quotient value\n>>"))
#         b = int(input("enter quotient value\n>>"))
#         print(a/b)
# simpleCall()

# def call():
#     for i in range(5):
#         a = int(input("enter quotient value\n>>"))
#         b = int(input("enter quotient value\n>>"))
#         try:
#             print(a/b)
#         except:
#             print("divisor can not be zero")
# call()       

# def call():
#     for i in range(5):
#         a = int(input("enter quotient value\n>>"))
#         b = int(input("enter quotient value\n>>"))
#         try:
#             print(a/b)
#         except ZeroDivisionError:
#             print("divisor can not be zero")
#         except TypeError:
#             pass
#         except:
#             pass
#         else: # execute if no error was raised
#             print('no error was raised')
#         finally: # execute either there is error or not
#             print('The execution was successful')
# call()     

# a = int(input('enter quotient value\n>>'))  
# b = int(input('enter quotient value\n>>')) 
# if type(b) is not int:
#     raise TypeError('divisor must be an integer type')
# else:
#     print(a/b) 



# Python Regular Expression
# regular expression is a sequence of characters that forms a search pattern.
# it can be used to check if a string contains the specified search pattern.
# import re
# text = """the value of a thing will determine the capacity you put to it. the value of 2019 is what you get in 2020
#        and now you get the value of 2020 in 2021"""
# val = re.search("^the.*get$", text)
# if val:
#     print("We have a match")
# else:
#     print("No match detected")
 
# re function
# findall() : returns list containing all matches
# search() : returns object of a match if there is a match anywhere in the string
# split() : returns a list where the string has been splitted at each match
# sub() : replace one or many matches  with a string
 
# re matacharacters
# [] : refers to set of characters to match eg "[a-m]"
# \ : can be use to escape special character eg "\d"
# . : any character except newline character eg 'he.o'
# ^ : starts with eg "^the"
# $ : ends with eg "world$"
# * : zero or more occurrences eg "aix*"
# + : one or more occurrences eg "aix+"
# {} : exactly specified number of occurrence eg "al{2}"
# | : either or eg "this|that"
# () : capture and group 

# re special Sequences
# \A : returns a match if the specified characters are at the begining of the string eg "\AThe"
# \b : returns a match if the specified characters are at the begining or at the end of the string eg r"\bthe" or r"the\b"
# \B : returns a match if the specified characters are present but not at the begining or at the end of the string eg r"\Bthe" or r"the\B"
# \d : returns a match where the string contains digits (number from 0-9) eg "\d"
# \D : returns a match where the string does not contains digits eg "\D"
# \s : returns a match where the string contains a white space character eg "\s"
# \S : returns a match where the string does not contains a white space character eg "\S"
# \w : returns a match where the string contains characters from letter A-Z and digits from 0-9 and underscore eg "\w"
# \W : returns a match where the string does not contains any word characters  
# \Z : returns a match if the specified characters are at the end of the string

# re sets
# [arn] : returns a match where one of the specified characters (a or r or n ) are present
# [a-n] : returns a match for any lower case character alphabetically between a and n
# [^arn] : returns a match for any character except a, r and n
# [0123] : returns a match where any of the specified digits (0, 1, 2, 3) are present
# [0-9] : returns a match for any digits between 0 and 9
# [0-5][0-9] : returns a match for any two digits between 00 and 59
# [a-zA-Z] : returns a match for any character alphabetically between a and z lower case or upper case
# [+] : returns a match for any character in the string

# x = re.findall(r'you', text)
# print(x)
# x = re.search(r'you', text)
# print(x)
# print(x.span())
# print(x.group())
# print(x.string)

# z = re.split(r'\s', text)
# print(z)
# z = re.split(r'\s', text, 10)
# print(z)
# tx = re.sub(r'\d', 'anything', text)
# print(tx)
# tx = re.sub(r'capacity', 'ability', text)
# print(tx)
# tx = re.sub(r'\d', '[]', text, 6)
# print(tx)

# Python DateTime
# import datetime 
# tim = datetime.datetime.now() #to display the current date
# print(tim)
# print(tim.strftime("%p"))
# print(tim.year) #to extract or get the year
# print(tim.strftime("%A")) #returns the weekday
# tm = datetime.datetime(2021, 4, 10)
# print(tm)   
# print(tm.month) #to get the month
# print(tm.strftime("%B"))

# To create Date object
# we use datetime() class constructor of the datetime module. it requires three parameters to create
# tm = datetime.datetime(2021, 4, 10, 11, 30, 20)
# print(tm)
# print(tm.day)
# print(tm.strftime("%a"))
# print(tm.strftime("%U"))

# strftime() method - use to format datetime object into readable string
# print(tm.strftime("%B")) #returns the name of month

# # strftime format codes
# %a : returns weekday in short version eg wed
# %A : returns weekday in full version eg wednesday
# %w : returns weekday in number version from 0-6 where 0 means sunday eg wed is 3 
# %d : returns day of the month in number version from 01-31
# %b : returns month name in short version eg Dec
# %B : returns month name in full version eg December
# %m : returns month in number format from 01-12 
# %y : returns year in short version eg 2021 is 21
# %Y : returns year in full version eg 2021
# %H : returns hour in 24hrs format from 00-23
# %I : returns hour in 12hrs format from 00-12
# %p : returns AM or PM of time
# %M : returns minute of time from 00-59
# %S : returns seconds of time from 00-59
# %f : returns microseconds of time form 000000-999999
# %Z : for timezone
# %j : days number of the year from 001-366
# %U : return week number of the year from 00-54 

# tm = datetime.datetime.now()
# print(tm.strftime("%j"))

# while True:
#     tm = datetime.datetime.now()
#     if tm.strftime("%I") == "04" and tm.strftime("%M") == "29" and tm.strftime("%S") == "00" and tm.strftime("%p") == "PM":
#         print("it's time for break")
#     else:
#         print("lecture continues")
#     break

# import datetime
# check = int(datetime.datetime.now().strftime("%M")) 
# # print(check)
# rang =[]
# [rang.append(rn) for rn in range(0,60)]
# # print(rang)
# while True:
#     time = datetime.datetime.now() 
#     nexttime = time.strftime('%M')
#     if int(nexttime) in rang and check == int(nexttime):   
#         for i in range(5):
#             print("i am going for class today")
#     check = int(nexttime )+ 1

# hour = hour[0]+str(int(hour[1]) + 2)

# Python Math class
# import math, cmath
# l = [2, 4, 5, 7, 3]
# print(min(l))
# print(max(l))
# print(abs(-5.34))
# print(pow(5, 3))
# print(math.sqrt(9))
# print(math.ceil(6.3492))
# print(math.floor(5.6732))
# print(math.pi)
# print(math.pi * 1000 + 25)












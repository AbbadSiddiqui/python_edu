#https://youtu.be/ix9cRaBkVe0?si=qM6tJ77dC-k0F1OI (Bro Code 12H YT Tutorial)
#https://www.youtube.com/watch?v=nLRL_NcnK-4 (Harvard CS50 Introdusction to Programming with Python)

#WHILE LOOPS#
#name = input("Enter your name : ")
#while name == "":
#    print("You did not enter your name")
#    name = input("Enter your name : ")
#print(f"Hello {name}")

#num = int(input("Enter a # between 1-10 : "))
#while num < 1 or num > 10 :
#    print(f"{num} is invalid")
#    num = int(input("Enter a # between 1-10 : "))
#print(f"Your number is {num}")

#FOR LOOPS#
#NESTED LOOPS#

#SHOPPING CART EXERCISE#
#foods = []
#prices = []
#total = 0

#while True:
#    food = input("Enter a food to buy (q to quit) : ")
#    if food.lower() == "q":
#        break
#    else:
#        price = float(input(f"Enter the price of a {food}: AED"))
#        foods.append(food)
#        prices.append(price)
#
#print("***YOUR CART***")
#for food in foods:
#    print(food)
#for price in prices:
#    total += price
#print(f"Your total is {total} AED")

##RECURSION##
#ITERATIVE#
#def walk(steps):
#    for step in range (1, steps + 1):
#        print(f"You're take step #{step} ")
#walk(100)

#RECURSIVE#
#def walk(steps):
#    if steps == 0:
#        return
#    walk(steps - 1)
#    print(f"You're take step #{steps} ")    
#walk(100)

#how to def#
#def main():
#    x = int(input("What is x? "))
#    print("x sqaured is", square(x))
#def square(n):
#    return n * n
#main()

#how to while loop#
#i = 7
#while i != 0:
#    print("meow")
#    i = i - 1

#i = 0
#while i < 6:
#    print("meow")
#    i += 1

#how to for loop#
#for i in range(7):
#   print("meow")

#how to dict# {dictionary uses curly brace}
#students = {
#    "Hermione": "Gryffindor",
#    "Harry": "Gryffindor",
#    "Ron": "Gryffindor",
#    "Draco": "Slytherin",
#}
#for student in students:
#   print(student, students[student], sep=", ")

#modules#
#import cowsay
#import sys

#if len(sys.argv) == 2:
#    cowsay.trex("hello, " + sys.argv[1])

#api's and json#
#import json
#import requests
#import sys

#if len(sys.argv) != 2:
#    sys.exit()

#response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

#o = response.json()
#for result in o ["results"]:
#   print(result["trackName"])

#file i/o#
#name = input("What's your name? ")
#file = open("names.txt", "a")
#file.write(f"{name}\n")
#file.close()

#name = input("What's your name? ")
#with open("names.txt", "a") as file:
#    file.write(f"{name}\n")

#regular expressions#
#email = input("What is your email? ").strip()
#if "@" in email:
#    print("Valid")
#else:
#    print("Invalid")
#
#import re

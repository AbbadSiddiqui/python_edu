#https://youtu.be/ix9cRaBkVe0?si=qM6tJ77dC-k0F1OI

#name = input("Enter your name : ")
#while name == "":
#    print("You did not enter your name")
#    name = input("Enter your name : ")
#print(f"Hello {name}")

num = int(input("Enter a # between 1-10 : "))
while num < 1 or num > 10 :
    print(f"{num} is invalid")
    num = int(input("Enter a # between 1-10 : "))
print(f"Your number is {num}")
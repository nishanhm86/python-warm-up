num = int(input("Enter a number: "))    #defining variable

if num > 0:
    print ("The number is positive")    #if variable > 0 result positive number
elif num < 0:
    print ("The number is negative")    #if variable > 0 result negative number
else:
    print ("The number is zero")        #if variable = 0 result says Zero

age = int(input("Enter your age: "))    #goruping people based on their age

if age < 13:
    print ("You are a child")
elif 13 <= age < 18:
    print ("You are a teenager")
elif 18 <= age < 60:
    print("You are an Adult")
else:
    print("You are a Senior Citizen")


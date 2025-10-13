def check_number():
    num = int(input("Enter a number: "))  # defining variable

    if num > 0:
        print("The number is positive")  # if variable > 0 result positive number
    elif num < 0:
        print("The number is negative")  # if variable > 0 result negative number
    else:
        print("The number is zero")  # if variable = 0 result says Zero

def check_age():
    age = int(input("Enter your age: "))  # goruping people based on their age

    if age < 13:
        print("You are a child")
    elif 13 <= age < 18:
        print("You are a teenager")
    elif 18 <= age < 60:
        print("You are an Adult")
    else:
        print("You are a Senior Citizen")
def check_loop():

    print ("===for loop===")
    for i in range(1,10):
        print(i)

    print("====whileloop====")
    count = 1
    while count <= 10:
        print(count)
        count += 1

    print("===break condition===")
    for j in range(1, 10):
        if j == 5:
            break
        print(j)

    print("===continue condition===")
    for a in range(1, 10):
        if a == 5:
            continue
        print(a)

#____________Main Menu____________

while True:
    print("\n Python Warm_up")
    print("1. Check if Number is positive/negative/zero")
    print("2. Check age category")
    print("3. Check Loop Demonstration")
    print("4. Exit")

    choice = input("Enter your choice(1-4): ")
    if choice == "1":
        check_number()
    elif choice == "2":
        check_age()
    elif choice == "3":
        check_loop()
    elif choice == "4":
        print("Exiting the program")
        break
    else:
        print("Invalid choice, please try again")

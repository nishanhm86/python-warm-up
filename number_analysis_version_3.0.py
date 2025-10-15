numbers = []

def save_to_file():
    with open("numbers.txt", "w") as file:
        for number in numbers:
            file.write(str(number) + "\n")
    print("Numbers Successfully Saved to the File!")

def load_from_file():
    global numbers
    try:
        with open("numbers.txt", "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]
            print("Numbers Loaded Successfully!")
    except FileNotFoundError:
        print("No saved file found!")
        print("No saved file found — new file created.")

load_from_file()


while True:
    print("=" * 25)
    print("Welcome to Number Analysis!")
    print("=" * 25)
    print("1. Add a number")
    print("2. Display numbers")
    print("3. Total of the numbers")
    print("4. Display the Average")
    print("5. Find Minimum Numbers")
    print("6. Find Maximum Numbers")
    print("7. Remove numbers")
    print("8. Sort Numbers Ascending Order")
    print("9. Sort Numbers Descending Order")
    print("10. Search a number")
    print("11. Clear all Numbers")
    print("12. Save Numbers to the file")
    print("13. Load Numbers from the file")
    print("14. Exit the program")

    choice = input("Enter your choice: ")
    if choice == "1":
        n = int(input("Enter How many numbers to be added: "))
        for i in range (n):
            num = int(input(f"Enter a number: {i + 1}: "))
            numbers.append(num)
        save_to_file()
        print("Numbers Successfully Added!")
        print("-" * 30)


    elif choice == "2":
        if len(numbers) == 0:
            print("No numbers added yet!")
        else:
            print("Numbers entered with indices")
            for i, num in enumerate(numbers):
                print(f"{i}: {num}")
            print("-" * 30)

    elif choice == "3":
        if len(numbers) == 0:
            print("No numbers added yet!")
        else:
            print(f"Total of the numbers: {sum(numbers)}")
        print("-" * 30)

    elif choice == "4":
        if len(numbers) == 0:
            print("No numbers added yet!")
        else:
            average = sum(numbers) / len(numbers)
            print(f"Average of the numbers: {average:.2f}")
        print("-" * 30)

    elif choice == "5":
        if len(numbers) == 0:
            print("No numbers added yet!")
        else:
            print("Minimum of the numbers", min(numbers))
        print("-" * 30)

    elif choice == "6":
        if len(numbers) == 0:
            print("No numbers added yet!")
        else:
            print("Maximum of the numbers", max(numbers))
        print("-" * 30)

    elif choice == "7":
        if len(numbers) == 0:
            print("No number to remove!")
        else:
            print("Number with indices")
            for i, num in enumerate(numbers):
                print(f"{i}: {num}")
            try:
                index = (int(input("Enter a Index to Remove Number: ")))
                if 0 <= index < len(numbers):
                    removed = numbers.pop(index)
                    print(f"Number {removed} Successfully Removed!")
                    save_to_file()
                else:
                    print("Invalid Index!")
            except ValueError:
                print("Enter valid Index!")
            print("-" * 30)

    elif choice == "8":
        if not numbers:
            print("No numbers to sort!")

        else:
            numbers.sort()
            print ("Numbers Sorted in Ascending Order:")
            for i, num in enumerate(numbers):
                print(f"{i}: {num}")
            save_to_file()
            print("-" * 30)

    elif choice == "9":
        if not numbers:
            print("No numbers to sort!")

        else:
            numbers.sort(reverse = True)
            print("Numbers Sorted in Descending Order:")
            for i, num in enumerate(numbers):
                print(f"{i}: {num}")
            save_to_file()
            print("-" * 30)

    elif choice == "10":
        if len(numbers) == 0:
            print("No numbers to be search!")
        else:
            print("Numbers entered with indices")
            for i, num in enumerate(numbers):
                print(f"{i}: {num}")
            print("-" * 30)
            try:
                target = int(input("Enter the Number to Search: "))
                indices = [i for i, num in enumerate(numbers) if num == target]
                if indices:
                    print(f"Number {target} Found at index/indices: {indices}!")
                else:
                    print(f"Number {target} not found in the list.")
            except ValueError:
                print("Enter a valid Index!")
            print("-" * 30)



    elif choice == "11":
        if len(numbers) == 0:
            print("No numbers to remove!")
        else:
            confirm = input("Are you sure you want to remove all numbers? (Y/N): ").lower()
            if confirm == "y":
                numbers.clear()
                print("All Numbers Successfully Cleared!")
            save_to_file()
            print("-" * 30)

    elif choice == "12":
        save_to_file()
        print("-" * 30)

    elif choice == "13":
        load_from_file()
        print("-" * 30)

    elif choice == "14":
        print("Final Numbers List:", numbers)
        print("Goodbye! Leaving the system")
        break

    else: print("The input is invalid. Please check and enter the correct number")

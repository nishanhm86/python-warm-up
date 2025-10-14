numbers = []

while True:
    print("=" * 20)
    print("Number Analysis Module")
    print("=" * 20)
    print("1. Add Numbers")
    print("2. Display Numbers")
    print("3. Display Total")
    print("4. Display Average")
    print("5. Find Maximum and Minimum")
    print("6. Remove a Number")
    print("7. Exit")

    choice = input("Enter your choice(1-7): ")
    if choice == "1":
        n = int(input("Enter how many numbers to add: "))
        for i in range(n):
            num = int(input(f"Enter a number {i + 1} : "))
            numbers.append(num)
        print("Numbers Added Successfully!")

    elif choice == "2":
        if len(numbers) == 0:
            print("No numbers added yet!")
        else:
            print("Numbers Entered:", numbers)

    elif choice == "3":
        if len(numbers) == 0:
            print("No numbers added yet!")
        else:
            total = sum(numbers)
            print("Total:", total)

    elif choice == "4":
        if len(numbers) == 0:
            print("No numbers added yet!")
        else:
            average = sum(numbers) / len(numbers)
            print(f"Average: {average:.2f}")
    elif choice == "5":
        if len(numbers) == 0:
            print("No numbers added yet!")
        else:
            print("Maximum:", max(numbers))
            print("Minimum:", min(numbers))

    elif choice == "6":
        if len(numbers) == 0:
            print("No numbers added yet!")
        else:
            print("Numbers Entered:", numbers)
            try:
                index = input("Enter index to remove number: ")
                if 0 <= int(index) < len(numbers):
                    removed_number = numbers.pop(int(index))
                    print(f"Numbers {removed_number} Removed Successfully!")
                    print("Updated list", numbers)
                else:
                    print("Invalid index provided!")
            except ValueError:
                print("Please enter a valid index!")

    elif choice == "7":
            print("Goodbye. Leaving the program.")
            break

    else:
        print("Enter a valid choice between 1-6")
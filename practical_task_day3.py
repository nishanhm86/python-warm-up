numbers = []

while True:
    print("=" * 20)
    print("Number Analysis Module")
    print("=" * 20)
    print("1. Add Numbers")
    print("2. Display Numbers")
    print("3. Display Total")
    print("4. Display Average")
    print("5.Find Maximum and Minimum")
    print("6.Exit")

    choice = input("Enter your choice(1-6): ")
    if choice == "1":
        n = int(input("Enter the size of numbers: : "))
        for i in range(n):
            num = int(input(f"Enter a number {i + 1} : "))
            numbers.append(num)
        print("Numbers Added Successfully")

    elif choice == "2":
        if len(numbers) == 0:
            print("No numbers added")
        else:
            print("Numbers Entered:", numbers)

    elif choice == "3":
        if len(numbers) == 0:
            print("No numbers added")
        else:
            total = sum(numbers)
            print("Total:", total)

    elif choice == "4":
        if len(numbers) == 0:
            print("No numbers added")
        else:
            average = sum(numbers) / len(numbers)
            print("Average:", average)
    elif choice == "5":
        if len(numbers) == 0:
            print("No numbers added")
        else:
            maximum = max(numbers)
            print("Maximum:", maximum)
            minimum = min(numbers)
            print("Minimum:", minimum)

    elif choice == "6":
            print("Goodbye. Leaving the program.")
            break

    else:
        print("Enter a valid choice between 1-6")
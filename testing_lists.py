numbers =[]

n = input("Enter how many number need to be entered: ")

for i in range(int(n)):
    num = int(input(f"Enter a number {i + 1} : "))
    numbers.append(num)

total = sum(numbers)
average = total/len(numbers)

print("Numbers Entered: ", numbers)
print("Total:", total)
print(f"Average: {average:.2f}")
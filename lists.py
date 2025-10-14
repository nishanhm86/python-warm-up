numbers = [10, -20, -30, 40, 50, 60, -70, -80, 90, 100]

print ("First Number:", numbers[0])
print ("Last Number:", numbers[-1])

print("Print All Numbers")
for num in numbers:
    print (num)

for n in numbers:
    if n>0:
        print(n , "is a positive number")
    elif n<0:
        print(n , "is a negative number")
    else:
        print (n, "is Zero")
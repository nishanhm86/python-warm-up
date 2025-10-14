print ("===for loop===")
for i in range(1,10):
    print(i)

print("====whileloop====")
count = 1
while count <= 10:
    print(count)
    count += 1

print("===break condition===")
for j in range(1,10):
    if j == 5:
        break
    print(j)

print("===continue condition===")
for a in range(1,10):
    if a == 5:
        continue
    print(a)
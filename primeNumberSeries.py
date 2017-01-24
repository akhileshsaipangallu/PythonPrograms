n = input("Enter the range for prime number series (greater than 1)\n")
print("1")
for count in range(2 , n + 1):
    flag = 1
    for i in range(2  , (count / 2) + 1):
        if count % i is 0:
            flag = 0
            break
    if flag is 1:
        print(count)

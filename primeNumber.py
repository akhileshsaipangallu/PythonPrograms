n = input("Enter a number \n")
flag = 1
for i in range(2  , (n / 2) + 1):
    if n % i is 0:
        flag = 0
        break

if flag is 0:
    print("\n%d is not a prime number" % (n , ))
else:
    print("\n%d is a prime number" % (n,))

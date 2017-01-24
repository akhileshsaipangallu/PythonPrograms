def series(a , b):
    temp = b
    b = a + b
    a = temp
    return (a , b)

num = input("Enter a number to check if its in Fibonacci Sequence \n")

f1 , f2 , f3 = (0 , 1 , 2)
fibSeries = [f1 , f2 , f3]

while True:
    f2 , f3 = series(f2 , f3)
    if(f3 <= num):
        fibSeries.append(f3)
    else:
        break
if num in fibSeries:
    print("Entered number is in Fibonacci Sequence")
else:
    print("Entered number is not in Fibonacci Sequence")

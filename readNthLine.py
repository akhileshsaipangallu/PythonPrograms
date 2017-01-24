f = open("test.txt" , "r" )
n = input("Enter the line number\n")

content = f.readlines()
print(content[n - 1])

#method 2
#for i in range(1 , n + 1):
 #   content = f.readline()
  #  if i is n:
   #     print(content)

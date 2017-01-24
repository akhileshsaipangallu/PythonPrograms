f = open("test.txt" , "r" )
givenWord = input("Enter a word\n")

w = []
for line in f:
    for word in line.split(" "):
        for miniWord in word.split("\n"):
            for realWord in miniWord.split("."):
                w.append(realWord)
counter = w.count(givenWord)
print("Word = %s \nOccourance = %d" % (givenWord , counter))

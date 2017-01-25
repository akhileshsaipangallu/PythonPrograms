
list = os.listdir(loc)

def listIt(list , loc):
    for elem in list:
        if os.path.isdir("%s/%s" % (loc , elem)):
            dirName.append(loc + " " + elem)
            listIt(os.listdir(loc + "/%s" % elem) , loc + "/%s" % elem) # recursion
        else:
            fileName.append(loc + " " + elem)


listIt(list , loc) #method call

print ("Dir:")
for i in dirName:
    print i
print ("\n")

print ("Files:")
for i in fileName:
    print i

#test variable insertion into strings
test_string = "test"
print(f'I want to {test_string}')

#test add elements to list
mylist = [1,2,3]
mylist

newlist = [4,5,6]
addedlist = mylist+newlist
print(f"{addedlist[0]}")

#Dictionnary nesting
MyDict = {1 : [1,2,3], 2 : [4,5,6], 3 : [7,8,9]}
print(MyDict[1][1])

#Test file open function
MyFile = open("TextTest.txt")

#print(MyFile.read())

print(MyFile.readlines())

#close to file to avoid error
MyFile.close()

with open("sfdsdfsdf.txt", mode="w") as f:
    f.write("I created this file")


#Print working directory only work in notebook
#print(pwd)


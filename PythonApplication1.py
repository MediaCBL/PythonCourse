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
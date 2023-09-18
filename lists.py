#lists basic overview
#define list and prepopulate with integers and a string
array = [5,6,7,8,"bob"]
print (array)
#add integer to list 
array.append(10)
print (array)
#remove string from list
array.remove("bob")
print (array)
#all arrays/lists start with 0, this prints the first item in the list
print (array[0])
#this prints the current last item in the list
print (array[4])
#change the value of a list item
array[3] = 89
print (array)
#user input evaluate int or str 
userInputOne = eval(input("Please enter an integer here so my code doesn't break: "))
#add user input variable to array
array.append(userInputOne)
print (array)
#variable adds first list item and the last list item input by user
addingListItems = array[0] + array[5]
print(addingListItems)
#create another array/list with only strings
secondList = ["apple", "orange", "banana"]
print (secondList)
#to swap items (ie.. apple[0] <~~|~~> banana[2]) in the list's number order you need to use another variable
temporaryVariable = secondList[0]
secondList[0] = secondList[2]
secondList[2] = temporaryVariable
print(secondList)


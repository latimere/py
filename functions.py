#python functions (I didn't grasp this concept entirely in CSMC210)
#
#defines function1()
def function1():
    print("hello, would you kindly close the door")
    print("this line is still within function1")
print("this is outside of function1")
#defines function2 as a mapping
def function2(numberPlusOne):
    print(numberPlusOne - 1)
#this calls function1()
function1()
#user input defines the variable x as an integer
number = int(input("Please enter a whole number for x: "))
print("You entered:")
print(number)
print("now we will add 1 to x")
#since we made the input an integer, you can do arithmetic with the user input variable
numberPlusOne = (number + 1)
print(numberPlusOne)
print("ok now lets call function2 and get the user input back to the original number")
#this calls function2 with the required input (numberPlusOne)
function2(numberPlusOne)


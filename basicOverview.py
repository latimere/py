#import library
import os
#define variables
stringVariable = "name"
integerVariable = 19
floatingPointVariable = 0.35
#define array
shortList = [7, 8, "casey", .586]
#variable = user's keyboard input   \n = escape character and newline
userStringInput = input("\n Would you kindly enter a word or letter (string): \n \n")
userIntegerInput = int(input("\n Would you kindly enter an integer (whole number): \n \n"))
userFloatInput = float(input("\n Would you kindly enter a floating point number (decimal number): \n \n"))
#define variable + arithmetic operators (** = exponentation)
arithmetic = (integerVariable + floatingPointVariable) - 1 * 2 ** 4 / 1.55
#add variable to end of array using method (methods are functions associated with specific objects)
shortList.append(userStringInput)
#define variable using information from imported os module
operatingSystemInformation = os.uname()
#print to console/terminal shortList[0,1] shows first item in array          
print("\nPrinted info: \n", 4, "\n", shortList[0], "\n", arithmetic, "\n", operatingSystemInformation, "\n", userFloatInput)
#float variable% = remainder
unformattedFloat = 20 % 3.12
#format floating point two decimal points
twoDecimalFormattedFloat ="{:.2f}" .format(unformattedFloat)
print("\n", "Unformatted float:", unformattedFloat, "\n \nFormatted float:", twoDecimalFormattedFloat, "\n")
#define variables for function
x = int(input("\n Would you kindly enter an integer for x: "))
y = int(input("\n Would you kindly enter an integer for y: "))
#define function with arguments
def functionWithArguments (x, y):
    subtractionAnswer = x - y
    print("\n x - y =", subtractionAnswer)
#call function
functionWithArguments(x,y)
#import module from local .py file as newly named function
from localPythonModule import functionToBeExported as importedFunction
#call function from imported module
importedFunction()
#define variables in while loop
whileLoopCounter = 0
whileLoopValue = 0
#while loop (infinate loop with escape value)
while whileLoopValue != -999:
    while True:
        try:
            whileLoopValue = int(input("\nWould you kindly enter an integer: \n"))
            whileLoopCounter = whileLoopCounter + 1
            break
        except:
            print("\nSorry, that input wasn't valid. Please try again.\n")
else:
    whileLoopCounter = whileLoopCounter - 1
    print("\nYou have now exited the while loop\n") 
    print("\nWhile loop iterations: ", whileLoopCounter, "\n")
#for loop
for i in "Python":
    print(i, "\n")
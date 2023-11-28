#import library
import os
#define variables
stringVariable = "name"
integerVariable = 19
floatingPointVariable = 0.35
#define array
shortList = [7, 8, "casey", .586]
#variable = user's keyboard input   \n = escape character and newline
userStringInput = input("\n input string only: \n \n")
userIntegerInput = int(input("\n input integer only: \n \n"))
userFloatInput = float(input("\n input float only: \n \n"))
#define variable + arithmetic operators (** = exponentation)
arithmetic = (integerVariable + floatingPointVariable) - 1 * 2 ** 4 / 1.55
#add variable to end of array using method (methods are functions associated with specific objects)
shortList.append(userStringInput)
#define variable using information from imported os module
operatingSystemInformation = os.uname()
#print to console/terminal shortList[0,1] shows first item in array          
print("\nprinted info: \n", 4, "\n", shortList[0], "\n", arithmetic, "\n", operatingSystemInformation, "\n", userFloatInput)
#float variable% = remainder
unformattedFloat = 20 % 3.12
#format floating point two decimal points
twoDecimalFormattedFloat ="{:.2f}" .format(unformattedFloat)
print("\n", "unformatted float:", unformattedFloat, "\n \n formatted float:", twoDecimalFormattedFloat, "\n")
#define variables for function
x = int(input("\n enter an integer for x: "))
y = int(input("\n enter an integer for y: "))
#define function with arguments
def functionWithArguments (x, y):
    subtractionAnswer = x - y
    print("\n x - y =", subtractionAnswer)
#call function
functionWithArguments(x,y)
#import module from local file as newly named function
from localPythonModule import importedFunction as iFunc
#call function from imported module
iFunc()
#while loop
#for loop

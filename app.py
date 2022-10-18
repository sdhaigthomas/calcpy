
"""
from statistics import mode
from timeit import repeat
from replit import clear
from random import randint

#########################
class BasicCalc():
    def addition(num1, num2):
        ans = num1 =+ num2
        return ans
    
    def subtraction(num1,num2):
        ans = num1 =- num2
        return ans

    def multiplication(num1,num2):
        ans = num1 =- num2
        return ans

class PrintTG():#tg is for terminal/gui
    pass


def printans(strtp):
    print("The answer is", str(strtp) + ".")

#########################
print("Welcome to Calcpy!")

#mode = input("Terminal[1], GUI[2]")


num1 = 1
num2 = 3

method = int(input("Addition[1] | Addition[2] | Multiplication[3]"))



if method == 1: printans(BasicCalc.addition(num1,num2))
elif method == 2: printans(BasicCalc.subtraction(num1,num2))

printans(BasicCalc.addition(num1,num2))


#########################

"""


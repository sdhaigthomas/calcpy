from statistics import mode
from replit import clear
from random import randint

#########################
class BasicCalc():
    def addition(num1, num2):
        ans = num1 =+ num2
        return ans


def printans(strtp):
    print("The answer is", str(strtp)+".")

#########################
print("Welcome to Calcpy!")
mode = input

num1 = 1
num2 = 3

printans(BasicCalc.addition(num1,num2))


#########################
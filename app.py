
#########################
import random

#########################

print("Calcpy! By sdht")


def gtn():
    while True:
        turn=0
        difficulty = input("Easy(1), Medium(2), Hard(3) or Custom(4)\n")
        if difficulty=="1": amount=25
        elif difficulty=="2": amount=50
        elif difficulty=="3": amount=100
        elif difficulty=="4": amount=int(input("Custom: 1 to\n"))
        else: print("Unknown mode. Defaulting to 0, 25"), amount
        ans=random.randint(1,amount)
        while True:
            try:geuss=int(input("Whats your guess?\n"))
            except: geuss=1
            turn+=1
            if geuss==ans:
                print("You won in",turn,"tries!")
                break
            else:
                if geuss<=ans:print("The number is larger then", geuss)
                else:print("The number is smaller then then", geuss)

gtn()
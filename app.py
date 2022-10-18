
#########################
import random, time

#########################

class Games():
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
    
    def dcms():
        currency = "£"

        up_down = 0
        doge_coin_price = 25
        doge_coin_owned = 0

        money = 100
        move = 0

        print("""
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@#((((///////////((((#@@@@@@@@@@@@@@
        @@@@@@@@@@@(((//*,//////////////*////((#@@@@@@@@@@
        @@@@@@@@((///////,*///////////////*((////((@@@@@@@
        @@@@@@((*///////*,/******//////(/((((///*//((@@@@@
        @@@@((//////*..               . .(%((////////((@@@
        @@@(////////,        .           .. */////////((@@
        @@((///////,  ...       ..         .. /////////((@
        @((/*///**   ,,,     .. *&**,,         /*///*///(&
        @(//////*...&&&&,.      ,,,,,,,        .////////((
        @(///////,..#&&&.       ,,,,,,,         /////////(
        @(/////*/. .,#&&.       ,,,,,,.         *///////((
        @((/////**...,*(. . .   ,,....         **///////(&
        @@((//////,..                      ...,/**/////((@
        @@@((/////,,*                      . *,,,/////((@@
        @@@@((////,,,                     ,,,,,,/////(#@@@
        @@@@@@/(*,,,,,,,*****,,,,,,,,,,,,,,,,,,*//*((@@@@@
        @@@@@@@@((*,,,,,**,,,,,,,,,,,,,,,,,,,*//((%@@@@@@@
        @@@@@@@@@@@#((****,,,,,,,,,,,,,,,,,,*((%@@@@@@@@@@
        @@@@@@@@@@@@@@@@((((*,,,,,,,,*/((((@@@@@@@@@@@@@@@
        """)

        play = input("Welcome To Doge Coin Mineing Simulator!\n         Press enter to play\n")

        


        while True:

            print("____________________________________________")
            print(" Doge Coin Owned:", doge_coin_owned, "\n Doge Coin Price:",doge_coin_price, "\n Money:", "£" + str(money))
            print("____________________________________________")
            move = input("\nWould you like to buy(1), sell(2) or wait till tomorrow (Enter)\n")
            max_buy = money / doge_coin_price
            if move == "1":
                amount_to_buy = int(input("How many doge coins do you want to buy?\n"))
                if (doge_coin_price * amount_to_buy) > money:
                    print("Oh no, You cant afford that!\n")
                else:
                    doge_coin_owned += amount_to_buy
                    money -= doge_coin_price * amount_to_buy
            elif move == "2":
                amount_to_sell = int(input("How many would you like to sell?\n"))
                if int(amount_to_sell) > int(doge_coin_owned):
                    print("You dont own that many doge coin!")
                else:
                    print("You just sold", amount_to_sell, "for", currency, (amount_to_sell * doge_coin_price), "\n\n")

                    money += (amount_to_sell * doge_coin_price)
                    doge_coin_owned -= amount_to_sell
            elif move == "":
                up_down = random.randint(1,10)
                doge_coin_price_u_d = random.randint(1,3)
                print(doge_coin_price_u_d)
                if doge_coin_price_u_d == 1:
                    doge_coin_price += up_down
                if doge_coin_price < 5:
                    doge_coin_price = random.randint(5,20)
                else:
                    doge_coin_price -= up_down
            else:
                print("Opps! Thats not somthing you can do! dum dum\n\n")
                time.sleep(1.5)



#########################


print("Calcpy! By sdht")


game = input("Guess the number[1] | ")



Games.gtn()
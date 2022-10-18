try:
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
            dcp = 25
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
                print(" Doge Coin Owned:", doge_coin_owned, "\n Doge Coin Price:",dcp, "\n Money:", "£" + str(money))
                print("____________________________________________")
                move = input("\nWould you like to buy(1), sell(2) or wait till tomorrow (Enter)\n")
                max_buy = money / dcp
                if move == "1":
                    amount_to_buy = int(input("How many doge coins do you want to buy?\n"))
                    if (dcp * amount_to_buy) > money:
                        print("Oh no, You cant afford that!\n")
                    else:
                        doge_coin_owned += amount_to_buy
                        money -= dcp * amount_to_buy
                elif move == "2":
                    amount_to_sell = int(input("How many would you like to sell?\n"))
                    if int(amount_to_sell) > int(doge_coin_owned):
                        print("You dont own that many doge coin!")
                    else:
                        print("You just sold", amount_to_sell, "for", currency, (amount_to_sell * dcp), "\n\n")
                        money += (amount_to_sell * dcp)
                        doge_coin_owned -= amount_to_sell
                elif move == "":
                    up_down = random.randint(1,10)
                    dcp_u_d = random.randint(1,3)
                    print(dcp_u_d)
                    if dcp_u_d == 1:dcp += up_down
                    if dcp < 5: dcp = random.randint(5,20)
                    else: dcp -= up_down

                    if dcp < 2: dcp = random.randint(5,10)


                else:
                    print("Opps! Thats not somthing you can do! dum dum\n\n")
                    time.sleep(1.5)



    #########################


    print("Calcpy! By sdht")


    game = int(input("Guess the number[1] | Doge Coin Mining Simulator![2]"))

    if game == 1: Games.gtn()
    elif game == 2: Games.dcms()

except:
    print("There Has Been A Critical Error!")
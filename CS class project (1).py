#CS project, A RANGE

import random
 
print("Welcome! Today we will be playing a slot machine game! You will both be given 5 dollar to start. The rules are as follows: Player one will go first, having the option to spin up to three times. Within each spin, you will be given a number 0-2. If you spin 3 of the same numbers, you lose all of your money and your turn ends. If the sum of the number is a multiple of 3, you will win half of your money. If the sum of the numbers is even, but not a multiple of 3, you will lose half of your money. Any other outcome you will win the amount of the sum of the number! Once player ones turn ends, player two, you will go! Whoever has the most money leftover wins! Good luck, let us begin!") 
name1=input(str("Player 1, what is your name?"))
name2=input(str("Player 2, what is your name?"))
print("Ok,", name1, "and", name2, "lets begin!", name1, "you will go first!")

name1total=0
name1turns=0
name2total=0
name2turns=0

name1cash=5
name2cash=5

keepgoing1='yes'
keepgoing2="yes"


while name1turns<3 and name1cash>0 and keepgoing1=='yes':
    reel1=random.randint(0,2)
    reel2=random.randint(0,2)
    reel3=random.randint(0,2)
    total1=name1cash

    if (reel1==reel2==reel3):
        name1cash=name1cash*0
        print(reel1,reel2,reel3)
        print(name1, "it seems like you got three of the same numbers and lost! You now have, $",name1cash, "total and your turn is over. Now onto the second players turn! Goodluck!")
        name1turns=name1turns+1
    elif (reel1+reel2+reel3)%3==0:
        name1cash=name1cash+name1cash/2
        print(reel1,reel2,reel3)
        print(name1, "you won half of your money! You now have, $",name1cash, "total")
        name1turns=name1turns+1
        if name1turns<3 and name1cash>0 and keepgoing1=='yes':
            keepgoing1=input(str("do you want to go again? (yes/no)"))
    elif (reel1+reel2+reel3)%2==0 and (reel1+reel2+reel3)%3!=0:
        name1cash=name1cash/2
        print(reel1,reel2,reel3)
        print(name1, "you lost half of your money!,", "You now have, $",name1cash, "total")
        name1turns=name1turns+1
        if name1turns<3 and name1cash>0 and keepgoing1=='yes':
            keepgoing1=input(str("do you want to go again? (yes/no)"))
    else:
        name1cash=name1cash+(reel1+reel2+reel3)
        print(reel1,reel2,reel3)
        print(name1, "you won something!", "You now have, $",name1cash, "total")
        name1turns=name1turns+1
        if name1turns<3 and name1cash>0 and keepgoing1=='yes':
            keepgoing1=input(str("do you want to go again? (yes/no)"))
              
print("ok, now its your turn", name2)

while name2turns<3 and name2cash>0 and keepgoing2=="yes":
    reel1=random.randint(0,2)
    reel2=random.randint(0,2)
    reel3=random.randint(0,2)

    if (reel1==reel2==reel3):
        name2cash=name2cash*0
        print(reel1,reel2,reel3)
        print(name2, "it seems like you got three of the same numbers and lost! You now have, $",name2cash, "total and your turn is over!")
        name2turns=name2turns+1
    elif (reel1+reel2+reel3)%3==0:
        name2cash=name2cash+name2cash/2
        print(reel1,reel2,reel3)
        print(name2, "you won half! You now have, $",name2cash, "total")
        name2turns=name2turns+1
        if name2turns<3 and name2cash>0 and keepgoing2=='yes':
            keepgoing2=input(str("do you want to go again? (yes/no)"))
        elif keepgoing2=="no" and name2turns>3 and name2cash<0:
            print(name2, "your turn is over, you have won $",total2, " total!")
    elif (reel1+reel2+reel3)%2==0 and (reel1+reel2+reel3)%3!=0:
        name2cash=name2cash/2
        print(reel1,reel2,reel3)
        print(name2, "you lost half!,", "You now have, $",name2cash, "total")
        name2turns=name2turns+1
        if name2turns<3 and name2cash>0 and keepgoing2=='yes':
            keepgoing2=input(str("do you want to go again? (yes/no)"))
        elif keepgoing2=="no" and name2turns>3 and name2cash<0:
            print(name2, "your turn is over, you have won $",total2, " total!")
    else:
        name2cash=name2cash+(reel1+reel2+reel3)
        print(reel1,reel2,reel3)
        print(name2, "you won something!", "You now have, $",name2cash, "total")
        name2turns=name2turns+1
        if name2turns<3 and name2cash>0 and keepgoing2=='yes':
            keepgoing2=input(str("do you want to go again? (yes/no)"))
        elif keepgoing2=="no" and name2turns>3 and name2cash<0:
            print(name2, "your turn is over, you have won $",total2, " total!")

if name1cash==name2cash:
    print("Both players turns are over!", name1, "and", name2, "it looks like you both had the same amount of money in the end, its a tie! You both are taking", name1cash, "dollars home today! Enjoy whatever winnings you got!")
elif name1cash>name2cash:
    print("Both players turns are over! Congragulations", name1, "at the end of the game you won! You finished with", name1cash, "dollars total! Enjoy your winnings!")
else:
    print("Both players turns are over! Congragulations", name2+"!", "At the end of the game you won! You finished with", name2cash, "dollars total! Enjoy your winnings!")
    


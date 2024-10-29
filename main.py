import random

playerhand = random.(randint) + random.(randint)(1,10)
dealerhand = random.(randint)(1,10)
print(dealerhand)
while dealerhand < 17:
    dealerhand =+ random.randit(1,10)
    print(dealerhand)

gamecondition = 2


if dealerhand >21:
    print("you win")
    gamecondition = 0
elif dealhand == 21:
    print("you lose")
    gamecondition = 1
if gamecondition >1:
    print(f"your current hand value is: {playerhand}")
    hitOrstand = input("hit or stand")

    while hitOrstand == ('hit'):
        playerhand =+ random.randint(1,10)


import random
options=["ROCK","PAPER","SCISSOR"]
option=random.choice(options)
print()
print("-----------_ROCK_PAPER_SCISSOR_-----------")
print()
while True:
    player=input("enter(ROCK,PAPER,SCISSOR):").upper()
    if option==player:
        print("TIE")
        pass
    elif player=="ROCK"and option=="SCISSOR" or player=="PAPER"and option=="ROCK" or player=="SCISSOR" and option=="PAPER":
        print("PLAYER WIN")
        break
    else:
        print("COMPUTER WIN")
        break
print("THANK YOU :)")
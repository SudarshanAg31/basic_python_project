#slot machine
import random
def choice():
    sloat=["L","K","J","H","G"]
    z=[]
    for _ in range(3):
       z.append(random.choice(sloat)) 
    return z

def balance(current_blance,amount):
    if current_blance<amount:
        print("no money left")
        exit()    
    current_blance=current_blance-amount
    return current_blance

def check_result(z):
    if z[0]==z[1]==z[2]:
        return "win"
    else:
        return "loose"

current_blance=100    
while True:
    print("************************")
    print("Welcome to python Sloats")
    print("symbols: L K J H G")
    print("************************")
    print(f"Current blance: ${current_blance}")
    amount=int(input("place your bet amount: "))
    z=choice()
    print(z)
    a=check_result(z)
    print(a)
    current_blance=balance(current_blance,amount)
    print(f"your balance:{current_blance}")
    y=input("do you want to spin again?(Y/N):")
    if y=="N"or"n":
        print("thank you")
        break 
    else:
        pass
        



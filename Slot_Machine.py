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

def check_result(z,amount):
    if z[0]==z[1]==z[2]:
        if z[0]=="L":
            return amount*200
        if z[0]=="K":
            return amount*300
        if z[0]=="J":
            return amount*400
        if z[0]=="H":
            return amount*500
        if z[0]=="G":
            return amount*600
    return 0

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
    a=check_result(z,amount)
    if a==0:
        print("loose")
    else:
        print("win")
        current_blance=a+current_blance
        
    current_blance=balance(current_blance,amount)
    print(f"your balance:{current_blance}")
    y=input("do you want to spin again?(Y/N):")
    if y==(("N")or("n")):
        print("thank you")
        break 
    else:
        pass
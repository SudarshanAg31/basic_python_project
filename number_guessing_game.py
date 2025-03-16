import random
number=random.randint(1,100)
number_of_guess=0
print("-----------GAME START-----------")
while True:
    guess=int(input("enter guess B/W (1-100):"))
    if guess==number:
        break
    elif guess>=number:
        print("guess is to high:")
        number_of_guess+=1
    elif guess<=number:
        print("guess is to low:")
        number_of_guess+=1
print()
print("-----------RESULT-----------")
print(f"CORRECT:{number}")
print(f"number of guess:{number_of_guess+1}")
print("THANK YOU :)")
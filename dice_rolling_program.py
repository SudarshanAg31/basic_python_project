import random
dice_art={ 
        1:("----------",
           "|        |",
           "|    *   |",
           "|        |",
           "----------",),
        
        2:("----------",
           "|       *|",
           "|        |",
           "|*       |",
           "----------",),
        
        3:("----------",
           "|       *|",
           "|    *   |",
           "|*       |",
           "----------",),
        
        4:("----------",
           "|*      *|",
           "|        |",
           "|*      *|",
           "----------",),
        
        5:("----------",
           "|*      *|",
           "|    *   |",
           "|*      *|",
           "----------",),
        
        6:("----------",
           "|*      *|",
           "|*      *|",
           "|*      *|",
           "----------",),
        }
dice=[]
total=0
number_of_dice=int(input("enter number of dice:"))#3
for i in range(number_of_dice):
    dice.append(random.randint(1,6))

for i in range(number_of_dice):
    for j in dice_art.get(dice[i]):
        print(j)

for i in dice:
    total+=i
print()
print(f"total:{total}")
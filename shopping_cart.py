food_item=[]
food_price=[]
total=0
while True:
    food=input("enter food item(press q for quit): ")
    if(food=="q"):
        break
    else:
        price=float(input(f"enter price of {food}:"))
        food_item.append(food)
        food_price.append(price)
print("------shopping cart------")
for food in (food_item):
    print(food,end=",")
for price in (food_price):
    total+=price
print()
print(f"total:${total}")

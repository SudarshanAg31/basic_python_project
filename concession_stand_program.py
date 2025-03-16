#concession stand program
menu={"apple":120,
      "banana":40,
      "orange":50,
      "pineapple":100,
      "coconat":60,
      "kevi":180,
      }
total=0
cart=[]
for i,j in menu.items():
    print(f"{i:10}:$ {j:.2f}")
while True:
    fruit=input("enter fruit name(q for quit):")
    if fruit=="q":
        break
    cart.append(fruit)
print(cart)
for i in cart:
    total+=menu.get(i)
    print(i,end=" ")
print()
print(total)
    

        
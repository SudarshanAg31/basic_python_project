enter_data=input("enter pasword:")
for i in enter_data:
    x=0
    x=ord(i)
    x=x-4
    print(chr(x),end="")

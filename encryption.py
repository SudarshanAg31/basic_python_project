enter_password=input("enter password:")
for i in enter_password:
    x=0
    x=ord(i)
    x=x+4
    if x>127:
        while x>127:
            x=x-127
    elif x<0:
        while x>0:
            x=x+127
    print(chr(x),end="")
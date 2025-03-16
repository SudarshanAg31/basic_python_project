#usser name program
#it must not contain more then 12 letter
#it must not contain any white spaces
#it must not contain any number
result=input("enter name:")
if len(result)<=12 and len(result)>0:
        if result.isalpha()==True:
            print(f"valid name: {result}")
        else:
            print("not valid")
else:
    print("not valid")
     
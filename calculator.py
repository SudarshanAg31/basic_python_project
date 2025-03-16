x=input("enter operation + - * / :- ")
y=float(input("enter number 1: "))
z=float(input("enter number 2: "))
if x=="+":
    result=y+z
    print(f"your answer: {round(result,2)}")
elif x=="-":
    result=y-z
    print(f"your answer: {round(result,2)}")
elif x=="*":
    result=y*z
    print(f"your answer: {round(result,2)}")
elif x=="/":
    result=y/z
    print(f"your answer: {round(result,2)}")
else:
    print("enter valid operation")
    
    
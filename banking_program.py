#BANKING_PROGRAM
def show_balance():
    global current_blance
    print(current_blance)
    choose_option()

def deposit():
    global current_blance
    enter_money=float(input("enter money:"))
    while enter_money<1:
        print("enter valid amount")
        enter_money=float(input("enter money:"))
    current_blance=current_blance+enter_money

def withdraw():
    global current_blance
    enter_money=float(input("enter money:"))
    while enter_money<1:
        print("enter valid amount")
        enter_money=float(input("enter money:"))
    current_blance=current_blance-enter_money

def options(option):
    if option==1:
        show_balance()
    elif option==2:
        deposit()
        show_balance()
    elif option==3:
        withdraw()
        show_balance()
    elif option==4:
        print("thank you")
        exit()

def choose_option():
    option=int(input("______press number______\n1:show blance\n2:deposit money\n3:withdraw money\n4:exit\nenter number:"))
    while option<1 or option>4:
        print("enter valid option")
        option=int(input("______press number______\n1:show blance\n2:deposit money\n3:withdraw money\n4:exit\nenter number:"))
    options(option)

current_blance=0.0
choose_option()
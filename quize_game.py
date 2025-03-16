
questions=["1:- 1+2=?",
        "2:- what is the color of sun?",
          "3:- which one is fruit",
          "4:- 3 times 5 is?",]

options=[["A: 2","B: 4","C: 3","D: 6"],
        ["A: red","B: yellow","C: pink","D: green"],
        ["A: apple","B: car","C: mobile phone","D: mouse"],
        ["A: 34","B: 51","C: 15","D: 67"]]

answer=["C","B","A","C"]

score=0
question_num=0
for i in questions:
        print(i)
        for y in options[question_num]:
                print(y)
        guess=input("ENTER ANSWER: ").upper()
        if guess==answer[question_num]:
                score+=1
                print("CORRECT ANSWER")
                print()
        else:
                print("INCORRECT ANSWER")
                print(f"CORRECT ANSWER IS: {answer[question_num]}")
                print()
        question_num+=1
        
print()
print(f"{score}/4")
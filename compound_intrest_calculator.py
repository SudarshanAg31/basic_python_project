import math
time=0
rate=0.0
principle_amount=0.0
number_of_rate=0
while time<=0:
    time=int(input("enter time: "))
    if(time<=0):
        time=int(input("enter time: "))

while rate<=0:
    rate=float(input("enter rate: "))
    if(rate<=0):
        rate=int(input("enter rate: "))
rate=rate*0.01

while principle_amount<=0:
    principle_amount=float(input("enter principle_amount: "))
    if(principle_amount<=0):
        principle_amount=float(input("enter principle_amount: "))

while number_of_rate<=0:
    number_of_rate=int(input("enter number_of_rate: "))
    if(number_of_rate<=0):
        number_of_rate=int(input("enter number_of_rate: "))

result=principle_amount*pow(1+rate/number_of_rate,number_of_rate*time)
print(f"final amount: {result:.2f}")
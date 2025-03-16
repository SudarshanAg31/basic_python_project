import time
sec=int(input("enter time in sec: "))
for x in range(sec,0,-1):
    second=x%60
    minutes=int(x/60)%60
    hours=int(x/3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{second:02}")
print("happy new year")
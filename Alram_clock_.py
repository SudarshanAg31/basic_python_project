import time
import datetime
import pygame
def set_alram():
    print("enter time for alram")
    alram=input("enter HH:MM:SS :-")
    return alram
def current_time(alram):
    file_pth="C:\\Users\\Lenovo\\Downloads\\baby-shark-122769.mp3"
    while True:
        current=datetime.datetime.now()
        current=current.strftime("%H:%M:%S")
        time.sleep(1)
        print(current)
        if current==alram:
            print("wake up!!")
            pygame.mixer.init()
            pygame.mixer.music.load(file_pth)# to load music
            pygame.mixer.music.play()#for play music
            while pygame.mixer.music.get_busy():#to play untile music stop
                time.sleep(1)
            break        
alram=set_alram()
current_time(alram)

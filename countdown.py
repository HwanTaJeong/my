from time import sleep #import time in sleep
import winsound #import winsound

def countdown(t):
   
    while t:
        mins, secs = divmod(t, 60) #define minutes, seconds
        timer = '{:02d}:{:02d}'.format(mins, secs) #define timer
        print(timer, end="\r") #reset timer
        winsound.Beep(450, 750) #play sound
        sleep(0.25) #give some delay
        t -= 1 #counting time

    print('00:00')
    winsound.Beep(900, 1000)
 
countdown(5)
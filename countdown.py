from time import sleep #ㅇ
import winsound

def countdown(t):
   
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        winsound.Beep(450, 750)
        sleep(0.25)
        t -= 1

    print('00:00')
    winsound.Beep(900, 1000)
 
countdown(5)
##import library
from tkinter import *
import time
from playsound import playsound


## display window 
root = Tk()
root.geometry('350x300')
root.resizable(0,0)
root.config(bg ='#FFD23F')
root.title('Siksha Sarthi-keep learning')
Label(root, text = 'You are focused!!' , font = 'arial 15 bold').pack()


#display current timeZ

Label(root, font ='arial 15 bold', text = 'current time :', bg = '#FFEFDB').place(x = 40 ,y = 70)


####fun to display current time
def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)

curr_time =Label(root, font ='arial 15 bold', text = '', fg = 'gray25' ,bg ='papaya whip')
curr_time.place(x = 190 , y = 70)
clock()


#######################timer countdown##########


#storing seconds
sec = StringVar()
Entry(root, textvariable = sec, width = 2, font = 'arial 12').place(x=250, y=155)
sec.set('00')

#storing minutes
mins= StringVar()
Entry(root, textvariable = mins, width =2, font = 'arial 12').place(x=225, y=155)
mins.set('00')


# storing hours
hrs= StringVar()
Entry(root, textvariable = hrs, width =2, font = 'arial 12').place(x=200, y=155)
hrs.set('00')

##########fun to start countdown

def countdown():
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > -1:
        minute,second = (times // 60 , times % 60)
        
        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)
            
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        
        root.update()
        time.sleep(1)

        if(times == 0):
            playsound('Loud_Alarm_Clock_Buzzer.mp3')
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1

Label(root, font ='arial 15 bold', text = 'set the time',   bg ='papaya whip').place(x = 40 ,y = 150)

Button(root, text='START', bd ='5', command = countdown, bg = 'antique white', font = 'arial 10 bold').place(x=150, y=210)
        


root.mainloop()

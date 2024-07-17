from Tkinter import *
root = Tk()

tt='vv'

def time(tt):
    from time import strftime
    tt=strftime('%H:%M:%S')
    return tt

Label= Label(root,bd=11,text=time(tt))
Label.pack()

root.mainloop()

from tkinter import *
from PIL import Image,ImageTk
import re
root = Tk()
root.iconbitmap(r'calciicon.ico')
root.geometry('220x400')
root.resizable(0,0)
root.config(background = 'Black')
root.title('calci')
scrn = StringVar()
c=0
screen = Entry(font = "Times 25 bold",width = 12,justify = 'right',bg = 'white',fg = "Black",textvariable = scrn).grid(row = 0,column =0,columnspan = 15,rowspan = 2)
var = [StringVar() for i in range(19)]
b = [Button() for i in range(19)]
iconlist = [ImageTk.PhotoImage(Image.open(rf"calu\{i}.jpeg") )for i in range(19)]
n = 0
def cmd(c):
    if c =='c':
        scrn.set("")
    if c=='sign':
        global n
        if n %2==0:
            scrn.set('-'+str(scrn.get()))
        else:
            scrn.set(scrn.get()[1:])
        n+=1
    if c=='cut':
        scrn.set(scrn.get()[0:len(scrn.get())-1])
    if c in  range(0,10):

        scrn.set(scrn.get()+str(c))
    if c in ['/', '*', '-', '+']:
        if scrn.get()[-1] not in ['/', '*', '-', '+']:
            scrn.set(scrn.get() + str(c))
    if c == '.':
        _set = re.split(r'[/*\-+]',scrn.get())

        for element in _set:
            if element.count('.')==0:
                scrn.set(scrn.get()+str(c))
    if c =='=':
        try:
            scrn.set(eval(scrn.get()))
        except:
            scrn.set('invalid syntax')
#making Buttons
for i in range(4):
    for j in range(4):
        b[c]= Button(root, image =iconlist[c] ,width = 28,height =38,textvariable = var[c])
        b[c].grid(row = i+12,column =j,ipadx = 8,ipady = 8,sticky = 'w',pady = 3)

        c+=1
b[c]=Button(root, image =iconlist[16] ,width = 35,height =38,textvariable = var[c],activebackground = "Black" )
b[c].grid(row = 17,column =0,ipadx = 8,ipady = 8,sticky = 'w',pady = 3)
c+=1
b[c] =Button(root, image =iconlist[17] ,width = 35,height =38,textvariable = var[c])
b[c].grid(row = 17,column =1,ipadx = 8,ipady = 8,sticky = 'w',pady = 3)
c+=1
b[c]=Button(root, image =iconlist[18],bg = 'Orange' ,width = 86,height =38,textvariable = var[c] )
b[c].grid(row = 17,column =2,columnspan = 4,ipadx = 8,ipady = 8,sticky = 'w',pady = 3)
#cmd configuration
b[0].configure(command = lambda :cmd('c'))
b[1].configure(command = lambda :cmd('sign'))
b[2].configure(command = lambda :cmd('cut'))
b[3].configure(command = lambda :cmd('/'))
b[4].configure(command = lambda :cmd(7))
b[5].configure(command = lambda :cmd(8))
b[6].configure(command = lambda :cmd(9))
b[7].configure(command = lambda :cmd('*'))
b[8].configure(command = lambda :cmd(4))
b[9].configure(command = lambda :cmd(5))
b[10].configure(command = lambda :cmd(6))
b[11].configure(command = lambda :cmd('-'))
b[12].configure(command = lambda :cmd(1))
b[13].configure(command = lambda :cmd(2))
b[14].configure(command = lambda :cmd(3))
b[15].configure(command = lambda :cmd('+'))
b[16].configure(command = lambda :cmd(0))
b[17].configure(command = lambda :cmd('.'))
b[18].configure(command = lambda :cmd('='))
root.mainloop()

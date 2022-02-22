from tkinter import *
import os
import random as rd
from time import perf_counter

x1=rd.randint(0,99)
x2=rd.randint(0,99)
x3=rd.randint(0,99)
x4=rd.randint(0,99)


print(x1,x2,x3,x4)   # print used for test purpous 

y1=x1-x2   #minus
y2=x3+x4   #add 
y3=x1+x3   #add
y4=x2-x4   #minus

tk=Tk()
tk.title("Math_puzzle")
counter1=0.0
def check():
    if(x1==en1.get() and x2==en2.get() and x3==en3.get() and x4==en4.get()):
        counter2=perf_counter()
        counter=counter2-counter1
        counter=counter/60
        lbr=Label(tk,text=f"Congrastulations, you complete puzzle in {counter} Minutes")
        lbr.place(x=60,y=120)

en1=IntVar()
en2=IntVar()
en3=IntVar()
en4=IntVar()

counter1=perf_counter()
tk.config(bg="yellow")
enl1=Entry(tk,textvariable=en1,bg="#00e6e6",fg="#cc0033")
enl2=Entry(tk,textvariable=en2,bg="#00e6e6",fg="#cc0033")
enl3=Entry(tk,textvariable=en3,bg="#00e6e6",fg="#cc0033")
enl4=Entry(tk,textvariable=en4,bg="#00e6e6",fg="#cc0033")

enl1.place(x=0,y=0)
enl2.place(x=60,y=0)
enl3.place(x=0,y=60)
enl4.place(x=60,y=60)

lb11=Label(tk,text="-", bg="#66ff66",fg="#4d0099")
lb12=Label(tk,text="=", bg="#66ff66",fg="#4d0099")
lb13=Label(tk,text=y1,  bg="#66ff66",fg="#4d0099")
lb21=Label(tk,text="+", bg="#66ff66",fg="#4d0099")
lb22=Label(tk,text="-", bg="#66ff66",fg="#4d0099")
lb31=Label(tk,text="+", bg="#66ff66",fg="#4d0099")
lb32=Label(tk,text="=", bg="#66ff66",fg="#4d0099")
lb33=Label(tk,text=y2,  bg="#66ff66",fg="#4d0099")
lb41=Label(tk,text="||",bg="#66ff66",fg="#4d0099")
lb42=Label(tk,text="||",bg="#66ff66",fg="#4d0099")
lb51=Label(tk,text=y3,  bg="#66ff66",fg="#4d0099")
lb52=Label(tk,text=y4,  bg="#66ff66",fg="#4d0099")
#66ff66
lb11.place(x=30,y=0)
lb12.place(x=90,y=0)  
lb13.place(x=120,y=0)
lb21.place(x=0,y=30)
lb22.place(x=60,y=30)
lb31.place(x=30,y=60)
lb32.place(x=90,y=60)
lb33.place(x=120,y=60)
lb41.place(x=0,y=90)
lb42.place(x=60,y=90)
lb51.place(x=0,y=120)
lb52.place(x=60,y=120)


bt=Button(tk,text="Chech now",command=check,bg="#00e673",fg="#cc0099")
bt.place(x=60,y=160)

tk.geometry("600x600")
tk.mainloop()

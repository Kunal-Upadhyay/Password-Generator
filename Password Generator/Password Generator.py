from tkinter import *
from tkinter import messagebox
import string
import random

def NEXT():
    if (L.get(),U.get(),N.get(),S.get())==(0,0,0,0):
        global x
        x+=1
        if(x==5):
            messagebox.showinfo(title="Made By : ",message="Kunal Upadhyay")
            x=0
        else:messagebox.showerror(title="Error",message="Select any one option before proceding")
    else:
        C.pack_forget()
        PassGen.unbind('1')
        PassGen.unbind('2')
        PassGen.unbind('3')
        PassGen.unbind('4')
        PassGen.bind('<BackSpace>',lambda event:BACK())
        PassGen.bind('<Return>',lambda event:password_generator())
        PassGen.bind('<Up>',lambda event: Len.set(str(int(Len.get())+1)))
        PassGen.bind('<Down>',lambda event: Len.set(str(int(Len.get())-1)) if(int(Len.get())>0)else Len.set(Len.get()))
        
        CN.pack(fill = "both", expand = True)
        CN.create_window( 570,230,window = Label(text="Enter Length : ",font="Ariel 22 bold",bg="black",fg="red"))
        CN.create_window( 770,230,window =Spinbox(textvariable=Len,from_=5,to=1000,bg="black",fg="white",font="Ariel 25 bold",width=5))
        CN.create_window( 655,340,window =Button(text="Generate Password",bg="black",fg="white",activebackground="red",font="Ariel 22 ",padx=20,pady=10,command=password_generator))
        CN.create_window( 655,450,window =F)
        CN.create_window( 555,600,window =Button(text="Back",bg="black",fg="white",activebackground="red",font="Ariel 22 ",padx=20,pady=10,command=BACK))
        CN.create_window( 755,600,window =Button(text="Copy",bg="black",fg="white",activebackground="red",font="Ariel 22 ",padx=20,pady=10,command=copy_button))

def copy_button():
    global PW
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(f"{PW.get()}")
    clip.destroy()

def BACK():
    CN.pack_forget()
    C.pack(fill = "both", expand = True)
    PassGen.bind('1',lambda event:L.set(1)if(L.get()==0) else L.set(0))
    PassGen.bind('2',lambda event:U.set(1)if(U.get()==0) else U.set(0))
    PassGen.bind('3',lambda event:N.set(1)if(N.get()==0) else N.set(0))
    PassGen.bind('4',lambda event:S.set(1)if(S.get()==0) else S.set(0))
    PassGen.unbind('<Up>')
    PassGen.unbind('<Down>')
    PassGen.bind('<Return>',lambda event:NEXT())

def password_generator():
    l=0
    Li=[]
    low=[]
    upp=[]
    num=[]
    spch=[]
    password=[]
    global PW
    PW=StringVar()
    if Len.get()=='' or int(Len.get())==0:messagebox.showerror(title="Error",message="length not given")
    else:
        if L.get()==1:
            for i in range(int(Len.get())):low.extend(list(string.ascii_lowercase))
            l+=1
            Li.append(low)
        if U.get()==1:
            for i in range(int(Len.get())):upp.extend(list(string.ascii_uppercase))
            l+=1
            Li.append(upp)
        if N.get()==1:
            for i in range(int(Len.get())):num.extend(list(string.digits))
            l+=1
            Li.append(num)
        if S.get()==1:
            for i in range(int(Len.get())):spch.extend(list(string.punctuation))
            l+=1
            Li.append(spch)
        if int(Len.get())<l:messagebox.showerror(title="Error",message="given length is not Sufficient")
        else:
            for i in range(l):password.extend(random.sample(Li[i],l+(int(int(Len.get())/l))))
            PW.set("".join(random.sample(password,int(Len.get()))))
            lop.delete(0)
            lop.insert(0,f"{PW.get()}")

PassGen=Tk()
PassGen.geometry("1280x700")
PassGen.resizable(0,0)
PassGen.iconphoto(True,PhotoImage(file = "icon.png"))
PassGen.title("Password Generator By Kunal Upadhyay")

global L,U,N,S,x
x=0
L=IntVar()
U=IntVar()
N=IntVar()
S=IntVar()
Len=StringVar()
LOGO= PhotoImage(file = r"Theme\LOGO.png")

C = Canvas(PassGen,bg='black')
C.create_rectangle(45,45,1235,650,outline='red',width=5)
C.create_rectangle(470,27,870,125,outline='white',fill="black",width=2)
C.create_text( 670,80,text="PASSWORD\n         GENERATOR",font="Algerian 25 bold",fill="red")
C.pack(fill = "both", expand = True)

CN = Canvas(bg='black')
CN.create_rectangle(45,45,1235,650,outline='red',width=5)
CN.create_rectangle(470,27,870,125,outline='white',fill="black",width=2)
CN.create_text( 670,80,text="PASSWORD\n         GENERATOR",font="Algerian 25 bold",fill="red")
C.create_window( 650,200,window =Checkbutton(text="Lower Case Letters", variable=L,font="Ariel 22 ",bg="black",fg="red"))
C.create_window( 650,300,window =Checkbutton(text="Upper Case Letters", variable=U,font="Ariel 22 ",bg="black",fg="red"))
C.create_window( 650,400,window =Checkbutton(text="  Numbers", variable=N,font="Ariel 22 ",bg="black",fg="red"))
C.create_window( 650,500,window =Checkbutton(text="Special Characters", variable=S,font="Ariel 22 ",bg="black",fg="red"))
C.create_window( 680,600,window =Button(text="Next",bg="black",fg="white",activebackground="red",font="Ariel 22 ",padx=20,pady=10,command=NEXT))

PassGen.bind('1',lambda event:L.set(1)if(L.get()==0) else L.set(0))
PassGen.bind('2',lambda event:U.set(1)if(U.get()==0) else U.set(0))
PassGen.bind('3',lambda event:N.set(1)if(N.get()==0) else N.set(0))
PassGen.bind('4',lambda event:S.set(1)if(S.get()==0) else S.set(0))
PassGen.bind('<Return>',lambda event:NEXT())

F=Frame(PassGen)
Scroll=Scrollbar(F,orient=HORIZONTAL,bg="red",troughcolor="red")
lop=Listbox(F,height=1,bg="black",fg="white",font="Ariel 25 bold",xscrollcommand=Scroll.set)
Scroll.config(command=lop.xview)
lop.pack()
Scroll.pack(fill=X)
PassGen.mainloop()

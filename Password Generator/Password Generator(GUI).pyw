from tkinter import *
from tkinter import messagebox
import string
import random

def CB(event,X,N):
    if N[0]==0:
        X.config(image=on)
        N[0]=1
    else :
        X.config(image=off)
        N[0]=0

def NEXT():
    if (L[0],U[0],N[0],S[0])==(0,0,0,0):
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
        PassGen.bind('<Down>',lambda event: Len.set(str(int(Len.get())-1))if(int(Len.get())>0)else Len.set(Len.get()))
        
        CN.create_image(0,0, image = bg,anchor=NW)
        CN.pack(fill = "both", expand = True)
        CN.create_window( 570,230,window = Label(text="Enter Length : ",font="Ariel 22 bold",bg="black",fg="red"))
        CN.create_window( 770,230,window =Spinbox(textvariable=Len,from_=5,to=1000,bg="black",fg="white",font="Ariel 25 bold",width=5))
        CN.create_window( 655,340,window =Button(image=GP,activebackground="red",command=password_generator,borderwidth=0))
        CN.create_window( 655,450,window =F)
        CN.create_window( 555,600,window =Button(image=Back,activebackground="red",command=BACK))
        CN.create_window( 755,600,window =Button(image=Copy,activebackground="red",command=copy_button))

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
    PassGen.unbind('<Up>')
    PassGen.unbind('<Down>')
    PassGen.bind('1',lambda event,X=Lc:CB(event,X,L))
    PassGen.bind('2',lambda event,X=Uc:CB(event,X,U))
    PassGen.bind('3',lambda event,X=Nm:CB(event,X,N))
    PassGen.bind('4',lambda event,X=Sc:CB(event,X,S))
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
        if L[0]==1:
            for i in range(int(Len.get())):low.extend(list(string.ascii_lowercase))
            l+=1
            Li.append(low)
        if U[0]==1:
            for i in range(int(Len.get())):upp.extend(list(string.ascii_uppercase))
            l+=1
            Li.append(upp)
        if N[0]==1:
            for i in range(int(Len.get())):num.extend(list(string.digits))
            l+=1
            Li.append(num)
        if S[0]==1:
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

global x,Len
x=0
L=[0]
U=[0]
N=[0]
S=[0]
Len=StringVar()

LOGO= PhotoImage(file = r"Theme\LOGO.png")
bg= PhotoImage(file = r"Theme\BG.png")
on= PhotoImage(file = r"Theme\on.png")
off= PhotoImage(file = r"Theme\off.png")
Next= PhotoImage(file = r"Buttons\Next.png")
Copy= PhotoImage(file = r"Buttons\copy.png")
Back= PhotoImage(file = r"Buttons\Back.png")
GP= PhotoImage(file = r"Buttons\GP.png")

C = Canvas(PassGen)
C.create_image(0,0, image = bg,anchor=NW)
C.pack(fill = "both", expand = True)
C.create_window( 670,77,window =Label(PassGen,image=LOGO))

Lc=Label(PassGen,image=off,borderwidth=0)
Uc=Label(PassGen,image=off,borderwidth=0)
Nm=Label(PassGen,image=off,borderwidth=0)
Sc=Label(PassGen,image=off,borderwidth=0)

CN = Canvas()
CN.create_window( 670,77,window =Label(PassGen,image=LOGO))
C.create_window( 500,200,window =Lc)
C.create_window( 500,300,window =Uc)
C.create_window( 500,400,window =Nm)
C.create_window( 500,500,window =Sc)
C.create_text( 700,350,text="Lower case letters \n\n\nUpper case letters\n\n\n       Numbers\n\n\nSpecial characters",font="Ariel 22 ",fill="red")
C.create_window( 680,600,window =Button(image=Next,bg="white",activebackground="red",command=NEXT))

Lc.bind('<1>',lambda event,X=Lc:CB(event,X,L))
Uc.bind('<1>',lambda event,X=Uc:CB(event,X,U))
Nm.bind('<1>',lambda event,X=Nm:CB(event,X,N))
Sc.bind('<1>',lambda event,X=Sc:CB(event,X,S))
PassGen.bind('1',lambda event,X=Lc:CB(event,X,L))
PassGen.bind('2',lambda event,X=Uc:CB(event,X,U))
PassGen.bind('3',lambda event,X=Nm:CB(event,X,N))
PassGen.bind('4',lambda event,X=Sc:CB(event,X,S))
PassGen.bind('<Return>',lambda event:NEXT())

F=Frame(PassGen)
Scroll=Scrollbar(F,orient=HORIZONTAL)
lop=Listbox(F,height=1,bg="black",fg="white",font="Ariel 25 bold",xscrollcommand=Scroll.set)
Scroll.config(command=lop.xview)
lop.pack()
Scroll.pack(fill=X)
PassGen.mainloop()

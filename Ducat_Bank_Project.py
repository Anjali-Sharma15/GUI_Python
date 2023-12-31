import tkinter
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
class BOG(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x800")
        self.title("Bank Of Ghaziabad")
        self.config(bg="light blue")
        self.balance=50000
        photo=PhotoImage(file="BankIcon.png")
        self.iconphoto(False,photo)
        Label(self,text="Welcome to online transaction at BOG!",bg="light blue",font="times 20 bold").pack(pady=10)
        f1=Frame(self).pack()
        f2=Frame(self).pack()
        Label(f1,text="User ID",bg="light blue",font="times 12 bold").place(x=500,y=70)
        Label(f2,text="Password",bg="light blue",font="times 12 bold").place(x=500,y=100)
        # userid=StringVar()
        # pswrd=StringVar()
        self.userid=StringVar()
        e1=Entry(f1,textvariable=self.userid)
        e1.place(x=610,y=70)
        self.pswrd=StringVar()
        e2=Entry(f2,textvariable=self.pswrd)
        e2.place(x=610,y=100)
        # self.data1=e1.get()
        # self.data2=e2.get()
        Label(self,text="New customers kindly register!",fg="red",bg="light blue").place(x=560,y=130)
        f3=Frame(self).pack()
        def login():            
            if self.userid.get()==self.user.get() and self.pswrd.get()==self.passcode.get():
                service=Toplevel(self)
                service.geometry("900x900")
                service.config(bg="light green")
                service.title("Services @ BOG")
                photo=PhotoImage(file="BankIcon.png")
                service.iconphoto(False,photo)
                Label(service,text="Welcome to online services at BOG",bg="light green",font="times 20 bold").pack(pady=20)
                def deposit():    
                    Label(service,text="Enter deposit amount",bg="light green").place(x=200,y=250)
                    self.var=StringVar()
                    self.e1=Entry(service,textvariable=self.var)   
                    self.e1.place(x=330,y=250)
                    def enter():
                        self.balance=self.balance+int(self.var.get())
                        Label(service,text="Account balance =",bg="light green").place(x=200,y=290)
                        Label(service,text=self.balance,bg="light green").place(x=300,y=290)
                    b5=Button(service,text="Enter",command=enter,relief=SUNKEN,bd=2,bg="light blue").place(x=230,y=320)
                    
                b1=Button(service,text="Deposit",command=deposit,bd=2,relief=SUNKEN,bg="pink",width=20,font="times 15 bold").place(x=200,y=180)
                def withdrawal():    
                    Label(service,text="Enter withdrawal amount",bg="light green").place(x=200,y=450)
                    self.var=StringVar()
                    self.e2=Entry(service,textvariable=self.var)   
                    self.e2.place(x=350,y=450)
                    def enter():
                        self.balance=self.balance-int(self.var.get())
                        Label(service,text="Account balance =",bg="light green").place(x=200,y=490)
                        Label(service,text=self.balance,bg="light green").place(x=300,y=490)
                    b5=Button(service,text="Enter",command=enter,relief=SUNKEN,bd=2,bg="light blue").place(x=200,y=530)
                    
                b2=Button(service,text="Withdrawal",command=withdrawal,bd=2,relief=SUNKEN,bg="pink",width=20,font="times 15 bold").place(x=200,y=400)
                def Check_Balance():
                    Label(service,text="Available account Balance =",bg="light green").place(x=500,y=230)
                    Label(service,text=self.balance,bg="light green").place(x=650,y=230)
                b3=Button(service,text="Check Balance",command=Check_Balance,bd=2,relief=SUNKEN,bg="pink",width=20,font="times 15 bold").place(x=500,y=180)
                def logout():
                    m=messagebox.askyesno("Logout","Are you sure you want to exit?",parent=service)
                    if m==YES:
                        service.destroy()
                    if m==NO:
                        pass
                b4=Button(service,text="Logout",command=logout,bd=2,relief=SUNKEN,bg="pink",width=20,font="times 15 bold").place(x=500,y=400)
                
                service.mainloop()
            else:
                Label(self,text="Please try again!",bg="light blue").place(x=560,y=200)
        def register():
            win=Toplevel(self)
            win.geometry("600x600")
            win.title("Registration Form @ BOG")
            win.config(bg="light green")
            photo=PhotoImage(file="BankIcon.png")
            win.iconphoto(False,photo)
            # registration form labels
            Label(win,text="Registration Credentials!",font="times 20 bold",bg="light green").pack(pady=10)
            Label(win,text="Name",font="times 11 bold",bg="light green").place(x=30,y=50)
            Label(win,text="Phone Number",font="times 11 bold",bg="light green").place(x=30,y=90)
            Label(win,text="User ID",font="times 11 bold",bg="light green").place(x=30,y=130)
            Label(win,text="Password",font="times 11 bold",bg="light green").place(x=30,y=170)
            # registration from entries
            self.name=StringVar()
            self.phoneno=StringVar()
            self.user=StringVar()
            self.passcode=StringVar()
            e3=Entry(win,textvariable=self.name)
            e3.place(x=140,y=50)
            e4=Entry(win,textvariable=self.phoneno)
            e4.place(x=140,y=90)
            e5=Entry(win,textvariable=self.user)
            e5.place(x=140,y=130)
            e6=Entry(win,textvariable=self.passcode)
            e6.place(x=140,y=170)
            # self.data3=self.name.get()
            # self.data4=self.phoneno.get()
            # self.data5=self.user.get()
            # self.data6=self.passcode.get()
            

            Checkbutton(win,bg="light green",text="All details filled!").place(x=80,y=200)
            
            def check():
                def phoneno():
                    return any(c.isalpha() for c in self.phoneno.get())
                if phoneno()==True:
                    messagebox.showerror("Registration","Invalid phone number!",parent=win)                   
                elif self.name.get()=="" or self.phoneno.get()=="" or self.user.get()=="" or self.passcode.get()=="":
                    messagebox.showerror("Registration","Please fill all the details!",parent=win)
                elif  len(self.phoneno.get())!=10:
                    messagebox.showerror("Registration","Invalid phone number!",parent=win)
                      
                else:
                    messagebox.showinfo("Registration","Registration complete! Please login Again!",parent=win)
                    win.destroy()
            def passcode():
                if len(self.passcode.get())>=5:
                    l,u,d,p=0,0,0,0
                    for ch in self.passcode.get():
                        if ch.isdigit():
                            d=d+1
                        if ch.isupper():
                            u=u+1
                        if ch.islower():
                            l=l+1
                        if (ch=='#' or ch=='@' or ch=='*'):
                            p=p+1
                    if (l>=1 and u>=1 and d>=1 and p>=1):
                        Label(win,text="Password available!",fg="blue",bg="light green").place(x=60,y=300)
                    else:
                        messagebox.showerror("Registration","Incorrect password!",parent=win)
                        win.destroy()
                else:
                    Label(win,text="Please enter a valid password!",bg="light green",fg="red").place(x=60,y=280)
                    win.destroy()
            
            t20=Label(win,bg="light green",fg="black",text="Password should contain atleast one Uppercase,\n one Lowercase, one digit and \n  any one of (#,@ or *)",font="helvetica 10 italic").place(x=370,y=60)
            Button(win,text="Check password",bg="light blue",relief=SUNKEN,bd=1,command=passcode,height=1).place(x=290,y=170)
            Button(win,text="Confirm registration",bg="light blue",relief=SUNKEN,bd=1,command=check).place(x=70,y=230)
        
        Button(f3,text="Login",bg="light green",command=login,relief=SUNKEN,bd=1).place(x=550,y=160)
        Button(f3,text="Register",bg="light green",command=register,relief=SUNKEN,bd=1).place(x=670,y=160)
       
        self.photo3=PhotoImage(file="Banking.png")
        
        L19=Label(self,image=self.photo3).place(x=490,y=250)
root=BOG()
root.mainloop()
        
        
 
 

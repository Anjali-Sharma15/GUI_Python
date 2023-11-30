import tkinter
import shutil
from tkinter import *
from tkcalendar import Calendar,DateEntry
from tkinter import messagebox,filedialog,Text

class signup(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x900")
        self.title("Signup Form")
        self.config(bg="light green")
        
        Label(self,text="Signup Form @ Job_Portal",font="times 18 bold",bg="light green").pack(pady=12)
        Label(self,text="Name",bg="light green",font="times 14 bold").place(x=80,y=90)
        self.var=StringVar()
        e1=Entry(self,textvariable=self.var)
        e1.place(x=210,y=90)    
        Label(self,text="Date of birth: ",font="times 14 bold",bg="light green").place(x=80,y=130)
        self.var10=StringVar()
        self.cal=DateEntry(self,selectmode="day",textvariable=self.var10)
        self.cal.place(x=210,y=130)     
        self.var5=IntVar()
        Label(self,text="Select gender",font="times 14 bold",bg="light green").place(x=80,y=190)
        Radiobutton(self,text="Male",bg="light green",font="times 12 bold",variable=self.var5,value=0).place(x=210,y=190)
        Radiobutton(self,text="Female",bg="light green",font="times 12 bold",variable=self.var5,value=1).place(x=270,y=190)
        self.var6=StringVar()
        self.var6.set("Select")
        l3=["Algeria","Australia","Brazil","Canada","Denmark","France","India","Nepal","Srilanka","Ukraine"]
        Label(self,text="Country",bg="light green",font="times 14 bold").place(x=80,y=230)
        OptionMenu(self,self.var6,*l3).place(x=210,y=230)
        Label(self,text="Address",bg="light green",font="times 14 bold").place(x=80,y=290)
        self.t6=Text(self,width=40,height=3)
        self.t6.place(x=210,y=290)
        Label(self,text="Resume",bg="light green",font="times 14 bold").place(x=80,y=370)
        def upload():
            win=Toplevel(self)         
            win.geometry("600x600")
            win.title("Upload resume")  
            win.config(bg="white")
            # f1=Frame(win)
            # f1.pack()
            self.t=Text(win,height=35,width=180,bg="white")
            self.t.pack()
            f=filedialog.askopenfilename(parent=win,filetypes=(("All files","*.*"),("Python files","*.txt")))
            self.f1=open(f,mode='r')
            mytext=self.f1.read()
            self.t.insert(1.0,mytext)
            self.f1.close()
    
            def save():
                self.mytext2=self.t.get(1.0,END)
                messagebox.showinfo("My Portfolio","Your Resume is saved! Kindly review before submitting.")
            b=Button(win,text="Save",command=save,bg="light pink",width=8,font="times 11 bold")
            b.pack()
            def edit():
                self.f1=open(f,mode='w')
                self.f1.write(self.t.get(1.0,END))
                self.f1.close()
            b=Button(win,text="Edit",command=edit,bg="light pink",width=8,font="times 11 bold")
            b.pack(pady=10)
            win.mainloop()       
        
        Button(self,text="Upload",command=upload,bd=2,width=8,relief=SUNKEN,bg="light pink",font="times 14 bold").place(x=210,y=370)
        def submit():
            messagebox.showinfo("My portfolio","Resume submitted!")
        def view():
            won=Toplevel(self)
            won.geometry("900x900")
            won.config(bg="light blue")
            Label(won,text="Candidate's Portfolio",font="times 18 bold",bg="light blue").pack(pady=10)
            Label(won,text="Name- "+self.var.get(),font="times 12 bold",bg="light blue").place(x=20,y=30)
            Label(won,text="Country- "+self.var6.get(),font="times 12 bold",bg="light blue").place(x=20,y=50)
            if self.var5.get()==0:
                Label(won,text="Gender- Male",font="times 12 bold",bg="light blue").place(x=20,y=70)
            elif self.var5.get()==1:
                Label(won,text="Gender- Female",font="times 12 bold",bg="light blue").place(x=20,y=70)
            Label(won,text="Date of birth- "+self.var10.get(),font="times 12 bold",bg="light blue").place(x=20,y=90)
            Label(won,text="Address- "+self.t6.get(1.0,END),font="times 12 bold",bg="light blue").place(x=20,y=110)
            f2=Frame(won)
            f2.place(x=20,y=150)
            t2=Text(f2,width=120,height=38,bg="light blue")
            t2.pack(side=LEFT,fill=BOTH)
            s2=Scrollbar(f2)
            s2.pack(side=RIGHT,fill=BOTH)
            t2.config(yscrollcommand=s2.set)
            s2.config(command=t2.yview)
            t2.insert(1.0,self.mytext2)
            won.mainloop()
        Button(self,text="Review",bg="light pink",command=view,bd=2,relief=SUNKEN,width=8,font="times 14 bold").place(x=310,y=370)     
        Button(self,text="Submit",bg="light pink",command=submit,bd=2,relief=SUNKEN,width=8,font="times 14 bold").place(x=410,y=370) 
        
root=signup()
root.mainloop()
import tkinter
from tkinter import messagebox, filedialog
from tkinter import *
from PIL import Image,ImageTk
import os
import time,datetime
import re
from tkinter import font

class notepad(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("860x900")
        self.title("Notepad")
        photo=ImageTk.PhotoImage(file="notepad_logo.png")
        self.iconphoto(False,photo)
        self.config(bg="white")
        f=Frame(self)  
        f.pack()
        s=Scrollbar(f)
        s.pack(side="right",fill=Y)        
        self.t=Text(f,height=600,width=700,wrap=WORD,undo=True,maxundo=-1)
        self.t.pack()
        s.config(command=self.t.yview)
        def new():
            self.t.delete(1.0,END)
            self.title("Untitled-Notepad")
        def openfile():
            self.t.delete(1.0,END)
            self.f=filedialog.askopenfilename(filetypes=(("Text file","*.txt"),("All files","*.*")))
            if self.f=="":
                self.f=None 
            else:
                f1=open(self.f,mode="r")
                s=self.f.split('/')
                self.s1=s[-1]
                self.title(self.s1)  
                self.mytext=f1.read() 
                self.t.insert(1.0,self.mytext)
                f1.close()   
            # f1=open(f,mode="w").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            # f1.close()
        def save():
            if self.title()=="Untitled-Notepad":
                self.f=filedialog.asksaveasfilename(filetypes=(("Text file","*.txt"),("All files","*.*")))
                self.title(self.f.split('/')[-1])
                f1=open(self.f,mode="w")
                f1.write(self.t.get(1.0,END))
                f1.close()
            else:
                f1=open(self.f,mode="w")
                f1.write(self.t.get(1.0,END))
                s=self.f.split('/')
                self.s1=s[-1]
                self.title(self.s1)  
                f1.close()   
        def exit():          
            
            m=messagebox.askyesno("Exit","Are you sure you want to exit? Kindly save your data before you exit!")
            if m==True:
                self.destroy()
        def Undo():
            self.t.edit_undo()
        def Redo():
            self.t.edit_redo()
        def Copy():
            self.t.clipboard_clear()
            self.t.clipboard_append(self.t.selection_get())
        def Cut():
            Copy()
            self.t.delete("sel.first","sel.last")           
      
        def Paste():
            # self.t.insert(INSERT,self.t.clipboard_get())
            self.t.event_generate(("<<Paste>>"))
        def Timecurrent():
            # self.t1.insert(1.0,self.t)
            s=time.strftime("%d-%m-%Y %H:%M:%S")
            self.t.insert(INSERT,s)       
        def Word_Wrap():
            self.t.selection_clear()
            self.t.tag_add("wrap","sel.first","sel.last")
            self.t.tag_config(wrap=WORD)
        def Bold():
            # self.t.selection_clear()        
            self.t.tag_add("to_bold","sel.first","sel.last")
            self.t.tag_config("to_bold",font="bold")
            
             
        def about():
            n=messagebox.showinfo("Notepad","First Notepad GUI made by Anjali!")
            
        
        
        menubar=tkinter.Menu(self)
        filemenu=tkinter.Menu(menubar,tearoff="off")
        editmenu=tkinter.Menu(menubar,tearoff="off")                                
        viewmenu=tkinter.Menu(menubar,tearoff="off")
        formatmenu=tkinter.Menu(menubar,tearoff="off")
        helpmenu=tkinter.Menu(menubar,tearoff="off")
        menubar.add_cascade(label="File",menu=filemenu)
        filemenu.add_command(label="New",command=new)
        filemenu.add_command(label="Open",command=openfile)
        filemenu.add_command(label="Save",command=save)
        filemenu.add_command(label="Exit",command=exit)
# edit menu-------
        menubar.add_cascade(label="Edit",menu=editmenu)
        editmenu.add_command(label="Undo",command=Undo)
        editmenu.add_command(label="Redo",command=Redo)
        editmenu.add_command(label="Paste",command=Paste)
        editmenu.add_command(label="Copy",command=Copy)
        editmenu.add_command(label="Cut",command=Cut)
        editmenu.add_command(label="Bold",command=Bold)
        editmenu.add_command(label="Time/Date",command=Timecurrent)
# format-----------
        menubar.add_cascade(label="Format",menu=formatmenu)

        formatmenu.add_command(label="Word Wrap",command=Word_Wrap)
        
        menubar.add_cascade(label="Help",menu=helpmenu)

        helpmenu.add_command(label="About",command=about)
        
        
        self.config(menu=menubar)
        # filemenu.add_command           
        
        
root=notepad()
root.mainloop()



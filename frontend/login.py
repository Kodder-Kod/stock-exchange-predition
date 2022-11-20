from home import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image, ImageDraw


import re
import time
from datetime import *

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title('Student Attendance')
        self.root.geometry('1200x600')
        self.root.config(bg='grey90')
        self.root.resizable(0, 0)

        def show(fram):
            return fram.tkraise(aboveThis=None)
        
        '''LOG IN PAGE'''  #######################################################################################################################
        self.frame0 = Frame(self.root)
        self.frame0.config(bg='#ffffff')
        self.frame0.place(x=0, y=0, width=1200, height=1000)

        self.frame1 = Frame(self.frame0)
        self.frame1.config(bg='slate blue')
        self.frame1.place(x=0, y=0, width=500, height=1000)

        self.frame2 = Frame(self.frame0)
        self.frame2.config(bg='#ffffff')
        self.frame2.place(x=400, y=0, width=600, height=1000)

        '''RIGHT SIDE'''  ##########################################################################################################

        Label(self.frame1, text="Create Account", bg='slate blue', fg='#ffffff', font=('Times', 20)).place(x=90, y=50)
        Label(self.frame1, text="And ", bg='slate blue', fg='#ffffff', font=('Times', 20)).place(x=150, y=80)
        Label(self.frame1, text=" Explore", bg='slate blue', fg='#ffffff', font=('Times', 20)).place(x=125, y=110)
        Label(self.frame1, text="E-AT APP", bg='slate blue', fg='#ffffff', font=('Times', 30)).place(x=90, y=140)

        Label(self.frame2, text='E-AT APP', font=('Times', 40), bg='#ffffff').place(x=250, y=30)
        Label(self.frame2, text='Sign In', font=('Times', 20), bg='#ffffff').place(x=330, y=140)

        # text in form
        Label(self.frame2, text='Email', font=23, bg='#ffffff').place(x=250, y=200)
        Label(self.frame2, text="Password", font=23, bg='#ffffff').place(x=250, y=280)

        # assign string  variable to tkinter
        nameValue1 = StringVar()
        passValue1 = StringVar()

        # Input
        nameEntry = Entry(self.frame2, textvariable=nameValue1, width=32, bd=0, font=20).place(x=250, y=225, height=30)
        Canvas(self.frame2, width=250, height=2.0, bg='#000000').place(x=250, y=250)
        passEntry = Entry(self.frame2, textvariable=passValue1, width=32, bd=0, font=20, show='*').place(x=250, y=305,
                                                                                                        height=30)
        Canvas(self.frame2, width=250, height=2.0, bg='#000000').place(x=250, y=330)

        # assign int variable to tkinter
        checkValue1 = IntVar()
        # checkbox
        checkbtn = Checkbutton(self.frame2, text='remember me ?', variable=checkValue1, cursor='hand2',
                               bg="#ffffff").place(x=250, y=350)  #
        # label in forgot
        Label(self.frame2, text='Forgot Password', font=('Times', 10, "underline"), fg='blue', bg='#ffffff',
              cursor='hand2').place(x=480, y=480)

        def submit():
            name1 = nameValue1.get()
            pas1 = passValue1.get()

            # connect to mysql
            if (name1 and pas1):


                    nyumba()

            else:
                messagebox.showerror("All Fields must be Filled", parent=root)

        # button of sign in
        def create2():
            return show(self.frame3)

        Button(self.frame2, text="Log In ", font=20, width=10, height=1, cursor='hand2', command=submit).place(x=330,
                                                                                                               y=400)
        Button(self.frame1, text="Create", font=20, width=10, height=1, cursor='hand2', command=create2).place(x=130,
                                                                                                               y=450)

        '''CREATE PAGE'''  ###########################################################################################################
        self.frame3 = Frame(self.root)
        self.frame3.config(bg='#ffffff')
        self.frame3.place(x=0, y=0, width=1200, height=1000)

        self.frame5 = Frame(self.frame3)
        self.frame5.config(bg='#ffffff')
        self.frame5.place(x=0, y=0, width=1000, height=1000)

        self.frame4 = Frame(self.frame3)
        self.frame4.config(bg='slate blue')
        self.frame4.place(x=750, y=0, width=1000, height=1000)

        Label(self.frame4, text="Already have An ", font=("Times", 25), bg='slate blue', fg='white').place(x=100, y=70)
        Label(self.frame4, text="Account", font=("Times", 25), bg='slate blue', fg='white').place(x=150, y=105)
        Label(self.frame4, text="Sign In", font=("Times", 30), bg='slate blue', fg='white').place(x=150, y=140)

        def login1():
            return show(self.frame0)

        Button(self.frame4, text="Sign In ", font=20, width=11, height=1, command=login1).place(x=170, y=450)

        Label(self.frame5, text="Create Account", font=("Times", 25), bg='white').place(x=250, y=30)

        Label(self.frame5, text='Name', font=23, bg='white').place(x=195, y=100)
        Label(self.frame5, text="Email", font=23, bg='white').place(x=195, y=170)
        Label(self.frame5, text="Phone ", font=23, bg='white').place(x=195, y=240)
        Label(self.frame5, text="Password ", font=23, bg='white').place(x=195, y=310)
        Label(self.frame5, text="Confirm Password", font=23, bg='white').place(x=195, y=380)

        nameValue = StringVar()
        emailValue = StringVar()
        phoneValue = StringVar()
        passValue = StringVar()
        conpassValue = StringVar()

        nameEntry = Entry(self.frame5, textvariable=nameValue, width=30, bd=0, font=20).place(x=200, y=125)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=200, y=145)

        emailEntry = Entry(self.frame5, textvariable=emailValue, width=30, bd=0, font=20).place(x=200, y=195)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=200, y=215)

        phoneEntry = Entry(self.frame5, textvariable=phoneValue, width=30, bd=0, font=20).place(x=200, y=265)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=200, y=285)

        passEntry = Entry(self.frame5, textvariable=passValue, width=30, bd=0, font=20, show='*').place(x=200, y=335)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=200, y=355)

        conpassEntry = Entry(self.frame5, textvariable=conpassValue, width=30, bd=0, font=20, show='*').place(x=200,
                                                                                                              y=405)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=200, y=425)

        def submit():
            name = nameValue.get()
            email = emailValue.get()
            phone = phoneValue.get()
            pas = passValue.get()
            con = conpassValue.get()

            mailform = re.findall('@', email)
            phoneform = re.findall('[^0-9]', phone)
            pasformsmall = re.findall('[a-z]', pas)
            d = pasformsmall
            passformbig = re.findall('[A-Z]', pas)
            e = passformbig
            passformnum = re.findall('[0-9]', pas)
            f = passformnum

            if (name and email and phone and pas):

                if pas != con:
                    return messagebox.showerror('password is not the same', parent=root)

                if phoneform:
                    return messagebox.showerror('only numbers', parent=root)

                if not mailform:
                    return messagebox.showerror('email formart', parent=root)

                if not f and not e or not d:
                    return messagebox.showerror('password formart', parent=root)



                    call()

                    conn.close()

            else:
                messagebox.showerror('All fields must be filled', parent=root)

        Button(self.frame5, text="register ", font=20, width=11, height=1, command=submit).place(x=270, y=450)
        self.call_fram(self.frame0)

    def call_fram(self,frame):
        return frame.tkraise(aboveThis=None)

def log():
    root=Tk()
    Login(root)
    root.mainloop()

if __name__ =="__main__":
    log()
from stocks import *
import os
from login import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.ttk import Treeview
import re
import mysql.connector as sa
import matplotlib.pyplot as plt
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Home:
    def __init__(self,root1,type,time,pop,kin):
        self.pop=pop
        pop=self.pop
        self.kin=kin
        kin=self.kin
        self.root=root1
        self.type=type
        types = self.type
        self.time=time
        time=self.time
        root=self.root
        root.geometry('1200x600')
        root.title('Stocks Prediction')
        root.config(bg='grey90')
        root.resizable(0, 0)

        def frame(show_f):
            return show_f.tkraise(aboveThis=None)

        '''LOG IN PAGE'''  #######################################################################################################################
        self.frame0 = Frame(self.root)
        self.frame0.config(bg='#ffffff')
        self.frame0.place(x=0, y=0, width=1200, height=1000)

        self.frame1 = Frame(self.frame0)
        self.frame1.config(bg='#ffffff')
        self.frame1.place(x=0, y=0, width=1000, height=1000)

        self.frame2 = Frame(self.frame0)
        self.frame2.config(bg='#ffffff')
        self.frame2.place(x=400, y=0, width=800, height=1000)

        '''RIGHT SIDE'''  ##########################################################################################################


        Label(self.frame1, text="Welcome ", bg='#ffffff', font=('Times', 40)).place(x=120, y=50)
        Label(self.frame1, text="to", bg='#ffffff', font=('Times', 20)).place(x=200, y=110)
        Label(self.frame1, text="Stock Trading Index", bg='#ffffff',  font=('Times', 30)).place(x=70, y=140)

        Label(self.frame2, text='Stock Trading Index', font=('Times', 40), bg='#ffffff').place(x=250, y=30)
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
                               bg="#ffffff").place(x=250, y=350)

        #create button

        Label(self.frame2, text='Don`t have an Account ??', font=('Times', 16), bg='#ffffff',
              cursor='hand2').place(x=150, y=500)


        # label in forgot
        Label(self.frame2, text='Forgot Password', font=('Times', 10, "underline"), fg='blue', bg='#ffffff',
              cursor='hand2').place(x=480, y=450)

        def submit():
            name1 = nameValue1.get()
            pas1 = passValue1.get()

            # connect to mysql
            if (name1 and pas1):
                conn = sa.connect(host='localhost', user='root', password='', database='stocks')
                cur = conn.cursor()  # assign cursor
                lol = "select email from admin where email =%s and Password=%s"
                cur.execute(lol, [(name1), (pas1)])
                result = cur.fetchall()

                if result:

                    self.show(self.dash)
                else:
                    messagebox.showerror('Username or Password  are invaild', parent=root)
                    conn.close()


            else:
                messagebox.showerror("All Fields must be Filled", parent=root)

        # button of sign in
        def create2():
            return frame(self.frame3)

        Button(self.frame2, text="Log In ", font=20, width=10, height=1, cursor='hand2', command=submit).place(x=330,
                                                                                                               y=400)
        Button(self.frame2, text="Create", font=20, width=10, height=1, cursor='hand2', command=create2).place(x=370,
                                                                                                               y=500)

        '''CREATE PAGE'''  ###########################################################################################################
        self.frame3 = Frame(self.root)
        self.frame3.config(bg='#ffffff')
        self.frame3.place(x=0, y=0, width=1200, height=1000)

        self.frame5 = Frame(self.frame3)
        self.frame5.config(bg='#ffffff')
        self.frame5.place(x=0, y=0, width=1000, height=1000)

        self.frame4 = Frame(self.frame3)
        self.frame4.config(bg='#ffffff')
        self.frame4.place(x=600, y=0, width=1000, height=1000)

        Label(self.frame4, text="Create an account  ", font=("Times", 30), bg='#ffffff').place(x=100, y=50)
        Label(self.frame4, text="and", font=("Times", 25), bg='#ffffff').place(x=220, y=105)
        Label(self.frame4, text="Start Trading ", font=("Times", 30),bg='#ffffff').place(x=150, y=150)

        def login1():
            return frame(self.frame0)

        Label(self.frame5, text="Already have an Account ??", font=("Times", 16), bg='white').place(x=80, y=520)

        Button(self.frame5, text="Sign In ", font=20, width=11, height=1, command=login1).place(x=330, y=520)

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


                try:
                    conn = sa.connect(host="localhost", user="root", password="", database="stocks")
                    cur = conn.cursor()  # assign cursor
                    sql = "CREATE TABLE IF NOT EXISTS admin( name varchar(100) not null,email  varchar(100) not null,phone int(11) not null,password  varchar(40) not null ) "
                    cur.execute(sql)  # execute the query
                    pin = "INSERT INTO  Admin (Name,Email,Phone,Password) Values(%s,%s,%s,%s)"
                    nip = ((name), (email), (phone), (pas))
                    print('lol')
                    cur.execute(pin, nip)
                    conn.commit()

                    self.show(self.dash)

                    conn.close()
                except:
                    print('Can not connect to the Database')





            else:
                messagebox.showerror('All fields must be filled', parent=root)

        Button(self.frame5, text="register ", font=20, width=11, height=1, command=submit).place(x=270, y=450)

        ##################################################################################################
        ##################################################################################################



        self.dash = Frame(root)
        self.dash.config(bg='#ffffff')
        self.dash.place(x=0, y=0, width=1200, height=1000)

        ''' DASHBOARD''' ###################################################################################################################################

        self.pop = Frame(self.dash)
        self.pop.config(bg='#ffae42')
        self.pop.place(x=0, y=0, height=1000, width=186)

        '''HOME PAGE''' ##############################################################################################################################################

        self.home = Frame(self.dash)
        self.home.config(bg='grey90')
        self.home.place(height=1000, width=1200, x=185, y=0)

        '''OVERALL UPPER DETAILS''' ##################################################################################################################################

        self.s=Frame(self.home)
        self.s.config( bg="#000000", cursor='hand2')
        self.s.place(x=10, y=30, height=100, width=180)
        Label(self.s, text='Google', font=('Times', 12,'italic'), bg='#ffffff').place(x=120, y=40)

        self.t=Frame(self.home)
        self.t.config( bg="#000000", cursor='hand2')
        self.t.place(x=200, y=30, height=100, width=180)
        Label(self.t, text='Safaricom', font=('Times', 12,'italic'), bg='#ffffff').place(x=100, y=40)


        self.u=Frame(self.home)
        self.u.config(bg="#000000", cursor='hand2')
        self.u.place(x=390, y=30, height=100, width=180)

        Label(self.u, text='Amazon', font=('Times', 12,'italic'), bg='#ffffff').place(x=120, y=40)

        self.c=Frame(self.home)
        self.c.config(bg="#000000", cursor='hand2')
        self.c.place(x=580, y=30, height=100, width=180)

        Label(self.c, text='Kengen', font=('Times', 12,'italic'), bg='#ffffff').place(x=120, y=40)

        self.z = Frame(self.home)
        self.z.config(bg="#000000", cursor='hand2')
        self.z.place(x=770, y=30, height=100, width=180)
        Label(self.z, text='Space X', font=('Times', 12, 'italic'), bg='#ffffff').place(x=120, y=40)

        ############################################################################
        ################################################################    #########
        ###############################################################
        self.stocks=Frame(self.home)
        self.stocks.config(bg="#ffffff", cursor='hand2')
        self.stocks.place(x=10, y=150, height=435, width=950)

        Label(self.stocks, text='Best Prediction in Performance ', font=('Times', 12), bg='#ffffff').place(x=400, y=8)
        Label(self.stocks, text='Worst Prediction in Performance ', font=('Times', 12), bg='#ffffff').place(x=400, y=225)

        self.stocks_line = Frame(self.stocks)
        self.stocks_line.config(bg="grey90", cursor='hand2')
        self.stocks_line.place(x=10, y=10, height=410, width=380)

        Label(self.stocks_line, text='Enter Time', font=('Times', 12), bg='grey90').place(x=10, y=20)

        clicked0=StringVar()

        OptionMenu(self.stocks_line,clicked0,*time).place(x=90,y=20)


        Label(self.stocks_line, text='The Stock Market', font=('Times', 15), bg='grey90').place(x=100, y=50)


###plotting



        fig =plt.figure(figsize=(4,4),dpi=80)
        plt.plot(pop, color='blue', label="Predicted Amazon stock price")
        plt.plot(kin, color="red", label="Real Amazon Price")
        plt.xlabel('time')
        plt.ylabel("stock Price")
        plt.legend()
        canvasbar =FigureCanvasTkAgg(fig, master = self.stocks_line)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(x=200,y=250, anchor=CENTER)









        self.stocks_best = Frame(self.stocks)
        self.stocks_best.config(bg="yellow", cursor='hand2')
        self.stocks_best.place(x=400, y=30, height=180, width=300)


        scroll_x = Scrollbar(self.stocks_best, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.stocks_best, orient=VERTICAL)

        self.ctable = Treeview(self.stocks_best, column=('name','increase'), xscrollcommand=scroll_x, yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.ctable.heading('name', text="Name")
        self.ctable.heading('increase', text="Increase")

        self.ctable['show'] = 'headings'
        self.ctable.column('name', width=100)
        self.ctable.column('increase', width=100)

        self.ctable.pack(fill=BOTH, expand=1)
        #self.ctable.bind("<Double-1>", cursor)

        self.stocks_bad = Frame(self.stocks)
        self.stocks_bad.config(bg="blue", cursor='hand2')
        self.stocks_bad.place(x=400, y=250, height=180, width=300)

        def cursor(e):
            c_row = self.ctable.focus()
            contents = self.ctable.item(c_row, 'values')


        scroll_x = Scrollbar(self.stocks_bad, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.stocks_bad, orient=VERTICAL)

        self.ctable = Treeview( self.stocks_bad, column=('name','decrease'), xscrollcommand=scroll_x, yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.ctable.heading('name', text="Name")
        self.ctable.heading('decrease', text="Decrease")

        self.ctable['show'] = 'headings'
        self.ctable.column('name', width=100)
        self.ctable.column('decrease', width=100)

        self.ctable.pack(fill=BOTH, expand=1)
        self.ctable.bind("<Double-1>", cursor)

        self.stocks_facts0 = Frame(self.stocks)
        self.stocks_facts0.config(bg="green", cursor='hand2')
        self.stocks_facts0.place(x=710, y=10, height=410, width=230)

        Label(self.stocks_facts0, text='Details', font=('Times', 12), bg='#ffffff').pack()



        #####################################################################################################
        ##############################################################################################3

        self.opp = Frame(self.dash)
        self.opp.config(bg="#ffffff", cursor='hand2')
        self.opp.place(height=1000, width=1200, x=185, y=0)

        Label(self.opp, text='Manage Your Stocks', font=('Times', 20), bg='#ffffff').place(x=350,y=10)

        search=StringVar()
        Label(self.opp, text='Name of Company ', font=('Times', 12), bg='#ffffff').place(x=25, y=80)
        Entry( self.opp, textvariable=search, font=('Times', 14), width=20, bd=0).place(x=40, y=100, height=30)
        Canvas(self.opp, width=180, height=2.0, bg='#000000').place(x=40, y=123)

        Button(self.opp, text='Search', bg='grey90', fg='Black', width=10, cursor='hand2').place(
            x=230, y=100)
        Button(self.opp, text='Show All', bg='grey90', fg='Black', width=10, cursor='hand2' ,command=self.read).place(
            x=350, y=100)

        Label(self.opp, text='Filter Types of Stock market ', font=('Times', 12), bg='#ffffff').place(x=500, y=75)

        choose=StringVar()
        OptionMenu(self.opp,choose,*types).place(x=560,y=100)

        self.stocks_opp = Frame(self.opp)
        self.stocks_opp.config(bg="grey90", cursor='hand2')
        self.stocks_opp.place(x=10, y=150, height=435, width=950)

        self.stocks_search = Frame(self.stocks_opp)
        self.stocks_search.config(bg="pink", cursor='hand2')
        self.stocks_search.place(x=10, y=10, height=300, width=450)


        scroll_x = Scrollbar(self.stocks_search, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.stocks_search, orient=VERTICAL)

        self.ctable = Treeview( self.stocks_search, column=('name','email'), xscrollcommand=scroll_x, yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.ctable.heading('name', text="Name")
        self.ctable.heading('email', text="Current Perfomance")

        self.ctable['show'] = 'headings'
        self.ctable.column('name', width=300)
        self.ctable.column('email',width=100)

        self.ctable.pack(fill=BOTH, expand=1)
        self.ctable.bind("<Double-1>", cursor)

        self.stocks_fact = Frame(self.stocks_opp)
        self.stocks_fact.config(bg="cyan", cursor='hand2')
        self.stocks_fact.place(x=480, y=10, height=300, width=450)


        Label(self.stocks_fact, text='Details', font=('Times', 12), bg='#ffffff').pack()

        def select_file():
            filetypes = (
                ('text files', '*.txt'),
                ('All files', '*.*')
            )

            filename = fd.askopenfilename(
                title='Open a file',
                initialdir='/',
                filetypes=filetypes)

            showinfo(
                title='Selected File',
                message=filename
            )



        Button(self.stocks_opp, text='Choose File', bg='blue', fg='white', width=10, cursor='hand2', command= select_file
              ).place(
            x=50, y=350)

        Label(self.stocks_opp,text="Type of File ",bg='grey90').place(x=190,y=350)



        clicked=StringVar()
        OptionMenu(self.stocks_opp,clicked,*types).place(x=260,y=350)

        Button(self.stocks_opp, text='Add File', bg='green', fg='white', width=20, cursor='hand2',
               ).place(
            x=120, y=400)


        Button(self.stocks_opp, text='Change Type of file', bg='Orange', fg='white', width=20, cursor='hand2').place(
            x=550, y=350)
        Button(self.stocks_opp, text='Delete', bg='red', fg='white', width=20, cursor='hand2').place(
            x=550, y=400)

        ####################################################################################################################################

        '''HELP PAGE'''  ###########################################################################################################################################

        self.help = Frame(self.dash)
        self.help.config(bg='grey90', cursor='hand2')
        self.help.place(height=1000, width=1200, x=185, y=0)

        Label(self.help, text='help page').place(x=10,y=20)



        '''SETTINGS PAGE'''  #####################################################################################################################################

        self.settings = Frame(self.dash)
        self.settings.config(bg='grey90', cursor='hand2')
        self.settings.place(height=1000, width=1200, x=185, y=0)

        '''OVERALL AVERAGE DETAILS'''  ##########################################################################################################################


        self.s=Frame(self.settings)
        self.s.config( bg="#000000", cursor='hand2')
        self.s.place(x=10, y=30, height=100, width=180)
        Label(self.s, text='Google', font=('Times', 12,'italic'), bg='#ffffff').place(x=120, y=40)

        self.t=Frame(self.settings)
        self.t.config( bg="#000000", cursor='hand2')
        self.t.place(x=200, y=30, height=100, width=180)
        Label(self.t, text='Safaricom', font=('Times', 12,'italic'), bg='#ffffff').place(x=10, y=40)


        self.u=Frame(self.settings)
        self.u.config(bg="#000000", cursor='hand2')
        self.u.place(x=390, y=30, height=100, width=180)

        Label(self.u, text='Amazon', font=('Times', 12,'italic'), bg='#ffffff').place(x=120, y=40)

        self.c=Frame(self.settings)
        self.c.config(bg="#000000", cursor='hand2')
        self.c.place(x=580, y=30, height=100, width=180)

        Label(self.c, text='Kengen', font=('Times', 12,'italic'), bg='#ffffff').place(x=120, y=40)

        self.z = Frame(self.settings)
        self.z.config(bg="#000000", cursor='hand2')
        self.z.place(x=770, y=30, height=100, width=180)
        Label(self.z, text='Space X', font=('Times', 12, 'italic'), bg='#ffffff').place(x=120, y=40)

        Label(self.settings, text='Change Your Profile',font=('Times',20),bg='grey90').place(x=200,y=250)

        Button(self.settings, text='Change Name',height=2,width=15,font=("times",12), command=lambda: frame(nameframe)).place(x=50, y=330)
        Button(self.settings, text='Change Email',height=2,width=15,font=("times",12), command=lambda: frame(emailframe)).place(x=50, y=410)
        Button(self.settings,text='Change Password',height=2,width=15,font=("times",12), command=lambda:frame(passwordframe)).place(x=50,y=480)

        ok=Frame(self.dash)
        ok.config(bg='grey90')
        ok.place (x=500,y=300,height=250,width=400)

        nameset = StringVar()
        emailset = StringVar()
        newpas = StringVar()
        conpas = StringVar()

        def setname():
            setname2()

        def setemail():
            setemail2()

        def setpass():
            setpass2()

        nameframe=Frame(self.dash)
        nameframe.config(bg='#ffffff')
        nameframe.place (x=500,y=300,height=250,width=400)

        Label(nameframe, text='Enter new Name', font=('Times', 12), bg='#ffffff').place(x=25, y=50)
        Entry( nameframe, textvariable=nameset, font=('Times', 14), width=20, bd=0).place(x=40, y=70, height=30)
        Canvas( nameframe, width=180, height=2.0, bg='#000000').place(x=40, y=93)
        Button(nameframe, text='Change', height=1, width=10, font=("times", 12),
               command=lambda: setname()).place(x=150, y=130)

        emailframe=Frame(self.dash)
        emailframe.config(bg='#ffffff')
        emailframe.place (x=500,y=300,height=250,width=400)

        Label(emailframe, text='Enter new Email', font=('Times', 12), bg='#ffffff').place(x=25, y=50)
        Entry( emailframe, textvariable=emailset, font=('Times', 14), width=20, bd=0).place(x=40, y=70, height=30)
        Canvas( emailframe, width=180, height=2.0, bg='#000000').place(x=40, y=93)
        Button(emailframe, text='Change', height=1, width=10, font=("times",12 ),
               command=lambda: setemail()).place(x=150, y=130)

        passwordframe=Frame(self.dash)
        passwordframe.config(bg='#ffffff')
        passwordframe.place (x=500,y=300,height=250,width=400)
        Button(passwordframe, text='Change', height=1, width=10, font=("times",12 ),
               command=lambda: setpass()).place(x=150, y=200)

        Label(passwordframe, text='Enter New Password', font=('Times', 12), bg='#ffffff').place(x=35, y=80)
        Entry( passwordframe, textvariable=newpas, font=('Times', 14), width=20, bd=0,show="*").place(x=40, y=100, height=30)
        Canvas( passwordframe, width=180, height=2.0, bg='#000000').place(x=40, y=123)

        Label(passwordframe, text='Confirm New Password', font=('Times', 12), bg='#ffffff').place(x=35, y=140)
        Entry( passwordframe, textvariable=conpas, font=('Times', 14), width=20, bd=0,show="*").place(x=40, y=160, height=30)
        Canvas( passwordframe, width=180, height=2.0, bg='#000000').place(x=40, y=183)

        '''SETTINGS EDIT FUNCTIONS '''###################################################################################################################################

        def setname2():
            name=nameset.get()
            if name:
                try:
                    conn = sa.connect(host='localhost', user='root', password='', database='stocks')
                    cur = conn.cursor()
                    das = "UPDATE admin SET name= %s WHERE phone='90'"
                    kumi = (name,)
                    cur.execute(das, kumi)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('New Name Set', parent=root)

                    frame(ok)
                except:
                    print('Database Error')

            else :
                messagebox.showerror('no blank name ', parent=root)

        def setemail2():
            email=emailset.get()
            if email:
                try:
                    conn = sa.connect(host='localhost', user='root', password='', database='stocks')
                    cur = conn.cursor()
                    das = "UPDATE admin SET email=%s WHERE phone ='90'"
                    kumi = (email,)
                    cur.execute(das, kumi)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('New Email Set', parent=root)

                    frame(ok)
                except:
                    print('Database error')

            else:
                messagebox.showerror('no blank name ', parent=root)

        def setpass2():

            new=newpas.get()
            con=conpas.get()

            if new and con:
                if new != con:
                    return messagebox.showerror('password is not the same', parent=root)

                try:
                    conn = sa.connect(host='localhost', user='root', password='', database='stocks')
                    cur = conn.cursor()
                    das = "UPDATE admin SET password=%s WHERE phone ='90'"
                    kumi = (new,)
                    cur.execute(das, kumi)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('New Password Set', parent=root)


                    frame(ok)

                except:
                    messagebox.showerror('no database connection ', parent=root)
            else:
                messagebox.showerror('no blank name ', parent=root)


        def call():
            return frame(self.dash)



        self.button()
        self.call()
        self.show(self.home)

    def call(self):
        return self.show(self.frame0)

    def show(self, frame):
        frame.tkraise(aboveThis=None)

    def button(self):
            Button(self.pop, activebackground='grey90', text='Dashboard', bg='#ffae42', fg='#000000', cursor='hand2',
                   bd=0,
                   font=('Times', 13), width=20, height=3, command=lambda: self.show(self.home)).place(x=0, y=200)
            Button(self.pop, activebackground='grey90', text='Manage', bg='#ffae42', fg='#000000', cursor='hand2',
                   bd=0,
                   font=('Times', 13), width=20, height=3, command=lambda: self.show(self.opp)).place(x=0, y=269)
            Button(self.pop, activebackground='grey90', text='Help', bg='#ffae42', fg='#000000', cursor='hand2',
                   bd=0,
                   font=('Times', 13), width=20, height=3, command=lambda: self.show(self.help)).place(x=0, y=337)
            Button(self.pop, activebackground='grey90', text='Settings', bg='#ffae42', fg='#000000', cursor='hand2',
                   bd=0, font=('Times', 13), width=20, height=3, command=lambda: self.show(self.settings)).place(x=0,
                                                                                                                 y=404)
            Button(self.pop, activebackground='grey90', text='Log Out', bg='#ffae42', fg='#000000', cursor='hand2',
                   bd=0,
                   font=('Times', 13), width=20, height=3, command=lambda: self.show(self.frame0)).place(x=0, y=470)

            load001h = Image.open("home.png")
            resize001h = load001h.resize((20, 20), Image.LANCZOS)
            render001h = ImageTk.PhotoImage(resize001h)
            img001h = Label(self.pop, image=render001h, bg='#ffae42')
            img001h.image = render001h
            img001h.place(x=30, y=220)

            load001m = Image.open("add-contact.png")
            resize001m = load001m.resize((30, 30), Image.LANCZOS)
            render001m = ImageTk.PhotoImage(resize001m)
            img001m = Label(self.pop, image=render001m, bg='#ffae42')
            img001m.image = render001m
            img001m.place(x=30, y=289)

            load001p = Image.open("help.png")
            resize001p = load001p.resize((20, 20), Image.LANCZOS)
            render001p = ImageTk.PhotoImage(resize001p)
            img001p = Label(self.pop, image=render001p, bg='#ffae42')
            img001p.image = render001p
            img001p.place(x=45, y=357)

            load001s = Image.open("settings-free-icon-font.png")
            resize001s = load001s.resize((20, 20), Image.LANCZOS)
            render001s = ImageTk.PhotoImage(resize001s)
            img001s = Label(self.pop, image=render001s, bg='#ffae42')
            img001s.image = render001s
            img001s.place(x=35, y=424)

            load001o = Image.open("exit.png")
            resize001o = load001o.resize((20, 20), Image.LANCZOS)
            render001o = ImageTk.PhotoImage(resize001o)
            img001o = Label(self.pop, image=render001o, bg='#ffae42')
            img001o.image = render001o
            img001o.place(x=30, y=490)

            load001h = Image.open("user (1).png")
            resize001h = load001h.resize((25, 25), Image.LANCZOS)
            render001h = ImageTk.PhotoImage(resize001h)
            img001h = Label(self.frame2, image=render001h, bg='#ffffff')
            img001h.image = render001h
            img001h.place(x=220, y=225)

            load001p = Image.open("unlock.png")
            resize001p = load001p.resize((25, 25), Image.LANCZOS)
            render001p = ImageTk.PhotoImage(resize001p)
            img001p = Label(self.frame2, image=render001p, bg='#ffffff')
            img001p.image = render001p
            img001p.place(x=220, y=305)

            load001p = Image.open("stock.png")
            resize001p = load001p.resize((230, 230), Image.LANCZOS)
            render001p = ImageTk.PhotoImage(resize001p)
            img001p = Label(self.frame1, image=render001p, bg='#ffffff')
            img001p.image = render001p
            img001p.place(x=80, y=220)

            load001h = Image.open("user (1).png")
            resize001h = load001h.resize((25, 25), Image.LANCZOS)
            render001h = ImageTk.PhotoImage(resize001h)
            img001h = Label(self.frame5, image=render001h, bg='#ffffff')
            img001h.image = render001h
            img001h.place(x=170, y=120)

            load001p = Image.open("email (1).png")
            resize001p = load001p.resize((25, 25), Image.LANCZOS)
            render001p = ImageTk.PhotoImage(resize001p)
            img001p = Label(self.frame5, image=render001p, bg='#ffffff')
            img001p.image = render001p
            img001p.place(x=170, y=190)

            load001p = Image.open("phone-call.png")
            resize001p = load001p.resize((25, 25), Image.LANCZOS)
            render001p = ImageTk.PhotoImage(resize001p)
            img001p = Label(self.frame5, image=render001p, bg='#ffffff')
            img001p.image = render001p
            img001p.place(x=170, y=260)

            load001p = Image.open("unlock.png")
            resize001p = load001p.resize((25, 25), Image.LANCZOS)
            render001p = ImageTk.PhotoImage(resize001p)
            img001p = Label(self.frame5, image=render001p, bg='#ffffff')
            img001p.image = render001p
            img001p.place(x=170, y=330)

            load001p = Image.open("door-key.png")
            resize001p = load001p.resize((25, 25), Image.LANCZOS)
            render001p = ImageTk.PhotoImage(resize001p)
            img001p = Label(self.frame5, image=render001p, bg='#ffffff')
            img001p.image = render001p
            img001p.place(x=170, y=400)

            load001p = Image.open("edit-tools.png")
            resize001p = load001p.resize((230, 230), Image.LANCZOS)
            render001p = ImageTk.PhotoImage(resize001p)
            img001p = Label(self.frame4, image=render001p, bg='#ffffff')
            img001p.image = render001p
            img001p.place(x=130, y=220)

    def read(self):
        table = self.ctable
        for i in os.listdir(r'C:\Users\D35KT0P\Desktop\stocks'):
            if len(i) != 0:
                table.insert("", 'end',values=(i))




def nyumba():
    root=Tk()
    type = ["Bonds", "Market Movers", "Future Commodities", "Currencies"]
    time=["1 week","2 weeks","1 month","3 months","6 months","1 yrs","2 yrs","3 yrs","4 yrs","5 yrs"]
    pop,kin = stocks()
    Home(root,type,time,pop,kin)
    root.mainloop()

if __name__=="__main__":
    plt.show()
    nyumba()
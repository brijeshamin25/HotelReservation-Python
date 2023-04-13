# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 15:47:42 2023

@author: brije
"""

import tkinter as win
from PIL import Image,ImageTk
import tkinter as ttk
from tkinter import messagebox 
import mysql.connector
import random
from time import strftime
from datetime import datetime
#from tkcalendar import Calendar,DateEntry 

myDatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "hotelsign"
    )

windows = win.Tk()


def mainClass():
    host = windows
    obj = LoginLogan(host)
    host.mainloop()
    
#----- LOGIN Page Class -----
class LoginLogan:
    def __init__(self,host):       
        self.host = host
        self.host.title("Login")
        self.host.geometry("1550x1000")
        
        #----- Background Image -----
        path = Image.open(r"C:\Users\brije\OneDrive\Desktop\MSC\SEM 4\CS625-151HY-Object Oriented Software\Project\Images\MainEnterance.jpeg")
        adj = path.resize((1550,900), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(adj)
        main1 = ttk.Label(self.host,image=self.img1)
        main1.place(x=0,y=0,relheight=1,relwidth=1)
        
        #----- Global Variable Declare -----
        global userName
        global password
        
        #----- Local Variable Declare indicate String Data Type -----
        userName = ttk.StringVar()
        password = ttk.StringVar()
        
        #----- Frame for the Login Credential -----
        frame = ttk.Frame(self.host,bg="#fff")
        frame.place(x=550,y=50,height=400,width=500)
        
        
        #----- Login Function -----
        def signin():
            if userName.get() == "" and password.get() == "":
                messagebox.showerror("Error","Fill both the fields",parent=self.host)
            else:
                myDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                poin = myDb.cursor()
                
                logSign = "SELECT * FROM signup WHERE userName = %s AND password = %s"
                logData = (userName.get(),password.get(),)
                
                poin.execute(logSign,logData)
                log = poin.fetchone()
                
                if log == None:
                    messagebox.showerror("Error","In-Valid User Name and Password",parent=self.host)
                else:
                    signWin = ttk.Toplevel()
                    signObj = LoganHotel(signWin)
                myDb.commit()
                myDb.close()
                
        def logClear():
            userName.set("")
            password.set("")
        
        
        #----- Signup Window Open Function -----
        def signupWin():
            signWin = ttk.Toplevel()
            signObj = SignupLogan(signWin)
                
        #----- Login Label -----
        logLbl = ttk.Label(frame,text="L O G I N",bg='#fff',fg='#7d7459',font=('Castellar',35,'bold'))
        logLbl.place(x=135,y=20,anchor='nw')
        
        #----- UserName Icon -----
        userIcon = Image.open(r"C:\Users\brije\OneDrive\Desktop\MSC\SEM 4\CS625-151HY-Object Oriented Software\Project\Images\person.png")
        userReset = userIcon.resize((25,25), Image.ANTIALIAS)
        self.use = ImageTk.PhotoImage(userReset)
        logoUser = ttk.Label(self.host,image=self.use,bg="#fff")
        logoUser.place(x=572,y=167,height=25,width=25)
        
        #----- User Name -----
        userLbl = ttk.Label(frame,text="User Name : ",bg='#fff',fg='#000',font=('Times',17,'bold'))
        userLbl.place(x=185,y=115,anchor='ne')
        
        #----- User Name Input -----
        self.userInp = ttk.Entry(frame,bg='#fff',fg='#7d7459',textvariable= userName,font=('Times',17),bd=2,relief='groove')
        self.userInp.place(x=187,y=115)
        
        #----- Hide Icone Function for Password -----
        def hide():
            showBtn = ttk.Button(self.host,image=showImg,command=show,bg="#fff",bd=0,activebackground="#fff")
            showBtn.place(x=980,y=225,height=25,width=25)
            self.pwdInp.config(show='*')
        
        #----- Show Icone Function for Password -----
        def show():
            hideBtn = ttk.Button(self.host,image=hideImg,command=hide,bg="#fff",bd=0,activebackground="#fff")
            hideBtn.place(x=980,y=225,height=25,width=25)
            self.pwdInp.config(show='')
        
        #----- Password Icon -----
        pwdIcon = Image.open(r"C:\Users\brije\OneDrive\Desktop\MSC\SEM 4\CS625-151HY-Object Oriented Software\Project\Images\password.png")
        pwdReset = pwdIcon.resize((25,25), Image.ANTIALIAS)
        self.pas = ImageTk.PhotoImage(pwdReset)
        logoPassword = ttk.Label(self.host,image=self.pas,bg="#fff")
        logoPassword.place(x=574,y=226,height=25,width=25)
        
        #----- Passwrod -----
        pwdLbl = ttk.Label(frame,text="Password : ",bg='#fff',fg='#000',font=('Times',17,'bold'))
        pwdLbl.place(x=180,y=170,anchor='ne')
        
        #----- Password Input -----
        self.pwdInp = ttk.Entry(frame,bg='#fff',fg='#7d7459',textvariable= password,show="*",font=('Times',17),bd=2,relief='groove')
        self.pwdInp.place(x=185,y=170)
        
        
        #----- Password Show Icon -----
        shwIcon = Image.open(r"C:\Users\brije\OneDrive\Desktop\MSC\SEM 4\CS625-151HY-Object Oriented Software\Project\Images\show.png")
        showReset = shwIcon.resize((25,25), Image.ANTIALIAS)
        showImg = ImageTk.PhotoImage(showReset)
        showBtn = ttk.Button(self.host,image=showImg,command=show,bg="#fff",bd=0,activebackground="#fff")
        showBtn.place(x=980,y=225,height=25,width=25)
        
        #----- Password Hide Icon -----
        hideIcon = Image.open(r"C:\Users\brije\OneDrive\Desktop\MSC\SEM 4\CS625-151HY-Object Oriented Software\Project\Images\hidden.png")
        hideReset = hideIcon.resize((25,25), Image.ANTIALIAS)
        hideImg = ImageTk.PhotoImage(hideReset)
        hideBtn = ttk.Button(self.host,image=hideImg,command=hide,bg="#fff",bd=0,activebackground="#fff")
        hideBtn.place(x=980,y=225,height=25,width=25)
        
        
        #----- SIGN In Button Hover using Event handeling -----
        def log_hover_in(Event):
            loginBtn['bg'] = "#7d7459"
            
        
        def log_hover_out(Event):
            loginBtn['bg'] = "#0b7697"


        #----- SIGN Out Button Hover using Event handeling -----            
        def reg_hover_in(Event):
            signBtn['bg'] = "#7d7459"
            
        
        def reg_hover_out(Event):
            signBtn['bg'] = "#0b7697"        
        
        
        #----- Sign in Button -----
        loginBtn = ttk.Button(frame,command = lambda:[signin(),logClear()],text="Sign in",font=('times',20,'bold'),bd=2,relief='raised',fg='#fff',bg="#0b7697",activeforeground='#fff',activebackground='#0b7697',cursor='hand2')
        loginBtn.place(x=252,y=252,height=45,width=100)
        
        #----- Sign Up -----
        signBtn = ttk.Button(frame,command = signupWin,text="Sign up",font=('times',20,'bold'),bd=2,relief='raised',fg='#fff',bg="#0b7697",activeforeground='#fff',activebackground='#0b7697',cursor='hand2')
        signBtn.place(x=122,y=252,height=45,width=100)
        
        #----- Using Bind to caputure the Event for Sign In -----
        loginBtn.bind("<Enter>",log_hover_in)
        loginBtn.bind("<Leave>",log_hover_out)

        #----- Using Bind to caputure the Event for Sign Out -----
        signBtn.bind("<Enter>",reg_hover_in)
        signBtn.bind("<Leave>",reg_hover_out)        
    
    
#----- SIGN UP Class -----    
class SignupLogan():
    
    def __init__(self,host):
        
        self.host = host
        self.host.title("Sign Up")
        self.host.geometry("1550x1000")
        
        #----- Golbal Variable -----
        global userName
        global firstName
        global lastName
        global gender
        global email
        global contact
        global country
        global password
        global comPassword
        
        #----- Global Variable DataType declare -----
        userName = ttk.StringVar()
        firstName = ttk.StringVar()
        lastName = ttk.StringVar()
        gender = ttk.StringVar()
        email = ttk.StringVar()
        contact = ttk.StringVar()
        country = ttk.StringVar()
        password = ttk.StringVar()
        comPassword = ttk.StringVar()   
        
        def clrData():
            userName.set("")
            firstName.set("")
            lastName.set("")
            gender.set("Male")
            email.set("")
            contact.set("")
            country.set("Select Country")
            password.set("")
            comPassword.set("")
        
        #----- Sign Up Validations -----
        def newRegister():
            
            if userName.get() == "":
                messagebox.showerror("Error","Fill the User Name Field",parent=self.host)
            
            elif firstName.get() == "":
                messagebox.showerror("Error","Fill the First Name Field",parent=self.host)
    
            elif lastName.get() == "":
                messagebox.showerror("Error","Fill the Last Name Field",parent=self.host)
            
            elif gender.get() == "":
                messagebox.showerror("Error","Please, Select gender",parent=self.host)
                
            elif email.get() == "":
                messagebox.showerror("Error","Fill the Email Field",parent=self.host)
                
            elif contact.get() == "" or len(contact.get()) != 10:
                messagebox.showerror("Error","Enter valid Contact",parent=self.host)
                
            elif country.get() == "" or country.get() == "Select Country":
                messagebox.showerror("Error","Please, Select Country",parent=self.host)
                
            elif password.get() == "":
                messagebox.showerror("Error","Fill the Password Field",parent=self.host)
                
            elif comPassword.get() == "":
                messagebox.showerror("Error","Fill the Confirm Password Field",parent=self.host)
            
            elif password.get() != comPassword.get():
                messagebox.showerror("Error","Enter Same Password in both Filed",parent=self.host)
            
            else:
                try:
                    myDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    poin = myDb.cursor()
            
                    data = "INSERT INTO signup (userName,firstName,lastName,gender,email,contact,country,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                    info = (userName.get(),firstName.get(),lastName.get(),gender.get(),email.get(),contact.get(),country.get(),password.get(),)
                    
                    poin.execute(data,info)
                    myDb.commit()
                    clrData()
                    messagebox.showinfo("Successful","Registration Successfully completed!",parent=self.host)
                        
                except Exception as e:
                       messagebox.showerror("Error",f"because of :{str(e)}",parent=self.host)
                        
                
        #----- Background Image -----
        bgImg = Image.open(r"C:\Users\brije\OneDrive\Desktop\MSC\SEM 4\CS625-151HY-Object Oriented Software\Project\Images\exterior.jpg")
        signSet = bgImg.resize((1550,900), Image.ANTIALIAS)
        self.signimg = ImageTk.PhotoImage(signSet)
        signMain = ttk.Label(self.host,image=self.signimg)
        signMain.place(x=0,y=0,relheight=1,relwidth=1)    
        
        
        #----- Frame for the Sign-UP Credential -----
        signFrame = ttk.Frame(self.host,bg="#000")
        signFrame.place(x=600,y=35,height=750,width=550)
        
        
        #----- Sign Up Label -----
        sgnLbl = ttk.Label(signFrame,text="SiGN-UP",bg='#000',fg='#7d7459',font=('Castellar',35,'bold'))
        sgnLbl.place(x=150,y=18,anchor='nw')
        
        
        #----- Horizental Tab Label -----
        hrLbl = ttk.Label(signFrame,bd=4,bg="#800000")
        hrLbl.place(x=0,y=85,width=550,height=1)
        
        
        #----- User Name -----
        userLbl = ttk.Label(signFrame,text="User Name : ",bg='#000',fg='#fff',font=('Times',17,'bold'))
        userLbl.grid(row=0,column=1,padx=100,pady=115,sticky="w")
        
        #----- User Name Input -----
        self.userSign = ttk.Entry(signFrame,textvariable=userName,bg='#000000',fg='#7d7459',font=('Times',17),bd=4,relief='groove')
        self.userSign.grid(row=0,column=1,padx=260,pady=115,sticky="w")
        
        
        #----- First Name -----
        fstName = ttk.Label(signFrame,text="First Name : ",bg='#000',fg='#fff',font=('Times',17,'bold'))
        fstName.place(x=100,y=190,anchor='w')
        
        #----- First Name Input -----
        self.fst = ttk.Entry(signFrame,textvariable=firstName,bg='#000000',fg='#7d7459',font=('Times',17),bd=4,relief='groove')
        self.fst.place(x=260,y=190,anchor='w')
        
        
        #----- Last Name -----
        lstName = ttk.Label(signFrame,text="Last Name : ",bg='#000',fg='#fff',font=('Times',17,'bold'))
        lstName.place(x=100,y=250,anchor='w')
        
        #----- Last Input -----
        self.lst = ttk.Entry(signFrame,textvariable=lastName,bg='#000000',fg='#7d7459',font=('Times',17),bd=4,relief='groove')
        self.lst.place(x=260,y=250,anchor='w')
        
        
        #----- Gender -----
        genderLbl = ttk.Label(signFrame,text="Gender : ",bg='#000',fg='#fff',font=('Times',17,'bold'))
        genderLbl.place(x=130,y=305,anchor='w')
        
        #----- Gender Frame -----
        gen = ttk.Frame(signFrame,bg='#fff')
        gen.place(x=260,y=305,anchor='w',width=230,height=35)
        
        #----- Male Gander Radio Button -----
        maleRb = ttk.Radiobutton(gen,variable=gender,value="Male",text="Male",font=('Times',17,'bold'),fg="#000",bg="#fff",activebackground="#fff",activeforeground="#000",cursor="hand1")
        maleRb.place(x=2,y=20,anchor='w')
        gender.set("Male")
        
        #----- Female Gander Radio Button -----
        maleRb = ttk.Radiobutton(gen,variable=gender,value="Female",text="Female",font=('Times',17,'bold'),fg="#000",bg="#fff",bd=0,activebackground="#fff",activeforeground="#000",cursor="hand1")
        maleRb.place(x=110,y=20,anchor='w')
        
        
        #----- Email -----
        emailLbl = ttk.Label(signFrame,text="Email : ",bg='#000',fg='#fff',font=('Times',17,'bold'))
        emailLbl.place(x=150,y=360,anchor='w')
        
        #----- Email Input -----
        self.eml = ttk.Entry(signFrame,textvariable=email,bg='#000000',fg='#7d7459',font=('Times',17),bd=4,relief='groove')
        self.eml.place(x=260,y=360,anchor='w')
        
    
        #----- Contact -----
        contactLbl = ttk.Label(signFrame,text="Contact : ",bg='#000',fg='#fff',font=('Times',17,'bold'))
        contactLbl.place(x=128,y=420,anchor='w')
        
        #----- Contact Input -----
        self.cnt = ttk.Entry(signFrame,textvariable=contact,bg='#000000',fg='#7d7459',font=('Times',17),bd=4,relief='groove')
        self.cnt.place(x=260,y=420,anchor='w')


        #----- Country -----
        countryLbl = ttk.Label(signFrame,text="Country : ",bg='#000',fg='#fff',font=('Times',17,'bold'))
        countryLbl.place(x=123,y=480,anchor='w')
        
        #----- Country Name Using List -----
        cntList = ['USA','India','Canada','UK','Mexico','Turkey','Africa','China']
        dropList = ttk.OptionMenu(signFrame,country,*cntList)
        dropList.config(width= 15,font=('Times',17),fg="#fff",bg="#000",bd=4,relief="groove",cursor="mouse")
        dropList.place(x=260,y=480,anchor='w')
        country.set('Select Country')
        
        
        #----- Password -----
        passwordLbl = ttk.Label(signFrame,text="Password : ",bg='#000',fg='#fff',font=('Times',17,'bold'))
        passwordLbl.place(x=110,y=545,anchor='w')
        
        #----- Password Input -----
        self.pwd = ttk.Entry(signFrame,textvariable=password,bg='#000000',fg='#7d7459',font=('Times',17),bd=4,relief='groove')
        self.pwd.place(x=260,y=545,anchor='w')        


        #----- Confirm Password -----
        cnfPwdLbl = ttk.Label(signFrame,text="Confirm Password : ",bg='#000',fg='#fff',font=('Times',17,'bold'))
        cnfPwdLbl.place(x=20,y=600,anchor='w')
        
        #----- Confirm Password Input -----
        self.cnfPwd = ttk.Entry(signFrame,textvariable=comPassword,bg='#000000',fg='#7d7459',font=('Times',17),bd=4,relief='groove')
        self.cnfPwd.place(x=260,y=600,anchor='w') 
        
        
        #----- SIGN In Button Hover using Event handeling -----
        def log_hover_in(Event):
            loginBack['bg'] = "#C0C0C0"
            
        
        def log_hover_out(Event):
            loginBack['bg'] = "#808080"


        #----- SIGN Out Button Hover using Event handeling -----            
        def reg_hover_in(Event):
            newReg['bg'] = "#C0C0C0"
            
        
        def reg_hover_out(Event):
            newReg['bg'] = "#808080"
 
        #----- LOGIN Window Open BACK Function -----
        def logWin():
            lgWin = ttk.Toplevel()
            lgObj = LoginLogan(lgWin)
        
        
        #----- New Regisration Button -----
        newReg = ttk.Button(signFrame,command= newRegister,text="Register",font=('times',20,'bold'),bd=2,relief='raised',fg='#fff',bg="#808080",activeforeground='#fff',activebackground='#808080',cursor='hand2')
        newReg.place(x=130,y=665,height=45,width=110)
        
        
        #----- Sign in Button -----
        loginBack = ttk.Button(signFrame,command= logWin,text="Login",font=('times',20,'bold'),bd=2,relief='raised',fg='#fff',bg="#808080",activeforeground='#fff',activebackground='#808080',cursor='hand2')
        loginBack.place(x=280,y=665,height=45,width=110)
        
        
        #----- Using Bind to caputure the Event for Sign In -----
        loginBack.bind("<Enter>",log_hover_in)
        loginBack.bind("<Leave>",log_hover_out)

        #----- Using Bind to caputure the Event for Sign Out -----
        newReg.bind("<Enter>",reg_hover_in)
        newReg.bind("<Leave>",reg_hover_out) 
        
        
#----- HOME PAGE Class -----
class LoganHotel:
    def __init__(self,host):
        self.host = host
        self.host.title("Luxury Philadelphia Hotel | The Logan")
        self.host.geometry("1550x1000")
    
        #---- Frame 1 on Main Window-----
        topFrame = ttk.Frame(self.host)
        topFrame.place(x=0,y=0,height=600,width=1550)
        
        #----- Home page Back grond Image 1 -----
        global resimg1
        loc = Image.open(r"C:\Users\brije\OneDrive\Desktop\MSC\SEM 4\CS625-151HY-Object Oriented Software\Project\Images\MainHall.jpg")
        bgimg = loc.resize((1550,500), Image.ANTIALIAS)
        resimg1 = ImageTk.PhotoImage(bgimg)
        bgmain = ttk.Label(topFrame,image=resimg1,padx=10)
        bgmain.place(x=0,y=0)
        
        #----- NavBar -----
        nav = win.Label(topFrame,text="The Logan Hotel",bg="black",fg="#fff",height=2,width=15,font=("times",25),cursor="heart")
        nav.place(x=2,y=10,width=1550,height=60)
        
        #----- Frame 2 for pictures and information on The Logan Hotel on Main Window -----
        bodyFrame = ttk.Frame(self.host)
        bodyFrame.place(x=0,y=510,height=500,width=1550)
        
        
        #----- Image 2 on the Frame 2 -----
        global bodyimg2
        loc2 = Image.open(r"C:\Users\brije\OneDrive\Desktop\MSC\SEM 4\CS625-151HY-Object Oriented Software\Project\Images\TheLogan_Carroll.jpg")
        bodysize = loc2.resize((800,400), Image.Resampling.LANCZOS)
        bodyimg2 = ImageTk.PhotoImage(bodysize)
        bodyImg = ttk.Label(bodyFrame,image=bodyimg2)
        bodyImg.place(x=0,y=0)
        
        #----- Heading for the Frame 2 Text ----- 
        heading = ttk.Label(bodyFrame,text="FEEL AT HOME",fg="#7d7459",height=2,width=15,font=("times",30))
        heading.place(x=1020,y=4)
        
        #----- Information on The Logan Hotel -----
        bdyTxt = ttk.Label(self.host,text="Step through our doors and instantly feel a sense of place. \n As Philadelphia’s favorite downtown hotel,\n The Logan offers guests a truly authentic experience in the heart of \n the city's vibrant cultural district. Feel at home in our collection of 391 guest \n rooms and suites, complete with generous thoughtful touches \n including locally curated, Philadelphia-inspired artwork. \n When you stay with us, everything you need is close at hand. \n Go on a culinary journey at our on-site bars and restaurants. \n Unwind and feel at ease at our Health Club and Spa. \n Play host in our selection of meeting and event venues. \n Whatever your needs may be, The Logan is always at the ready.",
                           fg="#000",height=15,width=72,font=("times",15),justify="center")
        bdyTxt.place(x=802,y=578)
        
        #----- Menu Configuration -----
        myMenu = ttk.Menu()
        self.host.config(menu=myMenu)
        
        #----- Open CUSTOMER INFORMATION Window -----
        def CustDet():
            custEnt = ttk.Toplevel()
            custObj = CustReg(custEnt)
            
        #----- Open BOOKING Window -----
        def RoomBook():
            custRes = ttk.Toplevel()
            roomObj = LoganRoom(custRes)
        
        def CloseMain():
            back = messagebox.askyesno("YesNo","Do you Want to Exit this Page?",parent=self.host)
            
            if back > 0:
                self.host.destroy()
                #logWin = ttk.Toplevel()
                #logObj = LoginLogan(logWin)
            else:
                if not back:
                    return
             
            
        #----- Dine Menu and it's Sub-Menu Creation -----
        bookingMenu = ttk.Menu(self.host, bg='white',fg="black",font=('times',15)) 
        myMenu.add_cascade(label="Reservation", menu = bookingMenu)
        bookingMenu.add_command(label="Customer Details", command = CustDet)
        bookingMenu.add_separator()
        bookingMenu.add_command(label="Booking", command=RoomBook)
        bookingMenu.add_separator()
        bookingMenu.add_command(label="Exit", command = CloseMain)

#----- SUB-MENU CUSTOMER INFORMATION of Reservation
class CustReg():
    def __init__(self,host):
        self.host=host
        self.host.title("Rresrvation")
        self.host.geometry("1550x1000")
        
        #----- Global Variable -----
        global custid
        global custfirst
        global custlast
        global custgen
        global custaddr
        global custemail
        global custphone
        global custproof
        global custproofnum
        global custnation
        
        #----- Declaring the Data Type of the Global Variable -----\
        custid = ttk.StringVar()
        custfirst = ttk.StringVar()
        custlast = ttk.StringVar()
        custgen = ttk.StringVar()
        custaddr = ttk.StringVar()
        custemail = ttk.StringVar()
        custphone = ttk.StringVar()
        custproof = ttk.StringVar()
        custproofnum = ttk.StringVar()
        custnation = ttk.StringVar()
        
        #----- Assigning the RANDOM Number for the Customer ID -----
        num = random.randint(1000, 9999) # 4 digit number
        custid.set(str(num))
        
        
        #----- Save Data Validations -----
        def saveData():
            if custfirst.get() == "":
                messagebox.showerror("Error","Fill the First Name Field",parent=self.host)
    
            elif custlast.get() == "":
                messagebox.showerror("Error","Fill the Last Name Field",parent=self.host)
            
            elif custgen.get() == "":
                messagebox.showerror("Error","Please, Select gender",parent=self.host)

            elif custaddr.get() == "":
                messagebox.showerror("Error","Fill the Address Field",parent=self.host)
                
            elif custemail.get() == "":
                messagebox.showerror("Error","Fill the Email Field",parent=self.host)
                
            elif custphone.get() == "" or len(custphone.get()) != 10:
                messagebox.showerror("Error","Enter valid Contact",parent=self.host)
                
            elif custproof.get() == "" or custproof.get() == "Select ID Proof":
                messagebox.showerror("Error","Please, Select ID Proof Type",parent=self.host)
            
            elif custproofnum.get() == "":
                messagebox.showerror("Error","Fill the ID Proof Number Field",parent=self.host)
                
            elif custnation.get() == "" or custnation.get() == "Select Country":
                messagebox.showerror("Error","Please, Select Country",parent=self.host)
            else:
                try:
                    mydata = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    mycur = mydata.cursor()
                    
                    user = "INSERT INTO customerinfo (custid,custfirst,custlast,custgen,custaddr,custemail,custphone,custproof,custproofnum,custnation) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    add = (custid.get(),custfirst.get(),custlast.get(),custgen.get(),custaddr.get(),custemail.get(),custphone.get(),custproof.get(),custproofnum.get(),custnation.get())
                
                    mycur.execute(user,add)
                    
                    mydata.commit()
                    messagebox.showinfo("Successful","Successfully Saved!",parent=self.host)
                except Exception as er:
                    messagebox.showerror("Error",f"because of :{str(er)}",parent=self.host)
                    
                    
        #----- Modify Customer Infomation Database Function -----
        def modeifyData():
            if custfirst.get() == "" or custemail == "" or custphone == "":
                messagebox.showerror("Error","Please Fill all the Form Details to Update the Data!",parent=self.host)
            else:
                mydata = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                mycur = mydata.cursor()
                  
                change = "UPDATE customerinfo set custfirst = %s,custlast = %s, custgen = %s, custaddr = %s, custemail = %s, custphone = %s, custproof = %s, custproofnum = %s, custnation = %s WHERE custid = %s" 
                modup = (custfirst.get(),custlast.get(),custgen.get(),custaddr.get(),custemail.get(),custphone.get(),custproof.get(),custproofnum.get(),custnation.get(),custid.get(),)            
                
                mycur.execute(change,modup)
                
                mydata.commit()
                messagebox.showinfo("Modify","Customer Information has been Updated!",parent=self.host)
        
        
        #----- Delete Customer Information Database Funcation -----    
        def delCust():
            if custfirst.get() == "" or custemail == "" or custphone == "":
                messagebox.showerror("Error","Please Fill all the Form Details to Delete the Data!",parent=self.host)
            else:
                que = messagebox.askyesno("YesNo","Are you sure do you want to DELETE the Record!",parent=self.host)
                if que > 0:
                    mydata = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    mycur = mydata.cursor()
            
                    custRemove = "DELETE from customerinfo WHERE custid = %s"
                    remVal = (custid.get(),)
            
                    mycur.execute(custRemove,remVal)
                    mydata.commit()
                    messagebox.showinfo("Successfully","Customer Information has been Deleted!",parent=self.host)            
                    saveRef()
                else:
                    return
        
        
        #----- Clear Customer Information Fields -----
        def saveRef():
            #custid.set("")
            custfirst.set("")
            custlast.set("")
            custgen.set("Male")
            custaddr.set("")
            custemail.set("")
            custphone.set("")
            custproof.set("Select ID Proof")
            custproofnum.set("")
            custnation.set("Select Country")
                        
        
        #---- Frame 1 on Customer Information Window-----
        custFrame = ttk.Frame(self.host,bg="#045F5F")
        custFrame.place(x=0,y=0,height=900,width=1550)
        
        #---- Frame 2 for Middle Main Frame on Customer Information Window-----
        innerFrame = ttk.Frame(self.host,bg="#A9A9A9")
        innerFrame.place(x=145,y=100,height=700,width=1220)
        
        #---- Frame 3 for LEFT Side of Frame 2 on Customer Information Window-----
        leftFrame = ttk.Frame(innerFrame,bd=2,relief="flat",bg="#A9A9A9")
        leftFrame.place(x=0,y=0,height=700,width=600)
        
        #----- Shadow Image on the Frame 3 Left Frame -----
        imgShad = ttk.Label(leftFrame,bg="#696969")
        imgShad.place(x=5,y=8,width=587,height=664)
        
        #----- Left Frame Background Image -----
        global custImg
        custLoc = Image.open(r"C:\Users\brije\OneDrive\Desktop\MSC\SEM 4\CS625-151HY-Object Oriented Software\Project\Images\theloganreg.jpg")
        custRe = custLoc.resize((580,666), Image.ANTIALIAS)
        custImg = ImageTk.PhotoImage(custRe)
        custBack = ttk.Label(leftFrame,image=custImg,bd=0)
        custBack.place(x=3,y=15)
        
        #----- Frame 4 for the Right side Customer Inforamtion -----
        rightFrame = ttk.Frame(innerFrame,bd=2,relief="flat",bg="#A9A9A9")
        rightFrame.place(x=600,y=0,height=700,width=655)
        
        #----- Customer Information Label -----
        cstFrmLbl = ttk.Label(rightFrame,text="Customer Information",bg='#A9A9A9',fg='#454545',font=('Castellar',30,'bold'))
        cstFrmLbl.place(x=0,y=5,anchor='nw')
        
        #----- Horizental Tab Label -----
        hrTab = ttk.Label(rightFrame,bd=4,bg="#800000")
        hrTab.place(x=100,y=60,width=400,height=1)
        
        
        #----- User ID Label -----
        cIdLbl = ttk.Label(rightFrame,text="User ID : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        cIdLbl.place(x=119,y=100,anchor='w')
        
        #----- User ID Input -----
        self.cstNm = ttk.Entry(rightFrame,textvariable=custid,bg='#C2C2C2',fg='#3D3D3D',font=('Times',17),bd=1,relief='sunken',state="disable",justify='center',cursor="arrow")
        self.cstNm.place(x=280,y=100,anchor='w',width=55)
        
        
        #----- First Name Label -----
        cstFstName = ttk.Label(rightFrame,text="First Name : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        cstFstName.place(x=55,y=150,anchor='w')
        
        #----- First Name Input -----
        self.cstF = ttk.Entry(rightFrame,textvariable=custfirst,bg='#C2C2C2',fg='#3D3D3D',font=('Times',17),bd=1,relief='sunken')
        self.cstF.place(x=280,y=150,anchor='w')
        

        #----- Last Name Label -----
        cstLstName = ttk.Label(rightFrame,text="Last Name : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        cstLstName.place(x=70,y=200,anchor='w')
        
        #----- Last Name Input -----
        self.cstL = ttk.Entry(rightFrame,textvariable=custlast,bg='#C2C2C2',fg='#3D3D3D',font=('Times',17),bd=1,relief='sunken')
        self.cstL.place(x=280,y=200,anchor='w')

        
        #----- Gender Label -----
        genLbl = ttk.Label(rightFrame,text="Gender : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        genLbl.place(x=111,y=250,anchor='w')
        
        #----- Gender Frame -----
        genFrame = ttk.Frame(rightFrame,bg='#A9A9A9')
        genFrame.place(x=280,y=250,anchor='w',width=280,height=35)
        
        #----- Male Gander Radio Button -----
        mGenRb = ttk.Radiobutton(genFrame,variable=custgen,value="Male",text="Male",bg='#A9A9A9',fg='#383838',font=('Bookman Old Style',17),activebackground="#A9A9A9",activeforeground="#383838",cursor="hand1")
        mGenRb.place(x=2,y=20,anchor='w')
        custgen.set("Male")
        
        #----- Female Gander Radio Button -----
        fGenRb = ttk.Radiobutton(genFrame,variable=custgen,value="Female",text="Female",bg='#A9A9A9',fg='#383838',font=('Bookman Old Style',17),bd=0,activebackground="#A9A9A9",activeforeground="#383838",cursor="hand1")
        fGenRb.place(x=120,y=20,anchor='w')
        
        
        #----- Address Label -----
        cstAddLbl = ttk.Label(rightFrame,text="Address : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        cstAddLbl.place(x=100,y=300,anchor='w')
        
        #----- Address Input -----
        self.cstAdd = ttk.Entry(rightFrame,textvariable=custaddr,bg='#C2C2C2',fg='#3D3D3D',font=('Times',17),bd=1,relief='sunken')
        self.cstAdd.place(x=280,y=300,anchor='w')    
        
        
        #----- Email Label -----
        cstEmlLbl = ttk.Label(rightFrame,text="Email : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        cstEmlLbl.place(x=150,y=350,anchor='w')
        
        #----- Email Input -----
        self.cstEml = ttk.Entry(rightFrame,textvariable=custemail,bg='#C2C2C2',fg='#3D3D3D',font=('Times',17),bd=1,relief='sunken')
        self.cstEml.place(x=280,y=350,anchor='w') 


        #----- Contact Label -----
        cstPhnLbl = ttk.Label(rightFrame,text="Contact : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        cstPhnLbl.place(x=100,y=400,anchor='w')
        
        #----- Contact Input -----
        self.cstPhn = ttk.Entry(rightFrame,textvariable=custphone,bg='#C2C2C2',fg='#3D3D3D',font=('Times',17),bd=1,relief='sunken')
        self.cstPhn.place(x=280,y=400,anchor='w') 
        
        
        #----- ID Proof Label -----
        idProofLbl = ttk.Label(rightFrame,text="ID Proof Type : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        idProofLbl.place(x=10,y=455,anchor='w')
        
        #----- ID Proff Type Display Using List -----
        idTypList = ['Driver License','State ID','Passport','Student ID']
        downList = ttk.OptionMenu(rightFrame,custproof,*idTypList)
        downList.config(width= 15,font=('Bookman Old Style',17),fg="#383838",bg="#A9A9A9",bd=0,relief="groove",cursor="mouse")
        downList.place(x=280,y=455,anchor='w',width=225)
        custproof.set('Select ID Proof')
        
        
        #----- ID Proof Number Label -----
        proofNumLbl = ttk.Label(rightFrame,text="ID Proof Num : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        proofNumLbl.place(x=16,y=505,anchor='w')
        
        #----- ID Proof Number Input -----
        self.proofNum = ttk.Entry(rightFrame,textvariable=custproofnum,bg='#C2C2C2',fg='#3D3D3D',font=('Times',17),bd=1,relief='sunken',justify="center")
        self.proofNum.place(x=280,y=505,anchor='w') 
        
        
        #----- Country Label -----
        cstConLbl = ttk.Label(rightFrame,text="Country : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        cstConLbl.place(x=90,y=555,anchor='w')
        
        #----- Country Name Using List -----
        cstConList = ['USA','India','Canada','UK','Mexico']
        conList = ttk.OptionMenu(rightFrame,custnation,*cstConList)
        conList.config(width= 15,font=('Bookman Old Style',17),fg="#383838",bg="#A9A9A9",bd=0,relief="groove",cursor="mouse")
        conList.place(x=280,y=555,anchor='w')
        custnation.set('Select Country')
        
        
        #----- DELETE Button Hover using Event handeling -----            
        def del_hover_in(Event):
            cstDelete['bg'] = "#C0C0C0"
            cstDelete['cursor'] = "cross"
            
        
        def del_hover_out(Event):
            cstDelete['bg'] = "#ADADD8"
            cstDelete['cursor'] = "cross"
            
            
        #----- MODIFY Out Button Hover using Event handeling -----            
        def mod_hover_in(Event):
            cstMod['bg'] = "#C0C0C0"
            cstMod['cursor'] = "exchange"
            
        
        def mod_hover_out(Event):
            cstMod['bg'] = "#ADADD8"
            cstMod['cursor'] = "exchange"
            
        
        #----- SAVE Button Hover using Event handeling -----
        def sav_hover_in(Event):
            cstSave['bg'] = "#C0C0C0"
            cstSave['cursor'] = "star"
            
        
        def sav_hover_out(Event):
            cstSave['bg'] = "#ADADD8"
            cstSave['cursor'] = "star"
            
        
        #----- SAVE Button Hover using Event handeling -----
        def cls_hover_in(Event):
            cstCls['bg'] = "#C0C0C0"
            cstCls['cursor']="circle"
            
        
        def cls_hover_out(Event):
            cstCls['bg'] = "#ADADD8"
            cstCls['cursor']="circle"

        #----- CLOSE Button Function to Return Back to Main -----    
        def closeCus(): 
            closeWin = messagebox.askyesno("YesNo","Do you want to close this window?",parent=self.host)
            if closeWin > 0:
                self.host.destroy()
                #backMain = ttk.Toplevel()
                #mainObj = LoganHotel(backMain)
            else:
                if not closeWin:
                    return
            
        
        #----- Customer Indormation DELETE Button -----
        cstDelete = ttk.Button(rightFrame,command=delCust,text="Delete",font=('Bookman Old Style',17,'bold'),bd=2,relief='raised',fg='#464682',bg="#ADADD8",activeforeground='#464682',activebackground='#ADADD8',cursor='hand2')
        cstDelete.place(x=50,y=605,height=45,width=110)
        
        
        #----- Customer Indormation MODIFY Button -----
        cstMod = ttk.Button(rightFrame,command=modeifyData,text="Modify",font=('Bookman Old Style',17,'bold'),bd=2,relief='raised',fg='#464682',bg="#ADADD8",activeforeground='#464682',activebackground='#ADADD8',cursor='hand2')
        cstMod.place(x=180,y=605,height=45,width=110)
        
        
        #----- Customer Information SAVE Button -----
        cstSave = ttk.Button(rightFrame,command=saveData,text="Save",font=('Bookman Old Style',17,'bold'),bd=2,relief='raised',fg='#464682',bg="#ADADD8",activeforeground='#464682',activebackground='#ADADD8',cursor='hand2')
        cstSave.place(x=310,y=605,height=45,width=110)

        #----- Customer Information CLOSE Button -----
        cstCls = ttk.Button(rightFrame,command=closeCus,text="Close",font=('Bookman Old Style',17,'bold'),bd=2,relief='raised',fg='#464682',bg="#ADADD8",activeforeground='#464682',activebackground='#ADADD8',cursor='hand2')
        cstCls.place(x=440,y=605,height=45,width=110) 
        
        
        #----- Using Bind to caputure the Event for DELETE Button -----
        cstDelete.bind("<Enter>",del_hover_in)
        cstDelete.bind("<Leave>",del_hover_out)

        #----- Using Bind to caputure the Event for MODIFY Button -----
        cstMod.bind("<Enter>",mod_hover_in)
        cstMod.bind("<Leave>",mod_hover_out) 
        
        #----- Using Bind to caputure the Event for SAVE Button -----
        cstSave.bind("<Enter>",sav_hover_in)
        cstSave.bind("<Leave>",sav_hover_out)
        
        #----- Using Bind to caputure the Event for CLOSE Button -----
        cstCls.bind("<Enter>",cls_hover_in)
        cstCls.bind("<Leave>",cls_hover_out)
        
        
#----- SUB-MENU BOOKING of Reservation
class LoganRoom():
    def __init__(self,host):
        self.host=host
        self.host.title("Room Booking")
        self.host.geometry("1550x1000")
        
        #----- Global Variable Declare -----
        global bookContact
        global bookRoom
        global bookCheckIn
        global bookCheckOut
        global bookGuest
        global bookMeal
        global bookNumDays
        global bookSubTT
        global bookTax
        global bookTotal
        
        #----- Meal Price -----
        breakfast = 20
        lunch = 150
        dinner = 250
        
        #----- Room Type Price -----
        single = 100 #Per Night
        double = 175 #Per Night
        king = 240 #Per Night
        
        #----- TAX -----
        roomTax = 12.0 / 100
        tax = 15.5 / 100
        
        
        #----- Declaring the Data Type of the Global Variable -----
        bookContact = ttk.StringVar()
        bookRoom = ttk.StringVar()
        bookCheckIn = ttk.StringVar()
        bookCheckOut = ttk.StringVar()
        bookGuest = ttk.StringVar()
        bookMeal = ttk.StringVar()
        bookNumDays = ttk.StringVar()
        bookSubTT = ttk.StringVar()
        bookTax = ttk.StringVar()
        bookTotal = ttk.StringVar()        
        
        
        #----- Retriving Data of the Customer Using CONTACT -----
        def RetData():
            if bookContact.get() == "" or len(bookContact.get()) != 10:
                messagebox.showerror("Error","Please Enter the Number!")
            else:
                #----- FIRST NAME DATA DISPLAY -----
                infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                cur = infoDb.cursor()
                
                retrive = "SELECT custfirst FROM customerinfo WHERE custphone = %s"
                retData = (bookContact.get(),)
                
                cur.execute(retrive,retData)
                store = cur.fetchone()
                
                if store == None:
                    messagebox.showerror("Error","Invalid Contact Number!, Please enter Valid Contact",parent=self.host)
                else:
                    infoDb.commit()
                    
                    firstName = ttk.Label(dispFrame,text="First Name:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    firstName.place(x=14,y=20)
                    
                    cstFirstName = ttk.Label(dispFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstFirstName.place(x=150,y=20)
                    
                    #------ CUSTOMER LAST NAME DATA DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT custlast FROM customerinfo WHERE custphone = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    lastName = ttk.Label(dispFrame,text="Last Name:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    lastName.place(x=17,y=60)
                    
                    cstLastName = ttk.Label(dispFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstLastName.place(x=150,y=60)
                    
                    
                    #----- CUSTOMER GENDER DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT custgen FROM customerinfo WHERE custphone = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    gend = ttk.Label(dispFrame,text="Gender:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    gend.place(x=17,y=100)
                    
                    cstGend = ttk.Label(dispFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstGend.place(x=150,y=100)
                    
                    
                    #----- CUSTOMER ADDRESS DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT custaddr FROM customerinfo WHERE custphone = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    address = ttk.Label(dispFrame,text="Address:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    address.place(x=17,y=140)
                    
                    cstAddress = ttk.Label(dispFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstAddress.place(x=148,y=140)
                    
                    
                    #----- CUSTOMER COUNTRY DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT custnation FROM customerinfo WHERE custphone = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    nation = ttk.Label(dispFrame,text="Country:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    nation.place(x=17,y=180)
                    
                    cstOrigin = ttk.Label(dispFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstOrigin.place(x=154,y=180)
                    
                    
                    #----- CUSTOMER EMAIL DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT custemail FROM customerinfo WHERE custphone = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    custEmail = ttk.Label(dispFrame,text="Email:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    custEmail.place(x=17,y=220)
                    
                    cstEmailId = ttk.Label(dispFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstEmailId.place(x=125,y=220)
                    
                    
        #----- Insert Room Booking Data -----        
        def RoomInsert():
            if bookContact.get() == "" or len(bookContact.get()) != 10:
                messagebox.showerror("Error","Fill the Contact Field",parent=self.host)
                
            elif bookRoom.get() == "" or bookRoom.get() == "Select Room":
                messagebox.showerror("Error","Select the Room Type Option",parent=self.host)
    
            elif bookCheckIn.get() == "":
                messagebox.showerror("Error","Fill the CHECK-IN Field",parent=self.host)
            
            elif bookCheckOut.get() == "":
                messagebox.showerror("Error","Fill the CHECK-OUT Field",parent=self.host)
            
            elif bookGuest.get() == "":
                messagebox.showerror("Error","Fill the Number of Guest Field",parent=self.host)

            elif bookMeal.get() == "" or bookMeal.get() == "Select Meal":
                messagebox.showerror("Error","Select the Meal Option",parent=self.host)
            else:
                try:
                    #----- Display Total Amount Function -----
                    checkIn = bookCheckIn.get()
                    checkOut = bookCheckOut.get()
                        
                    checkIn = datetime.strptime(checkIn,"%m/%d/%Y")
                    checkOut = datetime.strptime(checkOut,"%m/%d/%Y")
                    bookNumDays.set(abs(checkOut-checkIn).days)
                        
                        
                    if (bookMeal.get() == "BreakFast" and bookRoom.get() == "Single Bed"):
                        foodTyp = float(breakfast + single)
                        stay = float(bookNumDays.get())
                            
                        subTot = float(foodTyp * stay)
                        txCst  = float(tax + roomTax)
                        totCst = float(subTot + txCst)
                            
                        sub = "$ "+str("%.2f"%(subTot))
                        tx = "$ "+str("%.2f"%(txCst))
                        tot = "$ "+str("%.2f"%(totCst))
                            
                        bookSubTT.set(sub)
                        bookTax.set(tx)
                        bookTotal.set(tot)
                            
                    elif (bookMeal.get() == "Lunch" and bookRoom.get() == "Single Bed"):
                        foodTyp = float(lunch + single)
                        stay = float(bookNumDays.get())
                            
                        subTot = float(foodTyp * stay)
                        txCst  = float(tax + roomTax)
                        totCst = float(subTot + txCst)
                            
                        sub = "$ "+str("%.2f"%(subTot))
                        tx = "$ "+str("%.2f"%(txCst))
                        tot = "$ "+str("%.2f"%(totCst))
                            
                        bookSubTT.set(sub)
                        bookTax.set(tx)
                        bookTotal.set(tot)
                       
                    elif (bookMeal.get() == "Dinner" and bookRoom.get() == "Single Bed"):
                        foodTyp = float(dinner + single)
                        stay = float(bookNumDays.get())
                            
                        subTot = float(foodTyp * stay)
                        txCst  = float(tax + roomTax)
                        totCst = float(subTot + txCst)
                            
                        sub = "$ "+str("%.2f"%(subTot))
                        tx = "$ "+str("%.2f"%(txCst))
                        tot = "$ "+str("%.2f"%(totCst))
                            
                        bookSubTT.set(sub)
                        bookTax.set(tx)
                        bookTotal.set(tot)    
                            
                    elif (bookMeal.get() == "BreakFast" and bookRoom.get() == "Double Bed"):
                        foodTyp = float(breakfast + double)
                        stay = float(bookNumDays.get())
                            
                        subTot = float(foodTyp * stay)
                        txCst  = float(tax + roomTax)
                        totCst = float(subTot + txCst)
                            
                        sub = "$ "+str("%.2f"%(subTot))
                        tx = "$ "+str("%.2f"%(txCst))
                        tot = "$ "+str("%.2f"%(totCst))
                            
                        bookSubTT.set(sub)
                        bookTax.set(tx)
                        bookTotal.set(tot)
                            
                    elif (bookMeal.get() == "Lunch" and bookRoom.get() == "Double Bed"):
                        foodTyp = float(lunch + double)
                        stay = float(bookNumDays.get())
                            
                        subTot = float(foodTyp * stay)
                        txCst  = float(tax + roomTax)
                        totCst = float(subTot + txCst)
                            
                        sub = "$ "+str("%.2f"%(subTot))
                        tx = "$ "+str("%.2f"%(txCst))
                        tot = "$ "+str("%.2f"%(totCst))
                            
                        bookSubTT.set(sub)
                        bookTax.set(tx)
                        bookTotal.set(tot)
                            
                    elif (bookMeal.get() == "Dinner" and bookRoom.get() == "Double Bed"):
                        foodTyp = float(dinner + double)
                        stay = float(bookNumDays.get())
                            
                        subTot = float(foodTyp * stay)
                        txCst  = float(tax + roomTax)
                        totCst = float(subTot + txCst)
                            
                        sub = "$ "+str("%.2f"%(subTot))
                        tx = "$ "+str("%.2f"%(txCst))
                        tot = "$ "+str("%.2f"%(totCst))
                            
                        bookSubTT.set(sub)
                        bookTax.set(tx)
                        bookTotal.set(tot)
                            
                    elif (bookMeal.get() == "BreakFast" and bookRoom.get() == "King Bed"):
                        foodTyp = float(breakfast + king)
                        stay = float(bookNumDays.get())
                            
                        subTot = float(foodTyp * stay)
                        txCst  = float(tax + roomTax)
                        totCst = float(subTot + txCst)
                            
                        sub = "$ "+str("%.2f"%(subTot))
                        tx = "$ "+str("%.2f"%(txCst))
                        tot = "$ "+str("%.2f"%(totCst))
                            
                        bookSubTT.set(sub)
                        bookTax.set(tx)
                        bookTotal.set(tot)
                        
                    elif (bookMeal.get() == "Lunch" and bookRoom.get() == "King Bed"):
                        foodTyp = float(lunch + king)
                        stay = float(bookNumDays.get())
                            
                        subTot = float(foodTyp * stay)
                        txCst  = float(tax + roomTax)
                        totCst = float(subTot + txCst)
                            
                        sub = "$ "+str("%.2f"%(subTot))
                        tx = "$ "+str("%.2f"%(txCst))
                        tot = "$ "+str("%.2f"%(totCst))
                            
                        bookSubTT.set(sub)
                        bookTax.set(tx)
                        bookTotal.set(tot)
                        
                    elif (bookMeal.get() == "Dinner" and bookRoom.get() == "King Bed"):
                        foodTyp = float(dinner + king)
                        stay = float(bookNumDays.get())
                            
                        subTot = float(foodTyp * stay)
                        txCst  = float(tax + roomTax)
                        totCst = float(subTot + txCst)
                            
                        sub = "$ "+str("%.2f"%(subTot))
                        tx = "$ "+str("%.2f"%(txCst))
                        tot = "$ "+str("%.2f"%(totCst))
                        
                        bookSubTT.set(sub)
                        bookTax.set(tx)
                        bookTotal.set(tot)
                        
                    elif (bookMeal.get() == "None" and bookRoom.get() == "Single Bed"):
                        foodTyp = float(single)
                        stay = float(bookNumDays.get())
                            
                        subTot = float(foodTyp * stay)
                        txCst  = float(tax + roomTax)
                        totCst = float(subTot + txCst)
                            
                        sub = "$ "+str("%.2f"%(subTot))
                        tx = "$ "+str("%.2f"%(txCst))
                        tot = "$ "+str("%.2f"%(totCst))
                            
                        bookSubTT.set(sub)
                        bookTax.set(tx)
                        bookTotal.set(tot)
                        
                    elif (bookMeal.get() == "None" and bookRoom.get() == "Double Bed"):
                        foodTyp = float(double)
                        stay = float(bookNumDays.get())
                            
                        subTot = float(foodTyp * stay)
                        txCst  = float(tax + roomTax)
                        totCst = float(subTot + txCst)
                            
                        sub = "$ "+str("%.2f"%(subTot))
                        tx = "$ "+str("%.2f"%(txCst))
                        tot = "$ "+str("%.2f"%(totCst))
                            
                        bookSubTT.set(sub)
                        bookTax.set(tx)
                        bookTotal.set(tot)
                            
                    else:
                        foodTyp = float(king)
                        stay = float(bookNumDays.get())
                            
                        subTot = float(foodTyp * stay)
                        txCst  = float(tax + roomTax)
                        totCst = float(subTot + txCst)
                            
                        sub = "$ "+str("%.2f"%(subTot))
                        tx = "$ "+str("%.2f"%(txCst))
                        tot = "$ "+str("%.2f"%(totCst))
                            
                        bookSubTT.set(sub)
                        bookTax.set(tx)
                        bookTotal.set(tot)
                        
                    roomDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    roomCur = roomDb.cursor()
            
                    save = "INSERT INTO roombook (bookContact,bookRoom,bookCheckIn,bookCheckOut,bookGuest,bookMeal,bookNumDays,bookSubTT,bookTax,bookTotal) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    room = (bookContact.get(),bookRoom.get(),bookCheckIn.get(),bookCheckOut.get(),bookGuest.get(),bookMeal.get(),bookNumDays.get(),bookSubTT.get(),bookTax.get(),bookTotal.get(),)
                    
                    roomCur.execute(save,room)
                    #dispTotal()
                    roomDb.commit()
            
                    messagebox.showinfo("Successfully", "Room Successfully Registered!",parent=self.host)
                    
                except Exception as ex:
                    messagebox.showerror("Error",f"because of :{str(ex)}",parent=self.host)
                
        
        def bookCancel():
            if bookContact.get() == "" or bookGuest == "" or bookCheckOut == "":
                messagebox.showerror("Error","Please Fill all the Form Details to Cancle the Reservation!",parent=self.host)
            else:
                cl = messagebox.askyesno("YesNo","Are you sure! you want to cancle the Booking.",parent=self.host)
            
                if cl > 0:
                    roomDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    roomCur = roomDb.cursor()
            
                    bookCan = "DELETE from roombook where bookContact = %s"
                    custVal = (bookContact.get(),)
            
                    roomCur.execute(bookCan,custVal)
                    roomDb.commit()
                    messagebox.showinfo("Successfully","Your Information has been Deleted!",parent=self.host)            
                    clrBook()
                else:
                    if not cl:
                        return
        
        def clrBook():
            bookContact.set("")
            bookRoom.set("Select Room")
            bookCheckIn.set("")
            bookCheckOut.set("")
            bookGuest.set("1")
            bookMeal.set("Select Meal")
            bookNumDays.set("")
            bookSubTT.set("")
            bookTax.set("")
            bookTotal.set("")
            
            
        #---- Frame 1 for Booking Window-----
        roomBgFrame = ttk.Frame(self.host,bg="#045F5F")
        roomBgFrame.place(x=0,y=0,height=900,width=1550)
        
        #---- Frame 2 for Middle Main Frame for Booking Window-----
        midFrame = ttk.Frame(self.host,bg="#A9A9A9",)
        midFrame.place(x=135,y=80,height=750,width=1230)
        
        
        #---- Frame 3 Booking Window Image 1 -----
        roomFrame = ttk.Frame(midFrame,bg="#A9A9A9")
        roomFrame.place(x=10,y=15,height=320,width=380)
        
        #----- Left Frame First Background Image -----
        global roomImg
        hallLoc = Image.open(r"C:\Users\brije\OneDrive\Desktop\MSC\SEM 4\CS625-151HY-Object Oriented Software\Project\Images\LoganGuestroom.jpg")
        hallSet = hallLoc.resize((350,300), Image.ANTIALIAS)
        roomImg = ImageTk.PhotoImage(hallSet)
        hallMain = ttk.Label(roomFrame,image=roomImg,bd=0)
        hallMain.place(x=10,y=15)
        
        
        #----- Bottom Left Frame 9 for DISPLAY Receipt -----
        RecFrame = ttk.LabelFrame(midFrame,text="Receipt",bg="#A9A9A9",bd=2, relief="sunken",font=('Times',14))
        RecFrame.place(x=880,y=15,height=700,width=340)
        
        def Receipt():
            if bookContact.get() == "" or len(bookContact.get()) != 10:
                messagebox.showerror("Error","Please Enter the Number!",parent=self.host)
            else:
                #----- FIRST NAME DATA DISPLAY -----
                infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                cur = infoDb.cursor()
                
                retrive = "SELECT custid FROM customerinfo JOIN roombook ON customerinfo.custphone = roombook.bookContact WHERE bookContact = %s"
                retData = (bookContact.get(),)
                
                cur.execute(retrive,retData)
                store = cur.fetchone()
                
                if store == None:
                    messagebox.showerror("Error","Invalid Contact Number!, Please enter Valid Contact",parent=self.host)
                else:
                    infoDb.commit()
                    
                    cstIdLbl = ttk.Label(RecFrame,text="Customer ID :",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    cstIdLbl.place(x=14,y=15)
                    
                    cstIdDis = ttk.Label(RecFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstIdDis.place(x=150,y=15)
                    
                    
                    #----- First NAME RECEIPT DISPLAY -----
                    retrive = "SELECT custfirst FROM customerinfo JOIN roombook ON customerinfo.custphone = roombook.bookContact WHERE bookContact = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    firstName = ttk.Label(RecFrame,text="First Name:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    firstName.place(x=14,y=50)
                    
                    cstFirstName = ttk.Label(RecFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstFirstName.place(x=150,y=50)


                    #----- LAST NAME RECEIPT DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT custlast FROM customerinfo JOIN roombook ON customerinfo.custphone = roombook.bookContact WHERE bookContact = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    cstLastName = ttk.Label(RecFrame,text="Last Name:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    cstLastName.place(x=14,y=85)
                    
                    cstOrigin = ttk.Label(RecFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstOrigin.place(x=150,y=85)
                    
                    
                    #----- CUSTOMER GENDER RECEIPT DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT custgen FROM customerinfo JOIN roombook ON customerinfo.custphone = roombook.bookContact WHERE bookContact = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    cstLastName = ttk.Label(RecFrame,text="Gender:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    cstLastName.place(x=14,y=120)
                    
                    cstOrigin = ttk.Label(RecFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstOrigin.place(x=150,y=120)
                    
                    
                    #----- CUSTOMER EMAIL RECEIPT DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT custemail FROM customerinfo JOIN roombook ON customerinfo.custphone = roombook.bookContact WHERE bookContact = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    cstLastName = ttk.Label(RecFrame,text="EMAIL:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    cstLastName.place(x=14,y=155)
                    
                    cstOrigin = ttk.Label(RecFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstOrigin.place(x=140,y=155)
                    
                    
                    #----- CUSTOMER NATION RECEIPT DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT custnation FROM customerinfo JOIN roombook ON customerinfo.custphone = roombook.bookContact WHERE bookContact = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    cstLastName = ttk.Label(RecFrame,text="Country:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    cstLastName.place(x=14,y=190)
                    
                    cstOrigin = ttk.Label(RecFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstOrigin.place(x=145,y=190)
                 
                    
                    #----- CUSTOMER ROOM TYPE RECEIPT DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT bookRoom FROM customerinfo JOIN roombook ON customerinfo.custphone = roombook.bookContact WHERE bookContact = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    cstLastName = ttk.Label(RecFrame,text="Room Type:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    cstLastName.place(x=14,y=225)
                    
                    cstOrigin = ttk.Label(RecFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstOrigin.place(x=145,y=225)
                    
                    
                    #----- CUSTOMER ROOM CHECK-IN RECEIPT DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT bookCheckIn FROM customerinfo JOIN roombook ON customerinfo.custphone = roombook.bookContact WHERE bookContact = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    cstLastName = ttk.Label(RecFrame,text="Check-In:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    cstLastName.place(x=14,y=260)
                    
                    cstOrigin = ttk.Label(RecFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstOrigin.place(x=145,y=260)
                    
                    
                    #----- CUSTOMER ROOM CHECK-OUT RECEIPT DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT bookCheckOut FROM customerinfo JOIN roombook ON customerinfo.custphone = roombook.bookContact WHERE bookContact = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    cstLastName = ttk.Label(RecFrame,text="Check-Out:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    cstLastName.place(x=14,y=295)
                    
                    cstOrigin = ttk.Label(RecFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstOrigin.place(x=145,y=295)
                    
                    
                    #----- NUMBER OF CUSTOMER RECEIPT DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT bookGuest FROM customerinfo JOIN roombook ON customerinfo.custphone = roombook.bookContact WHERE bookContact = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    cstLastName = ttk.Label(RecFrame,text="Number of Guest:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    cstLastName.place(x=14,y=330)
                    
                    cstOrigin = ttk.Label(RecFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstOrigin.place(x=195,y=330)
                    
                    
                    #----- MEAL RECEIPT DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT bookMeal FROM customerinfo JOIN roombook ON customerinfo.custphone = roombook.bookContact WHERE bookContact = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    cstLastName = ttk.Label(RecFrame,text="Meal Selected:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    cstLastName.place(x=14,y=365)
                    
                    cstOrigin = ttk.Label(RecFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstOrigin.place(x=165,y=365)
                    
                    
                    #----- NUMBER OF STAY RECEIPT DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT bookNumDays FROM customerinfo JOIN roombook ON customerinfo.custphone = roombook.bookContact WHERE bookContact = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    cstLastName = ttk.Label(RecFrame,text="Number of Stay:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    cstLastName.place(x=14,y=400)
                    
                    cstOrigin = ttk.Label(RecFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstOrigin.place(x=190,y=400)
                    
                    
                    #----- SUB TOTAL RECEIPT DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT bookSubTT FROM customerinfo JOIN roombook ON customerinfo.custphone = roombook.bookContact WHERE bookContact = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    cstLastName = ttk.Label(RecFrame,text="SUB TOTAL:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    cstLastName.place(x=14,y=435)
                    
                    cstOrigin = ttk.Label(RecFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstOrigin.place(x=165,y=435)
                    
                    
                    #----- TAX RECEIPT DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT bookTax FROM customerinfo JOIN roombook ON customerinfo.custphone = roombook.bookContact WHERE bookContact = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    cstLastName = ttk.Label(RecFrame,text="TAX:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    cstLastName.place(x=14,y=470)
                    
                    cstOrigin = ttk.Label(RecFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstOrigin.place(x=165,y=470)
                    
                    
                    #----- TOTAL RECEIPT DISPLAY -----
                    infoDb = mysql.connector.connect(host = "localhost", user = "root", password = "1234",database = "hotelsign")
                    cur = infoDb.cursor()
                    
                    retrive = "SELECT bookTotal FROM customerinfo JOIN roombook ON customerinfo.custphone = roombook.bookContact WHERE bookContact = %s"
                    retData = (bookContact.get(),)
                    
                    cur.execute(retrive,retData)
                    store = cur.fetchone()
                    
                    cstLastName = ttk.Label(RecFrame,text="TOTAL:",bg='#A9A9A9',fg='#383838',font=('Times',17))
                    cstLastName.place(x=14,y=505)
                    
                    cstOrigin = ttk.Label(RecFrame,text=store,bg="#A9A9A9",fg='#3D3D3D',font=('Times',17))
                    cstOrigin.place(x=165,y=505)
                

        #----- Frame 5 for ROOM BOOKING -----
        rmBkFrame = ttk.Frame(self.host,bg="#045F5F",bd=0)
        rmBkFrame.place(x=550,y=5,height=70,width=390)
        
        #----- Room Booking Label -----
        bookLbl = ttk.Label(rmBkFrame,text="Room Booking",bg='#045F5F',fg='#7FFFD4',font=('Castellar',30,'bold'))
        bookLbl.place(x=0,y=5,anchor='nw')
        
        
        #----- Frame 6 for Boking Info. Center Frame for Booking Window -----
        roomInFrame = ttk.Frame(midFrame,bg="#A9A9A9")
        roomInFrame.place(x=390,y=15,height=360,width=490)
        
        
        #----- Contact Label -----
        rmContLbl = ttk.Label(roomInFrame,text="Contact : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        rmContLbl.place(x=4,y=19,anchor='w')
        
        #----- Contact Input -----
        self.cstPhn = ttk.Entry(roomInFrame,textvariable=bookContact,bg='#C2C2C2',fg='#3D3D3D',font=('Times',17),bd=1,relief='sunken',justify="center")
        self.cstPhn.place(x=170,y=19,anchor='w')
        
        
        #----- Customer Contact Display BUTTON -----
        fetCon = ttk.Button(roomInFrame,text="Show",command=RetData,font=('Bookman Old Style',17,'bold'),bd=2,relief='raised',fg='#464682',bg="#ADADD8",activeforeground='#464682',activebackground='#ADADD8',cursor='hand2')
        fetCon.place(x=408,y=8,height=25,width=64)
        
        
        #----- Room Type Label -----
        rmTypLbl = ttk.Label(roomInFrame,text="Room Type : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        rmTypLbl.place(x=1,y=70,anchor='w')
        
        #----- Room Type Using List -----
        rmTypeList = ['Single Bed','Double Bed','King Bed']
        rmList = ttk.OptionMenu(roomInFrame,bookRoom,*rmTypeList)
        rmList.config(width= 15,font=('Bookman Old Style',17),fg="#383838",bg="#A9A9A9",bd=0,relief="groove",cursor="mouse")
        rmList.place(x=210,y=70,anchor='w')
        bookRoom.set('Select Room')
        
        
        #----- Check-In-Date Label -----
        cidLbl = ttk.Label(roomInFrame,text="Check-In : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        cidLbl.place(x=30,y=120,anchor='w')
    
        #----- Check-In-Date Input -----
        self.chkIn = ttk.Entry(roomInFrame,textvariable=bookCheckIn,bg='#C2C2C2',fg='#3D3D3D',font=('Times',17),bd=1,relief='sunken',justify="center")
        self.chkIn.place(x=210,y=120,anchor='w')
        
        
        #----- Check-Out-Date Label -----
        codLbl = ttk.Label(roomInFrame,text="Check-Out : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        codLbl.place(x=0,y=170,anchor='w')   
        
        #----- Check-Out-Date Input -----
        self.chkOut = ttk.Entry(roomInFrame,textvariable=bookCheckOut,bg='#C2C2C2',fg='#3D3D3D',font=('Times',17),bd=1,relief='sunken',justify="center")
        self.chkOut.place(x=210,y=170,anchor='w')
        
        
        #----- Number of Guest Label -----
        guestLbl = ttk.Label(roomInFrame,text="No. of Guest : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        guestLbl.place(x=0,y=220,anchor='w')   
        
        
        #----- Number of Guest Input -----
        self.chkGuest = ttk.Entry(roomInFrame,textvariable=bookGuest,bg='#C2C2C2',fg='#3D3D3D',font=('Times',17),bd=1,relief='sunken',justify="center")
        self.chkGuest.place(x=250,y=220,anchor='w',width=40)
        bookGuest.set("1")
        
        
        #----- Meal Label -----
        mealLbl = ttk.Label(roomInFrame,text="Meal : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        mealLbl.place(x=97,y=270,anchor='w')   
        
        
        #----- Meal Option Using List -----
        mealList = ['None','BreakFast','Lunch','Dinner']
        mealList = ttk.OptionMenu(roomInFrame,bookMeal,*mealList)
        mealList.config(width= 15,font=('Bookman Old Style',17),fg="#383838",bg="#A9A9A9",bd=0,relief="groove",cursor="mouse")
        mealList.place(x=210,y=270,anchor='w')
        bookMeal.set('Select Meal')
        
        
        #----- DELETE Button Hover using Event handeling -----            
        def Can_hover_in(Event):
            roomCan['bg'] = "#C0C0C0"
            roomCan['cursor'] = "cross"
            
        
        def Can_hover_out(Event):
            roomCan['bg'] = "#ADADD8"
            roomCan['cursor'] = "cross"
        
        #----- SAVE Button Hover using Event handeling -----
        def Book_hover_in(Event):
            roomSave['bg'] = "#C0C0C0"
            roomSave['cursor'] = "star"
            
        
        def Book_hover_out(Event):
            roomSave['bg'] = "#ADADD8"
            roomSave['cursor'] = "star"
            
        
        #----- SAVE Button Hover using Event handeling -----
        def Off_hover_in(Event):
            roomCls['bg'] = "#C0C0C0"
            roomCls['cursor']="circle"
            
        
        def Off_hover_out(Event):
            roomCls['bg'] = "#ADADD8"
            roomCls['cursor']="circle"
        
        def closeBook():
            closeBook = messagebox.askyesno("YesNo","Do you want to close this window?",parent=self.host)
            if closeBook > 0:
                self.host.destroy()
            else:
                if not closeBook:
                    return
        
        #----- Room Booking SAVE Button -----
        roomSave = ttk.Button(roomInFrame,command=RoomInsert,text="Book",font=('Bookman Old Style',17,'bold'),bd=2,relief='raised',fg='#464682',bg="#ADADD8",activeforeground='#464682',activebackground='#ADADD8',cursor='hand2')
        roomSave.place(x=40,y=310,height=45,width=110)
        
        
        #----- Room Booking CANCLE Button -----
        roomCan = ttk.Button(roomInFrame,command=bookCancel,text="Cancelation",font=('Bookman Old Style',17,'bold'),bd=2,relief='raised',fg='#464682',bg="#ADADD8",activeforeground='#464682',activebackground='#ADADD8',cursor='hand2')
        roomCan.place(x=180,y=310,height=45,width=150)

        
        #----- Room Booking CLOSE Button -----
        roomCls = ttk.Button(roomInFrame,text="Close",command=closeBook,font=('Bookman Old Style',17,'bold'),bd=2,relief='raised',fg='#464682',bg="#ADADD8",activeforeground='#464682',activebackground='#ADADD8',cursor='hand2')
        roomCls.place(x=360,y=310,height=45,width=110) 
        
        
        #----- Using Bind to caputure the Event for SAVE Button -----
        roomSave.bind("<Enter>",Book_hover_in)
        roomSave.bind("<Leave>",Book_hover_out)
        
        #----- Using Bind to caputure the Event for DELETE Button -----
        roomCan.bind("<Enter>",Can_hover_in)
        roomCan.bind("<Leave>",Can_hover_out)
        
        #----- Using Bind to caputure the Event for CLOSE Button -----
        roomCls.bind("<Enter>",Off_hover_in)
        roomCls.bind("<Leave>",Off_hover_out)
                
        
        
        #----- Frame 7 for Display Customer Information by Contact Number on Right Frame of Booking Window -----
        dispFrame = ttk.LabelFrame(midFrame,text="Customer Information Display",bg="#A9A9A9",bd=2, relief="sunken",font=('Times',14))
        dispFrame.place(x=10,y=335,height=400,width=380)
        
        
        
        #----- Frame 8 for Booking Total; Bottom Left Frame of Booking Window -----
        totalFrame = ttk.Frame(midFrame,bg="#A9A9A9")
        totalFrame.place(x=420,y=400,height=340,width=430)        
        
        
        #----- DISPLAY Toatl Label -----
        displayLbl = ttk.Label(totalFrame,text="Total",bg='#A9A9A9',fg='#383838',font=('Castellar',24,'bold'))
        displayLbl.place(x=128,y=30,anchor='w') 
        

        #----- Number of Days Label -----
        nodLbl = ttk.Label(totalFrame,text="No. Stays : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        nodLbl.place(x=20,y=100,anchor='w')   
        
        #----- Number of Days Input -----
        self.nod = ttk.Entry(totalFrame,textvariable=bookNumDays,bg='#C2C2C2',fg='#3D3D3D',font=('Times',17),bd=1,relief='sunken',cursor="arrow",justify="center",state="disabled")
        self.nod.place(x=220,y=100,anchor='w',width=125)
        
        
        #----- SUB Total Label -----
        taxLbl = ttk.Label(totalFrame,text="Sub Total : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        taxLbl.place(x=10,y=150,anchor='w')   
        
        #----- SUB Total Input -----
        self.rmTax = ttk.Entry(totalFrame,textvariable=bookSubTT,bg='#C2C2C2',fg='#3D3D3D',font=('Times',17),bd=1,relief='sunken',cursor="arrow",justify="center",state="disabled")
        self.rmTax.place(x=220,y=150,anchor='w',width=125)
        
        
        #----- TAX Label -----
        subTtLbl = ttk.Label(totalFrame,text="Tax : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        subTtLbl.place(x=115,y=200,anchor='w')   
        
        #----- TAX Input -----
        self.rmSub = ttk.Entry(totalFrame,textvariable=bookTax ,bg='#C2C2C2',fg='#3D3D3D',font=('Times',17),bd=1,relief='sunken',cursor="arrow",justify="center",state="disabled")
        self.rmSub.place(x=220,y=200,anchor='w',width=125)
        
        
        #----- Total Label -----
        totLbl = ttk.Label(totalFrame,text="Total : ",bg='#A9A9A9',fg='#383838',font=('Engravers MT',17))
        totLbl.place(x=75,y=250,anchor='w')   
        
        #----- Total Input -----
        self.rmTot = ttk.Entry(totalFrame,textvariable=bookTotal,bg='#C2C2C2',fg='#3D3D3D',font=('Times',17),bd=1,relief='sunken',cursor="arrow",justify="center",state="disabled")
        self.rmTot.place(x=220,y=250,anchor='w',width=125)
        
        
        #----- Payment Note Label -----
        totLbl = ttk.Label(totalFrame,text="Pay At Desk*",bg='#A9A9A9',fg='#931314',font=('Engravers MT',12))
        totLbl.place(x=100,y=310,anchor='w')
        
        
        #----- Room Booking RECEIPT Button -----
        roomCls = ttk.Button(totalFrame,text="Receipt",command=Receipt,font=('Bookman Old Style',17,'bold'),bd=2,relief='raised',fg='#464682',bg="#ADADD8",activeforeground='#464682',activebackground='#ADADD8',cursor='hand2')
        roomCls.place(x=300,y=280,height=45,width=110)
            
        
if __name__ == "__main__":
    mainClass()
   

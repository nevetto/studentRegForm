# import calendar
# # Create a plain text calendar
# c = calendar.TextCalendar(calendar.THURSDAY)
# str = c.formatmonth(2025, 1, 0, 0)
# print(str)

# # Create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.THURSDAY)
# str = hc.formatmonth(2025, 1)
# print(str)
# # loop over the days of a month
# # zeroes indicate that the day of the week is in a next month or overlapping month
# for i in c.itermonthdays(2025, 4):
#     print(i)

#     # The calendar can give info based on local such a names of days and months (full and abbreviated forms)
#     for name in calendar.month_name:
#         print(name)
#     for day in calendar.day_name:
#         print(day)
#     # calculate days based on a rule: For instance an audit day on the second Monday of every month
#     # Figure out what days that would be for each month, we can use the script as shown here
#     for month in range(1, 13):
# 		# It retrieves a list of weeks that represent the month
#         mycal = calendar.monthcalendar(2025, month)
# 		# The first MONDAY has to be within the first two weeks
#         week1 = mycal[0]
#         week2 = mycal[1]
#         if week1[calendar.MONDAY] != 0:
#             auditday = week1[calendar.MONDAY]
#         else:
#         # if the first MONDAY isn't in the first week, it must be in the second week
#         	auditday = week2[calendar.MONDAY]
# print("%10s %2d" % (calendar.month_name[month], auditday))




import mysql.connector
mycon = mysql.connector.connect(host="localhost", user="root",password="",  database="studentRegistration_db")

  
# mycursor = mycon.cursor()
# mycursor.execute("CREATE TABLE studentsreg_info(id INT AUTO_INCREMENT PRIMARY KEY, First_Name VARCHAR(20), Last_Name VARCHAR(20), User_Name VARCHAR(11), Password VARCHAR(20), Address VARCHAR(50), Gender VARCHAR(10), Python VARCHAR(10), Java VARCHAR(10), Web VARCHAR(10), Csharp VARCHAR(10), State VARCHAR(10),  Age VARCHAR(10),  RegistrationNo VARCHAR(10))")

 
from tkinter import *
import tkinter.ttk as ttk
from tkinter.messagebox import *
import random

class RegistrationForm():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x800")
        self.root.iconbitmap("ball.ico")
        self.root.title('Registration Form')
        self.TitleFrame = Frame(self.root)
        self.TitleFrame.pack(side =TOP, fill = BOTH)
        self.TitleFrame.grid_propagate(0)

        self.mycon = mysql.connector.connect(host="localhost", user="root",password="",  database="studentRegistration_db")
        self.mycursor = self.mycon.cursor()     
        
        Label(self.TitleFrame, text= "Registration Form", bg='blue', font=('arial',15,"bold"), height=2).pack(side =TOP,  fill = BOTH)
        
        self.mainFrame = Frame(self.root)
        self.status = StringVar()
        self.mainFrame.pack(side =TOP, fill = BOTH)
         
        Label(self.mainFrame, text= "FirstName", font=('arial', 10, 'bold')).pack(side =TOP, fill = BOTH)
        self.firstname = Entry(self.mainFrame, width= 10,     justify="left", font=('arial',10,'bold'))
        self.firstname.pack(expand = YES, fill = BOTH)

        Label(self.mainFrame, text="LastName", font=('arial', 10, 'bold')).pack(side =TOP, fill = BOTH)
        self.lastname = Entry(self.mainFrame, width=10,     justify='left', font=('arial', 10, 'bold'))
        self.lastname.pack(expand = YES, fill = BOTH)

        Label(self.mainFrame, text="Age Range Selection", font=('arial', 10, 'bold')).pack(side =TOP, fill = BOTH)
        itemsforlistbox=['11-20','21-30', '31-40', '41-50', '51-60', '61-70', '71-80']
        self.mylistbox = Listbox(self.mainFrame, font=('times',10), selectmode='browse')
        for items in itemsforlistbox:
            self.mylistbox.insert(END,items)
        self.mylistbox.pack(expand = YES, fill = BOTH)
        self.mylistbox.bind("<<ListboxSelect>>", self.myselection)
        
        Label(self.mainFrame, text= "Username", font=('arial', 10, 'bold')).pack( side =TOP,fill = BOTH)
        self.username = Entry(self.mainFrame, width= 10,    justify="left", font=('arial',12,'bold'))
        self.username.pack(expand = YES, fill = BOTH)

        Label(self.mainFrame, text="Password", font=('arial', 10, 'bold')).pack(side =TOP, fill = BOTH)
        self.Password = Entry(self.mainFrame, show="*", width=10,     justify='left', font=('arial', 10, 'bold'))
        self.Password.pack(expand = YES, fill = BOTH)

        Label(self.mainFrame, text="Address", font=('arial', 10, 'bold')).pack(side =TOP, fill = BOTH)
        self.address = Entry(self.mainFrame,   width=10, justify='left', font=('arial', 10, 'bold'))
        self.address.pack(expand = YES, fill = BOTH)

        self.submainFrame = Frame(self.root)
        self.status = StringVar()
        self.submainFrame.pack(side =TOP, fill = BOTH)  

        item = ['Oyo', 'Ekiti', 'Ogun', 'Ondo', 'Benue', "Kano", 'Rivers', 'Enugu']
        self.cob = ttk.Combobox(self.submainFrame, values=(item), font=('arial', 10, 'bold'))
        self.cob.set('States')
        self.cob.grid(row=0, column=0)     
        
        Label(self.submainFrame, text= "Select Gender",justify='left', font=('arial', 12, 'bold')).grid(row=1, column=0, pady=5 )
        Radiobutton(self.submainFrame, variable= self.status, text = 'Female', value= 'female', tristatevalue= 0).grid(row=2, column=1 )
        Radiobutton(self.submainFrame, variable= self.status, text = 'Male', value= 'male', tristatevalue= 0).grid(row=2, column=3)
    
        Label(self.submainFrame, text="Choose your courses", font=('arial',12, 'bold')).grid(row=3, column=0, pady=5)
        self.python = BooleanVar()
        self.csharp = BooleanVar()
        self.web = BooleanVar()
        self.java = BooleanVar()
 
        Checkbutton(self.submainFrame, text="python", variable=self.python).grid(row=4, column=1)
        Checkbutton(self.submainFrame, text="C#", variable=self.csharp).grid(row=4, column=2)
        Checkbutton(self.submainFrame, text="web", variable=self.web).grid(row=4, column=3)
        Checkbutton(self.submainFrame, text="java", variable=self.java).grid(row=4, column=4)

        self.RegFrame = Frame(self.root)
        self.RegFrame.pack(side =TOP, fill = BOTH)

        self.regNo = StringVar()
        self.screenReg = Entry(self.RegFrame, textvariable=self.regNo, width=10, justify='left', font=('arial', 10, 'bold'))
        self.screenReg.pack(expand = YES, fill = BOTH)
        
        Button(self.submainFrame, width = 10, height=1, bg= 'blue' , font=('arial', 12),text= 'Register', command = self.register).grid(row=6, column=5, pady=10)            

        self.root.mainloop()
    
    def register(self):
        if self.python.get()==True:
            self.python = "Python"
        if self.java.get()==True:
            self.java = "Java"
        if self.web.get()==True:
            self.web = "Web"
        if self.csharp.get()==True:
            self.csharp = "C#"
        self.firstname = self.firstname.get()
        self.lastname = self.lastname.get()
        self.state = self.cob.get()
        self.userName = self.username.get()
        self.passwd = self.Password.get()
        self.address = self.address.get()
        self.gender = self.status.get()
        self.age = self.mylistbox.get(END)
        self.reg_no = "11"+str(random.randint(00000000, 90000))
        self.regNo.set('Your registration number is ' + self.reg_no)

        print(self.firstname,self.lastname, self.userName, self.passwd, self.address, self.gender, self.python, self.java, self.web, self.csharp, self.state, self.age, self.reg_no)
        myquery = """INSERT INTO studentsreg_info ( First_Name, Last_Name, User_Name, Password, Address, Gender, Python, Java, Web, Csharp, State,  Age, RegistrationNo)
        VALUE(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (self.firstname,self.lastname, self.userName, self.passwd, self.address, self.gender, str(self.python), str(self.java), str(self.web), str(self.csharp), self.state, self.age, self.reg_no)
        self.mycursor.execute(myquery, val)
        self.mycon.commit()        

    def myselection(self, event):
        showinfo("My selection", str(self.mylistbox.get(self.mylistbox.curselection(END))))

if __name__ == "__main__":
    fe = RegistrationForm()
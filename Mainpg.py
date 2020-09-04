import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
from connection import MyDb
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry


class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Student Management System")
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d-0+0" % (width, height))

        self.bg = ImageTk.PhotoImage(file="images/bg31.jpg")
        tk.Label(self, image=self.bg).grid()  # BACKGROUND

        self.headingLabel = Label(self, text="Student Management System", font=("comic sans ms", 30, "bold"),
                                  relief="raise", borderwidth=2, bg="#a391c1", height=2)
        self.headingLabel.place(x=0, y=0, relwidth=1)

        self.time = Label(self, font=("comic sans ms", 12), relief=GROOVE, fg="black", bg="#a391c1", height=3,
                          borderwidth=0)
        self.time.place(x=1380, y=15)
        self.timer()

        self.dgn1 = PhotoImage(file="images/dgn1.png")
        self.dgn_img = Label(self, image=self.dgn1, bg="#a391c1")
        self.dgn_img.place(x=400, y=13)

        self.dgn2 = PhotoImage(file="images/dgn1.png")
        self.dgn2_img = Label(self, image=self.dgn2, bg="#a391c1")
        self.dgn2_img.place(x=1050, y=13)

        self._frame = None
        self.switch_frame(Login)

    ############################################################################################################## TIME
    def timer(self):
        time_str = time.strftime("%H:%M:%S")
        date_str = time.strftime("%d/%m/%y")
        self.time.config(text="Date: " + date_str + "\n" "Time: " + time_str)
        self.time.after(200, self.timer)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()


####################################################################################################################################################### LOGIN
class Login(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)

        self.window = window
        self.login_frame = Frame(self.window, bg="#f9fafc", relief=GROOVE, borderwidth=0)
        self.login_frame.place(x=500, y=250, width=550, height=350)
        self.my_db = MyDb()
        ## ---------------------------- ICONS ---------------------------- ##
        self.user_icon = PhotoImage(file="images/user2.png")
        self.pass_icon = PhotoImage(file="images/pass2.png")
        self.login_icon = PhotoImage(file="images/login.png")

        ## ---------------------------- LOGIN LABELS AND ICONS ---------------------------- ##
        self.login_label = Label(self.login_frame, text="Login", fg="black", font=("Bell MT", 25, "bold"), bg="#f9fafc")
        self.login_label.place(x=280, y=15)

        self.login_img = Label(self.login_frame, image=self.login_icon, bg="#f9fafc")
        self.login_img.place(x=220, y=5)

        self.user_img = Label(self.login_frame, image=self.user_icon, bg="#f9fafc")
        self.user_img.place(x=100, y=110)

        self.pass_img = Label(self.login_frame, image=self.pass_icon, bg="#f9fafc")
        self.pass_img.place(x=95, y=190)

        self.user_label = Label(self.login_frame, text="Username", font=("comic sans ms", 14, "bold"), bg="#f9fafc")
        self.user_label.place(x=200, y=85)

        self.pass_label = Label(self.login_frame, text="Password", fg="black", font=("comic sans ms", 14, "bold"),
                                bg="#f9fafc")
        self.pass_label.place(x=200, y=167)

        ## ---------------------------- LOGIN ENTRYS ---------------------------- ##
        self.username = StringVar()
        self.password = StringVar()
        self.user_entry = Entry(self.login_frame, font=("Arial", 15), relief=GROOVE, textvariable=self.username)
        self.user_entry.place(x=200, y=126)

        self.pass_entry = Entry(self.login_frame, relief=GROOVE, font=("Arial", 15), textvariable=self.password)
        self.pass_entry.default_show_val = self.pass_entry["show"]
        self.pass_entry["show"] = "*"
        self.pass_entry.place(x=200, y=202)

        ## ---------------------------- HIDE PASSWORD ---------------------------- ##
        self.showpass_btn = Checkbutton(self.login_frame, text="Hide password", onvalue=True, offvalue=False,
                                        command=self.show_password, bg="#f9fafc")
        self.showpass_btn.var = tk.BooleanVar(value=True)
        self.showpass_btn.place(x=440, y=202)
        self.showpass_btn["variable"] = self.showpass_btn.var

        self.login_btn = Button(self.login_frame, text="Log In", command=self.login, cursor="hand2",
                                font=("Arial", 10, "bold"),
                                bd=1, padx=16)
        self.login_btn.place(x=275, y=260)
        self.register_btn = Button(self.login_frame, text="New user,Create Account", relief="flat", bg="#f9fafc",
                                   fg="dark blue",
                                   cursor="hand2", font=("Arial", 10, "bold", "underline", "italic"),
                                   command=self.register,
                                   bd=1, padx=16)
        self.register_btn.place(x=225, y=300)

    def show_password(self):
        if self.showpass_btn.var.get():
            self.pass_entry["show"] = "*"
        else:
            self.pass_entry["show"] = ""

    def login(self):
        qry = "SELECT username,password FROM users"
        all_user_pass = self.my_db.show_data(qry)
        data = []
        for i in all_user_pass:
            data.append(i[0] + "," + i[1])
        username = self.user_entry.get()
        password = self.pass_entry.get()
        if (username + "," + password) in data:
            messagebox.showinfo("Notification", "Login successful!")
            self.login_frame.destroy()
            self.window.switch_frame(Homepg)
        else:
            messagebox.showerror("Notification", "Username or password incorrect!")

    def register(self):
        self.login_frame.destroy()
        self.window.switch_frame(Registration)


##################################################################################################################################################### REGISTRATION
class Registration(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window
        self.register_frame = Frame(self.window, bg="#f9fafc")
        self.register_frame.place(x=450, y=150, width=600, height=600)
        self.my_db = MyDb()

        ## ---------------------------- ICONS ---------------------------- ##
        self.register_icon = PhotoImage(file="images/register.png")

        ## ---------------------------- LABELS---------------------------- ##
        self.register_label = Label(self.register_frame, text="Sign Up", bg="#f9fafc", fg="black",
                                    font=("Bell MT", 25, "bold"))
        self.register_label.place(x=240, y=15)

        self.register_img = Label(self.register_frame, bg="#f9fafc", image=self.register_icon)
        self.register_img.place(x=175, y=7)

        self.fname_label = Label(self.register_frame, text="First Name", bg="#f9fafc",
                                 font=("comic sans ms", 15))
        self.fname_label.place(x=50, y=117)

        self.lname_label = Label(self.register_frame, text="Last Name", bg="#f9fafc",
                                 font=("comic sans ms", 15))
        self.lname_label.place(x=335, y=117)

        self.username_label = Label(self.register_frame, text="Username", bg="#f9fafc",
                                    font=("comic sans ms", 15))
        self.username_label.place(x=50, y=200)

        self.mobile_no_label = Label(self.register_frame, text="Mobile No.", bg="#f9fafc",
                                     font=("comic sans ms", 15))
        self.mobile_no_label.place(x=335, y=200)

        self.pass_label = Label(self.register_frame, text="Password", bg="#f9fafc", font=("comic sans ms", 15))
        self.pass_label.place(x=50, y=280)

        self.cpass_label = Label(self.register_frame, text="Confirm Password", bg="#f9fafc",
                                 font=("comic sans ms", 15))
        self.cpass_label.place(x=50, y=350)

        self.email_label = Label(self.register_frame, text="Email", bg="#f9fafc",
                                 font=("comic sans ms", 15))
        self.email_label.place(x=335, y=350)

        self.gender_label = Label(self.register_frame, text="Gender: ", bg="#f9fafc",
                                  font=("comic sans ms", 15))
        self.gender_label.place(x=335, y=280)

        ## ---------------------------- ENTRY---------------------------- ##
        self.fname = StringVar()
        self.lname = StringVar()
        self.username = StringVar()
        self.mobile_no = StringVar()
        self.pass_var = StringVar()
        self.cpass_var = StringVar()
        self.email = StringVar()

        self.fname_entry = Entry(self.register_frame, font=("Arial", 15), relief=GROOVE, width=18,
                                 textvariable=self.fname)
        self.fname_entry.place(x=50, y=150)

        self.lname_entry = Entry(self.register_frame, font=("Arial", 15), relief=GROOVE, width=18,
                                 textvariable=self.lname)
        self.lname_entry.place(x=335, y=150)

        self.username_entry = Entry(self.register_frame, font=("Arial", 15), relief=GROOVE, width=18,
                                    textvariable=self.username)
        self.username_entry.place(x=50, y=235)

        self.mobile_no_entry = Entry(self.register_frame, font=("Arial", 15), relief=GROOVE, width=18,
                                     textvariable=self.mobile_no)
        self.mobile_no_entry.place(x=335, y=235)

        self.email_entry = Entry(self.register_frame, font=("Arial", 15), relief=GROOVE, width=15,
                                 textvariable=self.email)
        self.email_entry.place(x=335, y=385)

        self.pass_entry = Entry(self.register_frame, font=("Arial", 15), relief=GROOVE, width=15,
                                textvariable=self.pass_var)
        self.pass_entry.place(x=50, y=315)
        self.pass_entry.default_show_val = self.pass_entry["show"]
        self.pass_entry["show"] = "*"

        self.cpass_entry = Entry(self.register_frame, font=("Arial", 15), relief=GROOVE, width=15,
                                 textvariable=self.cpass_var)
        self.cpass_entry.place(x=50, y=385)
        self.cpass_entry.default_show_val = self.cpass_entry["show"]
        self.cpass_entry["show"] = "*"

        ## ---------------------------- Password show Button--------------------------- ##
        self.showpass_btn = Checkbutton(self.register_frame, text="Hide password", onvalue=True, offvalue=False,
                                        command=self.show_password, bg="#f9fafc")
        self.showpass_btn.var = tk.BooleanVar(value=True)
        self.showpass_btn.place(x=175, y=288)
        self.showpass_btn["variable"] = self.showpass_btn.var

        ## ---------------------------- Radio Button--------------------------- ##
        self.male = Label(self.register_frame, text="Male", bg="#f9fafc", font=("comic sans ms", 12))
        self.male.place(x=365, y=315)
        self.female = Label(self.register_frame, text="Female", bg="#f9fafc", font=("comic sans ms", 12))
        self.female.place(x=475, y=315)
        self.gender = StringVar()
        self.gender.set(0)
        self.radio_btn1 = Radiobutton(self.register_frame, value="Male", variable=self.gender, bg="#f9fafc")
        self.radio_btn1.place(x=335, y=318)
        self.radio_btn2 = Radiobutton(self.register_frame, value="Female", variable=self.gender, bg="#f9fafc")
        self.radio_btn2.place(x=450, y=318)

        ## ---------------------------- SUBMIT and RESET Button--------------------------- ##
        self.signup_btn = Button(self.register_frame, text="Create New Account!", command=self.createnew,
                                 cursor="hand2",
                                 font=("Arial", 10, "bold"),
                                 bd=1, padx=16)
        self.signup_btn.place(x=200, y=485)
        self.cancel_btn = Button(self.register_frame, text="Cancel", relief="flat", bg="#f9fafc",
                                 cursor="hand2", font=("Arial", 10, "bold", "underline"),
                                 command=self.cancel,
                                 bd=1, padx=16)
        self.cancel_btn.place(x=245, y=515)

    def createnew(self):
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        username = self.username_entry.get()
        mobile_no = self.mobile_no_entry.get()
        pass_var = self.pass_entry.get()
        cpass_var = self.cpass_entry.get()
        email = self.email_entry.get()
        gender = self.gender.get()

        if (fname == "") or (lname == "") or (username == "") or (mobile_no == "") or (pass_var == "") or (
                cpass_var == "") or (email == "") or (gender == ""):
            messagebox.showerror("Notification", "Please Fill all the fields!")
        else:
            if pass_var == cpass_var:
                try:
                    qry = "INSERT INTO users (first_name, last_name, username, mobile_no,password,email,gender) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    values = (fname, lname, username, mobile_no, pass_var, email, gender)
                    self.my_db.aur(qry, values)
                    messagebox.showinfo("Notification", "Username {} Added Successfully..".format(username))
                    self.register_frame.destroy()
                    self.window.switch_frame(Login)

                except:
                    messagebox.showerror("Notification", "Username already taken!")

            else:
                messagebox.showerror("Notification", "Your passwords doesnot match! Try again!")

    def show_password(self):
        if self.showpass_btn.var.get():
            self.pass_entry["show"] = "*"
            self.cpass_entry["show"] = "*"
        else:
            self.pass_entry["show"] = ""
            self.cpass_entry["show"] = ""

    def cancel(self):
        self.register_frame.destroy()
        self.window.switch_frame(Login)


####################################################################################################################################################### HOME PAGE
class Homepg(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)

        self.window = window
        self.home_frame = Frame(self.window, bg="#f0f0f0", relief=GROOVE, borderwidth=0)
        self.home_frame.place(x=270, y=142, width=1000, height=650)

        ## ---------------------------- IMAGES AND ICONS ---------------------------- ##
        self.login_sucess_icon = PhotoImage(file="images/loginsucc.png")
        self.college_logo = PhotoImage(file="images/schoollogo.png")

        # ------------------------Button IMG --------------------#
        self.add_student_icon = PhotoImage(file="images/studentadd.png")
        self.update_student_icon = PhotoImage(file="images/editcourse.png")
        self.info_student_icon = PhotoImage(file="images/studentinfo.png")
        self.refund_icon = PhotoImage(file="images/refund.png")
        self.fee_history_icon = PhotoImage(file="images/feehistory.png")
        self.add_course_icon = PhotoImage(file="images/course.png")
        self.pay_fee_icon = PhotoImage(file="images/fee1.png")

        ## ---------------------------- LOGGED IN AS ---------------------------- ##
        self.back_label = Label(self.home_frame, bg="#f9fafc", relief="groove", width=24, height=9)
        self.back_label.place(x=825, y=0)

        self.login_as = Label(self.home_frame, text="Logged in as, ", bg="#f9fafc", fg="black",
                              font=("comic sans ms", 12))
        self.login_as.place(x=850, y=5)

        self.login_as_img = Label(self.home_frame, bg="#f9fafc", image=self.login_sucess_icon)
        self.login_as_img.place(x=880, y=40)

        self.login_as_user = Label(self.home_frame, text="admin", bg="#f9fafc", fg="black",
                                   font=("comic sans ms", 12))
        self.login_as_user.place(x=886, y=100)

        ## ---------------------------- COLLEGE LOGO DESIGN ---------------------------- ##
        self.college_logo_img = Label(self.home_frame, image=self.college_logo, bg="#f0f0f0")
        self.college_logo_img.place(x=710, y=170)

        self.found_in = Label(self.home_frame, text="Found in 1209 \n England, UK", font=("Bell MT", 16, "bold"),
                              bg="#f0f0f0")
        self.found_in.place(x=795, y=435)

        ## ---------------------------- Sign Out BTN ---------------------------- ##
        self.sign_out_btn = Button(self.home_frame, text="Sign Out", command=self.sign_out, cursor="hand2",
                                   font=("Arial", 10, "bold"))
        self.sign_out_btn.place(x=830, y=580)

        ## ---------------------------- OPTIONS TABLE  ---------------------------- ##
        self.dgn_label = Label(self.home_frame, bg="#f9fafc", relief="sunken", width=100, height=40)
        self.dgn_label.place(x=20, y=30)

        ## ---------------------------- Design Buttons  ---------------------------- ##
        # ---------------------Manage Students
        self.add_student_btn = Button(self.home_frame, image=self.add_student_icon, relief="flat", cursor="hand2",
                                      command=self.add_student)
        self.add_student_btn.place(x=120, y=80)

        self.edit_student_btn = Button(self.home_frame, image=self.update_student_icon, relief="flat", cursor="hand2",
                                       command=self.edit_student)
        self.edit_student_btn.place(x=340, y=80)

        self.student_detail_btn = Button(self.home_frame, image=self.info_student_icon, relief="flat", cursor="hand2",
                                         command=self.student_details)
        self.student_detail_btn.place(x=560, y=80)

        # ---------------------Manage Courses
        self.add_course_btn = Button(self.home_frame, image=self.add_course_icon, relief="flat", cursor="hand2",
                                     command=self.add_course)
        self.add_course_btn.place(x=120, y=290)

        self.edit_course_btn = Button(self.home_frame, image=self.update_student_icon, relief="flat", cursor="hand2",
                                      command=self.edit_course)
        self.edit_course_btn.place(x=340, y=290)

        self.course_detail_btn = Button(self.home_frame, image=self.info_student_icon, relief="flat", cursor="hand2",
                                        command=self.course_details)
        self.course_detail_btn.place(x=560, y=290)

        # ------------------------Manage Fees
        self.pay_fee_btn = Button(self.home_frame, image=self.pay_fee_icon, relief="flat", cursor="hand2",
                                  command=self.pay_fee)
        self.pay_fee_btn.place(x=120, y=485)

        self.claim_refund_btn = Button(self.home_frame, image=self.refund_icon, relief="flat", cursor="hand2",
                                       command=self.claim_refund)
        self.claim_refund_btn.place(x=350, y=485)

        self.fee_details_btn = Button(self.home_frame, image=self.fee_history_icon, relief="flat", cursor="hand2",
                                      command=self.fee_history)
        self.fee_details_btn.place(x=560, y=485)

        ## ---------------------------- LABELS ---------------------------- ##
        # ----------------MANAGE STUDENTS
        self.manage_student = Label(self.home_frame, text="** Manage Students **",
                                    font=("comic sans ms", 14, "underline", "italic"), bg="#f9fafc")
        self.manage_student.place(x=35, y=35)

        self.add_student_label = Label(self.home_frame, text="Add Student", font=("comic sans ms", 12, "italic"),
                                       bg="#f9fafc")
        self.add_student_label.place(x=120, y=185)

        self.edit_student_label = Label(self.home_frame, text="Edit Student", font=("comic sans ms", 12, "italic"),
                                        bg="#f9fafc")
        self.edit_student_label.place(x=342, y=185)

        self.student_detail_btn = Label(self.home_frame, text="Students Detail", font=("comic sans ms", 12, "italic"),
                                        bg="#f9fafc")
        self.student_detail_btn.place(x=552, y=185)

        # ------------------Course Details
        self.manage_course_label = Label(self.home_frame, text="** Manage Course **",
                                         font=("comic sans ms", 14, "underline", "italic"), bg="#f9fafc")
        self.manage_course_label.place(x=35, y=240)

        self.add_course_label = Label(self.home_frame, text="Add Course", font=("comic sans ms", 12, "italic"),
                                      bg="#f9fafc")
        self.add_course_label.place(x=123, y=396)

        self.edit_course_label = Label(self.home_frame, text="Edit Course", font=("comic sans ms", 12, "italic"),
                                       bg="#f9fafc")
        self.edit_course_label.place(x=342, y=396)

        self.course_details_label = Label(self.home_frame, text="Courses Detail", font=("comic sans ms", 12, "italic"),
                                          bg="#f9fafc")
        self.course_details_label.place(x=555, y=396)

        # ------------------------- Fee Details
        self.manage_fee_label = Label(self.home_frame, text="** Manage Fee **",
                                      font=("comic sans ms", 14, "underline", "italic"), bg="#f9fafc")
        self.manage_fee_label.place(x=35, y=437)

        self.pay_fee_label = Label(self.home_frame, text="Pay Fee", font=("comic sans ms", 12, "italic"),
                                   bg="#f9fafc")
        self.pay_fee_label.place(x=150, y=592)

        self.claim_refund_label = Label(self.home_frame, text="Claim Refund", font=("comic sans ms", 12, "italic"),
                                        bg="#f9fafc")
        self.claim_refund_label.place(x=342, y=592)

        self.fee_details_label = Label(self.home_frame, text="Fee History", font=("comic sans ms", 12, "italic"),
                                       bg="#f9fafc")
        self.fee_details_label.place(x=572, y=592)

    def add_student(self):
        self.home_frame.destroy()
        self.window.switch_frame(Add_Student)

    def add_course(self):
        self.home_frame.destroy()
        self.window.switch_frame(Add_Course)

    def edit_student(self):
        self.home_frame.destroy()
        self.window.switch_frame(Update_Student)

    def student_details(self):
        self.home_frame.destroy()
        self.window.switch_frame(Student_Details)

    def edit_course(self):
        self.home_frame.destroy()
        self.window.switch_frame(Update_Course)

    def course_details(self):
        self.home_frame.destroy()
        self.window.switch_frame(Course_Details)

    def pay_fee(self):
        self.home_frame.destroy()
        self.window.switch_frame(Pay_Fee)

    def claim_refund(self):
        self.home_frame.destroy()
        self.window.switch_frame(Refund)

    def fee_history(self):
        self.home_frame.destroy()
        self.window.switch_frame(Fee_History)

    def sign_out(self):
        self.home_frame.destroy()
        self.window.switch_frame(Login)


###################################################################################################################################################### ADD STUDENT
class Add_Student(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window
        self.add_frame = Frame(self.window, bg="#f9fafc", relief=GROOVE, borderwidth=0)
        self.add_frame.place(x=435, y=160, width=600, height=630)

        self.my_db = MyDb()
        self.course = self.show_course()

        ## ---------------------------- IMAGE ---------------------------- ##
        self.reset_btn_icon = PhotoImage(file="images/reset.png")
        self.add_student_icon = PhotoImage(file="images/studentadd.png")
        self.add_student_img = Label(self.add_frame, bg="#f9fafc", image=self.add_student_icon)
        self.add_student_img.place(x=245, y=10)

        ## ---------------------------- LABELS ---------------------------- ##
        self.name_label = Label(self.add_frame, text="Full name: ", font=("comic sans ms", 15, "bold"), bg="#f9fafc")
        self.name_label.place(x=10, y=150)

        self.fname_label = Label(self.add_frame, text="(First Name)", font=("comic sans ms", 10, "italic"),
                                 bg="#f9fafc")
        self.fname_label.place(x=130, y=137)

        self.lname_label = Label(self.add_frame, text="(Last Name)", font=("comic sans ms", 10, "italic"),
                                 bg="#f9fafc")
        self.lname_label.place(x=310, y=137)

        self.reset_label = Label(self.add_frame, text="Reset", font=("comic sans ms", 10, "italic"),
                                 bg="#f9fafc")
        self.reset_label.place(x=505, y=170)

        self.dob_label = Label(self.add_frame, text="Date of Birth: ", font=("comic sans ms", 15, "bold"), bg="#f9fafc")
        self.dob_label.place(x=10, y=210)

        self.gender_label = Label(self.add_frame, text="Gender: ", font=("comic sans ms", 15, "bold"), bg="#f9fafc")
        self.gender_label.place(x=290, y=210)

        self.mobile_label = Label(self.add_frame, text="Mobile No.: ", font=("comic sans ms", 15, "bold"), bg="#f9fafc")
        self.mobile_label.place(x=10, y=270)

        self.num_warning = Label(self.add_frame, text="(10 digit number)", font=("comic sans ms", 12, "italic"),
                                 bg="#f9fafc", fg="grey")
        self.num_warning.place(x=310, y=270)

        self.email_label = Label(self.add_frame, text="Email: ", font=("comic sans ms", 15, "bold"), bg="#f9fafc")
        self.email_label.place(x=10, y=325)

        self.email_eg = Label(self.add_frame, text="(eg: example@example.com)", font=("comic sans ms", 12, "italic"),
                              bg="#f9fafc", fg="grey")
        self.email_eg.place(x=320, y=325)

        self.address_label = Label(self.add_frame, text="Address: ", font=("comic sans ms", 15, "bold"), bg="#f9fafc")
        self.address_label.place(x=10, y=380)

        self.country_label = Label(self.add_frame, text="Country: ", font=("comic sans ms", 15, "bold"), bg="#f9fafc")
        self.country_label.place(x=315, y=380)

        self.course_label = Label(self.add_frame, text="Course: ", font=("comic sans ms", 15, "bold"), bg="#f9fafc")
        self.course_label.place(x=163, y=430)

        ## ---------------------------- ENTRY ---------------------------- ##
        self.fname = StringVar()
        self.lname = StringVar()
        self.mobile = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.country = StringVar()

        self.fname_entry = Entry(self.add_frame, font=("Arial", 15), relief=GROOVE, width=12, textvariable=self.fname)
        self.fname_entry.place(x=120, y=157)

        self.lname_entry = Entry(self.add_frame, font=("Arial", 15), relief=GROOVE, width=12, textvariable=self.lname)
        self.lname_entry.place(x=290, y=157)

        self.mobile_entry = Entry(self.add_frame, font=("Arial", 15), relief=GROOVE, width=14, textvariable=self.mobile)
        self.mobile_entry.place(x=140, y=272)

        self.email_entry = Entry(self.add_frame, font=("Arial", 15), relief=GROOVE, textvariable=self.email)
        self.email_entry.place(x=85, y=330)

        self.address_entry = Entry(self.add_frame, font=("Arial", 15), relief=GROOVE, width=14,
                                   textvariable=self.address)
        self.address_entry.place(x=110, y=385)

        self.country_entry = Entry(self.add_frame, font=("Arial", 15), relief=GROOVE, width=12,
                                   textvariable=self.country)
        self.country_entry.place(x=410, y=385)

        self.cal_date = DateEntry(self.add_frame, width=12, background="sky blue", foreground="white", borderwidth=2)
        self.cal_date.place(x=165, y=220)

        self.course_combo = ttk.Combobox(self.add_frame, state="readonly", width=27)
        self.course_combo.place(x=250, y=440)
        self.course_combo.set("Choose Course")

        self.show_course_in_combo()

        ## ---------------------------- Radio Button--------------------------- ##
        self.male = Label(self.add_frame, text="Male", bg="#f9fafc", font=("comic sans ms", 12))
        self.male.place(x=415, y=215)
        self.female = Label(self.add_frame, text="Female", bg="#f9fafc", font=("comic sans ms", 12))
        self.female.place(x=500, y=215)
        self.gender = StringVar()
        self.gender.set(0)
        self.radio_btn1 = Radiobutton(self.add_frame, value="Male", variable=self.gender, bg="#f9fafc")
        self.radio_btn1.place(x=385, y=218)
        self.radio_btn2 = Radiobutton(self.add_frame, value="Female", variable=self.gender, bg="#f9fafc")
        self.radio_btn2.place(x=475, y=218)

        ## ---------------------------- Buttons--------------------------- ##
        self.add_student_btn = Button(self.add_frame, text="Add student", command=self.add_student, cursor="hand2",
                                      font=("Arial", 10, "bold"),
                                      bd=1, padx=16)
        self.add_student_btn.place(x=250, y=520)

        self.cancel_btn = Button(self.add_frame, text="Cancel", relief="flat", bg="#f9fafc",
                                 cursor="hand2", font=("Arial", 10, "bold", "underline"),
                                 command=self.cancel,
                                 bd=1, padx=16)
        self.cancel_btn.place(x=268, y=550)

        self.reset_btn = Button(self.add_frame, image=self.reset_btn_icon, bg="#f9fafc", bd=0, cursor="hand2",
                                command=self.reset)
        self.reset_btn.place(x=510, y=140)

    def show_course(self):
        qry = "SELECT course_name FROM course"
        all_course = self.my_db.show_data(qry)
        return all_course

    def show_course_in_combo(self):
        all_course = []
        for i in self.course:
            all_course.append(i)
        self.course_combo["values"] = all_course

    def add_student(self):
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        course = self.course_combo.get()
        mobile = self.mobile_entry.get()
        email = self.email_entry.get()
        gender = self.gender.get()
        dob = self.cal_date.get()
        address = self.address_entry.get()
        country = self.country.get()

        if (fname == "") or (lname == "") or (course == "Select Course") or (mobile == "") or (email == "") or (
                gender == "") or (dob == "") or (country == ""):
            messagebox.showerror("Notification", "Please Fill all the fields!")
            return False
        else:
            try:
                qry = "INSERT INTO students_info(first_name, last_name, course, mobile, email, gender, dob, address, country) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (fname, lname, course, mobile, email, gender, dob, address, country)
                self.my_db.aur(qry, values)
                messagebox.showinfo("Notification", "Student {} Added Successfully..".format(fname))
                self.add_frame.destroy()
                self.window.switch_frame(Add_Student)
                return True


            except Exception as abc:
                print(abc)
                messagebox.showerror("Notification", "Mobile Number already exists!")
                return False

    def cancel(self):
        self.add_frame.destroy()
        self.window.switch_frame(Homepg)

    def reset(self):
        self.add_frame.destroy()
        self.window.switch_frame(Add_Student)


###################################################################################################################################################### ADD COURSE
class Add_Course(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window
        self.add_frame = Frame(self.window, bg="#f9fafc", relief=GROOVE, borderwidth=0)
        self.add_frame.place(x=435, y=200, width=600, height=500)

        self.my_db = MyDb()
        self.all_usernames = self.show_username()

        ## ---------------------------- IMAGE ---------------------------- ##
        self.reset_btn_icon = PhotoImage(file="images/reset.png")
        self.add_course_icon = PhotoImage(file="images/course.png")
        self.add_course_img = Label(self.add_frame, bg="#f9fafc", image=self.add_course_icon)
        self.add_course_img.place(x=245, y=10)

        ## ---------------------------- LABEL ---------------------------- ##
        self.course_name_label = Label(self.add_frame, text="Course Name: ", font=("comic sans ms", 15),
                                       bg="#f9fafc")
        self.course_name_label.place(x=10, y=150)

        self.reset_label = Label(self.add_frame, text="Reset", font=("comic sans ms", 10, "italic"),
                                 bg="#f9fafc")
        self.reset_label.place(x=505, y=170)
        self.course_fee_label = Label(self.add_frame, text="Course Fee: ", font=("comic sans ms", 15),
                                      bg="#f9fafc")
        self.course_fee_label.place(x=10, y=200)

        self.course_descri_label = Label(self.add_frame, text="Course Description: ",
                                         font=("comic sans ms", 15),
                                         bg="#f9fafc")
        self.course_descri_label.place(x=10, y=250)

        self.course_added_by_label = Label(self.add_frame, text="Added By: ", font=("comic sans ms", 15),
                                           bg="#f9fafc")
        self.course_added_by_label.place(x=300, y=200)

        ## ---------------------------- ENTRY ---------------------------- ##
        self.cname = StringVar()
        self.cfee = StringVar()
        self.course_name_entry = Entry(self.add_frame, font=("Arial", 15), relief=GROOVE, textvariable=self.cname)
        self.course_name_entry.place(x=160, y=157)

        self.course_fee_entry = Entry(self.add_frame, font=("Arial", 15), width=13, relief=GROOVE,
                                      textvariable=self.cfee)
        self.course_fee_entry.place(x=140, y=207)

        self.user_combo = ttk.Combobox(self.add_frame, state="readonly", width=20)
        self.user_combo.place(x=425, y=209)
        self.user_combo.set("(Select your name)")
        self.show_users_in_combo()

        self.description = Text(self.add_frame, width=25, height=5, font=("Arial", 15), relief=GROOVE)
        self.description.place(x=210, y=250)

        ## ---------------------------- Buttons--------------------------- ##
        self.add_course_btn = Button(self.add_frame, text="Add Course", command=self.add_course, cursor="hand2",
                                     font=("Arial", 10, "bold"),
                                     bd=1, padx=16)
        self.add_course_btn.place(x=230, y=400)

        self.cancel_btn = Button(self.add_frame, text="Cancel", relief="flat", bg="#f9fafc",
                                 cursor="hand2", font=("Arial", 10, "bold", "underline"),
                                 command=self.cancel,
                                 bd=1, padx=16)
        self.cancel_btn.place(x=245, y=435)

        self.reset_btn = Button(self.add_frame, image=self.reset_btn_icon, bg="#f9fafc", bd=0, cursor="hand2",
                                command=self.reset)
        self.reset_btn.place(x=510, y=140)

    def add_course(self):
        cname = self.course_name_entry.get()
        fee = self.course_fee_entry.get()
        description = self.description.get("1.0", "end-1c")
        added_by = self.user_combo.get()

        if (cname == "") or (fee == "") or (description == "") or (added_by == "(Select your name)"):
            messagebox.showerror("Notification", "Please Fill all the fields!")
        else:
            try:
                qry = "INSERT INTO course(course_name,fee,description,added_by) VALUES (%s,%s,%s,%s)"
                values = (cname, fee, description, added_by)
                self.my_db.aur(qry, values)
                messagebox.showinfo("Notification", "Course {} Added Successfully..".format(cname))
            except:
                messagebox.showerror("Notification", "Course already exists")

    def cancel(self):
        self.add_frame.destroy()
        self.window.switch_frame(Homepg)

    def reset(self):
        self.add_frame.destroy()
        self.window.switch_frame(Add_Course)

    def show_username(self):
        qry = "SELECT username FROM users"
        all_usernames = self.my_db.show_data(qry)
        return all_usernames

    def show_users_in_combo(self):
        all_username = []
        for i in self.all_usernames:
            all_username.append(i)
        self.user_combo["values"] = all_username


###################################################################################################################################################### UPDATE STUDENT
class Update_Student(tk.Frame):
    def __init__(self,window):
        tk.Frame.__init__(self, window)
        self.window = window
        self.update_frame = Frame(self.window, bg="#f9fafc", relief=GROOVE, borderwidth=0)
        self.update_frame.place(x=130, y=150, width=1300, height=630)

        self.data_frame = Frame(self.update_frame, bg="black", relief=GROOVE, borderwidth=1)
        self.data_frame.place(x=10, y=10)
        self.my_db = MyDb()
        self.course = self.show_course()
        self.update_index = ""

        ## ---------------------------- IMAGE ---------------------------- ##
        self.reset_btn_icon = PhotoImage(file="images/reset.png")
        self.add_student_icon = PhotoImage(file="images/studentadd.png")
        self.search_icon = PhotoImage(file="images/search.png")

        self.add_student_img = Label(self.update_frame, bg="#f9fafc", image=self.add_student_icon)
        self.add_student_img.place(x=565, y=10)

        ## ---------------------------- LABELS ---------------------------- ##
        self.name_label = Label(self.update_frame, text="Full name: ", font=("comic sans ms", 15), bg="#f9fafc")
        self.name_label.place(x=10, y=150)

        self.fname_label = Label(self.update_frame, text="(First Name)", font=("comic sans ms", 10, "italic"),
                                 bg="#f9fafc")
        self.fname_label.place(x=130, y=137)

        self.lname_label = Label(self.update_frame, text="(Last Name)", font=("comic sans ms", 10, "italic"),
                                 bg="#f9fafc")
        self.lname_label.place(x=310, y=137)

        self.reset_label = Label(self.update_frame, text="Reset", font=("comic sans ms", 10, "italic"),
                                 bg="#f9fafc")
        self.reset_label.place(x=505, y=170)

        self.dob_label = Label(self.update_frame, text="Date of Birth: ", font=("comic sans ms", 15),
                               bg="#f9fafc")
        self.dob_label.place(x=10, y=210)

        self.gender_label = Label(self.update_frame, text="Gender: ", font=("comic sans ms", 15), bg="#f9fafc")
        self.gender_label.place(x=290, y=210)

        self.mobile_label = Label(self.update_frame, text="Mobile No.: ", font=("comic sans ms", 15),
                                  bg="#f9fafc")
        self.mobile_label.place(x=10, y=270)

        self.num_warning = Label(self.update_frame, text="(10 digit number)", font=("comic sans ms", 12, "italic"),
                                 bg="#f9fafc", fg="grey")
        self.num_warning.place(x=310, y=270)

        self.email_label = Label(self.update_frame, text="Email: ", font=("comic sans ms", 15), bg="#f9fafc")
        self.email_label.place(x=10, y=325)

        self.email_eg = Label(self.update_frame, text="(eg: example@example.com)", font=("comic sans ms", 12, "italic"),
                              bg="#f9fafc", fg="grey")
        self.email_eg.place(x=320, y=325)

        self.address_label = Label(self.update_frame, text="Address: ", font=("comic sans ms", 15),
                                   bg="#f9fafc")
        self.address_label.place(x=10, y=380)

        self.country_label = Label(self.update_frame, text="Country: ", font=("comic sans ms", 15),
                                   bg="#f9fafc")
        self.country_label.place(x=315, y=380)

        self.course_label = Label(self.update_frame, text="Course: ", font=("comic sans ms", 15), bg="#f9fafc")
        self.course_label.place(x=163, y=430)

        ## ---------------------------- ENTRY ---------------------------- ##
        self.fname = StringVar()
        self.lname = StringVar()
        self.mobile = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.country = StringVar()

        self.fname_entry = Entry(self.update_frame, font=("Arial", 15), relief=GROOVE, width=12,
                                 textvariable=self.fname)
        self.fname_entry.place(x=120, y=157)

        self.lname_entry = Entry(self.update_frame, font=("Arial", 15), relief=GROOVE, width=12,
                                 textvariable=self.lname)
        self.lname_entry.place(x=290, y=157)

        self.mobile_entry = Entry(self.update_frame, font=("Arial", 15), relief=GROOVE, width=14,
                                  textvariable=self.mobile)
        self.mobile_entry.place(x=140, y=272)

        self.email_entry = Entry(self.update_frame, font=("Arial", 15), relief=GROOVE, textvariable=self.email)
        self.email_entry.place(x=85, y=330)

        self.address_entry = Entry(self.update_frame, font=("Arial", 15), relief=GROOVE, width=14,
                                   textvariable=self.address)
        self.address_entry.place(x=110, y=385)

        self.country_entry = Entry(self.update_frame, font=("Arial", 15), relief=GROOVE, width=12,
                                   textvariable=self.country)
        self.country_entry.place(x=410, y=385)

        self.cal_date = DateEntry(self.update_frame, width=12, background="sky blue", foreground="white", borderwidth=2)
        self.cal_date.place(x=165, y=220)

        self.course_combo = ttk.Combobox(self.update_frame, state="readonly", width=27)
        self.course_combo.place(x=250, y=440)
        self.course_combo.set("Choose Course")

        self.show_course_in_combo()

        ## ---------------------------- Radio Button--------------------------- ##
        self.male = Label(self.update_frame, text="Male", bg="#f9fafc", font=("comic sans ms", 12))
        self.male.place(x=415, y=215)
        self.female = Label(self.update_frame, text="Female", bg="#f9fafc", font=("comic sans ms", 12))
        self.female.place(x=500, y=215)
        self.gender = StringVar()
        self.gender.set(0)
        self.radio_btn1 = Radiobutton(self.update_frame, value="Male", variable=self.gender, bg="#f9fafc")
        self.radio_btn1.place(x=385, y=218)
        self.radio_btn2 = Radiobutton(self.update_frame, value="Female", variable=self.gender, bg="#f9fafc")
        self.radio_btn2.place(x=475, y=218)

        ## ---------------------------- Buttons--------------------------- ##
        self.update_student_btn = Button(self.update_frame, text="Update student", command=self.update_student,
                                         cursor="hand2",
                                         font=("Arial", 10, "bold"),
                                         bd=1, padx=16)
        self.update_student_btn.place(x=400, y=550)

        self.remove_student_btn = Button(self.update_frame, text="Remove student", command=self.remove_student,
                                         cursor="hand2",
                                         font=("Arial", 10, "bold"),
                                         bd=1, padx=16)
        self.remove_student_btn.place(x=550, y=550)

        self.showall_student_btn = Button(self.update_frame, text="Show all students", command=self.show_all_student,
                                          font=("Arial", 10, "bold"),
                                          bd=1, padx=16)
        self.showall_student_btn.place(x=703, y=550)

        self.cancel_btn = Button(self.update_frame, text="Cancel", relief="flat", bg="#f9fafc",
                                 cursor="hand2", font=("Arial", 10, "bold", "underline"),
                                 command=self.cancel,
                                 bd=1, padx=16)
        self.cancel_btn.place(x=570, y=580)

        self.reset_btn = Button(self.update_frame, image=self.reset_btn_icon, bg="#f9fafc", bd=0, cursor="hand2",
                                command=self.reset)
        self.reset_btn.place(x=510, y=140)

        ## --------------------------------- Search ---------------------- ##
        self.search_label = Label(self.update_frame, text="Search by ID", font=("comic sans ms", 12), bg="#f9fafc")
        self.search_label.place(x=1100, y=90)
        self.search_var = StringVar()
        self.search_entry = Entry(self.update_frame, font=("Arial", 15), relief=GROOVE, textvariable=self.search_var,
                                  width=5)
        self.search_entry.place(x=1130, y=120)

        self.search_btn = Button(self.update_frame, image=self.search_icon, bg="#f9fafc", bd=0, cursor="hand2",
                                 command=self.search)
        self.search_btn.place(x=1200, y=120)

        ## --------------------------------- Sorting Method ---------------------- ##
        self.sortby_label = Label(self.update_frame, text="Sort by:                 /", font=("comic sans ms", 12),
                                  bg="#f9fafc")
        self.sortby_label.place(x=600, y=130)

        self.firstname_btn = Button(self.update_frame, text="First Name", bg="#f9fafc", fg="blue", bd=0, cursor="hand2",
                                    command=self.sortby_fname, font=("comic sans ms", 10, "italic", "underline"))
        self.firstname_btn.place(x=675, y=130)

        self.lastname_btn = Button(self.update_frame, text="Last Name", bg="#f9fafc", fg="blue", bd=0, cursor="hand2",
                                   command=self.sortby_lname, font=("comic sans ms", 10, "italic", "underline"))
        self.lastname_btn.place(x=760, y=130)

        ## ---------------------------------Tree View---------------------- ##
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("arial", 10, "bold"), foreground="#DC143C")

        self.data_frame = Frame(self.update_frame, height=500, width=200)
        self.data_frame.place(x=600, y=160, width=650)
        self.scroll_x = Scrollbar(self.data_frame, orient=HORIZONTAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y = Scrollbar(self.data_frame, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.data_tree = ttk.Treeview(self.data_frame, columns=(
            "id", "fname", "lname", "course", "mobile", "email", "gender", "dob", "country"),
                                      xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set, height=15)

        self.data_tree.column("id", width=30)
        self.data_tree.column("fname", width=100)
        self.data_tree.column("lname", width=85)
        self.data_tree.column("course", width=100)
        self.data_tree.column("mobile", width=90)
        self.data_tree.column("email", width=120)
        self.data_tree.column("gender", width=55)
        self.data_tree.column("dob", width=50)
        self.data_tree.column("country", width=90)
        self.data_tree.heading("id", text="ID")
        self.data_tree.heading("fname", text="First Name")
        self.data_tree.heading("lname", text="Last Name")
        self.data_tree.heading("course", text="Course")
        self.data_tree.heading("mobile", text="Mobile No.")
        self.data_tree.heading("email", text="Email")
        self.data_tree.heading("gender", text="Gender")
        self.data_tree.heading("dob", text="D.O.B")
        self.data_tree.heading("country", text="Country")
        self.data_tree["show"] = "headings"
        self.data_tree.pack()
        self.scroll_x.config(command=self.data_tree.xview)
        self.scroll_y.config(command=self.data_tree.yview)

    ## --------------------------------- QUERYS ---------------------- ##
    def show_course(self):
        qry = "SELECT course_name FROM course"
        all_course = self.my_db.show_data(qry)
        return all_course

    def show_course_in_combo(self):
        all_course = []
        for i in self.course:
            all_course.append(i)
        self.course_combo["values"] = all_course

    def all_student(self):
        qry = "SELECT * FROM students_info"
        all_student = self.my_db.show_data(qry)
        return all_student

    ## --------------------------------- FUNCTIONS --------------------- ##
    def show_all_student(self):
        self.data_tree.delete(*self.data_tree.get_children())
        data = self.all_student()
        for i in data:
            self.data_tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
        self.data_tree.bind("<Double-1>", self.select_data)

    def update_student(self):
        if self.update_index == "":
            messagebox.showerror("Error", "Please select the student first")

        else:
            fname = self.fname_entry.get()
            lname = self.lname_entry.get()
            course = self.course_combo.get()
            mobile = self.mobile_entry.get()
            email = self.email_entry.get()
            gender = self.gender.get()
            dob = self.cal_date.get()
            address = self.address_entry.get()
            country = self.country.get()
            if (fname == "") or (lname == "") or (course == "Select Course") or (mobile == "") or (email == "") or (
                    gender == "") or (dob == "") or (address == "")or (country == ""):
                messagebox.showerror("Notification", "Please Fill all the fields!")
            else:
                try:
                    qry = "UPDATE students_info SET first_name = %s, last_name = %s, course= %s, mobile= %s, email= %s, gender= %s, dob= %s, address= %s, country= %s WHERE id =%s"
                    values = (fname, lname, course, mobile, email, gender, dob, address, country, self.update_index)
                    self.my_db.aur(qry, values)

                    messagebox.showinfo("Notification", "Student {} Updated Successfully..".format(fname))

                except:
                    messagebox.showerror("Notification", "Mobile Number already exists!")

    def remove_student(self):
        if self.update_index == "":
            messagebox.showerror("Error", "Please select the student first")
            return False
        else:
            fname = self.fname_entry.get()
            qry = "DELETE FROM students_info WHERE id = %s"
            values = (self.update_index,)
            self.my_db.aur(qry, values)
            messagebox.showinfo("Notification", "Student {} Removed Successfully..".format(fname))
            self.show_all_student()
            return True

    def search(self):
        qry = "SELECT id FROM students_info"
        all_id = self.my_db.show_data(qry)
        searched_value = self.search_entry.get()
        ids = []
        for i in all_id:
            ids.append(i[0])
        if int(searched_value) in ids:
            self.data_tree.delete(*self.data_tree.get_children())
            qry = "SELECT id, first_name,last_name,course,mobile,email,gender, dob, address, country FROM students_info WHERE id= %s"
            value = (int(searched_value),)
            data = self.my_db.show_data_from_p(qry, value)
            for i in data:
                self.data_tree.insert("", "end",
                                      values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))

            return True
        else:
            messagebox.showerror("Notification", "No student found with that ID")
            return False

    def select_data(self, event):
        selected_row = self.data_tree.selection()[0]
        selected_data = self.data_tree.item(selected_row, "values")
        self.update_index = selected_data[0]
        self.fname_entry.delete(0, END)
        self.fname_entry.insert(0, selected_data[1])
        self.lname_entry.delete(0, END)
        self.lname_entry.insert(0, selected_data[2])
        self.course_combo.set(selected_data[3])
        self.mobile_entry.delete(0, END)
        self.mobile_entry.insert(0, selected_data[4])
        self.email_entry.delete(0, END)
        self.email_entry.insert(0, selected_data[5])
        self.gender.set(selected_data[6])
        self.cal_date.set_date(selected_data[7])
        self.address_entry.delete(0, END)
        self.address_entry.insert(0, selected_data[8])
        self.country_entry.delete(0, END)
        self.country_entry.insert(0, selected_data[9])

    def sortby_fname(self):
        self.data_tree.delete(*self.data_tree.get_children())
        qry = "SELECT * FROM students_info ORDER BY first_name ASC"
        by_fname = self.my_db.show_data(qry)
        for i in by_fname:
            self.data_tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
        self.data_tree.bind("<Double-1>", self.select_data)

    def sortby_lname(self):
        self.data_tree.delete(*self.data_tree.get_children())
        qry = "SELECT * FROM students_info ORDER BY last_name ASC"
        by_lname = self.my_db.show_data(qry)
        for i in by_lname:
            self.data_tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
        self.data_tree.bind("<Double-1>", self.select_data)

    def cancel(self):
        self.update_frame.destroy()
        self.window.switch_frame(Homepg)

    def reset(self):
        self.update_frame.destroy()
        self.window.switch_frame(Update_Student)


###################################################################################################################################################### UPDATE COURSE
class Update_Course(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window
        self.update_frame = Frame(self.window, bg="#f9fafc", relief=GROOVE, borderwidth=0)
        self.update_frame.place(x=200, y=200, width=1150, height=550)

        self.my_db = MyDb()
        self.all_usernames = self.show_username()
        self.update_index = ""

        ## ---------------------------- IMAGE ---------------------------- ##
        self.reset_btn_icon = PhotoImage(file="images/reset.png")
        self.update_course_icon = PhotoImage(file="images/course.png")
        self.search_icon = PhotoImage(file="images/search.png")
        self.update_course_img = Label(self.update_frame, bg="#f9fafc", image=self.update_course_icon)
        self.update_course_img.place(x=500, y=10)

        ## ---------------------------- LABEL ---------------------------- ##
        self.course_name_label = Label(self.update_frame, text="Course Name: ", font=("comic sans ms", 15),
                                       bg="#f9fafc")
        self.course_name_label.place(x=10, y=150)

        self.reset_label = Label(self.update_frame, text="Reset", font=("comic sans ms", 10, "italic"),
                                 bg="#f9fafc")
        self.reset_label.place(x=505, y=170)
        self.course_fee_label = Label(self.update_frame, text="Course Fee: ", font=("comic sans ms", 15),
                                      bg="#f9fafc")
        self.course_fee_label.place(x=10, y=200)

        self.course_descri_label = Label(self.update_frame, text="Course Description: ",
                                         font=("comic sans ms", 15),
                                         bg="#f9fafc")
        self.course_descri_label.place(x=10, y=250)

        self.course_added_by_label = Label(self.update_frame, text="Added By: ", font=("comic sans ms", 15),
                                           bg="#f9fafc")
        self.course_added_by_label.place(x=300, y=200)

        ## ---------------------------- ENTRY ---------------------------- ##
        self.cname = StringVar()
        self.cfee = StringVar()
        self.course_name_entry = Entry(self.update_frame, font=("Arial", 15), relief=GROOVE, textvariable=self.cname)
        self.course_name_entry.place(x=160, y=157)

        self.course_fee_entry = Entry(self.update_frame, font=("Arial", 15), width=13, relief=GROOVE,
                                      textvariable=self.cfee)
        self.course_fee_entry.place(x=140, y=207)

        self.user_combo = ttk.Combobox(self.update_frame, state="readonly", width=20)
        self.user_combo.place(x=425, y=209)
        self.user_combo.set("(Select your name)")
        self.show_users_in_combo()

        self.description = Text(self.update_frame, width=25, height=5, font=("Arial", 15), relief=GROOVE)
        self.description.place(x=210, y=250)

        ## ---------------------------- Buttons--------------------------- ##
        self.update_course_btn = Button(self.update_frame, text="Update Course", command=self.update_course,
                                        cursor="hand2",
                                        font=("Arial", 10, "bold"),
                                        bd=1, padx=16)
        self.update_course_btn.place(x=300, y=440)

        self.remove_course_btn = Button(self.update_frame, text="Remove Course", command=self.remove_course,
                                        cursor="hand2",
                                        font=("Arial", 10, "bold"),
                                        bd=1, padx=16)
        self.remove_course_btn.place(x=450, y=440)

        self.showall_course_btn = Button(self.update_frame, text="Show All Course", command=self.show_all_course,
                                         cursor="hand2",
                                         font=("Arial", 10, "bold"),
                                         bd=1, padx=16)
        self.showall_course_btn.place(x=600, y=440)

        self.cancel_btn = Button(self.update_frame, text="Cancel", relief="flat", bg="#f9fafc",
                                 cursor="hand2", font=("Arial", 10, "bold", "underline"),
                                 command=self.cancel,
                                 bd=1, padx=16)
        self.cancel_btn.place(x=500, y=480)

        self.reset_btn = Button(self.update_frame, image=self.reset_btn_icon, bg="#f9fafc", bd=0, cursor="hand2",
                                command=self.reset)
        self.reset_btn.place(x=510, y=140)

        ## --------------------------------- Search ---------------------- ##
        self.search_label = Label(self.update_frame, text="Search by ID", font=("comic sans ms", 12), bg="#f9fafc")
        self.search_label.place(x=1000, y=90)
        self.search_var = StringVar()
        self.search_entry = Entry(self.update_frame, font=("Arial", 15), relief=GROOVE, textvariable=self.search_var,
                                  width=5)
        self.search_entry.place(x=1030, y=120)

        self.search_btn = Button(self.update_frame, image=self.search_icon, bg="#f9fafc", bd=0, cursor="hand2",
                                 command=self.search)
        self.search_btn.place(x=1100, y=120)

        ## --------------------------------- Sorting Method ---------------------- ##
        self.sortby_label = Label(self.update_frame, text="Sort by:                   /", font=("comic sans ms", 12),
                                  bg="#f9fafc")
        self.sortby_label.place(x=600, y=130)

        self.firstname_btn = Button(self.update_frame, text="Course Name", bg="#f9fafc", fg="blue", bd=0,
                                    cursor="hand2",
                                    command=self.sortby_cname, font=("comic sans ms", 10, "italic", "underline"))
        self.firstname_btn.place(x=670, y=130)

        self.lastname_btn = Button(self.update_frame, text="Fee", bg="#f9fafc", fg="blue", bd=0, cursor="hand2",
                                   command=self.sortby_fee, font=("comic sans ms", 10, "italic", "underline"))
        self.lastname_btn.place(x=770, y=130)

        ## ---------------------------- Tree View ---------------------------- ##
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("arial", 10, "bold"), foreground="#DC143C")
        self.data_frame = Frame(self.update_frame, height=500, width=200)
        self.data_frame.place(x=600, y=160, width=510)
        self.scroll_x = Scrollbar(self.data_frame, orient=HORIZONTAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y = Scrollbar(self.data_frame, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.data_tree = ttk.Treeview(self.data_frame, columns=(
            "id", "name", "fee", "added_by", "description"), height=10, xscrollcommand=self.scroll_x.set,
                                      yscrollcommand=self.scroll_y.set)

        self.data_tree["show"] = "headings"
        self.data_tree.column("id", width=35)
        self.data_tree.column("name", width=110)
        self.data_tree.column("fee", width=85)
        self.data_tree.column("added_by", width=85)
        self.data_tree.column("description", width=250)
        self.data_tree.heading("id", text="ID")
        self.data_tree.heading("name", text="Name")
        self.data_tree.heading("fee", text="Fee")
        self.data_tree.heading("added_by", text="Added By")
        self.data_tree.heading("description", text="Description")
        self.data_tree.pack()
        self.scroll_x.config(command=self.data_tree.xview)
        self.scroll_y.config(command=self.data_tree.yview)

    def all_course(self):
        qry = "SELECT * FROM course"
        all_course = self.my_db.show_data(qry)
        return all_course

    def select_data(self, event):
        selected_row = self.data_tree.selection()[0]
        selected_data = self.data_tree.item(selected_row, "values")
        self.update_index = selected_data[0]
        self.course_name_entry.delete(0, END)
        self.course_name_entry.insert(0, selected_data[1])
        self.course_fee_entry.delete(0, END)
        self.course_fee_entry.insert(0, selected_data[2])
        self.user_combo.set(selected_data[3])
        self.description_var = selected_data[4]
        self.description.delete(1.0, END)
        self.description.insert("end-1c", self.description_var)

    def show_all_course(self):
        self.data_tree.delete(*self.data_tree.get_children())
        data = self.all_course()
        for i in data:
            self.data_tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4]))
        self.data_tree.bind("<Double-1>", self.select_data)

    def update_course(self):
        if self.update_index == "":
            messagebox.showerror("Error", "Please select the course first")
        else:
            cname = self.course_name_entry.get()
            fee = self.course_fee_entry.get()
            description = self.description.get("1.0", "end-1c")
            added_by = self.user_combo.get()

            qry = "UPDATE course SET course_name = %s, fee = %s, added_by = %s, description= %s WHERE id =%s"
            values = (cname, fee, added_by, description, self.update_index)
            self.my_db.aur(qry, values)

            messagebox.showinfo("Notification", "Student {} Updated Successfully..".format(cname))
            self.show_all_course()

    def remove_course(self):
        if self.update_index == "":
            messagebox.showerror("Error", "Please select the course first")
        else:
            cname = self.course_name_entry.get()
            qry = "DELETE FROM course WHERE id = %s"
            values = (self.update_index,)
            self.my_db.aur(qry, values)
            messagebox.showinfo("Notification", "Course {} Removed Successfully..".format(cname))
            self.course_name_entry.delete(0, END)
            self.course_fee_entry.delete(0, END)
            self.description.delete(1.0, END)
            self.user_combo.set("")
            self.show_all_course()

    def search(self):
        qry = "SELECT id FROM course"
        all_id = self.my_db.show_data(qry)
        searched_value = self.search_entry.get()
        ids = []
        for i in all_id:
            ids.append(i[0])
        if int(searched_value) in ids:
            self.data_tree.delete(*self.data_tree.get_children())
            qry = "SELECT id, course_name, fee, added_by, description FROM course WHERE id= %s"
            value = (int(searched_value),)
            data = self.my_db.show_data_from_p(qry, value)
            for i in data:
                self.data_tree.insert("", "end",
                                      values=(i[0], i[1], i[2], i[3], i[4]))

        else:
            messagebox.showerror("Error", "No course found with that ID!")

    def sortby_cname(self):
        self.data_tree.delete(*self.data_tree.get_children())
        qry = "SELECT * FROM course ORDER BY course_name ASC"
        by_cname = self.my_db.show_data(qry)
        for i in by_cname:
            self.data_tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4]))
        self.data_tree.bind("<Double-1>", self.select_data)

    def sortby_fee(self):
        self.data_tree.delete(*self.data_tree.get_children())
        qry = "SELECT * FROM course ORDER BY fee ASC"
        by_fee = self.my_db.show_data(qry)
        for i in by_fee:
            self.data_tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4]))
            self.data_tree.bind("<Double-1>", self.select_data)

    def cancel(self):
        self.update_frame.destroy()
        self.window.switch_frame(Homepg)

    def reset(self):
        self.update_frame.destroy()
        self.window.switch_frame(Update_Course)

    def show_username(self):
        qry = "SELECT username FROM users"
        all_usernames = self.my_db.show_data(qry)
        return all_usernames

    def show_users_in_combo(self):
        all_username = []
        for i in self.all_usernames:
            all_username.append(i)
        self.user_combo["values"] = all_username


###################################################################################################################################################### PAY FEE
class Pay_Fee(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window
        self.pay_frame = Frame(self.window, bg="#f9fafc", relief=GROOVE, borderwidth=0)
        self.pay_frame.place(x=340, y=150, width=900, height=600)
        self.my_db = MyDb()

        ## ---------------------------------IMAGES  ---------------------- ##

        self.fee_icon = PhotoImage(file="images/fee1.png")
        self.search_icon = PhotoImage(file="images/search.png")
        self.pay_fee_img = Label(self.pay_frame, bg="#f9fafc", image=self.fee_icon)
        self.pay_fee_img.place(x=400, y=10)

        ## ---------------------------------LABELS  ---------------------- ##

        self.name_label = Label(self.pay_frame, text="Name:", font=("comic sans ms", 15), bg="#f9fafc")
        self.name_label.place(x=10, y=180)

        self.course_label = Label(self.pay_frame, text="Course:", font=("comic sans ms", 15), bg="#f9fafc")
        self.course_label.place(x=255, y=180)

        self.username_label = Label(self.pay_frame, text="Mobile no.:", font=("comic sans ms", 15),
                                    bg="#f9fafc")
        self.username_label.place(x=555, y=180)

        self.course_fee = Label(self.pay_frame, text="Course Fee:", font=("comic sans ms", 13), bg="#f9fafc")
        self.course_fee.place(x=250, y=250)

        self.due_label = Label(self.pay_frame, text="Remaining Due:", font=("comic sans ms", 13), bg="#f9fafc")
        self.due_label.place(x=250, y=290)

        self.amount_label = Label(self.pay_frame, text="Payment Amount:", font=("comic sans ms", 13), bg="#f9fafc")
        self.amount_label.place(x=250, y=330)

        self.paid_date_label = Label(self.pay_frame, text="Payment Date:", font=("comic sans ms", 13), bg="#f9fafc")
        self.paid_date_label.place(x=250, y=370)

        self.payment_method_label = Label(self.pay_frame, text="Payment Method:", font=("comic sans ms", 13),
                                          bg="#f9fafc")
        self.payment_method_label.place(x=250, y=415)

        ## ---------------------------------ENTRY ---------------------- ##
        self.name_var = StringVar()
        self.course_var = StringVar()
        self.mobile_var = StringVar()
        self.course_fee_var = StringVar()
        self.remaining_due_var = StringVar()
        self.amount_var = StringVar()

        self.found_name = Entry(self.pay_frame, font=("Arial", 12), relief=GROOVE, textvariable=self.name_var, width=15,
                                state=DISABLED)
        self.found_name.place(x=80, y=188)

        self.found_course = Entry(self.pay_frame, font=("Arial", 12), relief=GROOVE, textvariable=self.course_var,
                                  width=18,
                                  state=DISABLED)
        self.found_course.place(x=340, y=188)

        self.found_mobile = Entry(self.pay_frame, font=("Arial", 12), relief=GROOVE, textvariable=self.mobile_var,
                                  width=13,
                                  state=DISABLED)
        self.found_mobile.place(x=675, y=188)

        self.course_fee_entry = Entry(self.pay_frame, font=("Arial", 12), relief=GROOVE,
                                      textvariable=self.course_fee_var,
                                      width=15,
                                      state=DISABLED)
        self.course_fee_entry.place(x=420, y=255)

        self.remaining_due_entry = Entry(self.pay_frame, font=("Arial", 12), relief=GROOVE,
                                         textvariable=self.remaining_due_var, width=15,
                                         state=DISABLED)
        self.remaining_due_entry.place(x=420, y=295)

        self.amount_entry = Entry(self.pay_frame, font=("Arial", 12), relief=GROOVE, textvariable=self.amount_var,
                                  width=15)
        self.amount_entry.place(x=420, y=335)

        self.paid_date = DateEntry(self.pay_frame, width=15, background="sky blue", foreground="white", borderwidth=2)
        self.paid_date.place(x=420, y=375)

        ## ---------------------------- Radio Button--------------------------- ##
        self.cash = Label(self.pay_frame, text="Cash", bg="#f9fafc", font=("comic sans ms", 12))
        self.cash.place(x=450, y=417)
        self.cheque = Label(self.pay_frame, text="Cheque", bg="#f9fafc", font=("comic sans ms", 12))
        self.cheque.place(x=550, y=417)
        self.payment_method = StringVar()
        self.payment_method.set(0)
        self.radio_btn1 = Radiobutton(self.pay_frame, value="Cash", variable=self.payment_method, bg="#f9fafc")
        self.radio_btn1.place(x=415, y=420)
        self.radio_btn2 = Radiobutton(self.pay_frame, value="Cheque", variable=self.payment_method, bg="#f9fafc")
        self.radio_btn2.place(x=515, y=420)

        ## --------------------------------- Search ---------------------- ##
        self.search_label = Label(self.pay_frame, text="Search by ID", font=("comic sans ms", 12), bg="#f9fafc")
        self.search_label.place(x=700, y=90)
        self.search_var = StringVar()
        self.search_entry = Entry(self.pay_frame, font=("Arial", 15), relief=GROOVE, textvariable=self.search_var,
                                  width=5)
        self.search_entry.place(x=700, y=120)

        self.search_btn = Button(self.pay_frame, image=self.search_icon, bg="#f9fafc", bd=0, cursor="hand2",
                                 command=self.search)
        self.search_btn.place(x=770, y=120)

        ## --------------------------------- Buttons ---------------------- ##
        self.pay_btn = Button(self.pay_frame, text="Pay Fee", command=self.pay, cursor="hand2",
                              font=("Arial", 10, "bold"), bd=1, padx=16)
        self.pay_btn.place(x=375, y=500)

        self.cancel_btn = Button(self.pay_frame, text="Cancel", relief="flat", bg="#f9fafc",
                                 cursor="hand2", font=("Arial", 10, "bold", "underline"),
                                 command=self.cancel,
                                 bd=1, padx=16)
        self.cancel_btn.place(x=380, y=530)

    def search(self):
        qry = "SELECT id FROM students_info"
        all_id = self.my_db.show_data(qry)
        searched_value = self.search_entry.get()
        ids = []
        for i in all_id:
            ids.append(i[0])
        if int(searched_value) in ids:
            qry = "SELECT first_name, last_name, course, mobile from students_info WHERE id= %s"
            value = (int(searched_value),)
            data = self.my_db.show_data_from_p(qry, value)
            for i in data:
                self.name_var.set(i[0] + " " + i[1])
                self.course_var.set(i[2])
                self.mobile_var.set(i[3])

                qry2 = "SELECT fee FROM course WHERE course_name = %s"
                value2 = (i[2],)
                course_fee = self.my_db.show_data_from_p(qry2, value2)
                self.course_fee_var.set(course_fee[0][0])

                qry3 = "SELECT remaining_due FROM fee WHERE course = %s"
                value3 = (i[2],)
                remaining_due = self.my_db.show_data_from_p(qry3, value3)
                if not remaining_due:
                    self.remaining_due_var.set((course_fee[0][0]))
                else:
                    self.remaining_due_var.set(remaining_due[0][0])
        else:
            messagebox.showerror("Notification", "Id does not match!")
        self.amount_var.set("")
        self.payment_method.set("Cash")

    def pay(self):
        name = self.name_var.get()
        course = self.course_var.get()
        mobile = self.mobile_var.get()
        t_course_amt = (int(self.course_fee_entry.get()) + 5000)
        refund_amt = str(t_course_amt - int(self.course_fee_entry.get()))
        course_fee = str(int(self.course_fee_entry.get()) - int(refund_amt))
        amount_paid = self.amount_var.get()
        remaining_due = self.remaining_due_var.get()
        date_paid = self.paid_date.get()
        payment_method = self.payment_method.get()

        ac_remaining_due = int(remaining_due) - int(amount_paid)
        if int(amount_paid) > int(remaining_due):
            messagebox.showerror("Notification", "Amount is more than due!")
        else:
            qry = "SELECT student_name FROM fee"
            all_student_name = self.my_db.show_data(qry)

            if not all_student_name:
                qry = "INSERT INTO fee(student_name, course, mobile, course_fee, amount_paid, remaining_due, date_paid, payment_method, refund) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (
                    name, course, mobile, course_fee, amount_paid, ac_remaining_due, date_paid, payment_method,
                    refund_amt)
                self.my_db.aur(qry, values)

                messagebox.showinfo("Notification", f"Amount paid sucessfully! You reamining due is {ac_remaining_due}")
            else:
                student_name = []
                for i in all_student_name:
                    student_name.append(i[0])

                if name in student_name:
                    qry = "UPDATE fee SET remaining_due =%s, date_paid=%s WHERE course =%s"
                    values = (ac_remaining_due, date_paid, course)
                    self.my_db.aur(qry, values)
                    messagebox.showinfo("Notification",
                                        f"Amount paid successfully! You reamining due is {ac_remaining_due}")

                else:
                    qry = "INSERT INTO fee(student_name, course, mobile, course_fee, amount_paid, remaining_due, date_paid, payment_method,refund) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    values = (
                        name, course, mobile, course_fee, amount_paid, ac_remaining_due, date_paid, payment_method,
                        refund_amt)
                    self.my_db.aur(qry, values)

                    messagebox.showinfo("Notification",
                                        f"Amount paid successfully! You reamining due is {ac_remaining_due}")
            self.pay_frame.destroy()
            self.window.switch_frame(Pay_Fee)

    def cancel(self):
        self.pay_frame.destroy()
        self.window.switch_frame(Homepg)


###################################################################################################################################################### STUDENT DETAILS
class Student_Details(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window
        self.detail_frame = Frame(self.window, bg="#f9fafc", relief=GROOVE, borderwidth=0)
        self.detail_frame.place(x=340, y=150, width=900, height=620)

        self.my_db = MyDb()
        self.course = self.show_course()

        self.add_student_icon = PhotoImage(file="images/studentadd.png")
        self.add_student_img = Label(self.detail_frame, bg="#f9fafc", image=self.add_student_icon)
        self.add_student_img.place(x=390, y=10)

        ## --------------------------------- Search ---------------------- ##
        self.search_icon = PhotoImage(file="images/search.png")
        self.search_label = Label(self.detail_frame, text="Search by ID", font=("comic sans ms", 12), bg="#f9fafc")
        self.search_label.place(x=720, y=120)
        self.search_var = StringVar()
        self.search_entry = Entry(self.detail_frame, font=("Arial", 15), relief=GROOVE, textvariable=self.search_var,
                                  width=5)
        self.search_entry.place(x=730, y=150)

        self.search_btn = Button(self.detail_frame, image=self.search_icon, bg="#f9fafc", bd=0, cursor="hand2",
                                 command=self.search)
        self.search_btn.place(x=810, y=150)

        ## --------------------------------- Buttons ---------------------- ##
        self.showall_student_btn = Button(self.detail_frame, text="Show all students", command=self.show_all_student,
                                          font=("Arial", 10, "bold"),
                                          bd=1, padx=16)
        self.showall_student_btn.place(x=365, y=560)

        self.cancel_btn = Button(self.detail_frame, text="Cancel", relief="flat", bg="#f9fafc",
                                 cursor="hand2", font=("Arial", 10, "bold", "underline"),
                                 command=self.cancel,
                                 bd=1, padx=16)
        self.cancel_btn.place(x=390, y=591)

        ## --------------------------------- Sorting Method ---------------------- ##
        self.sortby_label = Label(self.detail_frame, text="Sort by:                 /", font=("comic sans ms", 12),
                                  bg="#f9fafc")
        self.sortby_label.place(x=30, y=165)

        self.firstname_btn = Button(self.detail_frame, text="First Name", bg="#f9fafc", fg="blue", bd=0, cursor="hand2",
                                    command=self.sortby_fname, font=("comic sans ms", 10, "italic", "underline"))
        self.firstname_btn.place(x=105, y=165)

        self.lastname_btn = Button(self.detail_frame, text="Last Name", bg="#f9fafc", fg="blue", bd=0, cursor="hand2",
                                   command=self.sortby_lname, font=("comic sans ms", 10, "italic", "underline"))
        self.lastname_btn.place(x=190, y=165)

        self.sort_btn = Button(self.detail_frame, text="Sort", bg="#f9fafc", fg="blue", bd=0, cursor="hand2",
                               command=self.sortby_course, font=("comic sans ms", 10, "italic", "underline"))
        self.sort_btn.place(x=450, y=165)

        self.course_combo = ttk.Combobox(self.detail_frame, state="readonly", width=20)
        self.course_combo.place(x=300, y=170)
        self.course_combo.set("Choose Course")

        self.show_course_in_combo()
        ## --------------------------------- TreeView ---------------------- ##
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("arial", 10, "bold"), foreground="#DC143C")
        self.data_frame = Frame(self.detail_frame, height=450, width=320)
        self.data_frame.place(x=30, y=200, width=850)
        self.scroll_x = Scrollbar(self.data_frame, orient=HORIZONTAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y = Scrollbar(self.data_frame, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.data_tree = ttk.Treeview(self.data_frame, columns=(
            "id", "fname", "lname", "course", "mobile", "email", "gender", "dob", "country"),
                                      xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set, height=15)

        self.data_tree.column("id", width=50)
        self.data_tree.column("fname", width=150)
        self.data_tree.column("lname", width=150)
        self.data_tree.column("course", width=120)
        self.data_tree.column("mobile", width=100)
        self.data_tree.column("email", width=100)
        self.data_tree.column("gender", width=60)
        self.data_tree.column("dob", width=70)
        self.data_tree.column("country", width=100)
        self.data_tree.heading("id", text="ID")
        self.data_tree.heading("fname", text="First Name")
        self.data_tree.heading("lname", text="Last Name")
        self.data_tree.heading("course", text="Course")
        self.data_tree.heading("mobile", text="Mobile No.")
        self.data_tree.heading("email", text="Email")
        self.data_tree.heading("gender", text="Gender")
        self.data_tree.heading("dob", text="D.O.B")
        self.data_tree.heading("country", text="Country")
        self.data_tree["show"] = "headings"
        self.data_tree.pack()
        self.scroll_x.config(command=self.data_tree.xview)
        self.scroll_y.config(command=self.data_tree.yview)

        self.show_all_student()

    ## --------------------------------- QUERYS ---------------------- ##
    def show_course(self):
        qry = "SELECT course_name FROM course"
        all_course = self.my_db.show_data(qry)
        return all_course

    def show_course_in_combo(self):
        all_course = []
        for i in self.course:
            all_course.append(i)
        self.course_combo["values"] = all_course

    def all_student(self):
        qry = "SELECT * FROM students_info"
        all_student = self.my_db.show_data(qry)
        return all_student

    def search(self):
        qry = "SELECT id FROM students_info"
        all_id = self.my_db.show_data(qry)
        searched_value = self.search_entry.get()
        ids = []
        for i in all_id:
            ids.append(i[0])
        if int(searched_value) in ids:
            self.data_tree.delete(*self.data_tree.get_children())
            qry = "SELECT id, first_name,last_name,course,mobile,email,gender, dob, address, country FROM students_info WHERE id= %s"
            value = (int(searched_value),)
            data = self.my_db.show_data_from_p(qry, value)
            for i in data:
                self.data_tree.insert("", "end",
                                      values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
        else:
            messagebox.showerror("Notification", "No student found with that ID")

    def show_all_student(self):
        self.data_tree.delete(*self.data_tree.get_children())
        data = self.all_student()
        for i in data:
            self.data_tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))

    def sortby_fname(self):
        self.data_tree.delete(*self.data_tree.get_children())
        qry = "SELECT * FROM students_info ORDER BY first_name ASC"
        by_fname = self.my_db.show_data(qry)
        for i in by_fname:
            self.data_tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))

    def sortby_lname(self):
        self.data_tree.delete(*self.data_tree.get_children())
        qry = "SELECT * FROM students_info ORDER BY last_name ASC"
        by_lname = self.my_db.show_data(qry)
        for i in by_lname:
            self.data_tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))

    def sortby_course(self):
        if self.course_combo.get() == "Choose Course":
            messagebox.showerror("Notification", "Please select a course first!")
        else:
            self.data_tree.delete(*self.data_tree.get_children())
            qry = "SELECT * FROM students_info WHERE course = %s "
            value = (self.course_combo.get(),)
            by_course = self.my_db.show_data_from_p(qry, value)
            for i in by_course:
                self.data_tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))

    def cancel(self):
        self.detail_frame.destroy()
        self.window.switch_frame(Homepg)


###################################################################################################################################################### COURSE DETAILS
class Course_Details(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window
        self.detail_frame = Frame(self.window, bg="#f9fafc", relief=GROOVE, borderwidth=0)
        self.detail_frame.place(x=380, y=200, width=700, height=550)

        self.my_db = MyDb()
        self.all_usernames = self.show_username()

        ## ---------------------------- IMAGE ---------------------------- ##

        self.update_course_icon = PhotoImage(file="images/course.png")
        self.search_icon = PhotoImage(file="images/search.png")
        self.update_course_img = Label(self.detail_frame, bg="#f9fafc", image=self.update_course_icon)
        self.update_course_img.place(x=298, y=10)

        ## --------------------------------- Search ---------------------- ##
        self.search_icon = PhotoImage(file="images/search.png")
        self.search_label = Label(self.detail_frame, text="Search by ID", font=("comic sans ms", 12), bg="#f9fafc")
        self.search_label.place(x=540, y=120)
        self.search_var = StringVar()
        self.search_entry = Entry(self.detail_frame, font=("Arial", 15), relief=GROOVE, textvariable=self.search_var,
                                  width=5)
        self.search_entry.place(x=550, y=150)

        self.search_btn = Button(self.detail_frame, image=self.search_icon, bg="#f9fafc", bd=0, cursor="hand2",
                                 command=self.search)
        self.search_btn.place(x=625, y=150)

        ## --------------------------------- Buttons ---------------------- ##
        self.showall_course_btn = Button(self.detail_frame, text="Show All Course", command=self.show_all_course,
                                         cursor="hand2",
                                         font=("Arial", 10, "bold"),
                                         bd=1, padx=16)
        self.showall_course_btn.place(x=270, y=460)

        self.cancel_btn = Button(self.detail_frame, text="Cancel", relief="flat", bg="#f9fafc",
                                 cursor="hand2", font=("Arial", 10, "bold", "underline"),
                                 command=self.cancel,
                                 bd=1, padx=16)
        self.cancel_btn.place(x=298, y=490)

        ## --------------------------------- Sorting Method ---------------------- ##
        self.sortby_label = Label(self.detail_frame, text="Sort by:                   /", font=("comic sans ms", 12),
                                  bg="#f9fafc")
        self.sortby_label.place(x=30, y=165)

        self.firstname_btn = Button(self.detail_frame, text="Course Name", bg="#f9fafc", fg="blue", bd=0,
                                    cursor="hand2",
                                    command=self.sortby_cname, font=("comic sans ms", 10, "italic", "underline"))
        self.firstname_btn.place(x=100, y=165)

        self.lastname_btn = Button(self.detail_frame, text="Fee", bg="#f9fafc", fg="blue", bd=0, cursor="hand2",
                                   command=self.sortby_fee, font=("comic sans ms", 10, "italic", "underline"))
        self.lastname_btn.place(x=200, y=165)

        self.sort_btn = Button(self.detail_frame, text="Sort", bg="#f9fafc", fg="blue", bd=0, cursor="hand2",
                               command=self.sortby_username, font=("comic sans ms", 10, "italic", "underline"))
        self.sort_btn.place(x=400, y=165)

        self.user_combo = ttk.Combobox(self.detail_frame, state="readonly", width=17)
        self.user_combo.place(x=270, y=170)
        self.user_combo.set("Select Username")
        self.show_users_in_combo()

        ## ---------------------------- Tree View ---------------------------- ##
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("arial", 10, "bold"), foreground="#DC143C")
        self.data_frame = Frame(self.detail_frame, height=500, width=200)
        self.data_frame.place(x=30, y=200, width=620)
        self.scroll_x = Scrollbar(self.data_frame, orient=HORIZONTAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y = Scrollbar(self.data_frame, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.data_tree = ttk.Treeview(self.data_frame, columns=(
            "id", "name", "fee", "added_by", "description"), height=10, xscrollcommand=self.scroll_x.set,
                                      yscrollcommand=self.scroll_y.set)

        self.data_tree["show"] = "headings"
        self.data_tree.column("id", width=30)
        self.data_tree.column("name", width=150)
        self.data_tree.column("fee", width=100)
        self.data_tree.column("added_by", width=100)
        self.data_tree.column("description", width=300)
        self.data_tree.heading("id", text="ID")
        self.data_tree.heading("name", text="Name")
        self.data_tree.heading("fee", text="Fee")
        self.data_tree.heading("added_by", text="Added By")
        self.data_tree.heading("description", text="Description")
        self.data_tree.pack()
        self.scroll_x.config(command=self.data_tree.xview)
        self.scroll_y.config(command=self.data_tree.yview)

    def all_course(self):
        qry = "SELECT * FROM course"
        all_course = self.my_db.show_data(qry)
        return all_course

    def show_all_course(self):
        self.data_tree.delete(*self.data_tree.get_children())
        data = self.all_course()
        for i in data:
            self.data_tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4]))

    def show_username(self):
        qry = "SELECT username FROM users"
        all_usernames = self.my_db.show_data(qry)
        return all_usernames

    def show_users_in_combo(self):
        all_username = []
        for i in self.all_usernames:
            all_username.append(i)
        self.user_combo["values"] = all_username

    def search(self):
        qry = "SELECT id FROM students_info"
        all_id = self.my_db.show_data(qry)
        searched_value = self.search_entry.get()
        ids = []
        for i in all_id:
            ids.append(i[0])
        if int(searched_value) in ids:
            self.data_tree.delete(*self.data_tree.get_children())
            qry = "SELECT id, course_name, fee, added_by, description FROM course WHERE id= %s"
            value = (int(searched_value),)
            data = self.my_db.show_data_from_p(qry, value)
            for i in data:
                self.data_tree.insert("", "end",
                                      values=(i[0], i[1], i[2], i[3], i[4]))

        else:
            messagebox.showerror("Notification", "No course found with that ID")


    def sortby_cname(self):
        self.data_tree.delete(*self.data_tree.get_children())
        qry = "SELECT * FROM course ORDER BY course_name ASC"
        by_cname = self.my_db.show_data(qry)
        for i in by_cname:
            self.data_tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4]))

    def sortby_fee(self):
        self.data_tree.delete(*self.data_tree.get_children())
        qry = "SELECT * FROM course ORDER BY fee ASC"
        by_fee = self.my_db.show_data(qry)
        for i in by_fee:
            self.data_tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4]))

    def sortby_username(self):
        if self.user_combo.get() == "Select Username":
            messagebox.showerror("Notification", "Please select a course first!")
        else:
            self.data_tree.delete(*self.data_tree.get_children())
            qry = "SELECT * FROM course WHERE added_by = %s "
            value = (self.user_combo.get(),)
            by_username = self.my_db.show_data_from_p(qry, value)
            for i in by_username:
                self.data_tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4]))

    def cancel(self):
        self.detail_frame.destroy()
        self.window.switch_frame(Homepg)


###################################################################################################################################################### REFUND
class Refund(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window
        self.refund_frame = Frame(self.window, bg="#f9fafc", relief=GROOVE, borderwidth=0)
        self.refund_frame.place(x=420, y=150, width=570, height=600)

        self.my_db = MyDb()

        ## ---------------------------- IMAGE ---------------------------- ##
        self.refund_icon = PhotoImage(file="images/refund.png")
        self.search_icon = PhotoImage(file="images/search.png")
        self.refund_img = Label(self.refund_frame, bg="#f9fafc", image=self.refund_icon)
        self.refund_img.place(x=235, y=15)

        ## ---------------------------- LABEL ---------------------------- ##
        self.name_label = Label(self.refund_frame, text="Name:", font=("comic sans ms", 15,), bg="#f9fafc")
        self.name_label.place(x=30, y=200)

        self.course_label = Label(self.refund_frame, text="Course:", font=("comic sans ms", 15), bg="#f9fafc")
        self.course_label.place(x=275, y=200)

        self.info_label = Label(self.refund_frame, text="(Some amount of fee should be payed first!)",
                                font=("comic sans ms", 12), bg="#f9fafc", fg="grey")
        self.info_label.place(x=135, y=255)

        self.refund_deposit_label = Label(self.refund_frame, text="Refundable Amount", font=("comic sans ms", 15),
                                          bg="#f9fafc")
        self.refund_deposit_label.place(x=200, y=300)

        ## --------------------------------- Entry ---------------------- ##
        self.name_var = StringVar()
        self.course_var = StringVar()
        self.refund_var = StringVar()

        self.found_name = Entry(self.refund_frame, font=("Arial", 12), relief=GROOVE, textvariable=self.name_var,
                                width=15,
                                state=DISABLED)
        self.found_name.place(x=100, y=208)

        self.found_course = Entry(self.refund_frame, font=("Arial", 12), relief=GROOVE, textvariable=self.course_var,
                                  width=18,
                                  state=DISABLED)
        self.found_course.place(x=360, y=208)

        self.refund_amt = Entry(self.refund_frame, font=("Arial", 12), relief=GROOVE, textvariable=self.refund_var,
                                width=18,
                                state=DISABLED)
        self.refund_amt.place(x=207, y=345)

        ## --------------------------------- Buttons ---------------------- ##
        self.claim_btn = Button(self.refund_frame, text="Give Refund", command=self.claim, cursor="hand2",
                                font=("Arial", 10, "bold"), bd=1, padx=16)
        self.claim_btn.place(x=225, y=430)

        self.cancel_btn = Button(self.refund_frame, text="Cancel", relief="flat", bg="#f9fafc",
                                 cursor="hand2", font=("Arial", 10, "bold", "underline"),
                                 command=self.cancel,
                                 bd=1, padx=16)
        self.cancel_btn.place(x=245, y=460)

        ## --------------------------------- Search ---------------------- ##
        self.search_label = Label(self.refund_frame, text="Search by ID", font=("comic sans ms", 12), bg="#f9fafc")
        self.search_label.place(x=420, y=105)
        self.search_var = StringVar()
        self.search_entry = Entry(self.refund_frame, font=("Arial", 15), relief=GROOVE, textvariable=self.search_var,
                                  width=5)
        self.search_entry.place(x=430, y=140)

        self.search_btn = Button(self.refund_frame, image=self.search_icon, bg="#f9fafc", bd=0, cursor="hand2",
                                 command=self.search)
        self.search_btn.place(x=500, y=140)

    def search(self):
        qry = "SELECT id FROM students_info"
        all_id = self.my_db.show_data(qry)
        searched_value = self.search_entry.get()
        ids = []
        for i in all_id:
            ids.append(i[0])
        if int(searched_value) in ids:
            qry = "SELECT first_name, last_name, course FROM students_info WHERE id= %s"
            value = (int(searched_value),)
            data = self.my_db.show_data_from_p(qry, value)
            for i in data:
                self.name_var.set(i[0] + " " + i[1])
                self.course_var.set(i[2])

                qry2 = "SELECT refund FROM fee WHERE student_name = %s"
                value2 = (i[0] + " " + i[1],)
                refund = self.my_db.show_data_from_p(qry2, value2)
                self.refund_var.set(refund[0][0])

        else:
            messagebox.showerror("Notification", "Id does not match!")

    def claim(self):
        if self.refund_var.get() != 0:
            full_name = self.name_var.get()
            qry = "UPDATE fee SET refund = %s WHERE student_name =%s"
            value = (self.refund_var.get(), full_name)
            self.my_db.aur(qry, value)
            messagebox.showinfo("Notification", "Refunded successfully!")

        else:
            messagebox.showerror("Notification", "Refund already claimed!")

    def cancel(self):
        self.refund_frame.destroy()
        self.window.switch_frame(Homepg)


class Fee_History(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window
        self.detail_frame = Frame(self.window, bg="#f9fafc", relief=GROOVE, borderwidth=0)
        self.detail_frame.place(x=320, y=150, width=850, height=620)

        self.my_db = MyDb()

        ## ---------------------------------IMAGES  ---------------------- ##

        self.fee_icon = PhotoImage(file="images/fee1.png")
        self.search_icon = PhotoImage(file="images/search.png")
        self.pay_fee_img = Label(self.detail_frame, bg="#f9fafc", image=self.fee_icon)
        self.pay_fee_img.place(x=360, y=10)

        ## --------------------------------- Search ---------------------- ##
        self.search_icon = PhotoImage(file="images/search.png")
        self.search_label = Label(self.detail_frame, text="Search by ID", font=("comic sans ms", 12), bg="#f9fafc")
        self.search_label.place(x=655, y=120)
        self.search_var = StringVar()
        self.search_entry = Entry(self.detail_frame, font=("Arial", 15), relief=GROOVE, textvariable=self.search_var,
                                  width=5)
        self.search_entry.place(x=665, y=150)

        self.search_btn = Button(self.detail_frame, image=self.search_icon, bg="#f9fafc", bd=0, cursor="hand2",
                                 command=self.search)
        self.search_btn.place(x=745, y=150)

        ## --------------------------------- Buttons ---------------------- ##
        self.refresh_course_btn = Button(self.detail_frame, text="Refresh Data", command=self.refresh,
                                         cursor="hand2",
                                         font=("Arial", 10, "bold"),
                                         bd=1, padx=16)
        self.refresh_course_btn.place(x=360, y=550)

        self.cancel_btn = Button(self.detail_frame, text="Cancel", relief="flat", bg="#f9fafc",
                                 cursor="hand2", font=("Arial", 10, "bold", "underline"),
                                 command=self.cancel,
                                 bd=1, padx=16)
        self.cancel_btn.place(x=378, y=580)

        ## --------------------------------- Sorting Method ---------------------- ##
        self.sortby_label = Label(self.detail_frame, text="Sort by:         /", font=("comic sans ms", 12),
                                  bg="#f9fafc")
        self.sortby_label.place(x=30, y=155)

        self.name_btn = Button(self.detail_frame, text="Name", bg="#f9fafc", fg="blue", bd=0,
                               cursor="hand2",
                               command=self.sortby_name, font=("comic sans ms", 10, "italic", "underline"))
        self.name_btn.place(x=100, y=155)

        self.date_paid_btn = Button(self.detail_frame, text="Date Paid", bg="#f9fafc", fg="blue", bd=0, cursor="hand2",
                                    command=self.sortby_date, font=("comic sans ms", 10, "italic", "underline"))
        self.date_paid_btn.place(x=150, y=155)

        ## --------------------------------- TreeView ---------------------- ##
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("arial", 10, "bold"), foreground="#DC143C")
        self.data_frame = Frame(self.detail_frame, height=430, width=320)
        self.data_frame.place(x=30, y=195, width=775)
        self.scroll_x = Scrollbar(self.data_frame, orient=HORIZONTAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y = Scrollbar(self.data_frame, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.data_tree = ttk.Treeview(self.data_frame, columns=(
            "student_name", "course", "date_paid", "course_fee", "amount_paid", "remaining_due", "mobile",
            "payment_method"),
                                      xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set, height=15)

        self.data_tree["show"] = "headings"
        self.data_tree.column("student_name", width=150)
        self.data_tree.column("course", width=150)
        self.data_tree.column("date_paid", width=100)
        self.data_tree.column("course_fee", width=100)
        self.data_tree.column("amount_paid", width=100)
        self.data_tree.column("remaining_due", width=120)
        self.data_tree.column("mobile", width=100)
        self.data_tree.column("payment_method", width=120)
        self.data_tree.heading("student_name", text="Student Name")
        self.data_tree.heading("course", text="Course")
        self.data_tree.heading("mobile", text="Mobile")
        self.data_tree.heading("course_fee", text="Course Fee")
        self.data_tree.heading("amount_paid", text="Amount_Paid")
        self.data_tree.heading("remaining_due", text="Remaining Due")
        self.data_tree.heading("date_paid", text="Date Paid")
        self.data_tree.heading("payment_method", text="Payment Method")
        self.data_tree.pack()
        self.scroll_x.config(command=self.data_tree.xview)
        self.scroll_y.config(command=self.data_tree.yview)
        self.show_all_history()

    def all_history(self):
        qry = "SELECT * FROM fee"
        all_course = self.my_db.show_data(qry)
        return all_course

    def show_all_history(self):
        self.data_tree.delete(*self.data_tree.get_children())
        data = self.all_history()
        for i in data:
            self.data_tree.insert("", "end", values=(i[1], i[2], i[7], i[4], i[5], i[6], i[3], i[8]))

    def search(self):
        qry = "SELECT id FROM students_info"
        all_id = self.my_db.show_data(qry)
        searched_value = self.search_entry.get()
        ids = []
        for i in all_id:
            ids.append(i[0])
        if int(searched_value) in ids:
            self.data_tree.delete(*self.data_tree.get_children())
            qry = "SELECT first_name,last_name FROM students_info WHERE id= %s"
            value = (int(searched_value),)
            data = self.my_db.show_data_from_p(qry, value)
            for i in data:
                full_name = (i[0] + " " + i[1])

            qry2 = "SELECT * FROM fee WHERE student_name = %s"
            value2 = (full_name,)
            data = self.my_db.show_data_from_p(qry2, value2)
            for i in data:
                self.data_tree.insert("", "end", values=(i[1], i[2], i[7], i[4], i[5], i[6], i[3], i[8]))

        else:
            messagebox.showerror("Notification", "No student found with that ID")

    def refresh(self):
        self.data_tree.delete(*self.data_tree.get_children())
        data = self.all_history()
        for i in data:
            self.data_tree.insert("", "end", values=(i[1], i[2], i[7], i[4], i[5], i[6], i[3], i[8]))

    def cancel(self):
        self.detail_frame.destroy()
        self.window.switch_frame(Homepg)

    def sortby_name(self):
        self.data_tree.delete(*self.data_tree.get_children())
        qry = "SELECT * FROM fee ORDER BY student_name ASC"
        by_name = self.my_db.show_data(qry)
        for i in by_name:
            self.data_tree.insert("", "end", values=(i[1], i[2], i[7], i[4], i[5], i[6], i[3], i[8]))

    def sortby_date(self):
        self.data_tree.delete(*self.data_tree.get_children())
        qry = "SELECT * FROM fee ORDER BY date_paid ASC"
        by_date = self.my_db.show_data(qry)
        for i in by_date:
            self.data_tree.insert("", "end", values=(i[1], i[2], i[7], i[4], i[5], i[6], i[3], i[8]))



run = Main()
run.mainloop()

from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE, font=("times new roman", 40, "bold"), bg="#FF69B4", fg="blue")
        title.pack(side=TOP, fill=X)

        #====All Variables====
        self.Roll_NO_var = StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.contact_var = StringVar()
        self.Dob_var = StringVar()
        self.Address_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # === Manage Frame ====
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#696969")
        Manage_Frame.place(x=20, y=100, width=450, height=580)

        m_title = Label(Manage_Frame, text="Manage Students", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll No.", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_NO_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame, textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame, textvariable=self.Email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.Gender_var, font=("times new roman", 13, "bold"), state="readonly")
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, padx=20, pady=10)

        lbl_Contact = Label(Manage_Frame, text="Contact", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_DOB = Label(Manage_Frame, text="D.O.B", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_DOB = Entry(Manage_Frame, textvariable=self.Dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_Address = Text(Manage_Frame, width=30, height=4, font=("times new roman", 10))
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # ===== Button Frame ======
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="blue")
        btn_Frame.place(x=15, y=500, width=420)

        Addbtn = Button(btn_Frame, text="Add", width=10, command=self.add_students)
        Addbtn.grid(row=0, column=0, padx=10, pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=10, command=self.update_data)
        updatebtn.grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10, command=self.delete_data)
        deletebtn.grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_Frame, text="Clear", width=10, command=self.clear)
        clearbtn.grid(row=0, column=3, padx=10, pady=10)

        # === Detail Frame ====
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#696969")
        Detail_Frame.place(x=500, y=100, width=800, height=580)

        lbl_search = Label(Detail_Frame, text="Search By", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=10, font=("times new roman", 13, "bold"), state="readonly")
        combo_search['values'] = ("Roll_No", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_Search = Entry(Detail_Frame, textvariable=self.search_txt, width=20, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchbtn = Button(Detail_Frame, text="Search", width=10, pady=5, command=self.search_data)
        Searchbtn.grid(row=0, column=3, padx=10, pady=10)
        Showallbtn = Button(Detail_Frame, text="Show All", width=10, pady=5, command=self.fetch_data)
        Showallbtn.grid(row=0, column=4, padx=10, pady=10)

        # ===== Table Frame =====
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        Scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        Scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame, columns=("roll", "name", "email", "gender", "contact", "dob", "address"), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_x.config(command=self.Student_table.xview)
        Scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll", text="Roll No.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("address", text="Address")
        self.Student_table['show'] = 'headings'
        self.Student_table.pack(fill=BOTH, expand=1)

        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=150)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()  # Load data into the table when the application starts

    def add_students(self):
        if self.Roll_NO_var.get()=="" or self.Name_var.get()=="":
            messagebox.showerror("Error","All fields are required !!!")
        else:    
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (
            self.Roll_NO_var.get(),
            self.Name_var.get(),
            self.Email_var.get(),
            self.Gender_var.get(),
            self.contact_var.get(),
            self.Dob_var.get(),
            self.txt_Address.get('1.0', END).strip()  # Remove trailing newlines
            ))
            con.commit()
            con.close()
            self.clear()
            self.fetch_data()  # Refresh table after adding student
            messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())  # Corrected table reference
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_NO_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.contact_var.set("")
        self.Dob_var.set("")
        self.txt_Address.delete("1.0", END)
    
    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_NO_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.Dob_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()  
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s", (
            self.Name_var.get(),
            self.Email_var.get(),
            self.Gender_var.get(),
            self.contact_var.get(),
            self.Dob_var.get(),
            self.txt_Address.get('1.0', END).strip(),  # Remove trailing newlines
            self.Roll_NO_var.get()
        ))
        con.commit()
        con.close()
        self.fetch_data()  # Refresh table after updating student
        self.clear()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("delete from students where roll_no = %s", self.Roll_NO_var.get())
        con.commit()
        con.close()
        self.fetch_data()  # Refresh table after deleting student
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("SELECT * FROM students WHERE " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()
        

root = Tk()
ob = Student(root)
root.mainloop()

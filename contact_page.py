from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class ContactPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1290x570+240+220")
        
        # Title
        lbl_title = Label(self.root, text="Hotel Management System", font=("Algerian", 20), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.pack(fill=X)
        
        #================Left Frame for Contact Us================
        LabelFrameleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Contact Us", font=("Times New Roman", 12, "bold"), padx=2)
        LabelFrameleft.place(x=5, y=50, width=540, height=350)

        # Username
        lbl_username = Label(LabelFrameleft, text="Username:", font=("Times New Roman", 12))
        lbl_username.grid(row=0, column=0, sticky=W)
        
        self.var_username = StringVar()
        entry_username = ttk.Entry(LabelFrameleft, textvariable=self.var_username, font=("Arial", 12))
        entry_username.grid(row=0, column=1, padx=10, pady=5)

        # Email
        lbl_email = Label(LabelFrameleft, text="Email ID:", font=("Times New Roman", 12))
        lbl_email.grid(row=1, column=0, sticky=W)
        
        self.var_email = StringVar()
        entry_email = ttk.Entry(LabelFrameleft, textvariable=self.var_email, font=("Arial", 12))
        entry_email.grid(row=1, column=1, padx=10, pady=5)

        # Contact Number
        lbl_contact_no = Label(LabelFrameleft, text="Contact No.:", font=("Times New Roman", 12))
        lbl_contact_no.grid(row=2, column=0, sticky=W)
        
        self.var_contact_no = StringVar()
        entry_contact_no = ttk.Entry(LabelFrameleft, textvariable=self.var_contact_no, font=("Arial", 12))
        entry_contact_no.grid(row=2, column=1, padx=10, pady=5)

        # Problem Description
        lbl_problem = Label(LabelFrameleft, text="Problem Description:", font=("Times New Roman", 12))
        lbl_problem.grid(row=3, column=0, sticky=W)
        
        self.txt_problem = Text(LabelFrameleft, height=5, width=30, font=("Arial", 12))
        self.txt_problem.grid(row=3, column=1, padx=10, pady=5)

        # Submit Button
        btn_submit = Button(LabelFrameleft, text="Submit", command=self.submit, font=("Arial", 12, "bold"), bg="black", fg="gold")
        btn_submit.grid(row=4, column=1, pady=10, sticky=E)
        
        #================Right Frame for Room Details================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show problem", font=("Times New Roman", 12, "bold"), padx=2)
        Table_Frame.place(x=600, y=55, width=600, height=350)

        # Scrollbar for the table
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        
        self.room_Table = ttk.Treeview(Table_Frame, columns=("username", "email", "contact_no","problem"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        # Room Table Setup
        self.room_Table.heading("username", text="Username")
        self.room_Table.heading("email", text="Email")
        self.room_Table.heading("contact_no", text="Contact Number")
        self.room_Table.heading("problem", text="Problem Description")
        self.room_Table["show"] = "headings"
        
        self.room_Table.column("username", width=100)
        self.room_Table.column("email", width=100)
        self.room_Table.column("contact_no", width=100)
        self.room_Table.column("problem", width=100)
        
        self.room_Table.pack(fill=BOTH, expand=1)
        self.room_Table.bind("<ButtonRelease-1>", self.get_cursor)

        # Fetch Room Data
        self.fetch_data()

    def submit(self):
        username = self.var_username.get()
        email = self.var_email.get()
        contact_no = self.var_contact_no.get()
        problem = self.txt_problem.get("1.0", END).strip()

        if username == "" or email == "" or contact_no == "" or problem == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # Connect to MySQL database
                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Shivam@7177",
                    database="management"
                )
                cursor = db.cursor()

                # Insert data into the contacts table
                cursor.execute("""
                    INSERT INTO contacts (username, email, contact_no, problem)
                    VALUES (%s, %s, %s, %s)
                """, (username, email, contact_no, problem))

                db.commit()

                messagebox.showinfo("Success", "Your message has been submitted successfully", parent=self.root)
                self.reset()

                cursor.close()
                db.close()

            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {str(err)}", parent=self.root)

    def reset(self):
        self.var_username.set("")
        self.var_email.set("")
        self.var_contact_no.set("")
        self.txt_problem.delete("1.0", END)

    def fetch_data(self):
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Shivam@7177",
                database="management"
            )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM contacts")
            rows = cursor.fetchall()
            if rows:
                self.room_Table.delete(*self.room_Table.get_children())  # Clear the table before inserting new data
                for row in rows:
                    self.room_Table.insert("", END, values=row)
            cursor.close()
            db.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {str(err)}", parent=self.root)

    def get_cursor(self, event):
        cursor_row = self.room_Table.focus()
        content = self.room_Table.item(cursor_row)
        row = content['values']  # You can process the selected row as needed

if __name__ == "__main__":
    root = Tk()
    app = ContactPage(root)
    root.mainloop()

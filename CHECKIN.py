from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from tkinter import simpledialog
import os

class CheckOutWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Check-Out")
        self.root.geometry("1290x570+240+220")

        #=============Image dimensions==============
        img_height = 50
        
        # Title Label at the top
        lbl_title = Label(self.root, text="Hotel Check Out Details", font=("Algerian", 25), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=100, y=0, width=1180, height=50)  # Adjust width for title after logo

        #=================logo img ==================
        img2 = Image.open(r"C:/Users/shiva/OneDrive/Desktop/MINI PROJECT/logo.png")
        img2 = img2.resize((100, img_height), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=100, height=img_height)

        # Frame for Search and Hotel Details - Positioned below the Title Label at the top
        self.frame_top = Frame(self.root, bd=4, relief=RIDGE, padx=10,bg="lightblue")
        self.frame_top.place(relx=0.5, y=50,anchor="n", width=1280, height=100)  # Positioned below the title (y=50)

        # Configure the frame's grid layout for centering
        self.frame_top.grid_columnconfigure(0, weight=1)  # Left empty space
        self.frame_top.grid_columnconfigure(1, weight=0)  # Actual content
        self.frame_top.grid_columnconfigure(2, weight=0)  # Actual content
        self.frame_top.grid_columnconfigure(3, weight=0)  # Actual content
        self.frame_top.grid_columnconfigure(4, weight=1)  # Right empty space

        # Search Section inside the Frame
        lbl_search = Label(self.frame_top, text="Search CheckIn Details", font=("times new roman", 12, "bold"))
        lbl_search.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky=W)

        lbl_contact = Label(self.frame_top, text="Contact", font=("arial", 10))
        lbl_contact.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        self.entry_contact = Entry(self.frame_top, font=("arial", 10), width=30)
        self.entry_contact.grid(row=1, column=2, padx=5, pady=5)

        btn_search = Button(self.frame_top, text="Search", font=("arial", 10, "bold"), bg="green", fg="white", command=self.search_details)
        btn_search.grid(row=1, column=3, padx=5, pady=5)



        # Left Frame for Check-In Details
        self.frame_left = Frame(self.root, bd=4, relief=RIDGE, padx=10)
        self.frame_left.place(x=0, y=150, width=400, height=410)

        lbl_checkin = Label(self.frame_left, text="Check In Details", font=("times new roman", 18, "bold"))
        lbl_checkin.grid(row=0, column=0, columnspan=2, pady=10)

        lbl_invoice = Label(self.frame_left, text="Invoice No.", font=("arial", 12))
        lbl_invoice.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.entry_invoice = Entry(self.frame_left, font=("arial", 12), width=20)
        self.entry_invoice.grid(row=1, column=1, padx=10, pady=5)

        lbl_name = Label(self.frame_left, text="Name", font=("arial", 12))
        lbl_name.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.entry_name = Entry(self.frame_left, font=("arial", 12), width=20)
        self.entry_name.grid(row=2, column=1, padx=10, pady=5)

        lbl_contact_no = Label(self.frame_left, text="Contact No.", font=("arial", 12))
        lbl_contact_no.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.entry_contact_no = Entry(self.frame_left, font=("arial", 12), width=20)
        self.entry_contact_no.grid(row=3, column=1, padx=10, pady=5)

        lbl_room_no = Label(self.frame_left, text="Room No.", font=("arial", 12))
        lbl_room_no.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        self.entry_room_no = Entry(self.frame_left, font=("arial", 12), width=20)
        self.entry_room_no.grid(row=4, column=1, padx=10, pady=5)

        lbl_checkin_date = Label(self.frame_left, text="Check In", font=("arial", 12))
        lbl_checkin_date.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        self.entry_checkin_date = Entry(self.frame_left, font=("arial", 12), width=20)
        self.entry_checkin_date.grid(row=5, column=1, padx=10, pady=5)

        lbl_checkout_date = Label(self.frame_left, text="Check Out", font=("arial", 12))
        lbl_checkout_date.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        self.entry_checkout_date = Entry(self.frame_left, font=("arial", 12), width=20)
        self.entry_checkout_date.grid(row=6, column=1, padx=10, pady=5)

        lbl_total_bill = Label(self.frame_left, text="Total Bill", font=("arial", 12))
        lbl_total_bill.grid(row=7, column=0, padx=10, pady=5, sticky=W)
        self.entry_total_bill = Entry(self.frame_left, font=("arial", 12), width=20)
        self.entry_total_bill.grid(row=7, column=1, padx=10, pady=5)

        lbl_advance = Label(self.frame_left, text="Advance", font=("arial", 12))
        lbl_advance.grid(row=8, column=0, padx=10, pady=5, sticky=W)
        self.entry_advance = Entry(self.frame_left, font=("arial", 12), width=20)
        self.entry_advance.grid(row=8, column=1, padx=10, pady=5)

        lbl_balance = Label(self.frame_left, text="Balance", font=("arial", 12))
        lbl_balance.grid(row=9, column=0, padx=10, pady=5, sticky=W)
        self.entry_balance = Entry(self.frame_left, font=("arial", 12), width=20)
        self.entry_balance.grid(row=9, column=1, padx=10, pady=5)

        # Buttons
        btn_checkout = Button(self.frame_left, text="Check Out", font=("arial", 12, "bold"), bg="black", fg="gold", command=self.check_out)
        btn_checkout.grid(row=10, column=0, padx=10, pady=10)

        btn_clear = Button(self.frame_left, text="Clear", font=("arial", 12, "bold"),bg="black", fg="gold", command=self.clear_fields)
        btn_clear.grid(row=10, column=1, padx=10, pady=10)

        btn_print = Button(self.frame_left, text="Print", font=("arial", 12, "bold"),bg="black", fg="gold", command=self.print_invoice)
        btn_print.grid(row=10, column=2, padx=10, pady=10)

        # Right Frame for Invoice and Hotel Info
        self.frame_right = Frame(self.root, bd=4, relief=RIDGE, padx=10)
        self.frame_right.place(x=400, y=150, width=450, height=410)

        self.lbl_hotel_name = Label(self.frame_right, text="Aditi hotel", font=("times new roman", 18, "bold"))
        self.lbl_hotel_name.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.lbl_address = Label(self.frame_right, text="Address: plot no. 585, badlapr (e)", font=("arial", 12))
        self.lbl_address.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

        self.lbl_contact_info = Label(self.frame_right, text="Contact: 0000000000", font=("arial", 12))
        self.lbl_contact_info.grid(row=2, column=0, padx=10, pady=5, columnspan=2)

        self.lbl_invoice_info = Label(self.frame_right, text="Invoice No.:", font=("arial", 12))
        self.lbl_invoice_info.grid(row=3, column=0, padx=10, pady=5)
        self.lbl_invoice_number = Label(self.frame_right, text="", font=("arial", 12))
        self.lbl_invoice_number.grid(row=3, column=1, padx=10, pady=5)

        self.lbl_issue_date = Label(self.frame_right, text="Issue Date:", font=("arial", 12))
        self.lbl_issue_date.grid(row=4, column=0, padx=10, pady=5)
        self.lbl_issue_date_value = Label(self.frame_right, text="", font=("arial", 12))
        self.lbl_issue_date_value.grid(row=4, column=1, padx=10, pady=5)

        self.lbl_customer_details = Label(self.frame_right, text="Customer Details", font=("times new roman", 15, "bold"))
        self.lbl_customer_details.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

        self.lbl_customer_name = Label(self.frame_right, text="Name:", font=("arial", 12))
        self.lbl_customer_name.grid(row=6, column=0, padx=10, pady=5)
        self.lbl_customer_name_value = Label(self.frame_right, text="", font=("arial", 12))
        self.lbl_customer_name_value.grid(row=6, column=1, padx=10, pady=5)

        self.lbl_customer_checkin = Label(self.frame_right, text="CheckIn:", font=("arial", 12))
        self.lbl_customer_checkin.grid(row=7, column=0, padx=10, pady=5)
        self.lbl_customer_checkin_value = Label(self.frame_right, text="", font=("arial", 12))
        self.lbl_customer_checkin_value.grid(row=7, column=1, padx=10, pady=5)

        self.lbl_customer_days = Label(self.frame_right, text="Days:", font=("arial", 12))
        self.lbl_customer_days.grid(row=8, column=0, padx=10, pady=5)
        self.lbl_customer_days_value = Label(self.frame_right, text="", font=("arial", 12))
        self.lbl_customer_days_value.grid(row=8, column=1, padx=10, pady=5)

    def search_details(self):
        contact = self.entry_contact.get()
        if contact:
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Shivam@7177",
                    database="management"
                )
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM room WHERE Contact= %s", (contact,))
                result = cursor.fetchone()
                if result:
                    self.entry_invoice.insert(0, result[0])
                    self.entry_name.insert(0, result[1])
                    self.entry_contact_no.insert(0, result[2])
                    self.entry_room_no.insert(0, result[3])
                    self.entry_checkin_date.insert(0, result[4])
                    self.entry_checkout_date.insert(0, result[5])
                    self.entry_total_bill.insert(0, result[6])
                    self.entry_advance.insert(0, result[7])
                    self.entry_balance.insert(0, result[8])
                else:
                    messagebox.showerror("Error", "No record found.")
                cursor.close()
                connection.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")
        else:
            messagebox.showwarning("Input Error", "Please enter contact number.")

    def check_out(self):
        invoice = self.entry_invoice.get()
        name = self.entry_name.get()
        checkin_date = self.entry_checkin_date.get()
        days = self.calculate_days(self.entry_checkin_date.get(), self.entry_checkout_date.get())
        
        # Update right frame with details
        self.lbl_invoice_number.config(text=invoice)
        self.lbl_issue_date_value.config(text="09-09-2024")  # You might want to generate or fetch this date dynamically
        self.lbl_customer_name_value.config(text=name)
        self.lbl_customer_checkin_value.config(text=checkin_date)
        self.lbl_customer_days_value.config(text=days)
    
    def calculate_days(self, checkin, checkout):
        # Simple calculation, might need to be improved based on date format
        from datetime import datetime
        checkin_date = datetime.strptime(checkin, "%d-%m-%Y")
        checkout_date = datetime.strptime(checkout, "%d-%m-%Y")
        delta = checkout_date - checkin_date
        return delta.days

    def clear_fields(self):
        self.entry_invoice.delete(0, END)
        self.entry_name.delete(0, END)
        self.entry_contact_no.delete(0, END)
        self.entry_room_no.delete(0, END)
        self.entry_checkin_date.delete(0, END)
        self.entry_checkout_date.delete(0, END)
        self.entry_total_bill.delete(0, END)
        self.entry_advance.delete(0, END)
        self.entry_balance.delete(0, END)
        self.entry_contact.delete(0, END)

        self.lbl_invoice_number.config(text="")
        self.lbl_issue_date_value.config(text="")
        self.lbl_customer_name_value.config(text="")
        self.lbl_customer_checkin_value.config(text="")
        self.lbl_customer_days_value.config(text="")

    def print_invoice(self):
        messagebox.showinfo("Print", "Print functionality is not implemented.")

if __name__ == "__main__":
    root = Tk()
    app = CheckOutWindow(root)
    root.mainloop()

from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from CUSTOMER import Cust_win 
from room import roombooking
from details import Detailsrooms
from contact_page import ContactPage
from aboutus import AboutPage


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # Image dimensions
        img_height = 150
        img_height1 = 590

        #==================1st img ===================
        img1 = Image.open(r"C:/Users/shiva/OneDrive/Desktop/MINI PROJECT/hotel_pic1.png")
        img1 = img1.resize((1300, img_height), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg1.place(x=250, y=0, width=1300, height=img_height)

        #=================logo img ==================
        img2 = Image.open(r"C:/Users/shiva/OneDrive/Desktop/MINI PROJECT/logo.png")
        img2 = img2.resize((250, img_height), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=250, height=img_height)

        # ============title================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("Algerian",25),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=150,width=1550,height=50)

        #==============main fram============
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        
        #=================menu===============
        lbl_menu=Label(main_frame,text="MENU",font=("Times New Roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=250)
        
        #==============btn fram============
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=251,height=550)
        
        cust_btn=Button(master=btn_frame,text="CUSTOMER",command=self.cust_detsils,width=18,font=("Times New Roman",18,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=1,column=0,pady=1)
        
        room_btn=Button(btn_frame,text="ROOM",command=self.room_booking,width=18,font=("Times New Roman",18,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=2,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=18,font=("Times New Roman",18,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        details_btn.grid(row=3,column=0,pady=1)
        
        #checkin_btn=Button(btn_frame,text="CHECK - IN",width=18,font=("Times New Roman",18,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        #checkin_btn.grid(row=4,column=0,pady=1)
        
        #checkout_btn=Button(btn_frame,text="CHECK - OUT",width=18,font=("Times New Roman",18,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        #checkout_btn.grid(row=5,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="CONTACT US",command=self.contact_pages,width=18,font=("Times New Roman",18,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        report_btn.grid(row=6,column=0,pady=1)
        
        about_btn=Button(btn_frame,text="ABOUT US",command=self.about_us,width=18,font=("Times New Roman",18,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        about_btn.grid(row=7,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LOG-OUT",width=18,font=("Times New Roman",18,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        logout_btn.grid(row=8,column=0,pady=1)
        
        #=======================right side img=================
        img3 = Image.open(r"C:/Users/shiva/OneDrive/Desktop/MINI PROJECT/hotel.png")
        img3 = img3.resize((1310, img_height1), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=240, y=0, width=1280, height=img_height1)
        
    def cust_detsils(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)
        
    
    def room_booking(self):
        self.new_window=Toplevel(self.root)
        self.app=roombooking(self.new_window)
        
    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=Detailsrooms(self.new_window)
        
    def contact_pages(self):
        self.new_window=Toplevel(self.root)
        self.app=ContactPage(self.new_window)
        
    def about_us(self):
        self.new_window=Toplevel(self.root)
        self.app=AboutPage(self.new_window)
        
            
if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()

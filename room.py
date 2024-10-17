from tkinter import*
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1290x570+240+220")
        
        
        #=============variable==========
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        self.var_meal=StringVar()
        
        
        
        #=============Image dimensions==============
        img_height = 50
        img_height1 = 590
        
        #===============title==============
        lbl_title=Label(self.root,text="ROOM-BOOKING DETAILS",font=("Algerian",25),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
        #=================logo img ==================
        img2 = Image.open(r"C:/Users/shiva/OneDrive/Desktop/MINI PROJECT/logo.png")
        img2 = img2.resize((100, img_height), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=100, height=img_height)
        
        #================lable fram=============
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM-BOOKING DEATILS",font=("Times New Roman",12,"bold"),padx=2)
        LabelFrameleft.place(x=5,y=50,width=425,height=510)
        
        #====================labels and entrys============
        #==============contact ================
        lbl_cust_contact=Label(LabelFrameleft,text="Customer Contact : ",font=("Times New Roman",13,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        entry_contact=ttk.Entry(LabelFrameleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)
        
        #=========fetch data
        btnFetchData=Button(LabelFrameleft,command=self.Fecth_contact,text="Fetch Data",font=("arial",9,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)
        
        #============check in ============
        check_in_data=Label(LabelFrameleft,font=("arial",12,"bold"),text="Check-in Data : ",padx=2,pady=6)
        check_in_data.grid(row=1,column=0,sticky=W)
        txtcheck_in_data=ttk.Entry(LabelFrameleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
        txtcheck_in_data.grid(row=1,column=1)
        
        #============check Outt ============
        check_Out_data=Label(LabelFrameleft,font=("arial",12,"bold"),text="Check-Out Data : ",padx=2,pady=6)
        check_Out_data.grid(row=2,column=0,sticky=W)
        txtcheck_Out_data=ttk.Entry(LabelFrameleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
        txtcheck_Out_data.grid(row=2,column=1)
        
        #===========room type combobox==========
        label_RoomType=Label(LabelFrameleft,font=("arial",12,"bold"),text="Room Type : ",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ids=my_cursor.fetchall()
        
        combo_RoomType=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=ids
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)
        
        #============Available Room ============
        lblRoomAvailable=Label(LabelFrameleft,font=("arial",12,"bold"),text="Room available : ",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        #txtRoomAvailable=ttk.Entry(LabelFrameleft,textvariable=self.var_roomavailable,width=29,font=("arial",13,"bold"))
        #txtRoomAvailable.grid(row=4,column=1)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()
        
        combo_Roomno=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Roomno["value"]=rows
        combo_Roomno.current(0)
        combo_Roomno.grid(row=4,column=1)
        
        #============Meal ============
        lblMeal=Label(LabelFrameleft,font=("arial",12,"bold"),text="Meal : ",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(LabelFrameleft,textvariable=self.var_meal,width=29,font=("arial",13,"bold"))
        txtMeal.grid(row=5,column=1)
        
        #============No of Days ============
        lblNoofDays=Label(LabelFrameleft,font=("arial",12,"bold"),text="No of Days : ",padx=2,pady=6)
        lblNoofDays.grid(row=6,column=0,sticky=W)
        txtNoofDays=ttk.Entry(LabelFrameleft,textvariable=self.var_noofdays,width=29,font=("arial",13,"bold"))
        txtNoofDays.grid(row=6,column=1)
        
        #============Paid Tax ============
        lblNoofDays=Label(LabelFrameleft,font=("arial",12,"bold"),text="Paid Tax : ",padx=2,pady=6)
        lblNoofDays.grid(row=7,column=0,sticky=W)
        txtNoofDays=ttk.Entry(LabelFrameleft,textvariable=self.var_paidtax,width=29,font=("arial",13,"bold"))
        txtNoofDays.grid(row=7,column=1)
        
        #============Sub Total ============
        lblNoofDays=Label(LabelFrameleft,font=("arial",12,"bold"),text="Sub Total : ",padx=2,pady=6)
        lblNoofDays.grid(row=8,column=0,sticky=W)
        txtNoofDays=ttk.Entry(LabelFrameleft,textvariable=self.var_actualtotal,width=29,font=("arial",13,"bold"))
        txtNoofDays.grid(row=8,column=1)
        
        #======Total Cost==============
        lblIDNumder=Label(LabelFrameleft,font=("arial",12,"bold"),text="Total Cost : ",padx=2,pady=6)
        lblIDNumder.grid(row=9,column=0,sticky=W)
        txtIDNumder=ttk.Entry(LabelFrameleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
        txtIDNumder.grid(row=9,column=1)
        
        #=============bill btn=========
        btnBill=Button(LabelFrameleft,text="BILL",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)
        
        #======================btns================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=430,width=412,height=40)
        
        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="DELETE",command=self.mdelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)
        
        
        #================Right side img==============
        img3 = Image.open(r"C:/Users/shiva/OneDrive\Desktop/MINI PROJECT/img3.png")
        img3 = img3.resize((520,300), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root,image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=215)
        
        
        
        #================table fram search system===============
        Table_Fram=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW DEATILS AND SEARCH SYSTEM",font=("Times New Roman",12,"bold"),padx=2)
        Table_Fram.place(x=435,y=280,width=860,height=260)
        
        lblSEarchBy=Label(Table_Fram,font=("arial",12,"bold"),text="Search By : ",bg="red",fg="white")
        lblSEarchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_Serach=ttk.Combobox(Table_Fram,textvariable=self.search_var,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Serach["value"]=("Contact", "Room")
        combo_Serach.current(0)
        combo_Serach.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSerach=ttk.Entry(Table_Fram,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtSerach.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Table_Fram,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShowAll=Button(Table_Fram,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)
        
        
        #=======================Show data table ===============
        details_table=Frame(Table_Fram,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=850,height=195)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.room_Table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","AvailableRoom","Meal","NoofDays",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)
        
        self.room_Table.heading("contact",text="contact No")
        self.room_Table.heading("checkin",text="check-in")
        self.room_Table.heading("checkout",text="check-out")
        self.room_Table.heading("roomtype",text="room type")
        self.room_Table.heading("AvailableRoom",text="Available Room")
        self.room_Table.heading("Meal",text="Meal")
        self.room_Table.heading("NoofDays",text="No of Days")
        
        
        self.room_Table["show"]="headings"
        
        self.room_Table.column("contact",width=100)
        self.room_Table.column("checkin",width=100)
        self.room_Table.column("checkout",width=100)
        self.room_Table.column("roomtype",width=100)
        self.room_Table.column("AvailableRoom",width=100)
        self.room_Table.column("Meal",width=100)
        self.room_Table.column("NoofDays",width=100)
        self.room_Table.pack(fill=BOTH,expand=1)

        self.room_Table.bind("<ButtonRelease -1>", self.get_cuersor)
        self.fetch_data()
    
    
    
    #========================add btn==========
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_contact.get(),
                                                                            self.var_checkin.get(),
                                                                            self.var_checkout.get(),
                                                                            self.var_roomtype.get(),
                                                                            self.var_roomavailable.get(),
                                                                            self.var_noofdays.get(),
                                                                            self.var_meal.get()
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went is wrong:{str(es)}",parent=self.root)
    
    # ===========fetch data========            
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from room")
            rows=my_cursor.fetchall()
            if len(rows)!=0 :
               self.room_Table.delete(*self.room_Table.get_children())
               for i in rows:
                   self.room_Table.insert("",END,values=i)
            conn.commit() 
            conn.close()
    
    #===========get cursor==========
    def get_cuersor(self,event=""):
        cusrsor_row=self.room_Table.focus()
        content=self.room_Table.item(cusrsor_row)
        row=content["values"]
        
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_noofdays.set(row[5])
        self.var_meal.set(row[6])
        
    #================update btn=============
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Pleace enter Contact no.", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where Contact=%s", (
                                                                                                                                                                        
                                                                                                                                    self.var_checkin.get(),
                                                                                                                                    self.var_checkout.get(),
                                                                                                                                    self.var_roomtype.get(),
                                                                                                                                    self.var_roomavailable.get(),
                                                                                                                                    self.var_meal.get(),
                                                                                                                                    self.var_noofdays.get(),
                                                                                                                                    self.var_contact.get()
                                                                                                                            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Room details has been updated",parent=self.root)
    
    
    #============delete ======================
    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management system ", "Do you want delete the custumer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
        
        #==============reset========
    def reset(self):
            self.var_contact.set(""),
            self.var_checkin.set(""),
            self.var_checkout.set(""),
            self.var_roomtype.set(""),
            self.var_roomavailable.set(""),
            self.var_noofdays.set(""),
            self.var_meal.set(""),
            self.var_paidtax.set(""),
            self.var_actualtotal.set(""),
            self.var_total.set(""),
    
    #=============all data fetch   === ==========  
    def Fecth_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Pleace enter Contact Number" ,parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                
                showDatafram=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDatafram.place(x=450,y=55,width=300,height=180)
                
                lblName=Label(showDatafram,text="Name : ",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)
                
                lbl=Label(showDatafram,text=row[0],font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
                
                #gender
                conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblgender=Label(showDatafram,text="Gender : ",font=("arial",12,"bold"))
                lblgender.place(x=0,y=30)
                
                lbl2=Label(showDatafram,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)
                
                # E-mail
                conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblemail=Label(showDatafram,text="E-mail : ",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)
                
                lbl3=Label(showDatafram,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)
                
                # Nationality
                conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblnationlity=Label(showDatafram,text="Nationality: ",font=("arial",12,"bold"))
                lblnationlity.place(x=0,y=90)
                
                lbl3=Label(showDatafram,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=90)
                
                # Address
                conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblAddress=Label(showDatafram,text="Address : ",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=120)
                
                lbl3=Label(showDatafram,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=120)
                
    #===============Search system=================
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
        my_cursor=conn.cursor()
        
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
    
                
    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()

        # Check if dates are provided
        if not inDate or not outDate:
            print("One or both date fields are empty.")
            return

        try:
            inDate = datetime.strptime(inDate, "%d/%m/%y")
            outDate = datetime.strptime(outDate, "%d/%m/%y")
            self.var_noofdays.set(abs((outDate - inDate).days))
        except ValueError as ve:
            print(f"Error parsing dates: {ve}")
            
        #====================billing ==========================================
        #  break-fast
        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Laxary"):
            q1=float(300)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)  
            
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)  
        
        
        # Launch
        elif (self.var_meal.get()=="Launch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Launch" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 
            
        
        elif (self.var_meal.get()=="Launch" and self.var_roomtype.get()=="Laxary"):
            q1=float(300)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)   
        
        # Dinner
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Laxary"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            

        


if __name__ == "__main__":
    root=Tk()
    obj=roombooking(root)
    root.mainloop()
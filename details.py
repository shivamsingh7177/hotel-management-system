from tkinter import*
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Detailsrooms:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1290x570+240+220")
        
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
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="NEW ROOM ADD",font=("Times New Roman",12,"bold"),padx=2)
        LabelFrameleft.place(x=5,y=50,width=540,height=350)
        
        
        #====================labels and entrys============
        #==============FLOOR ================
        lbl_floor=Label(LabelFrameleft,text="Floor : ",font=("Times New Roman",13,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        
        self.var_floor=StringVar()
        entry_floor=ttk.Entry(LabelFrameleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)
        
        #==============ROOM NO ================
        lbl_roonno=Label(LabelFrameleft,text="Room No : ",font=("Times New Roman",13,"bold"),padx=2,pady=6)
        lbl_roonno.grid(row=1,column=0,sticky=W)
        
        self.var_RoomNo=StringVar()
        entry_roonno=ttk.Entry(LabelFrameleft,textvariable=self.var_RoomNo,width=20,font=("arial",13,"bold"))
        entry_roonno.grid(row=1,column=1,sticky=W)
        
        #==============ROOM TYPES ================
        #lbl_roontypes=Label(LabelFrameleft,text="Room Type : ",font=("Times New Roman",13,"bold"),padx=2,pady=6)
       # lbl_roontypes.grid(row=2,column=0,sticky=W)
        
        self.var_RoomTypes=StringVar()
       # entry_roontypes=ttk.Entry(LabelFrameleft,textvariable=self.var_RoomTypes,width=20,font=("arial",13,"bold"))
        #entry_roontypes.grid(row=2,column=1,sticky=W)
        
        lbl_roomtype=Label(LabelFrameleft,font=("arial",12,"bold"),text="Room Type : ",padx=2,pady=6)
        lbl_roomtype.grid(row=2,column=0,sticky=W)
        
        combo_roomtype=ttk.Combobox(LabelFrameleft,textvariable=self.var_RoomTypes,font=("Times New Roman",13,"bold"),width=27,state="readonly")
        combo_roomtype["value"]=("Single","Double","Laxary")
        combo_roomtype.current(0)
        combo_roomtype.grid(row=2,column=1)
        
        
        #======================btns================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)
        
        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="DELETE",command=self.mdelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)
        
        #================table fram search system===============
        Table_Fram=LabelFrame(self.root,bd=2,relief=RIDGE,text="SHOW ROOMS DETAILS",font=("Times New Roman",12,"bold"),padx=2)
        Table_Fram.place(x=600,y=55,width=600,height=350)
        
        #==============Scrollbar
        scroll_x=ttk.Scrollbar(Table_Fram,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Fram,orient=VERTICAL)
        
        self.room_Table=ttk.Treeview(Table_Fram,columns=("Floor","RoomNo","RoomType",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.room_Table.heading("Floor",text="Floor")
        self.room_Table.heading("RoomNo",text="Room No")
        self.room_Table.heading("RoomType",text="Room Type")
        
        self.room_Table["show"]="headings"
        
        self.room_Table.column("Floor",width=100)
        self.room_Table.column("RoomNo",width=100)
        self.room_Table.column("RoomType",width=100)
        
        self.room_Table.pack(fill=BOTH,expand=1) 
        self.room_Table.bind("<ButtonRelease -1>", self.get_cuersor)
        self.fetch_data()
        
        
    #========================add btn==========
    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomTypes.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                            self.var_floor.get(),
                                                                            self.var_RoomNo.get(),
                                                                            self.var_RoomTypes.get()
                                                                              
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New room added sussessfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went is wrong:{str(es)}",parent=self.root)
        
    # ===========fetch data========            
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from details")
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
        
        self.var_floor.set(row[0]),
        self.var_RoomNo.set(row[1]),
        self.var_RoomTypes.set(row[2])
        
    #================update btn=============
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Pleace enter Contact no.", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s", (
                                                                                                                                                                        
                                                                                                                                    self.var_floor.get(),
                                                                                                                                    self.var_RoomTypes.get(),
                                                                                                                                    self.var_RoomNo.get()
                                                                                                                            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)
    
    
    #============delete ======================
    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management system ", "Do you want delete the room details",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    #==============reset========
    def reset(self):
            self.var_floor.set(""),
            self.var_RoomNo.set(""),
            self.var_RoomTypes.set(""),
            
            

if __name__ == "__main__":
    root=Tk()
    obj=Detailsrooms(root)
    root.mainloop()
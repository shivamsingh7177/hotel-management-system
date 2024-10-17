from tkinter import*
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

 
class Cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1290x570+240+220")
        
        #================== varabile============
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        
        #=============Image dimensions==============
        img_height = 50
        img_height1 = 590
        
        #===============title==============
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("Algerian",25),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
        #=================logo img ==================
        img2 = Image.open(r"C:/Users/shiva/OneDrive/Desktop/MINI PROJECT/logo.png")
        img2 = img2.resize((100, img_height), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=100, height=img_height)
        
        #================lable fram=============
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DEATILS",font=("Times New Roman",12,"bold"),padx=2)
        LabelFrameleft.place(x=5,y=50,width=425,height=510)
        
        #====================labels and entrys============
        #==============ref ================
        lbl_cust_ref=Label(LabelFrameleft,text="Customer Ref : ",font=("Times New Roman",13,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(LabelFrameleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)
        
        #============cust name============
        cname=Label(LabelFrameleft,font=("arial",12,"bold"),text="Customer Name : ",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(LabelFrameleft,textvariable=self.var_cust_name,width=29,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)
        
        #============mother name============
        mname=Label(LabelFrameleft,font=("arial",12,"bold"),text="Mother Name : ",padx=2,pady=6)
        mname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(LabelFrameleft,textvariable=self.var_mother,width=29,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)
        
        #===========gender combobox==========
        label_gender=Label(LabelFrameleft,font=("arial",12,"bold"),text="Gender : ",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        
        combo_gender=ttk.Combobox(LabelFrameleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male", "Femail","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        
        
        #======postcpde==============
        lblPostCode=Label(LabelFrameleft,font=("arial",12,"bold"),text="PostCode : ",padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(LabelFrameleft,width=29,textvariable=self.var_post,font=("arial",13,"bold"))
        txtPostCode.grid(row=4,column=1)
        
        #======moMobile==============
        lblMobile=Label(LabelFrameleft,font=("arial",12,"bold"),text="Mobile no. : ",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(LabelFrameleft,textvariable=self.var_mobile,width=29,font=("arial",13,"bold"))
        txtMobile.grid(row=5,column=1)
        
        #======email==============
        lblEmail=Label(LabelFrameleft,font=("arial",12,"bold"),text="E-mail ID : ",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(LabelFrameleft,textvariable=self.var_email,width=29,font=("arial",13,"bold"))
        txtEmail.grid(row=6,column=1)
        
        #======Nationality==============
        lblNationality=Label(LabelFrameleft,font=("arial",12,"bold"),text="Nationality : ",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)
        
        combo_nationality=ttk.Combobox(LabelFrameleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nationality["value"]=("Indian", "NRI")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)
        
        #======id proof type combobox==============
        lblNationality=Label(LabelFrameleft,font=("arial",12,"bold"),text="ID Proof Type : ",padx=2,pady=6)
        lblNationality.grid(row=8,column=0,sticky=W)
        
        combo_IDProof=ttk.Combobox(LabelFrameleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_IDProof["value"]=("Adhar Card", "Driving Licence" , "Passport")
        combo_IDProof.current(0)
        combo_IDProof.grid(row=8,column=1)
        
        #======ID numder==============
        lblIDNumder=Label(LabelFrameleft,font=("arial",12,"bold"),text="ID-Numder : ",padx=2,pady=6)
        lblIDNumder.grid(row=9,column=0,sticky=W)
        txtIDNumder=ttk.Entry(LabelFrameleft,textvariable=self.var_id_number,width=29,font=("arial",13,"bold"))
        txtIDNumder.grid(row=9,column=1)
        
        #======Address==============
        lblAddress=Label(LabelFrameleft,font=("arial",12,"bold"),text="Address : ",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(LabelFrameleft,textvariable=self.var_address,width=29,font=("arial",13,"bold"))
        txtAddress.grid(row=10,column=1)

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
        
        #================table fram search system===============
        Table_Fram=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW DEATILS AND SEARCH SYSTEM",font=("Times New Roman",12,"bold"),padx=2)
        Table_Fram.place(x=435,y=50,width=860,height=510)
        
        lblSEarchBy=Label(Table_Fram,font=("arial",12,"bold"),text="Search By : ",bg="red",fg="white")
        lblSEarchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_Serach=ttk.Combobox(Table_Fram,textvariable=self.search_var,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Serach["value"]=("Mobile", "Ref")
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
        details_table.place(x=0,y=50,width=850,height=390)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("Ref","Name","Mother Name","Gender","Post","Mobile",
                                                                    "E-mail","Nationlity","Id-proof","Id-number","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        
        self.Cust_Details_Table.heading("Ref",text="Refer No")
        self.Cust_Details_Table.heading("Name",text="Name")
        self.Cust_Details_Table.heading("Mother Name",text="Mother Name")
        self.Cust_Details_Table.heading("Gender",text="Gender")
        self.Cust_Details_Table.heading("Post",text="PostCode")
        self.Cust_Details_Table.heading("Mobile",text="Mobile No")
        self.Cust_Details_Table.heading("E-mail",text="E-mail")
        self.Cust_Details_Table.heading("Nationlity",text="Nationlity")
        self.Cust_Details_Table.heading("Id-proof",text="Id-proof")
        self.Cust_Details_Table.heading("Id-number",text="Id-number")
        self.Cust_Details_Table.heading("Address",text="Address")
        
        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("Ref",width=100)
        self.Cust_Details_Table.column("Name",width=100)
        self.Cust_Details_Table.column("Mother Name",width=100)
        self.Cust_Details_Table.column("Gender",width=100)
        self.Cust_Details_Table.column("Post",width=100)
        self.Cust_Details_Table.column("Mobile",width=100)
        self.Cust_Details_Table.column("E-mail",width=100)
        self.Cust_Details_Table.column("Nationlity",width=100)
        self.Cust_Details_Table.column("Id-proof",width=100)
        self.Cust_Details_Table.column("Id-number",width=100)
        self.Cust_Details_Table.column("Address",width=100)
        
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease -1>", self.get_cuersor)
        self.fetch_data()
       
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_ref.get(),
                                                                                            self.var_cust_name.get(),
                                                                                            self.var_mother.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_post.get(),
                                                                                            self.var_mobile.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_nationality.get(),
                                                                                            self.var_id_proof.get(),
                                                                                            self.var_id_number.get(),
                                                                                            self.var_address.get(),
                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went is wrong:{str(es)}",parent=self.root)
        
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from customer")
            rows=my_cursor.fetchall()
            if len(rows)!=0 :
               self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
               for i in rows:
                   self.Cust_Details_Table.insert("",END,values=i)
            conn.commit() 
            conn.close()
            
    def get_cuersor(self,event=""):
        cusrsor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cusrsor_row)
        row=content["values"]
        
        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])


    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Pleace enter Mobile no.", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                                                                                                                        
                                                                                                                                                                        self.var_cust_name.get(),
                                                                                                                                                                        self.var_mother.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_post.get(),
                                                                                                                                                                        self.var_mobile.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_nationality.get(),
                                                                                                                                                                        self.var_id_proof.get(),
                                                                                                                                                                        self.var_id_number.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_ref.get()
                                                                                                                                                                    ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Customer details has been updated",parent=self.root)
        
    
    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management system ", "Do you want delete the custumer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
       # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@7177",database="management")
        my_cursor=conn.cursor()
        
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
    
        

if __name__ == "__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()
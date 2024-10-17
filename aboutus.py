from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class AboutPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System - About Us")
        self.root.geometry("1290x570+240+220")

        # Main Frame to contain everything
        main_frame = Frame(self.root)
        main_frame.pack(fill=BOTH, expand=1)

        # Create a canvas
        canvas = Canvas(main_frame)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add a scrollbar to the canvas
        scroll_y = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        canvas.configure(yscrollcommand=scroll_y.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create another frame inside the canvas
        content_frame = Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")  # Center alignment

        # Title
        lbl_title = Label(content_frame, text="About Us - Hotel Management System", font=("Algerian", 20), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.pack(fill=X, padx=10)

        # About Us Section
        lbl_about = Label(content_frame, text="About Our Hotel", font=("Times New Roman", 16, "bold"))
        lbl_about.pack(pady=10)

        # Introduction/About Us Text
        about_text = """Welcome to Aaditi hotel, your ultimate destination for comfort and luxury.
We have been serving our customers since 2001, offering the finest in hospitality and services. 
Our hotel is equipped with modern amenities to provide our guests with the best possible experience.

We offer:
- Spacious and luxurious rooms
- 24/7 customer service
- Fine dining and catering services
- Convenient online room booking and check-in services

Our mission is to deliver outstanding service and exceed guest expectations with every visit."""

        self.txt_about = Text(content_frame, height=12, width=140, font=("Arial", 12), wrap=WORD)
        self.txt_about.insert(END, about_text)
        self.txt_about.config(state=DISABLED)
        self.txt_about.pack(pady=10)

        # Team Section with a Frame
        team_frame = Frame(content_frame, bd=2, relief=SOLID, padx=20, pady=20)
        team_frame.pack(pady=10, padx=5, fill=X)

        lbl_team = Label(team_frame, text="Meet Our Team", font=("Times New Roman", 16, "bold"))
        lbl_team.pack(pady=10)

        # Display Employee Photos and Names
        self.show_team(team_frame)

    def show_team(self, frame):
        # Sample employee details: name and image paths
        employees = [
            {"name": "TEACHER'S", "image": r"C:\Users\shiva\OneDrive\Desktop\MINI PROJECT\teacher.jpg"},
            {"name": "SHIVAM - CEO", "image": r"C:\Users\shiva\OneDrive\Desktop\MINI PROJECT\me.jpg"},
        ]

        # Aligning the employee photos and names to the center
        for employee in employees:
            try:
                img = Image.open(employee["image"])
                img = img.resize((150, 150), Image.Resampling.LANCZOS)
                photo_img = ImageTk.PhotoImage(img)

                emp_frame = Frame(frame)
                emp_frame.pack(pady=10, anchor=CENTER)  # Center alignment

                # Adding a border to the image label
                lbl_img = Label(emp_frame, image=photo_img, bd=5, relief=SOLID)
                lbl_img.image = photo_img
                lbl_img.pack(pady=5)

                lbl_name = Label(emp_frame, text=employee["name"], font=("Arial", 12, "bold"))
                lbl_name.pack()

            except Exception as e:
                lbl_error = Label(frame, text=f"Image not found for {employee['name']}", font=("Arial", 10), fg="red")
                lbl_error.pack(pady=5)

        # Adding the remaining team members with a new line after 6 members
        sujal_and_krish_frame = Frame(frame)
        sujal_and_krish_frame.pack(pady=10, anchor=CENTER)  # Center alignment

        sujal_and_krish = [
            
            {"name": "KRISH", "image": r"C:\Users\shiva\OneDrive\Desktop\MINI PROJECT\krish.jpg"},
            {"name": "DHANANJAY", "image": r"C:\Users\shiva\OneDrive\Desktop\MINI PROJECT\DHANANJAY.jpg"},
            {"name": "BHAVIK", "image": r"C:\Users\shiva\OneDrive\Desktop\MINI PROJECT\BHAVIK.jpg"},
            {"name": "SUJAL", "image": r"C:\Users\shiva\OneDrive\Desktop\MINI PROJECT\sujal.jpg"},
            {"name": "SOHAM", "image": r"C:\Users\shiva\OneDrive\Desktop\MINI PROJECT\SOHAM.jpg"},
            {"name": "AADI", "image": r"C:\Users\shiva\OneDrive\Desktop\MINI PROJECT\AADI.jpg"},
            {"name": "ARSALAN", "image": r"C:\Users\shiva\OneDrive\Desktop\MINI PROJECT\arsalan.jpg"},
            {"name": "UDAY", "image": r"C:\Users\shiva\OneDrive\Desktop\MINI PROJECT\uday.jpg"},
            {"name": "SANKET", "image": r"C:\Users\shiva\OneDrive\Desktop\MINI PROJECT\sanket.jpg"}
        ]

        # Add first 6 members in a row
        row_frame = Frame(sujal_and_krish_frame)
        row_frame.pack(anchor=CENTER)

        for i, employee in enumerate(sujal_and_krish[:6]):  # first 6 members
            try:
                img = Image.open(employee["image"])
                img = img.resize((150, 150), Image.Resampling.LANCZOS)
                photo_img = ImageTk.PhotoImage(img)

                emp_frame = Frame(row_frame)
                emp_frame.pack(side=LEFT, padx=20)  # Align side by side with space in between

                # Adding a border to the image label
                lbl_img = Label(emp_frame, image=photo_img, bd=5, relief=SOLID)
                lbl_img.image = photo_img
                lbl_img.pack(pady=5)

                lbl_name = Label(emp_frame, text=employee["name"], font=("Arial", 12, "bold"))
                lbl_name.pack()

            except Exception as e:
                lbl_error = Label(row_frame, text=f"Image not found for {employee['name']}", font=("Arial", 10), fg="red")
                lbl_error.pack(side=LEFT, padx=10)

        # Add Arsalan, UDAY, and SANKET on the next line
        next_row_frame = Frame(sujal_and_krish_frame)
        next_row_frame.pack(anchor=CENTER)

        for employee in sujal_and_krish[6:9]:  # Arsalan, UDAY, SANKET
            try:
                img = Image.open(employee["image"])
                img = img.resize((150, 150), Image.Resampling.LANCZOS)
                photo_img = ImageTk.PhotoImage(img)

                emp_frame = Frame(next_row_frame)
                emp_frame.pack(side=LEFT, padx=20)  # Align side by side

                # Adding a border to the image label
                lbl_img = Label(emp_frame, image=photo_img, bd=5, relief=SOLID)
                lbl_img.image = photo_img
                lbl_img.pack(pady=5)

                lbl_name = Label(emp_frame, text=employee["name"], font=("Arial", 12, "bold"))
                lbl_name.pack()

            except Exception as e:
                lbl_error = Label(next_row_frame, text=f"Image not found for {employee['name']}", font=("Arial", 10), fg="red")
                lbl_error.pack(side=LEFT, padx=10)


if __name__ == "__main__":
    root = Tk()
    app = AboutPage(root)
    root.mainloop()

import tkinter
import os
import openpyxl
from tkinter import ttk
from tkinter import messagebox


# pip install openpyxl

def enter_data():
    # recuperer les valeurs
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    nationality = nationality_combobox.get()
    completed_courses = num_courses_spinbox.get()
    nb_semestre = num_semestre_spinbox.get()

    registrat_status = reg_status_var.get()
    term_et_cond = term.get()

    if first_name == "" or last_name == "" or title == "" or nationality == "" or registrat_status == "not registed" or term_et_cond == "Not Accepted":
        tkinter.messagebox.showerror(title="erreur", message="Remplissez tous les champs")
    else:
        print("Firstname =  ", first_name)
        print("Lastname = ", last_name)
        print("Title = ", title)
        print("Age = ", age)
        print("Nationality = ", nationality)
        print("Nb complete course = ", completed_courses)
        print("Nb semestre = ", nb_semestre)
        print("registration status = ", registrat_status)
        print("term = ", term_et_cond)
        print(" ")

        # chemin_fichier = "C:\Users\Admin\Documents\GitHub\TkinterDataEntry\data.xlsx"
        # file_path = "~C:\Utilisateurs\Admin\Documents\GitHub\TkinterDataEntry\data1.xlsx"
        # filepath = "https://github.com/robertsergo/TkinterDataEntry/data.xlsx"
        file_path = "~C:\Admin\Documents\GitHub\TkinterDataEntry\data.xlsx"
        if not os.path.exists(file_path):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            heading = ["Firstname", "Lastname", "Title", "Age", "Nationality", "Nb completed course", "Nb sesmestre",
                       "registration status"]
            # heading.append(sheet)
            sheet.append(heading)
            workbook.save(file_path)


window = tkinter.Tk()

window.title("Tkinter Data Entry ")

frame = tkinter.Frame(window)
frame.pack()
user_info_frame = tkinter.LabelFrame(frame, text="user_infomation")
user_info_frame.grid(row=0, column=0, padx=30, pady=30)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)
first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["Mr", "Mme", "Miss", "Dr.", "Prof."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_label.grid(row=2, column=0)
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=60)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_label.grid(row=2, column=1)
nationality_combobox = ttk.Combobox(user_info_frame,
                                    values=["Argentine", "Bresil", "Bolivie", "Peru", "Paraguay", "Uruguay",
                                            "Venezuela", "Equator", "Colonbia"])
nationality_combobox.grid(row=3, column=1)

for wiget in user_info_frame.winfo_children():
    wiget.grid_configure(padx=15, pady=10)

# save course info
course_frame = tkinter.LabelFrame(frame)
course_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

reg_status_var = tkinter.StringVar(value="not registed")
registered_label = tkinter.Label(course_frame, text="Registration Status")
registered_check = tkinter.Checkbutton(course_frame, text="Currently Registered", variable=reg_status_var,
                                       onvalue="registed", offvalue="not registed")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

num_courses_label = tkinter.Label(course_frame, text="# Completed Couses")
num_courses_spinbox = tkinter.Spinbox(course_frame, from_=0, to="infinity")
num_courses_label.grid(row=0, column=1)
num_courses_spinbox.grid(row=1, column=1)

num_semestre_label = tkinter.Label(course_frame, text="# semestre")
num_semestre_spinbox = tkinter.Spinbox(course_frame, from_=0, to="infinity")
num_semestre_label.grid(row=0, column=2)
num_semestre_spinbox.grid(row=1, column=2)

for wiget in course_frame.winfo_children():
    wiget.grid_configure(padx=10, pady=10)

# Accept term
terms_frame = tkinter.LabelFrame(frame, text="Terms & Condition")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)
term = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions", variable=term,
                                  onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

button = tkinter.Button(frame, text="Enter Data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

window.mainloop()

import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.title("Tkinter Data Entry ")


frame = tkinter.Frame(window)
frame.pack()
user_info_frame = tkinter.LabelFrame(frame, text = "user_infomation")
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
nationality_combobox = ttk.Combobox(user_info_frame, values=["Argentine", "Bresil", "Bolivie", "Peru", "Paraguay", "Uruguay", "Venezuela", "Equator", "Colonbia"])
nationality_combobox.grid(row=3, column=1)

for wiget in user_info_frame.winfo_children():
    wiget.grid_configure(padx=15, pady=10)


window.mainloop()
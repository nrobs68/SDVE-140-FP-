import tkinter as tk
from tkinter import *
from tkinter.ttk import *

root = tk.Tk()
main_frame = tk.Frame(root)

# Title
title_lbl = tk.Label(main_frame, text="Patient Age, Height, Weight, and Sex Calculator", font=("Arial", 14))
title_lbl.pack()

# Patient information labels
patient_lbl = tk.Label(main_frame, text="Enter Patient Information:")
patient_lbl.pack()

# Age entry
age_frame = tk.Frame(main_frame)
age_lbl = tk.Label(age_frame, text="Patient Age (1-18):")
age_lbl.pack(side="left")
age_entry = tk.Entry(age_frame)
age_entry.pack(side="right")
age_frame.pack()

# Height and Weight dropdown list
hw_frame = tk.Frame(main_frame)
hw_lbl = tk.Label(hw_frame, text="Patient Height/Weight Range:")
hw_lbl.pack(side="left")
hw_dropdown = Combobox(hw_frame, values=["Short/Light", "Short/Medium", "Short/Heavy",
                                        "Tall/Light", "Tall/Medium", "Tall/Heavy"])
hw_dropdown.pack(side="right")
hw_frame.pack()

# Sex dropdown list
sex_frame = tk.Frame(main_frame)
sex_lbl = tk.Label(sex_frame, text="Patient Sex:")
sex_lbl.pack(side="left")
sex_dropdown = Combobox(sex_frame, values=["Male", "Female"])
sex_dropdown.pack(side="right")
sex_frame.pack()

# Submit Button
def submit_data():
    patient_ages = age_entry.get()
    patient_hw_range = hw_dropdown.get()
    patient_sex = sex_dropdown.get()

    # Calculating average age, height, weight and sex
    sum_ages = 0
    for i in range(1, 18):
        sum_ages += int(patient_ages[i])
    avg_age = sum_ages / 10
    avg_hw_range = patient_hw_range
    avg_sex = patient_sex

    # Create second window with average data
    avg_frame = tk.Toplevel(main_frame)
    avg_frame.title("Average Data")

    # Average Age Label
    avg_age_lbl = tk.Label(avg_frame, text="Average Age: " + str(avg_age))
    avg_age_lbl.pack()

    # Average Height/Weight Label
    avg_hw_lbl = tk.Label(avg_frame, text="Average Height/Weight Range: " + str(avg_hw_range))
    avg_hw_lbl.pack()

    # Average Sex Label
    avg_sex_lbl = tk.Label(avg_frame, text="Average Sex: " + str(avg_sex))
    avg_sex_lbl.pack()

submit_btn = tk.Button(main_frame, text="Submit", command=submit_data)
submit_btn.pack()

# Exit Button
def exit_program():
    root.destroy()

exit_btn = tk.Button(main_frame, text="Exit", command=exit_program)
exit_btn.pack()

main_frame.pack()

root.mainloop()

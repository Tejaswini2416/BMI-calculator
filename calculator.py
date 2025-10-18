from tkinter import *
from datetime import datetime

#===== constants =====#
COLOR = 'white smoke'
FONT = 'Courier'

window = Tk()
window.minsize(500, 500)
window.title('BMI Calculator')
window.config(bg=COLOR)

# Center columns
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

#------------------ FRAMES ------------------#
details_frame = Frame(window, bg=COLOR)
bmi_frame = Frame(window, bg=COLOR)

for frame in (details_frame, bmi_frame):
    frame.grid(row=0, column=0, sticky='nsew')

#=====================================================
#                DETAILS PAGE
#=====================================================

title_label = Label(details_frame, text='Welcome to BMI Calculator', bg=COLOR, fg='brown', font=('Times', 22, 'bold'))
title_label.grid(row=0, column=0, columnspan=2, pady=30)

#----- Name -----#
name_label = Label(details_frame, text='Enter your name:', bg=COLOR, fg='black', font=(FONT, 11))
name_label.grid(row=1, column=0, pady=10, sticky='e')
user_name = Entry(details_frame, width=25, justify='center')
user_name.grid(row=1, column=1, pady=10, sticky='w')

#----- Age -----#
age_label = Label(details_frame, text='Enter your age:', bg=COLOR, fg='black', font=(FONT, 11))
age_label.grid(row=2, column=0, pady=10, sticky='e')
user_age = Entry(details_frame, width=25, justify='center')
user_age.grid(row=2, column=1, pady=10, sticky='w')

#----- Error label for details -----#
details_error = Label(details_frame, text='', bg=COLOR, fg='red', font=(FONT, 10))
details_error.grid(row=3, column=0, columnspan=2, pady=5)

#----- Next button -----#
def go_to_bmi_page():
    name = user_name.get().strip()
    age = user_age.get().strip()

    if not name or not age:
        details_error.config(text="Please fill in both fields.")
        return

    try:
        age_val = int(age)
        if age_val <= 0:
            raise ValueError
    except ValueError:
        details_error.config(text="Please enter a valid age.")
        return

    greeting_label.config(text=f"Hello, {name} (Age: {age_val})")
    details_frame.grid_forget()
    bmi_frame.grid(row=0, column=0, sticky='nsew')

next_button = Button(details_frame, text='Next ➜', font=(FONT, 11), bg='brown', fg='white', command=go_to_bmi_page)
next_button.grid(row=4, column=0, columnspan=2, pady=20)

#=====================================================
#                BMI PAGE
#=====================================================

#---------- Greeting ----------#
greeting_label = Label(bmi_frame, text='', bg=COLOR, fg='brown', font=('Times', 18, 'bold'))
greeting_label.grid(row=0, column=0, columnspan=2, pady=20)

#------------ Weight label & entry ------------#
weight_label = Label(bmi_frame, text='Enter your weight (kg)', bg=COLOR, fg='black', font=(FONT, 11))
weight_label.grid(row=1, column=0, pady=10, sticky="e")

user_weight = Entry(bmi_frame, width=20, justify="center")
user_weight.grid(row=1, column=1, pady=10, sticky="w")

#------------ Height label & entry ------------#
height_label = Label(bmi_frame, text='Enter your height (cm)', bg=COLOR, fg='black', font=(FONT, 11))
height_label.grid(row=2, column=0, pady=10, sticky="e")

user_height = Entry(bmi_frame, width=20, justify="center")
user_height.grid(row=2, column=1, pady=10, sticky="w")

#------------ BMI Result Label ------------#
bmi_label = Label(bmi_frame, text='', bg=COLOR, fg='black', font=(FONT, 11))
bmi_label.grid(row=5, column=0, columnspan=2, pady=15)

# Variables to store BMI data for saving
bmi_value = None
bmi_status = None

#------------ BMI Calculation ------------#
def bmi_calculation():
    global bmi_value, bmi_status

    if not user_weight.get().strip() or not user_height.get().strip():
        bmi_label.config(text='Please fill in both fields.', bg=COLOR, fg='red')
        return

    try:
        weight = float(user_weight.get())
        height = float(user_height.get()) / 100
        bmi_value = weight / (height)**2
        text_color = 'white'

        if bmi_value <= 18.4:
            bmi_status = "Underweight"
            color = 'blue'
        elif 18.5 <= bmi_value <= 24.9:
            bmi_status = "Normal"
            color = 'green'
        elif 25.0 <= bmi_value <= 29.9:
            bmi_status = "Overweight"
            color = 'yellow'
            text_color = 'black'
        elif 30 <= bmi_value <= 39.9:
            bmi_status = "Obese"
            color = 'orange'
        else:
            bmi_status = "Severely Obese"
            color = 'red'

        bmi_result = f"Your BMI is: {round(bmi_value,2)}\nStatus: {bmi_status}"
        bmi_label.config(text=bmi_result, bg=color, fg=text_color, font=(FONT, 12, 'bold'))
    except ValueError:
        bmi_label.config(text='Invalid inputs! Please enter numbers.', bg=COLOR, fg='red')

#------------ Calculate button ------------#
calculate = Button(bmi_frame, text='Calculate', font=(FONT, 11), bg='brown', fg='white', command=bmi_calculation)
calculate.grid(row=4, column=0, columnspan=2, pady=20)

#------------ Reset button ------------#
def reset_fields():
    user_weight.delete(0, END)
    user_height.delete(0, END)
    bmi_label.config(text='', bg=COLOR, fg='black')

reset_button = Button(bmi_frame, text='Reset', font=(FONT, 11), bg='gray', fg='white', command=reset_fields)
reset_button.grid(row=6, column=0, columnspan=2, pady=10)

#------------ Back to details button ------------#
def go_back_to_details():
    reset_fields()
    bmi_frame.grid_forget()
    details_frame.grid(row=0, column=0, sticky='nsew')

back_button = Button(bmi_frame, text='⏪ Back', font=(FONT, 11), bg='brown', fg='white', command=go_back_to_details)
back_button.grid(row=7, column=0, columnspan=2, pady=10)

#------------ Save Result Button ------------#
def save_result():
    global bmi_value, bmi_status
    name = user_name.get().strip()
    age = user_age.get().strip()

    if bmi_value is None or bmi_status is None:
        bmi_label.config(text='Please calculate BMI before saving.', bg=COLOR, fg='red')
        return

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = f"{now} | Name: {name}, Age: {age}, BMI: {round(bmi_value,2)}, Status: {bmi_status}\n"

    with open("bmi_results.txt", "a") as file:
        file.write(data)

    bmi_label.config(text='Result saved to bmi_results.txt', bg='green', fg='white', font=(FONT, 10, 'bold'))

save_button = Button(bmi_frame, text='💾 Save Result', font=(FONT, 11), bg='darkgreen', fg='white', command=save_result)
save_button.grid(row=9, column=0, columnspan=2, pady=10)

#------------ BMI Guide ------------#
guide = Label(
    bmi_frame,
    text='BMI Guide:\nUnderweight ≤ 18.4\nNormal 18.5–24.9\nOverweight 25–29.9\nObese 30–39.9\nSeverely obese ≥ 40',
    bg=COLOR, fg='black', font=(FONT, 10)
)
guide.grid(row=8, column=0, columnspan=2, pady=10)

#------------ Bind Enter Key ------------#
window.bind('<Return>', lambda event: bmi_calculation())

# Start with details frame
details_frame.grid(row=0, column=0, sticky='nsew')

window.mainloop()

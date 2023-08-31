import tkinter as tk

#window
window = tk.Tk()
window.minsize(width=230, height=250)
window.title("BMI Calculator")

TYPE = None

w_label = tk.Label(text="Enter Wour Weight (kg)")
w_label.place(x=50, y=20)

def take_entry():
    user_w = w_entry.get()
    user_h = h_entry.get()
    try:
        BMI = int(user_w)/(int(user_h)**2/10000)
        if BMI<18.5:
            TYPE = "Underweight"
        elif BMI>= 18.5 and BMI<25:
            TYPE = "Normal"
        elif BMI>=25 and BMI<30:
            TYPE = "Overweight"
        else:
            TYPE = "Obese"
        last_label = tk.Label(text="Your BMI is {}. Your body type is {}.".format(BMI, TYPE))
        last_label.place(y=140)
    except:
        error_label = tk.Label(text="Enter a valid number")
        error_label.place(x=60, y=160)

w_entry = tk.Entry()
w_entry.focus()
w_entry.place(x=50, y=40)

h_label = tk.Label(text="Enter Wour Height (cm)")
h_label.place(x=50, y=70)

h_entry = tk.Entry()
h_entry.place(x=50, y=90)

calculate_button = tk.Button(text="Calculate", command=take_entry)
calculate_button.place(x=83, y=125)

window.mainloop()
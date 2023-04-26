import tkinter


def bmi_calculater():

    try:
        person_weight_input = int(person_weight.get())
        person_height_input = int(person_height.get())
        person_height_input_meter = person_height_input / 100
        bmi_real = person_weight_input/person_height_input_meter**2
        bmi = round(bmi_real, 2)
        result = "Enter "
        if bmi <= 18.4:
            result = "Underweight"
        elif 18.4 < bmi < 24.9:
            result = "Normal"
        elif 25.0 < bmi < 39.9:
            result = "Overweight"
        elif bmi >= 40.0:
            result = "Obese"
        bmi_label.config(text=f"Your BMI is {bmi} You are {result}")
        bmi_label.pack()

    except:
        bmi_label.config(text="Enter a valid number!")


window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=50, pady=20)


weight_label = tkinter.Label(text="Enter Your Weight (kg)", font=("Arial", 10))
weight_label.config(pady=5)
weight_label.pack()

person_weight = tkinter.Entry(width=15)
person_weight.focus()
person_weight.pack()

height_label = tkinter.Label(text="Enter Your Height (cm)", font=("Arial", 10))
height_label.config(pady=5)
height_label.pack()

person_height = tkinter.Entry(width=15)
person_height.pack()

calculater_button = tkinter.Button(text="Calculate",command=bmi_calculater)
calculater_button.config(pady=5)
calculater_button.pack()

bmi_label = tkinter.Label()


window.mainloop()
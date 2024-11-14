from tkinter import *
from  tkinter import ttk

windows = Tk()
windows.configure(bg= "#000FFF")
windows.title("GP Calculator designed by Andrew Halilu")


def Total():
    def first():
        global unit1
        unit1 = int(credit1_entry.get())
        global graded1
        graded1 = grad1.get()

        if graded1 == "A":
            return unit1 * 5
        elif graded1 == "B":
            return unit1 * 4
        elif graded1 == "C":
            return unit1 * 3
        elif graded1 == "D":
            return unit1 * 2
        elif graded1 == "E":
            return unit1 * 1
        elif graded1 == "F":
            return unit1 * 0

    def second():
        global unit2
        unit2 = int(credit2_entry.get())
        global graded2
        graded2 = grad2.get()

        if graded2 == "A":
            return unit2 * 5
        elif graded2 == "B":
            return unit2 * 4
        elif graded2 == "C":
            return unit2 * 3
        elif graded2 == "D":
            return unit2 * 2
        elif graded2 == "E":
            return unit2 * 1
        elif graded2 == "F":
            return unit2 * 0

    def third():
        global unit3
        unit3 = int(credit3_entry.get())
        global graded3
        graded3 = grad3.get()

        if graded3 == "A":
            return unit3 * 5
        elif graded3 == "B":
            return unit3 * 4
        elif graded3 == "C":
            return unit3 * 3
        elif graded3 == "D":
            return unit3 * 2
        elif graded3 == "E":
            return unit3 * 1
        elif graded3 == "F":
            return unit3 * 0

    def fouth():
        global unit4
        unit4 = int(credit4_entry.get())
        global graded4
        graded4 = grad4.get()

        if graded4 == "A":
            return unit4 * 5
        elif graded4 == "B":
            return unit4 * 4
        elif graded4 == "C":
            return unit4 * 3
        elif graded4 == "D":
            return unit4 * 2
        elif graded4 == "E":
            return unit4 * 1
        elif graded4 == "F":
            return unit4 * 0

    def fifth():
        global unit5
        unit5 = int(credit5_entry.get())
        global graded5
        graded5 = grad5.get()

        if graded5 == "A":
            return unit5 * 5
        elif graded5 == "B":
            return unit5 * 4
        elif graded5 == "C":
            return unit5 * 3
        elif graded5 == "D":
            return unit5 * 2
        elif graded5 == "E":
            return unit5 * 1
        elif graded5 == "F":
            return unit5 * 0

    def sixth():
        global unit6
        unit6 = int(credit6_entry.get())
        global graded6
        graded6 = grad6.get()

        if graded6 == "A":
            return unit6 * 5
        elif graded6 == "B":
            return unit6 * 4
        elif graded6 == "C":
            return unit6 * 3
        elif graded6 == "D":
            return unit6 * 2
        elif graded6 == "E":
            return unit6 * 1
        elif graded6 == "F":
            return unit6 * 0

    def seventh():
        global unit7
        unit7 = int(credit7_entry.get())
        global graded7
        graded7 = grad7.get()

        if graded7 == "A":
            return unit7 * 5
        elif graded7 == "B":
            return unit7 * 4
        elif graded7 == "C":
            return unit7 * 3
        elif graded7 == "D":
            return unit7 * 2
        elif graded7 == "E":
            return unit7 * 1
        elif graded7 == "F":
            return unit7 * 0

    def eight():
        global unit8
        unit8 = int(credit8_entry.get())
        global graded8
        graded8 = grad8.get()

        if graded8 == "A":
            return unit8 * 5
        elif graded8 == "B":
            return unit8 * 4
        elif graded8 == "C":
            return unit8 * 3
        elif graded8 == "D":
            return unit8 * 2
        elif graded8 == "E":
            return unit8 * 1
        elif graded8 == "F":
            return unit8 * 0


    total_credit_unit_score = int(first()) + int(second()) + int(third()) + int(fouth()) + int(fifth()) + int(sixth()) + int(seventh()) + int(eight())


    credit_score = unit1 + unit2 + unit3 + unit4 + unit5 + unit6 + unit7 + unit8


    cgpa_grade = round(total_credit_unit_score/credit_score, 2)

    credit_unit9_entry.insert(0, total_credit_unit_score)

    total_unit_entry.insert(0, credit_score)

    cgpa_value11_entry.insert(0, cgpa_grade)

    if cgpa_grade < 3.5:
        title.configure(text=f"Your CGPA Grade is {cgpa_grade}", font=(("Arial bold"), 20), fg="red")
    else:
        title.configure(text=f"Your CGPA Grade is {cgpa_grade}", font=(("Arial bold"), 20), fg="green")


def Clear():
    course1_entry.delete(0, END)
    course2_entry.delete(0, END)
    course3_entry.delete(0, END)
    course4_entry.delete(0, END)
    course5_entry.delete(0, END)
    course6_entry.delete(0, END)
    course7_entry.delete(0, END)
    course8_entry.delete(0, END)

    grad1.delete(0, END)
    grad2.delete(0, END)
    grad3.delete(0, END)
    grad4.delete(0, END)
    grad5.delete(0, END)
    grad6.delete(0, END)
    grad7.delete(0, END)
    grad8.delete(0, END)

    credit1_entry.delete(0, END)
    credit2_entry.delete(0, END)
    credit3_entry.delete(0, END)
    credit4_entry.delete(0, END)
    credit5_entry.delete(0, END)
    credit6_entry.delete(0, END)
    credit7_entry.delete(0, END)
    credit8_entry.delete(0, END)

    credit_unit9_entry.delete(0, END)
    total_unit_entry.delete(0, END)
    cgpa_value11_entry.delete(0, END)





menubars = Menu(windows)

views = Menu(menubars, tearoff = 0)
views.add_command(label= "View As",)
menubars.add_cascade(label="View", menu= views)


help = Menu(menubars, tearoff = 0)
help.add_command(label= "FAQ",)
menubars.add_cascade(label="Help", menu= help)


contac = Menu(menubars, tearoff = 0)
contac.add_command(label= "Official Email")
menubars.add_cascade(label="Contact Us", menu= contac)


quis = Menu(menubars, tearoff = 0)
quis.add_command(label="Exit", command=windows.quit)
menubars.add_cascade(label= "Quit", menu= quis)
windows.config(menu=menubars)

frame1 = Frame(windows, bg = "#000FFF")
title = Label(frame1, bg = "#000FFF", fg="white", text="MAU Institute of Information Technology", font=(("Arial bold"), 20))
title.grid(row=0, column=0, sticky= "news")
frame1.pack()

frame = Frame(windows, bg = "#000FFF")
main_body = LabelFrame(frame, bg = "#000FFF", relief = "raised")
main_body.grid(row=2, column =0,sticky= "news")


code_name = Label(main_body, bg = "#000FFF")
code_name.grid(row=1, column =0)


code_title_list = Label(code_name, fg="white",text="COURSE CODE", font= (("Arial bold"), 12), bg = "#000FFF")
code_title_list.grid(row=0, column =1)

course1 = Label(code_name, text="COURSE 1", bg = "#000FFF", fg="white")
course2 = Label(code_name, text="COURSE 2",bg = "#000FFF", fg="white")
course3 = Label(code_name, text="COURSE 3", bg = "#000FFF", fg="white")
course4 = Label(code_name, text="COURSE 4", bg = "#000FFF", fg="white")
course5 = Label(code_name, text="COURSE 5",bg = "#000FFF", fg="white")
course6 = Label(code_name, text="COURSE 6",bg = "#000FFF", fg="white")
course7 = Label(code_name, text="COURSE 7", bg = "#000FFF", fg="white")
course8 = Label(code_name, text="COURSE 8",bg = "#000FFF", fg="white")

course1.grid(row=1, column =0)
course2.grid(row=2, column =0)
course3.grid(row=3, column =0)
course4.grid(row=4, column =0)
course5.grid(row=5, column =0)
course6.grid(row=6, column =0)
course7.grid(row=7, column =0)
course8.grid(row=8, column =0)






course1_entry = Entry(code_name)
course2_entry = Entry(code_name)
course3_entry = Entry(code_name)
course4_entry = Entry(code_name)
course5_entry = Entry(code_name)
course6_entry = Entry(code_name)
course7_entry = Entry(code_name)
course8_entry = Entry(code_name)
btn_cal = Button(code_name, text="Calculate", font= (("Arial bold"), 12), padx=10, pady= 5, command=Total)
btn_clr = Button(code_name, text="Clear", font= (("Arial bold"), 12), padx=14, pady= 5, command=Clear)


course1_entry.grid(row=1, column =1)
course2_entry.grid(row=2, column =1)
course3_entry.grid(row=3, column =1)
course4_entry.grid(row=4, column =1)
course5_entry.grid(row=5, column =1)
course6_entry.grid(row=6, column =1)
course7_entry.grid(row=7, column =1)
course8_entry.grid(row=8, column =1)
btn_cal.grid(row=9, column =1)
btn_clr.grid(row=10, column =1)


grade_name = Label(main_body, bg = "#000FFF")
grade_name.grid(row=1, column =1)

grade_title_list = Label(grade_name, text="GRADE", font= (("Arial bold"), 12), bg = "#000FFF", fg="white")
grade_title_list.grid(row=0, column =0)

options = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F"
]

grad1 = ttk.Combobox(grade_name, values=options)
grad2 = ttk.Combobox(grade_name, values=options)
grad3 = ttk.Combobox(grade_name, values=options)
grad4 = ttk.Combobox(grade_name, values=options)
grad5 = ttk.Combobox(grade_name, values=options)
grad6 = ttk.Combobox(grade_name, values=options)
grad7 = ttk.Combobox(grade_name, values=options)
grad8 = ttk.Combobox(grade_name, values=options)
lab_credit_unt = Label(grade_name, text="Total CGPA Credit Unit", font= (("Arial bold"), 10), bg = "#000FFF", fg="white")
lab_grade_unt = Label(grade_name, text="Total Unit Score", font= (("Arial bold"), 10), bg = "#000FFF", fg="white")
lab_cgps_unt = Label(grade_name, text="Your CGPA is", font= (("Arial bold"), 10), bg = "#000FFF", fg = "white")

grad1.grid(row=1, column =0)
grad2.grid(row=2, column =0)
grad3.grid(row=3, column =0)
grad4.grid(row=4, column =0)
grad5.grid(row=5, column =0)
grad6.grid(row=6, column =0)
grad7.grid(row=7, column =0)
grad8.grid(row=8, column =0)
lab_credit_unt.grid(row=9, column =0)
lab_grade_unt.grid(row=10, column =0)
lab_cgps_unt.grid(row=11, column =0)


credit_unit = Label(main_body, bg = "#000FFF")
credit_unit.grid(row=1, column =2)

credit_unit_list = Label(credit_unit, text="CREDIT UNIT", fg="white", font= (("Arial bold"), 12), bg = "#000FFF")
credit_unit_list.grid(row=0, column =0)

credit1_entry = Entry(credit_unit)
credit2_entry = Entry(credit_unit)
credit3_entry = Entry(credit_unit)
credit4_entry = Entry(credit_unit)
credit5_entry = Entry(credit_unit)
credit6_entry = Entry(credit_unit)
credit7_entry = Entry(credit_unit)
credit8_entry = Entry(credit_unit)
credit_unit9_entry = Entry(credit_unit)
total_unit_entry = Entry(credit_unit)
cgpa_value11_entry = Entry(credit_unit)

credit1_entry.grid(row=1, column =0)
credit2_entry.grid(row=2, column =0)
credit3_entry.grid(row=3, column =0)
credit4_entry.grid(row=4, column =0)
credit5_entry.grid(row=5, column =0)
credit6_entry.grid(row=6, column =0)
credit7_entry.grid(row=7, column =0)
credit8_entry.grid(row=8, column =0)
credit_unit9_entry.grid(row=9, column =0)
total_unit_entry.grid(row=10, column =0)
cgpa_value11_entry.grid(row=11, column =0)

frame.pack()




for widget in frame1.winfo_children():
    widget.pack_configure(padx=10, pady=50)
for widget in main_body.winfo_children():
    widget.grid_configure(padx=10, pady=10)
for widget in code_name.winfo_children():
    widget.grid_configure(padx=10, pady=10)
for widget in grade_name.winfo_children():
    widget.grid_configure(padx=10, pady=10)
for widget in credit_unit.winfo_children():
    widget.grid_configure(padx=10, pady=10.5)




windows.mainloop()
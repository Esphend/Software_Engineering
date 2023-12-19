import tkinter as tk
from tkinter import *
from gen_2L import generate_2L
from gen_3L import generate_3l
from gen_4L import generate_4l
def SearchGen():
    searchstr = ""
    value = links.get()
    value = value.split(" ")
    for element in value:
        if len(element) == 2:
            searchstr += generate_2L(element) + "|"
        elif len(element) == 3:
            searchstr += generate_3l(element) + "|"
        elif len(element) == 4:
            searchstr += generate_4l(element) + "|"
    searchstr = searchstr[:-1]
    if len(searchstr) <= 50:
        output_label.config(text=f"{searchstr} \n {len(searchstr)} / 50", fg="white",bg="gray")
        window.clipboard_clear()
        window.clipboard_append(searchstr)
    else:
        output_label.config(text=f"{searchstr} \n {len(searchstr)} / 50", fg="red", bg="gray")

window = tk.Tk()

window.resizable(width=False, height=False)

window.title(" Генератор строки поиска.")

window.geometry('720x360')

window["bg"] = "gray"

input_label = tk.Label(window, text="Введите нужные сокеты", font=("Arial_Bold", 15), fg="white", bg="gray")
input_label.place(x=250, y=20)

output_label = tk.Label(window, text="", font=("Arial_Bold", 15), fg="black", bg="gray")
output_label.place(relx=0.5, rely=0.3, anchor=CENTER)

links = tk.Entry(fg="black", width=47)
links.place(x=220, y=170)

btn1 = tk.Button(window, text="Сгенерировать", command=SearchGen, width=40, height=2, fg="black", bg="gray")
btn1.place(x=220, y=220)

btn2 = tk.Button(window, text="Сгенерировать", command=SearchGen, width=40, height=2, fg="black", bg="white")
btn2.place(x=220, y=220)

window.mainloop()

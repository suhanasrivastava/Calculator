import tkinter

root = tkinter.Tk()
root.title("Mini Calculator")

root.configure(background="gray")
a = tkinter.StringVar()


def show(c):
    a.set(a.get() + c)


def clear():
    e1.delete("0", "end")


def addition():
    first_num = e1.get()
    global f_num
    global math
    math = 'addition'
    f_num = float(first_num)
    e1.delete('0', 'end')


def subtraction():
    first_num = e1.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = float(first_num)
    e1.delete('0', 'end')


def multiplication():
    first_num = e1.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = float(first_num)
    e1.delete('0', 'end')


def division():
    first_num = e1.get()
    global f_num
    global math
    math = 'division'
    f_num = float(first_num)
    e1.delete('0', 'end')


def remainder():
    first_num = e1.get()
    global f_num
    global math
    math = 'remainder'
    f_num = int(first_num)
    e1.delete('0', 'end')


def power():
    first_num = e1.get()
    global f_num
    global math
    math = 'power'
    f_num = int(first_num)
    e1.delete('0', 'end')


def equal_button():
    sec_num = e1.get()
    e1.delete('0', 'end')
    if (math == 'addition'):
        e1.insert('0', f_num + float(sec_num))
    if (math == 'subtraction'):
        e1.insert('0', f_num - float(sec_num))
    if (math == 'multiplication'):
        e1.insert('0', f_num * float(sec_num))
    if (math == 'division'):
        try:
            e1.insert('0', f_num / float(sec_num))
        except:
            print("invalid input")
    if (math == 'remainder'):
        try:
            e1.insert('0', f_num % int(sec_num))
        except:
            print("invalid input")
    if (math == 'power'):
        e1.insert(0, pow(f_num, int(sec_num)))


e1 = tkinter.Entry(root, font=("Arial", 20), justify="right", textvariable=a)
e1.grid(row=0, column=0, columnspan=4, pady=1, ipady=1)

b1 = tkinter.Button(root, text="7", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b1.grid(row=1, column=0)
b1.configure(command=lambda: show("7"))
b2 = tkinter.Button(root, text="8", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b2.grid(row=1, column=1)
b2.configure(command=lambda: show("8"))
b3 = tkinter.Button(root, text="9", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b3.grid(row=1, column=2)
b3.configure(command=lambda: show("9"))
b4 = tkinter.Button(root, text="+", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b4.grid(row=1, column=3)
b4.configure(command=addition)

b5 = tkinter.Button(root, text="4", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b5.grid(row=2, column=0)
b5.configure(command=lambda: show("4"))
b6 = tkinter.Button(root, text="5", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b6.grid(row=2, column=1)
b6.configure(command=lambda: show("5"))
b7 = tkinter.Button(root, text="6", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b7.grid(row=2, column=2)
b7.configure(command=lambda: show("6"))
b8 = tkinter.Button(root, text="-", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b8.grid(row=2, column=3)
b8.configure(command=subtraction)

b9 = tkinter.Button(root, text="1", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b9.grid(row=3, column=0)
b9.configure(command=lambda: show("1"))
b10 = tkinter.Button(root, text="2", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b10.grid(row=3, column=1)
b10.configure(command=lambda: show("2"))
b11 = tkinter.Button(root, text="3", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b11.grid(row=3, column=2)
b11.configure(command=lambda: show("3"))
b12 = tkinter.Button(root, text="*", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b12.grid(row=3, column=3)
b12.configure(command=multiplication)

b13 = tkinter.Button(root, text="C", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black', command=clear)
b13.grid(row=4, column=0)
b14 = tkinter.Button(root, text="0", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b14.grid(row=4, column=1)
b14.configure(command=lambda: show("0"))
b15 = tkinter.Button(root, text="=", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b15.grid(row=4, column=2)
b15.configure(command=equal_button)
b16 = tkinter.Button(root, text="/", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b16.grid(row=4, column=3)
b16.configure(command=division)

b17 = tkinter.Button(root, text="pow", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b17.grid(row=5, column=0)
b17.configure(command=power)
b18 = tkinter.Button(root, text="00", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b18.grid(row=5, column=1)
b18.configure(command=lambda: show("00"))
b19 = tkinter.Button(root, text=".", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b19.grid(row=5, column=2)
b19.configure(command=lambda: show("."))
b20 = tkinter.Button(root, text="%", width=3, padx=18, pady=5, bg='gray', font=('Arial', 10), fg='black')
b20.grid(row=5, column=3)
b20.configure(command=remainder)

root.mainloop()
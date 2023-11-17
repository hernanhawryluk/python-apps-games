import tkinter as tk


def keydown(e):
    if e.char == "1":
        click_1()
    elif e.char == "2":
        click_2()
    elif e.char == "3":
        click_3()
    elif e.char == "4":
        click_4()
    elif e.char == "5":
        click_5()
    elif e.char == "6":
        click_6()
    elif e.char == "7":
        click_7()
    elif e.char == "8":
        click_8()
    elif e.char == "9":
        click_9()
    elif e.char == "0":
        click_0()
    elif e.char == ".":
        click_dot()
    elif e.char == "+":
        click_add()
    elif e.char == "-":
        click_minus()
    elif e.char == "*":
        click_multi()
    elif e.char == "/":
        click_divide()
    elif e.char == "(":
        input.insert(50, "(")
        pare.append("(")
        pare.remove(")")
    elif e.char == ")":
        input.insert(50, ")")
        pare.append(")")
        pare.remove("(")
    elif e.keycode == 8:
        click_AC()
    elif e.keycode == 46:
        click_AC()
    elif e.keycode == 13:
        click_equal()
    else:
        pass


pare = [")"]

window = tk.Tk()
window.title("Calculadora")
window.geometry("388x510")
window.resizable(False, False)
window.bind("<KeyPress>", keydown)

input = tk.Entry(
    window, width=14, font=("Comic Sans MS", 38), justify="right", text="0"
)
input.place(x=20, y=12)
input.insert(0, "")
# entry.config(text="")


def click_AC():
    input.delete(0, "end")


button_AC = tk.Button(window, width=6, height=3, text="AC", command=click_AC)
button_AC.place(x=18, y=100)


def click_parenthesis():
    if ")" in pare:
        input.insert(50, "(")
        pare.append("(")
        pare.remove(")")
    elif "(" in pare:
        input.insert(50, ")")
        pare.append(")")
        pare.remove("(")


button_parenthesis = tk.Button(
    window, width=6, height=3, text="( )", command=click_parenthesis
)
button_parenthesis.place(x=106, y=100)


def click_divide():
    input.insert(50, "÷")


button_divide = tk.Button(window, width=6, height=3, text="÷", command=click_divide)
button_divide.place(x=194, y=100)


def click_multi():
    input.insert(50, "x")


button_multi = tk.Button(window, width=6, height=3, text="x", command=click_multi)
button_multi.place(x=282, y=100)


def click_7():
    input.insert(50, "7")


button_7 = tk.Button(window, width=6, height=3, text="7", command=click_7)
button_7.place(x=18, y=176)


def click_8():
    input.insert(50, "8")


button_8 = tk.Button(window, width=6, height=3, text="8", command=click_8)
button_8.place(x=106, y=176)


def click_9():
    input.insert(50, "9")


button_9 = tk.Button(window, width=6, height=3, text="9", command=click_9)
button_9.place(x=194, y=176)


def click_minus():
    input.insert(50, "-")


button_minus = tk.Button(window, width=6, height=3, text="-", command=click_minus)
button_minus.place(x=282, y=176)


def click_4():
    input.insert(50, "4")


button_4 = tk.Button(window, width=6, height=3, text="4", command=click_4)
button_4.place(x=18, y=252)


def click_5():
    input.insert(50, "5")


button_5 = tk.Button(window, width=6, height=3, text="5", command=click_5)
button_5.place(x=106, y=252)


def click_6():
    input.insert(50, "6")


button_6 = tk.Button(window, width=6, height=3, text="6", command=click_6)
button_6.place(x=194, y=252)


def click_add():
    input.insert(50, "+")


button_add = tk.Button(window, width=6, height=3, text="+", command=click_add)
button_add.place(x=282, y=252)


def click_1():
    input.insert(50, "1")


button_1 = tk.Button(window, width=6, height=3, text="1", command=click_1)
button_1.place(x=18, y=328)


def click_2():
    input.insert(50, "2")


button_2 = tk.Button(window, width=6, height=3, text="2", command=click_2)
button_2.place(x=106, y=328)


def click_3():
    input.insert(50, "3")


button_3 = tk.Button(window, width=6, height=3, text="3", command=click_3)
button_3.place(x=194, y=328)


def click_equal():
    equal = input.get()
    equal = equal.replace("x", "*", -1)
    equal = equal.replace("÷", "/", -1)
    equal = eval(equal)
    input.delete(0, 50)
    input.insert(0, equal)


button_equal = tk.Button(window, width=6, height=8, text="=", command=click_equal)
button_equal.place(x=282, y=328)


def click_0():
    input.insert(50, "0")


button_0 = tk.Button(window, width=20, height=3, text="0", command=click_0)
button_0.place(x=18, y=408)


def click_dot():
    input.insert(50, ".")


button_dot = tk.Button(window, width=6, height=3, text=".", command=click_dot)
button_dot.place(x=194, y=408)

window.mainloop()

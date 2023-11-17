from cgitb import reset
import tkinter
import tkinter.ttk
from tkinter import messagebox
import random
import time


numbers = [1, 2, 3, 4, 5, 6, 7, 8 ,9]
total = []
total_opponent = []
win_lose = False

def game():
    time.sleep(0.5)
    if (1 in total_opponent) and (2 in total_opponent) and (3 not in total):
        if random.randint(1,10) < 10:
            marking(3)
        else:
            random_game()
    elif (2 in total_opponent) and (3 in total_opponent) and (1 not in total):
        if random.randint(1,10) < 10:
            marking(1)
        else:
            random_game()
    elif (4 in total_opponent) and (5 in total_opponent) and (6 not in total):
        if random.randint(1,10) < 10:
            marking(6)
        else:
            random_game()
    elif (5 in total_opponent) and (6 in total_opponent) and (4 not in total):
        if random.randint(1,10) < 10:
            marking(4)
        else:
            random_game()
    elif (7 in total_opponent) and (8 in total_opponent) and (9 not in total):
        if random.randint(1,10) < 10:
            marking(9)
        else:
            random_game()
    elif (8 in total_opponent) and (9 in total_opponent) and (7 not in total):
        if random.randint(1,10) < 10:
            marking(7)
        else:
            random_game()
    elif (1 in total_opponent) and (4 in total_opponent) and (7 not in total):
        if random.randint(1,10) < 10:
            marking(7)
        else:
            random_game()
    elif (4 in total_opponent) and (7 in total_opponent) and (1 not in total):
        if random.randint(1,10) < 10:
            marking(1)
        else:
            random_game()
    elif (2 in total_opponent) and (5 in total_opponent) and (8 not in total):
        if random.randint(1,10) < 10:
            marking(8)
        else:
            random_game()
    elif (2 in total_opponent) and (8 in total_opponent) and (2 not in total):
        if random.randint(1,10) < 10:
            marking(2)
        else:
            random_game()
    elif (3 in total_opponent) and (6 in total_opponent) and (9 not in total):
        if random.randint(1,10) < 10:
            marking(9)
        else:
            random_game()
    elif (6 in total_opponent) and (9 in total_opponent) and (3 not in total):
        if random.randint(1,10) < 10:
            marking(3)
        else:
            random_game()
    elif (1 in total_opponent) and (5 in total_opponent) and (9 not in total):
        if random.randint(1,10) < 10:
            marking(9)
        else:
            random_game()
    elif (5 in total_opponent) and (9 in total_opponent) and (1 not in total):
        if random.randint(1,10) < 10:
            marking(1)
        else:
            random_game()
    elif (3 in total_opponent) and (5 in total_opponent) and (7 not in total):
        if random.randint(1,10) < 10:
            marking(7)
        else:
            random_game()
    elif (5 in total_opponent) and (7 in total_opponent) and (9 not in total):
        if random.randint(1,10) < 10:
            marking(9)
        else:
            random_game()
    elif (1 in total_opponent) and (9 in total_opponent) and (5 not in total):
        if random.randint(1,10) < 10:
            marking(5)
        else:
            random_game()
    elif (2 in total_opponent) and (8 in total_opponent) and (5 not in total):
        if random.randint(1,10) < 10:
            marking(5)
        else:
            random_game()
    elif (7 in total_opponent) and (3 in total_opponent) and (5 not in total):
        if random.randint(1,10) < 10:
            marking(5)
        else:
            random_game()
    elif (4 in total_opponent) and (6 in total_opponent) and (5 not in total):
        if random.randint(1,10) < 10:
            marking(5)
        else:
            random_game()
    elif (1 in total_opponent) and (7 in total_opponent) and (4 not in total):
        if random.randint(1,10) < 10:
            marking(4)
        else:
            random_game()
    elif (2 in total_opponent) and (8 in total_opponent) and (5 not in total):
        if random.randint(1,10) < 10:
            marking(5)
        else:
            random_game()
    elif (3 in total_opponent) and (9 in total_opponent) and (3 not in total):
        if random.randint(1,10) < 10:
            marking(6)
        else:
            random_game()
    elif (1 in total_opponent) and (3 in total_opponent) and (2 not in total):
        if random.randint(1,10) < 10:
            marking(2)
        else:
            random_game()
    elif (4 in total_opponent) and (6 in total_opponent) and (5 not in total):
        if random.randint(1,10) < 10:
            marking(5)
        else:
            random_game()
    elif (7 in total_opponent) and (9 in total_opponent) and (8 not in total):
        if random.randint(1,10) < 10:
            marking(8)
        else:
            random_game()
    elif (1 in total) and (2 in total) and (3 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(3)
        else:
            random_game()
    elif (2 in total) and (3 in total) and (1 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(1)
        else:
            random_game()
    elif (4 in total) and (5 in total) and (6 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(6)
        else:
            random_game()
    elif (5 in total) and (6 in total) and (4 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(4)
        else:
            random_game()
    elif (7 in total) and (8 in total) and (9 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(9)
        else:
            random_game()
    elif (8 in total) and (9 in total) and (7 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(7)
        else:
            random_game()
    elif (1 in total) and (4 in total) and (7 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(7)
        else:
            random_game()
    elif (4 in total) and (7 in total) and (1 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(1)
        else:
            random_game()
    elif (2 in total) and (5 in total) and (8 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(8)
        else:
            random_game()
    elif (5 in total) and (8 in total) and (2 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(2)
        else:
            random_game()
    elif (3 in total) and (6 in total) and (9 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(9)
        else:
            random_game()
    elif (6 in total) and (9 in total) and (3 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(3)
        else:
            random_game()
    elif (1 in total) and (5 in total) and (9 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(9)
        else:
            random_game()
    elif (5 in total) and (9 in total) and (1 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(1)
        else:
            random_game()
    elif (3 in total) and (5 in total) and (7 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(7)
        else:
            random_game()
    elif (7 in total) and (5 in total) and (3 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(3)
        else:
            random_game()
    elif (1 in total) and (3 in total) and (2 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(2)
        else:
            random_game()
    elif (4 in total) and (6 in total) and (5 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(5)
        else:
            random_game()
    elif (7 in total) and (9 in total) and (8 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(8)
        else:
            random_game()
    elif (1 in total) and (7 in total) and (4 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(4)
        else:
            random_game()
    elif (2 in total) and (8 in total) and (5 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(5)
        else:
            random_game()
    elif (3 in total) and (9 in total) and (6 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(6)
        else:
            random_game()
    elif (1 in total) and (9 in total) and (5 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(5)
        else:
            random_game()
    elif (3 in total) and (7 in total) and (2 not in total_opponent):
        if random.randint(1,10) < 10:
            marking(5)
        else:
            random_game()
    else:
        if (5 in numbers) and (5 not in total):
            if random.randint(1,10) < 9:
                marking(5)
            else:
                random_game()
        else:
            random_game()

def random_game():
    if len(numbers) >= 1:
        random_pick = random.choice(numbers)
        marking(random_pick)
    else:
        pass

def marking(random_pick):
    if len(numbers) > 0:
        if random_pick == 1:
            button1.configure(bg="red", fg="red")
            total_opponent.append(random_pick)
            numbers.remove(random_pick)
            check_opponent()
        elif random_pick == 2:
            button2.configure(bg="red", fg="red")
            total_opponent.append(random_pick)
            numbers.remove(random_pick)
            check_opponent()
        elif random_pick == 3:
            button3.configure(bg="red", fg="red")
            total_opponent.append(random_pick)
            numbers.remove(random_pick)
            check_opponent()
        elif random_pick == 4:
            button4.configure(bg="red", fg="red")
            total_opponent.append(random_pick)
            numbers.remove(random_pick)
            check_opponent()
        elif random_pick == 5:
            button5.configure(bg="red", fg="red")
            total_opponent.append(random_pick)
            numbers.remove(random_pick)
            check_opponent()
        elif random_pick == 6:
            button6.configure(bg="red", fg="red")
            total_opponent.append(random_pick)
            numbers.remove(random_pick)
            check_opponent()
        elif random_pick == 7:
            button7.configure(bg="red", fg="red")
            total_opponent.append(random_pick)
            numbers.remove(random_pick)
            check_opponent()
        elif random_pick == 8:
            button8.configure(bg="red", fg="red")
            total_opponent.append(random_pick)
            numbers.remove(random_pick)
            check_opponent()
        elif random_pick == 9:
            button9.configure(bg="red", fg="red")
            total_opponent.append(random_pick)
            numbers.remove(random_pick)
            check_opponent()
    else:
        pass
    

def check():
    if (1 in total) and (2 in total) and (3 in total):
        message_box = tkinter.messagebox.showwarning("Ganaste","Haz ganado la partida.")
    elif(4 in total) and (5 in total) and (6 in total):
        message_box = tkinter.messagebox.showwarning("Ganaste","Haz ganado la partida.")
    elif (7 in total) and (8 in total) and (9 in total):
        message_box = tkinter.messagebox.showwarning("Ganaste","Haz ganado la partida.")
    elif(1 in total) and (4 in total) and (7 in total):
        message_box = tkinter.messagebox.showwarning("Ganaste","Haz ganado la partida.")
    elif (2 in total) and (5 in total) and (8 in total):
        message_box = tkinter.messagebox.showwarning("Ganaste","Haz ganado la partida.")
    elif (3 in total) and (6 in total) and (9 in total):
        message_box = tkinter.messagebox.showwarning("Ganaste","Haz ganado la partida.")        
    elif (1 in total) and (5 in total) and (9 in total):
        message_box = tkinter.messagebox.showwarning("Ganaste","Haz ganado la partida.")
    elif (3 in total) and (5 in total) and (7 in total):
        message_box = tkinter.messagebox.showwarning("Ganaste","Haz ganado la partida.")        
    else:
        pass

def check_opponent():
    if (1 in total_opponent) and (2 in total_opponent) and (3 in total_opponent):
        message_box = tkinter.messagebox.showwarning("Perdiste","Haz perdido la partida.")
        win_lose.var = True
        return win_lose
    elif(4 in total_opponent) and (5 in total_opponent) and (6 in total_opponent):
        message_box = tkinter.messagebox.showwarning("Perdiste","Haz perdido la partida.")
        win_lose = True
        return win_lose
    elif (7 in total_opponent) and (8 in total_opponent) and (9 in total_opponent):
        message_box = tkinter.messagebox.showwarning("Perdiste","Haz perdido la partida.")
        win_lose = True
        return win_lose
    elif(1 in total_opponent) and (4 in total_opponent) and (7 in total_opponent):
        message_box = tkinter.messagebox.showwarning("Perdiste","Haz perdido la partida.")
        win_lose = True
        return win_lose
    elif (2 in total_opponent) and (5 in total_opponent) and (8 in total_opponent):
        message_box = tkinter.messagebox.showwarning("Perdiste","Haz perdido la partida.")
        win_lose = True
        return win_lose
    elif (3 in total_opponent) and (6 in total_opponent) and (9 in total_opponent):
        message_box = tkinter.messagebox.showwarning("Perdiste","Haz perdido la partida.")        
        win_lose = True
        return win_lose
    elif (1 in total_opponent) and (5 in total_opponent) and (9 in total_opponent):
        message_box = tkinter.messagebox.showwarning("Perdiste","Haz perdido la partida.")
        win_lose = True
        return win_lose
    elif (3 in total_opponent) and (5 in total_opponent) and (7 in total_opponent):
        message_box = tkinter.messagebox.showwarning("Perdiste","Haz perdido la partida.")
        win_lose = True
        return win_lose
    else:
        pass

window = tkinter.Tk()
window.title("Ta Te Ti")
window.geometry("450x450")

def button1():
    if (1 in numbers) and (1 not in total_opponent):
        button1.configure(bg="green", fg="red")
        numbers.remove(1)
        total.append(1)
        check()
        if win_lose == False:
            game()
    else:
        message_box = tkinter.messagebox.showerror("Error","Ya se encuentra marcado.")
button1 = tkinter.Button(window, width=15, height=5, command=button1)
button1.grid(padx=10, pady=10, row=0, column=0)

def button2():
    if (2 in numbers) and (2 not in total_opponent):
        button2.configure(bg="green", fg="red")
        numbers.remove(2)
        total.append(2)
        check()
        if win_lose == False:
            game()
    else:
        message_box = tkinter.messagebox.showerror("Error","Ya se encuentra marcado.")
button2 = tkinter.Button(window, width=15, height=5, command=button2)
button2.grid(padx=10, pady=10, row=0, column= 1)

def button3():
    if (3 in numbers) and (3 not in total_opponent):
        button3.configure(bg="green", fg="red")
        numbers.remove(3)
        total.append(3)
        check()
        if win_lose == False:
            game()
    else:
        message_box = tkinter.messagebox.showerror("Error","Ya se encuentra marcado.")
button3 = tkinter.Button(window, width=15, height=5, command=button3)
button3.grid(padx=10, pady=10, row=0, column= 2)

def button4():
    if (4 in numbers) and (4 not in total_opponent):
        button4.configure(bg="green", fg="red")
        numbers.remove(4)
        total.append(4)
        check()
        if win_lose == False:
            game()
    else:
        message_box = tkinter.messagebox.showerror("Error","Ya se encuentra marcado.")
button4 = tkinter.Button(window, width=15, height=5, command=button4)
button4.grid(padx=10, pady=10, row=2, column=0)

def button5():
    if (5 in numbers) and (5 not in total_opponent):
        button5.configure(bg="green", fg="red")
        numbers.remove(5)
        total.append(5)
        check()
        if win_lose == False:
            game()
    else:
        message_box = tkinter.messagebox.showerror("Error","Ya se encuentra marcado.")
button5 = tkinter.Button(window, width=15, height=5, command=button5)
button5.grid(padx=10, pady=10, row=2, column= 1)

def button6():
    if (6 in numbers) and (6 not in total_opponent):
        button6.configure(bg="green", fg="red")
        numbers.remove(6)
        total.append(6)
        check()
        if win_lose == False:
            game()
    else:
        message_box = tkinter.messagebox.showerror("Error","Ya se encuentra marcado.")
button6 = tkinter.Button(window, width=15, height=5, command=button6)
button6.grid(padx=10, pady=10, row=2, column= 2)

def button7():
    if (7 in numbers) and (7 not in total_opponent):
        button7.configure(bg="green", fg="red")
        numbers.remove(7)
        total.append(7)
        check()
        if win_lose == False:
            game()
    else:
        message_box = tkinter.messagebox.showerror("Error","Ya se encuentra marcado.")
button7 = tkinter.Button(window, width=15, height=5, command=button7)
button7.grid(padx=10, pady=10, row=3, column=0)

def button8():
    if (8 in numbers) and (8 not in total_opponent):
        button8.configure(bg="green", fg="red")
        numbers.remove(8)
        total.append(8)
        check()
        if win_lose == False:
            game()
    else:
        message_box = tkinter.messagebox.showerror("Error","Ya se encuentra marcado.")
button8 = tkinter.Button(window, width=15, height=5, command=button8)
button8.grid(padx=10, pady=10, row=3, column= 1)

def button9():
    if (9 in numbers) and (9 not in total_opponent):
        button9.configure(bg="green", fg="red")
        numbers.remove(9)
        total.append(9)
        check()
        if win_lose == False:
            game()
    else:
        message_box = tkinter.messagebox.showerror("Error","Ya se encuentra marcado.")
button9 = tkinter.Button(window, width=15, height=5, command=button9)
button9.grid(padx=10, pady=10, row=3, column= 2)

def button10():
    for i in range(1,10):
        if i in numbers:
            numbers.remove(i)
    for i in range(1,10):
        numbers.append(i)
    for i in range(1,10):
        if i in total:
            total.remove(i)
    for i in range(1,10):
        if i in total_opponent:
            total_opponent.remove(i)
    win_lose = False
    button1.configure(bg="SystemButtonFace", fg="Black")
    button2.configure(bg="SystemButtonFace", fg="Black")
    button3.configure(bg="SystemButtonFace", fg="Black")
    button4.configure(bg="SystemButtonFace", fg="Black")
    button5.configure(bg="SystemButtonFace", fg="Black")
    button6.configure(bg="SystemButtonFace", fg="Black")
    button7.configure(bg="SystemButtonFace", fg="Black")
    button8.configure(bg="SystemButtonFace", fg="Black")
    button9.configure(bg="SystemButtonFace", fg="Black")
    if 1 == random.randint(1,2):
        game()
    else:
        pass
button10 = tkinter.Button(window, text="Empezar", width=15, height=1, command=button10)
button10.grid(padx=10, pady=10, row=4, column= 0)

txt = tkinter.Entry(window, width=15, state="disabled")
txt.grid(padx=10, pady=10, row=4, column= 1)
txt.focus()

def button11():
    window.destroy()
button11 = tkinter.Button(window, text="Salir", width=15, height=1, command=button11)
button11.grid(padx=10, pady=10, row=4, column=2)

window.mainloop()

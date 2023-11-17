import tkinter
import tkinter.ttk
import time
import threading
from turtle import st

clock_paused = False
countdown_finished = True


def run(how_many):
    global clock_paused
    global countdown_finished
    inst = MainApplication(window)
    inst.button["text"] = "Pausar"
    timer = how_many
    total_seconds = int(timer[:1]) * 60
    while total_seconds >= 0:
        if clock_paused == True:
            continue
        else:
            hours = int(0)
            minutes = int(0)
            seconds = int(0)
            total_seconds -= 1
            if total_seconds >= 3600:
                hours = total_seconds // 3600
                minutes = total_seconds - 3600
                minutes = minutes // 60
                seconds = total_seconds - (hours * 3600)
                seconds = seconds - (minutes * 60)
            elif total_seconds >= 60:
                hours = 0
                minutes = total_seconds // 60
                seconds = total_seconds - (minutes * 60)
            elif total_seconds > 0:
                hours = 0
                minutes = 0
                seconds = total_seconds

        hours = str(hours)
        minutes = str(minutes)
        seconds = str(seconds)
        if len(hours) == 1:
            hours = "0" + hours
        if len(minutes) == 1:
            minutes = "0" + minutes
        if len(seconds) == 1:
            seconds = "0" + seconds

        to_print = hours + ":" + minutes + ":" + seconds
        inst.label_variable.set(to_print)
        time.sleep(1)
    countdown_finished = True
    inst.button["text"] = "Empezar"


class MainApplication(tkinter.Frame):
    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.label = tkinter.Label(window, text="Cuenta regresiva:")
        self.label.place(x=15, y=15)
        self.prog_timer = []
        self.prog_timer.append("1 minuto")
        for i in range(2, 61):
            if i == 1:
                self.prog_timer.append("1 minuto")
            self.prog_timer.append(str(i) + " minutos")
        self.combobox = tkinter.ttk.Combobox(
            window, values=(self.prog_timer), width=9, font=("", 12)
        )
        self.combobox.place(x=127, y=14)
        self.combobox.current(0)

        self.label_variable = tkinter.StringVar()
        self.label_variable.set("00:00:00")
        self.labeltimer = tkinter.Label(
            window, font=("", 40), textvariable=self.label_variable
        )
        self.labeltimer.place(x=35, y=40)

        self.button = tkinter.Button(
            window, text="Empezar", width=9, command=self.click_button
        )
        self.button.place(x=60, y=100)

    def click_button(self):
        global clock_paused
        global countdown_finished
        if countdown_finished == True:
            self.button["text"] = "Pausar"
            countdown_finished = False
            how_many = self.combobox.get()
            t1 = threading.Thread(target=run, args=(how_many,))
            t1.start()
        else:
            if clock_paused == True:
                clock_paused = False
                self.button["text"] = "Pausar"
            else:
                clock_paused = True
                self.button["text"] = "Empezar"


if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("Timer")
    window.geometry("240x155")
    window.resizable(False, False)

    MainApplication(window).pack(side="top", fill="both", expand=True)
    window.mainloop()

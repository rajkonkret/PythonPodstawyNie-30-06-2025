import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label1 = tkinter.Label(self.main_window, text="Witaj Świecie")
        self.label2 = tkinter.Label(self.main_window, text="Witaj Świecie")

        self.label1.pack(side="left")
        self.label2.pack(side="right")

        tkinter.mainloop()


my_gui = MyGui()

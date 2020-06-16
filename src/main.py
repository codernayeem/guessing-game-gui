from tkinter import *
import tkinter.messagebox


class Application:
    def __init__(self, master):
        self.master = master
        master.title('Gussing game')

        self.left = Frame(master, width=500, height=450, bg='lightgreen')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=300, height=450, bg='steelblue')
        self.right.pack(side=RIGHT)

        Label(self.left, text='Guessing Game', font='arial 27 bold', fg='black', bg='lightgreen').place(x=10, y=10)
        Label(self.right, text='Config', font='arial 21 bold', fg='black', bg='steelblue').place(x=10, y=10)
        Label(self.right, text='Minimum', font='arial 16 bold', fg='black', bg='steelblue').place(x=10, y=100)
        Label(self.right, text='Maximum', font='arial 16 bold', fg='black', bg='steelblue').place(x=10, y=140)
        self.min_ent = Entry(self.right, width=10, font='arial 16')
        self.min_ent.place(x=120, y=100)
        self.max_ent = Entry(self.right, width=10, font='arial 16')
        self.max_ent.place(x=120, y=140)
        Button(self.right, width=9, bg='green', font='arial 16', text='Set', command=self.set_config).place(x=120, y=180)

        self.info_text = Label(self.left, font='arial 17 bold', fg='black', bg='lightgreen')
        self.info_text.place(x=10, y=55)
        self.ques = Label(self.left, font='arial 16', fg='black', bg='lightgreen')
        self.ques.place(x=10, y=200)
        self.yes = Button(self.left, text='Yes', width=16, bg='green', font='arial 19')
        self.yes.place(x=0, y=400)
        self.no = Button(self.left, text='No', width=16, bg='red', font='arial 19')
        self.no.place(x=248, y=400)

        self.set_default_config()
        self.reset()

    def set_default_config(self):
        self.min_ent.delete(0, END)
        self.max_ent.delete(0, END)
        global range_list
        self.min_ent.insert(0, '0')
        self.max_ent.insert(0, '100')

    def set_config(self):
        # coming soon
        self.set_default_config()

    def reset(self):
        self.ques.configure(text="Are you Ready?")
        pass
    
root = Tk()
b = Application(root)
root.geometry("800x450+0+0")
root.resizable(False, False)

root.mainloop()

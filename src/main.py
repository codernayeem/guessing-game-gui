from tkinter import *
import tkinter.messagebox

minimum = 1
maximum = 100
range_list = [minimum, maximum]


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
        self.min_ent.insert(0, str(range_list[0]))
        self.max_ent.insert(0, str(range_list[1]))

    def set_config(self):
        try:
            self.val1 = int(self.min_ent.get())
            self.val2 = int(self.max_ent.get())

            if self.val1 > self.val2:
                tkinter.messagebox.showwarning('Warning', 'Minimum value can not be larger than maximum value.')
            elif self.val1 == self.val2:
                tkinter.messagebox.showwarning('Warning', 'Minimum value and maximum value can not be same.')
            else:
                global range_list
                range_list[0] = self.val1
                range_list[1] = self.val2
                self.reset()
        except:
            tkinter.messagebox.showerror('Error', 'Your input was\'t valid. Please, try again.')
            self.set_default_config()

    def reset(self):
        global minimum, maximum, range_list
        minimum = range_list[0]
        maximum = range_list[1]
        self.info_text.configure(text=f'Guess a number between {range_list[0]} and {range_list[1]}.')
        self.ques.configure(text='Are you ready?')
        self.yes.configure(text='Yes', command=self.ready)
        self.no.configure(text='No', command=root.destroy)
    
    def ready(self):
        self.yes.configure(command=self.yes_click)
        self.no.configure(command=self.no_click)
        self.make_ques()

    def make_ques(self):
        if not self.check_last():
            global minimum, maximum
            self.ques.configure(text=f'Is your number is between {minimum} and {(minimum + maximum) // 2}?')

    def yes_click(self):
        global maximum, minimum
        maximum = (minimum + maximum) // 2
        self.make_ques()
        
    def no_click(self):
        global maximum, minimum
        minimum = (minimum + maximum) // 2 + 1
        self.make_ques()

    def check_last(self):
        global maximum, minimum
        if maximum - minimum == 1:
            self.ques.configure(text=f'Is your number is between {maximum} and {maximum+1}?')
            self.yes.configure(command=lambda: self.result(maximum))
            self.no.configure(command=lambda: self.result(minimum))
            return True
        elif maximum == minimum:
            self.result(maximum)
            return True
        else:
            return False
    
    def result(self, res):
        self.ques.configure(text=f'Ha! Got it. Your guessed number is {res}.')
        self.yes.configure(text='Play again', command=self.reset)
        self.no.configure(text='Exit', command=root.destroy)


root = Tk()
b = Application(root)
root.geometry("800x450+0+0")
root.resizable(False, False)

root.mainloop()

# imports
from tkinter import *
import tkinter.messagebox

# default minimum and maximum value
minimum, maximum = 1, 100

range_list = [minimum, maximum]


class Application:
    def __init__(self, master):
        ''' Initialize Game Screen '''

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
        ''' Set default configuration to Screen '''

        self.min_ent.delete(0, END)
        self.max_ent.delete(0, END)
        self.min_ent.insert(0, str(range_list[0]))
        self.max_ent.insert(0, str(range_list[1]))

    def set_config(self):
        ''' Set configuration to Screen '''

        try:
            val_min = int(self.min_ent.get())
            val_max = int(self.max_ent.get())

            if val_min > val_max:
                tkinter.messagebox.showwarning('Warning', 'Minimum value can not be larger than maximum value.')
            elif val_min == val_max:
                tkinter.messagebox.showwarning('Warning', 'Minimum value and maximum value can not be same.')
            else:
                global range_list
                range_list = [val_min, val_max]
                self.reset()
        except:
            tkinter.messagebox.showerror('Error', "Your input was't valid. Please, try again.")
            self.set_default_config()

    def reset(self):
        ''' Reset Game and Start Again '''

        global minimum, maximum
        minimum = range_list[0]
        maximum = range_list[1]

        self.info_text.configure(text=f'Guess a number between {minimum} and {maximum}.')
        self.ques.configure(text='Are you ready?')
        self.yes.configure(text='Yes', command=self.ready)
        self.no.configure(text='Exit', command=root.destroy)
    
    def ready(self):
        ''' Start asking question '''

        self.yes.configure(command=self.yes_click)
        self.no.configure(text='No', command=self.no_click)
        self.make_ques()

    def make_ques(self):
        ''' Make Questions '''

        if not self.check_last():
            self.ques.configure(text=f'Is your number between {minimum} and {(minimum + maximum) // 2}?')

    def yes_click(self):
        ''' Set maximum value on YES click '''

        global maximum
        maximum = (minimum + maximum) // 2
        self.make_ques()
        
    def no_click(self):
        ''' Set minimum value on NO click '''
        
        global minimum
        minimum = (minimum + maximum) // 2 + 1
        self.make_ques()

    def check_last(self):
        ''' Check if it is time for the last question '''

        if maximum - minimum == 1:
            self.ques.configure(text=f'Is your number between {maximum} and {maximum+1}?')
            self.yes.configure(command=lambda: self.result(maximum))
            self.no.configure(command=lambda: self.result(minimum))
            return True
        elif maximum == minimum:
            self.result(maximum)
            return True
        return False
    
    def result(self, res):
        ''' Show the result '''

        self.ques.configure(text=f'Ha! Got it. Your guessed number is {res}.')
        self.yes.configure(text='Play again', command=self.reset)
        self.no.configure(text='Exit', command=root.destroy)


root = Tk()
application = Application(root)
root.geometry("800x450+0+0")
root.resizable(False, False)

root.mainloop()

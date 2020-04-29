#Madeleine Brown


import tkinter
import tkinter.messagebox as box
import random

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("200x200")

        # Create two frames. One for the Radiobuttons
        # and another for the regular Button widgets.
        self.radioFrame = tkinter.Frame(self.mainWindow)
        # self.middle_frame = tkinter.Frame(self.main_window)
        self.buttonFrame = tkinter.Frame(self.mainWindow)

        # Create an IntVar object to use with
        # the Radiobuttons.
        self.radioVar = tkinter.StringVar()

        # Set the intVar object to 1.
        self.radioVar.set(1)

        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = tkinter.Radiobutton(self.radioFrame, text='Rock', variable=self.radioVar, value='Rock')
        self.rb2 = tkinter.Radiobutton(self.radioFrame, text='Paper', variable=self.radioVar, value='Paper')
        self.rb3 = tkinter.Radiobutton(self.radioFrame, text='Scissors', variable = self.radioVar, value='Scissors')
        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Set up buttons
        self.okButton = tkinter.Button(self.buttonFrame, text='OK', command=self.showOption)
        self.quitButton = tkinter.Button(self.buttonFrame, text='Quit', command=self.mainWindow.destroy)

        # Pack the Buttons.
        self.okButton.pack(side='left')
        self.quitButton.pack(side='left')

        # Pack the frames.
        self.radioFrame.pack()
        self.buttonFrame.pack()

        # Start the mainloop.
        tkinter.mainloop()

    def showOption(self):
        #gets random computer choice
        compChoice = random.randint(1,3)
        if compChoice == 1:
            compChoice = 'Rock'
        elif compChoice == 2:
            compChoice = 'Paper'
        elif compChoice == 3:
            compChoice ='Scissors'
        box.showinfo('Selection', 'You selected: ' + self.radioVar.get()
                     + '\nComputer selected: ' + compChoice)

        #win/lose statements
        if compChoice == 'Rock' and self.radioVar.get() == 'Rock':
            box.showinfo('Winner', 'It was a draw!')
        elif compChoice == 'Rock' and self.radioVar.get() == 'Paper':
            box.showinfo('Winner', 'Paper covers rock. You won!')
        elif compChoice == 'Rock' and self.radioVar.get() == 'Scissors':
            box.showinfo('Winner', 'Rock crushes scissors. You lost!')
        elif compChoice == 'Paper' and self.radioVar.get() == 'Rock':
            box.showinfo('Winner', 'Paper covers rock. You lost!')
        elif compChoice == 'Paper' and self.radioVar.get() == 'Paper':
            box.showinfo('Winner', 'It was a draw!')
        elif compChoice == 'Paper' and self.radioVar.get() == 'Scissors':
            box.showinfo('Winner', 'Scissors cuts paper. You won!')
        elif compChoice == 'Scissors' and self.radioVar.get() == 'Rock':
            box.showinfo('Winner', 'Rock crushes scissors. You won!')
        elif compChoice == 'Scissors' and self.radioVar.get() == 'Paper':
            box.showinfo('Winner', 'Scissors cuts paper. You lost!')
        elif compChoice == 'Scissors' and self.radioVar.get() == 'Scissors':
            box.showinfo('Winner', 'It was a draw!')

demoGUI = MyGUI()

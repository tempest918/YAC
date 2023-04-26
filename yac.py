from tkinter import *
from tkinter import messagebox

class YAC(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("YAC")
        self.master.geometry("+300+300")
        self.master.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Create input frame
        input_frame = Frame(self.master, bg='beige')
        input_frame.grid(row=0, column=0, padx=10, pady=10)

        # Create input text widget
        self.input_text = Text(input_frame, bg='gray', fg='black', font=('OCR A Extended', 32), height=1, width=13)
        self.input_text.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Create image for solar panel
        solar_panel = PhotoImage(file='solar_panel.png')

        # Create label for solar panel
        solar_panel_label = Label(input_frame, image=solar_panel)
        solar_panel_label.image = solar_panel
        solar_panel_label.configure(text="This is how the calculator gets power, it's an enigma.")
        solar_panel_label.grid(row=1, column=2, columnspan=4, padx=0, pady=5)

        # Create history window
        history_window = Toplevel(self.master)
        history_window.title("YAC History")
        history_window.geometry("+700+300")
        history_frame = Frame(history_window, bg='black')
        history_frame.pack(padx=10, pady=10)

        # Create history text widget
        self.history_text = Text(history_frame, bg='black', fg='green', font=('Terminal', 12), height=20, width=50)
        self.history_text.pack()

        # Create image for logo
        logo = PhotoImage(file='yac.png')

        # Create label for logo
        logo_label = Label(input_frame, image=logo)
        logo_label.image = logo
        logo_label.configure(text="This is the logo for YAC, seems clicky.")
        logo_label.grid(row=2, column=1, padx=5, pady=5)
        logo_label.bind('<Button-1>', self.on_click)

        #Create exit button
        exit_button = Button(input_frame, text='Exit', width=10, height=3, bg='beige', command=self.master.destroy)
        exit_button.grid(row=2, column=0, padx=5, pady=5)

        # Create clear button
        clear_button = Button(input_frame, text='Clear', width=10, height=3, bg='beige', command=self.clear_equation)
        clear_button.grid(row=2, column=2, padx=5, pady=5)

        # Create buttons
        buttons = ['/', '7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', '-', '0', '.', '=']
        row = 2
        col = 3
        for button in buttons:
            Button(input_frame, text=button, width=10, height=3, bg='beige', command=lambda text=button: self.button_pressed(text)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_pressed(self, text):
        if text == '=':
            # Calculate result
            try:
                result = str(eval(self.equation))
                self.history_text.insert(END, f"{self.equation} = {result}\n")
                self.input_text.delete('1.0', END)
                self.input_text.insert(END, result)
            except:
                self.history_text.insert(END, f"{self.equation} = Error\n")
                self.input_text.delete('1.0', END)
                self.input_text.insert(END, "Error")
            self.equation = result
        elif text == 'Clear':
            self.clear_equation()
            self.input_text.delete('1.0', END)
        else:
            self.equation += text
            self.input_text.insert(END, text)

    def clear_equation(self):
        self.equation = ''
        #self.history_text.delete('1.0', END)
        self.input_text.delete('1.0', END)

            #fun stuff
    def on_click(self, event=None):
        messagebox.showinfo('Secret','YAC 1.0 created by Anthony Barnes')

    def run(self):
        self.equation = ''
        self.master.mainloop()

root = Tk()
app = YAC(root)
app.run()

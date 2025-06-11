"""
Version 1 
Program that converts temperautres.
Basic Functionality no error prevention

"""


from tkinter import *

class Converter:

    def __init__(self):
        self.root = Tk()
        self.root.title("Temperature Converter")

        self.container = Frame(self.root)
        self.container.grid(row=0,column=0,sticky="nsew")

        self.frames = {}

        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["C_to_F"] = self.create_c_to_f()
        self.frames["F_to_C"] = self.create_f_to_c()

        self.show_frame("MainFrame")

    def run(self):
        self.root.mainloop()

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def create_main_frame(self):
        frame = Frame(self.container)

        self.Temperature_Converter = Label(frame, font = "Verdana 16 bold", text="Temperature converter")
        self.Temperature_Converter.grid(row=0, columnspan=2)

        self.Navigate1 = Button(frame, text ="To Centigrade", bg="yellow", font="Verdana 12 bold", command=lambda:self.show_frame("F_to_C"))
        self.Navigate1.grid(row=1, column=0,padx=10,pady=10)
    
        self.Navigate2 = Button(frame, text ="To Fahrenheit", bg="Red", font="Verdana 12 bold", command=lambda:self.show_frame("C_to_F"))
        self.Navigate2.grid(row=1, column=1,padx=10,pady=10)
    
        frame.grid(row=0)
        return frame

    def create_c_to_f(self):
        frame = Frame(self.container)

        self.title = Label(frame, font = "Verdana 16 bold", text="Farenheit Converter")
        self.title.grid(row=0, columnspan=2)

        self.entry = Entry(frame, justify=CENTER)
        self.entry.grid(row=1, columnspan=2)

        



        frame.grid(row=0)
        return frame
    
    def create_f_to_c(self):
        pass
    

    def Centigrade_TO_Farenheiht(self):
        self.farenheit = int(self.entry.get())

if __name__ == "__main__":
    app = Converter()
    app.run()

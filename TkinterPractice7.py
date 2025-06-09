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
        
        self.Temperature_Converter = Label(Frame, font = "Verdana 16 Bold", text="Temperature converter")
        self.grid(row=0, columnspan=2)

if __name__ == "__main__":
    app = Converter()
    app.run()

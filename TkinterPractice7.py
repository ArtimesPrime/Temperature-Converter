"""
Version 2 
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

        self.a = StringVar()
        self.frames = {}

        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["C_to_F"] = self.create_c_to_f()
        self.frames["F_to_C"] = self.create_f_to_c()
        
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.show_frame("MainFrame")

    def run(self):
        self.root.mainloop()

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    
    def Calculate_F(self):
        self.farenheit = (int(self.entry1.get()) * 9/5) + 32
        self.farenheit = round(self.farenheit, 2)
        self.a.set(self.farenheit)
        
    def Calculate_C(self):
        self.centigrade = (int(self.entry.get())-32) * 5/9
        self.centigrade = round(self.centigrade, 2)
        self.a.set(self.centigrade)

    def Clear(self):
        self.a.set("")
        self.entry.delete(0)

    def create_main_frame(self):
        frame = Frame(self.container)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure([0,1], weight=1)

        self.Temperature_Converter = Label(frame, font = "Verdana 16 bold", text="Temperature converter")
        self.Temperature_Converter.grid(row=0, columnspan=2, sticky="nsew")

        self.Navigate1 = Button(frame, text ="To Centigrade", bg="yellow", font="Verdana 12 bold", command=lambda:self.show_frame("F_to_C"))
        self.Navigate1.grid(row=1, column=0,padx=10,pady=10, sticky="nsew")
    
        self.Navigate2 = Button(frame, text ="To Fahrenheit", bg="Red", font="Verdana 12 bold", command=lambda:self.show_frame("C_to_F"))
        self.Navigate2.grid(row=1, column=1,padx=10,pady=10, sticky="nsew")
    
        frame.grid(row=0, sticky="nsew")
        return frame

    def create_c_to_f(self):
        frame = Frame(self.container)
        frame.rowconfigure([0], weight=1)
        frame.columnconfigure([0,1,2], weight=1)

        self.title1 = Label(frame, font = "Verdana 16 bold", text="Centigrade to Farenheit")
        self.title1.grid(row=0, columnspan=3, sticky="nsew")

        self.entry1 = Entry(frame, justify=CENTER)
        self.entry1.grid(row=1, columnspan=3, pady=3, sticky="nsew")

        self.Calculate1 = Button(frame, font="Verdana 12 bold", text="Calculate", command= self.Calculate_F, width=9)
        self.Calculate1.grid(row=2, column=0, sticky="nsew")        

        self.Back1 = Button(frame, font="Verdana 12 bold", text="Back", command= lambda: self.show_frame("MainFrame"), width=9)
        self.Back1.grid(row=2,column=1, sticky="nsew")

        self.clear1 = Button(frame, font="Verdana 12 bold", text="Clear", command= self.Clear, width=9)
        self.clear1.grid(row=2,column=2, sticky="nsew")

        self.result1 = Label(frame, font ="Verdana 16 bold", textvariable=self.a)
        self.result1.grid(row=3, columnspan=3, sticky="nsew")

        frame.grid(row=0, sticky="nsew")
        return frame
    
    def create_f_to_c(self):
        frame = Frame(self.container)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure([0,1,2], weight=1)

        self.title = Label(frame, font = "Verdana 16 bold", text="Farenheit to Centigrade")
        self.title.grid(row=0, columnspan=3, sticky="nsew")

        self.entry = Entry(frame, justify=CENTER)
        self.entry.grid(row=1, columnspan=3, pady=3, sticky="nsew")

        self.Calculate = Button(frame, font="Verdana 12 bold", text="Calculate", command= self.Calculate_C, width=9)
        self.Calculate.grid(row=2, column=0, sticky="nsew")        

        self.Back = Button(frame, font="Verdana 12 bold", text="Back", command= lambda: self.show_frame("MainFrame"), width=9)
        self.Back.grid(row=2,column=1, sticky="nsew")

        self.clear = Button(frame, font="Verdana 12 bold", text="Clear", command= self.Clear, width=9)
        self.clear.grid(row=2,column=2, sticky="nsew")

        self.result = Label(frame, font ="Verdana 16 bold", textvariable=self.a)
        self.result.grid(row=3, columnspan=3, sticky="nsew")

        frame.grid(row=0, sticky="nsew")
        return frame
    
    


if __name__ == "__main__":
    app = Converter()
    app.run()



# helloworld.py
import tkinter as tk
import pygubu




class HelloWorldApp:
    
    def __init__(self):

        parameter_1 = 69

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('gui.ui')

        #3: Create the mainwindow
        self.mainwindow = builder.get_object('Frame_2')
        
    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = HelloWorldApp()
    app.run()
    
        
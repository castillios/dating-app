import tkinter

class MainWindow():
    def __init__(self):
        self.create_window()


    def create_window(self):
        self.window = tkinter.Tk()
        self.window.mainloop()



if __name__ == "__main__":
    MainWindow()
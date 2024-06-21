import tkinter as tk
import PIL


class Fullscreen_Window:

    def __init__(self):
        self.tk = tk()
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)


    def Programm_Start(self):
        print("start")

    def GUI_Spawn_Menu(self):
        print("gui spawn menü")
        img = tk.PhotoImage(Image.open('dein_bild.png'))



    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

if __name__ == '__main__':
    w = Fullscreen_Window()
    w.tk.mainloop()
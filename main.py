import tkinter as tk
import PIL


class Budencrawler:
    def __init__(self, master):
        self.master = master
        self.state = False
        root.title("Budencrawler Alpha")
        root.bind("<F11>", self.toggle_fullscreen)
        root.bind("<Escape>", self.end_fullscreen)
        self.Bild = tk.PhotoImage(file="2.png")
        #self.Bild_L = tk.Label(root, image=self.Bild)


    def Programm_Start(self):
        print("start")

    def GUI_Spawn_Menu(self):
        print("gui spawn menü")

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

if __name__ == '__main__':
    root = tk.Tk()
    width = 420
    height = 420

    def mittig_fenster(root, width, height):
        fenster_breite = root.winfo_screenwidth()
        fenster_höhe = root.winfo_screenheight()
        x = (fenster_breite - width) // 2
        y = (fenster_höhe - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}")
        root.resizable(False,False)

    mittig_fenster(root, width, height)
    Budencrawler = Budencrawler(root)
    root.mainloop()
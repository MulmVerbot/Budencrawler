import tkinter as tk
import PIL
import time
import threading

class Budencrawler:
    def __init__(self, master):
        self.master = master
        self.state = False
        self.Programm_Name = "Budencrawler"
        self.Version = "Alpha 0.0.1 (1)"
        self.Programm_läuft = True
        self.Punkte_erhöhen_thread = threading.Timer(1, self.Punkte_erhöhen)
        self.Punkte_erhöhen_thread.daemon = True
        
        
        ### fürs game
        self.Punkte = 0
        self.hat_was_gekillt = False
        self.anderes_event_fuer_Punkte = False
        self.Inventar_offen = False

        ###

        root.title("Budencrawler Alpha")
        root.bind("<F11>", self.toggle_fullscreen)
        root.bind("<Escape>", self.end_fullscreen)
        root.bind('<Return>', self.tun)
        self.Punkte_erhöhen_thread.start()
        self.GUI_Spawn_Menu()

    def Punkte_erhöhen(self):
        while self.Programm_läuft == True:
            if self.hat_was_gekillt == True:
                self.Punkte += 100
                self.hat_was_gekillt = False
                self.Punkte_l.pack_forget()
                self.Punkte_l = tk.Label(root, text=self.Punkte)
                self.Punkte_l.pack()
            if self.anderes_event_fuer_Punkte == True:
                self.Punkte += 10
                self.anderes_event_fuer_Punkte = False
                self.Punkte_l.pack_forget()
                self.Punkte_l = tk.Label(root, text=self.Punkte)
                self.Punkte_l.pack()
            time.sleep(0.70)
            

    def Programm_Start(self):
        print("start")

    def GUI_Spawn_Menu(self):
        print("gui spawn menü")
        self.Punkte_l = tk.Label(root, text=self.Punkte)
        self.Punkte_l.pack()
        self.instr = tk.Label(root, text="führe einen Befehl aus um etwas zu tun!")
        self.instr.place(x=10,y=30)

        self.tun_e = tk.Entry(root)
        self.tun_e.place(x=10,y=100)

    def tun(self, event):
        was_tun = self.tun_e.get()
        was_tun.lower()
        if was_tun:
            if was_tun == "inventar" or "inv" or "beutel" or "i":
                print("Inventar geöffnet.")
                was_tun = None
                self.Inventar_offen = True
                self.tun_e.delete(0,tk.END)

            if was_tun == "angreifen" or "agr" or "angr" or "a":
                print("etwas angreifen")
                was_tun = None
                self.anderes_event_fuer_Punkte = True



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
import tkinter as tk
from Game import Game
import os
os.system("xset r off")
class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("HILL ADVENTURE CLIMBER")
        self.canvas = tk.Canvas(self)
        self.canvas.pack()
        self.bind("<KeyPress>", self.keydown)
        self.bind("<KeyRelease>", self.keyup)
        self.mainloop()

    def keyup(self, event):
        print("Keyup", event.char)

    def keydown(self, event):
        print("Keydown", event.char)
window = GameWindow()
import ttkbootstrap as tb

from welcome_screen import WelcomeScreen
from belajar_hijaiyah import BelajarHijaiyah

class MainMenu:
    def __init__(self):
        pass

if __name__ == "__main__":
    root = tb.Window()
    welcome_screen = WelcomeScreen(root)
    #BelajarHijaiyah(root).open_main_display()
    resw = root.winfo_screenwidth()
    resh = root.winfo_screenheight()
    root.geometry(f'{resw}x{resh}')
    root.mainloop()

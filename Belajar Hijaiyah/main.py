import ttkbootstrap as tb

from welcome_screen import WelcomeScreen
from home import MainMenu
from belajar_hijaiyah import BelajarHijaiyah
from acak_huruf import AcakHuruf

if __name__ == "__main__":
    root = tb.Window()
    welcome_screen = WelcomeScreen(root)
    #MainMenu(root)
    #BelajarHijaiyah(root).open_main_display()
    #AcakHuruf(root)
    resw = root.winfo_screenwidth()
    resh = root.winfo_screenheight()
    root.geometry(f'{resw}x{resh}')
    root.mainloop()

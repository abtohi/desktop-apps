import ttkbootstrap as tb
import os
from PIL import Image, ImageTk

from welcome_screen import WelcomeScreen
from home import MainMenu
from belajar_hijaiyah import BelajarHijaiyah
from acak_huruf import AcakHuruf

if __name__ == "__main__":
    root = tb.Window()
    root.state('zoomed')
    root.title("Alifbacaku")
    #WelcomeScreen(root)
    MainMenu(root)
    #BelajarHijaiyah(root)
    #AcakHuruf(root)
    resw = root.winfo_screenwidth()
    resh = root.winfo_screenheight()
    root.geometry(f'{resw}x{resh}')
    icon_path = "images/icon/logo.png"  # Ganti dengan path ikon Anda
    img = Image.open(icon_path)
    photo = ImageTk.PhotoImage(img)
    root.tk.call('wm', 'iconphoto', root._w, photo)

    root.mainloop()

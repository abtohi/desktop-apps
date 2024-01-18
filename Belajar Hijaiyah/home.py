import ttkbootstrap as tb
from threading import Thread
from funcs import *

from belajar_hijaiyah import BelajarHijaiyah
from acak_huruf import AcakHuruf
from quiz_hijaiyah import QuizHijaiyah

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.main_frame = tb.Frame(root)
        self.main_frame.pack()

        frame_title = tb.Frame(self.main_frame)
        frame_title.pack()

        title_welcome = tb.Label(frame_title, text="Selamat Belajar", font=("comic sans ms",45))
        title_welcome.pack(pady=(70,200))

        frame_menu1 = tb.Frame(self.main_frame)
        frame_menu1.pack()

        style = tb.Style()
        style.configure('success.Outline.TButton', font=("comic sans ms",20), width=25)

        btn_menu1 = tb.Button(frame_menu1, text="Belajar Hijaiyah", style="success.Outline.TButton", command=lambda: (self.clicked_menu("Belajar")))
        btn_menu1.pack(pady=10)
        btn_menu1.bind("<Enter>", self.on_hover)
        #btn_menu1.bind("<Leave>", self.on_leave)

        btn_menu2 = tb.Button(frame_menu1, text="Acak Huruf", style="success.Outline.TButton", command=lambda: self.clicked_menu("Acak"))
        btn_menu2.pack(pady=10)
        btn_menu2.bind("<Enter>", self.on_hover)
        #btn_menu2.bind("<Leave>", self.on_leave)

        btn_menu3 = tb.Button(frame_menu1, text="Quiz Hijaiyah", style="success.Outline.TButton", command=lambda: self.clicked_menu("Quiz"))
        btn_menu3.pack(pady=10)
        btn_menu3.bind("<Enter>", self.on_hover)
        #btn_menu3.bind("<Leave>", self.on_leave)

        btn_menu4 = tb.Button(frame_menu1, text="Keluar Aplikasi", style="success.Outline.TButton", command=lambda: self.clicked_menu("Keluar") )
        btn_menu4.pack(pady=10)
        btn_menu4.bind("<Enter>", self.on_hover)
        #btn_menu4.bind("<Leave>", self.on_leave)

        backsound_thread = Thread(target=play_backsound)
        backsound_thread.start()

    def clicked_menu(self, menu_type):
        if menu_type == "Belajar":
            self.main_frame.pack_forget()
            BelajarHijaiyah(self.root).open_main_display()
        elif menu_type == "Acak":
            self.main_frame.pack_forget()
            AcakHuruf(self.root)
        elif menu_type == "Quiz":
            self.main_frame.pack_forget()
            QuizHijaiyah(self.root)

        else:
            self.root.destroy()

    # Fungsi yang akan dipanggil saat mouse hover pada button
    def on_hover(self, event):
        play_thread = Thread(target=play_sound, args=('/effects/bubble-click',))
        play_thread.start()

    # Fungsi yang akan dipanggil saat mouse meninggalkan button
    def on_leave(self,event):
        stop_thread = Thread(target=stop_sound)
        stop_thread.start()
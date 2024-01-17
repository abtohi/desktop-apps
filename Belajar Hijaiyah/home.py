import ttkbootstrap as tb
from belajar_hijaiyah import BelajarHijaiyah
from acak_huruf import AcakHuruf

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.main_frame = tb.Frame(root)
        self.main_frame.pack()

        frame_title = tb.Frame(self.main_frame)
        frame_title.pack()

        title_welcome = tb.Label(frame_title, text="Selamat Belajar", font=("Helvetica",40))
        title_welcome.pack(pady=(70,240))

        frame_menu1 = tb.Frame(self.main_frame)
        frame_menu1.pack()

        style = tb.Style()
        style.configure('success.Outline.TButton', font=("Helvetica",20), width=25)

        btn_menu1 = tb.Button(frame_menu1, text="Belajar Hijaiyah", style="success.Outline.TButton", command=lambda: self.clicked_menu("Belajar"))
        btn_menu1.pack(pady=10)

        btn_menu2 = tb.Button(frame_menu1, text="Acak Huruf", style="success.Outline.TButton", command=lambda: self.clicked_menu("Acak"))
        btn_menu2.pack(pady=10)

        btn_menu3 = tb.Button(frame_menu1, text="Quiz Hijaiyah", style="success.Outline.TButton", command=lambda: self.clicked_menu("Quiz"))
        btn_menu3.pack(pady=10)

        btn_menu4 = tb.Button(frame_menu1, text="Keluar Aplikasi", style="success.Outline.TButton", command=lambda: self.clicked_menu("Keluar") )
        btn_menu4.pack(pady=10)

    def clicked_menu(self, menu_type):
        if menu_type == "Belajar":
            self.main_frame.pack_forget()
            BelajarHijaiyah(self.root).open_main_display()
        elif menu_type == "Acak":
            self.main_frame.pack_forget()
            AcakHuruf(self.root)
        elif menu_type == "Quiz":
            self.main_frame.pack_forget()
        else:
            self.root.destroy()
import ttkbootstrap as tb
from threading import Thread
from configure.funcs import *

from menu.belajar_hijaiyah import BelajarHijaiyah
from menu.acak_huruf import AcakHuruf
from menu.quiz_hijaiyah import QuizHijaiyah
from display.animasi import SmoothMoveImageLabel

class MainMenu:
    def __init__(self, root):
        self.root = root
        
        #START BACKGROUND
        # Load the image and get its size
        image_path = "images/others/bg.png"  # Ganti dengan path gambar PNG Anda
        self.original_image = Image.open(image_path)
        self.image_width, self.image_height = self.original_image.size

        # Get the screen size
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Resize the image to fit the screen without cropping
        self.resized_image = self.original_image.resize((screen_width, screen_height), Image.ADAPTIVE)

        # Create a Tkinter-compatible photo image
        self.photo = ImageTk.PhotoImage(self.resized_image)

        # Create a label with the image
        self.background_label = tb.Label(root, image=self.photo)
        self.background_label.place(relwidth=1, relheight=1)

        #END BACKGROUND

        self.main_frame = tb.Frame(root)
        self.main_frame.pack(fill="x")

        frame_title = tb.Frame(self.main_frame)
        frame_title.pack()

        title_welcome = tb.Label(frame_title, text="Selamat Datang di Alifbacaku", font=("comic sans ms",45))
        title_welcome.pack(pady=(70,5))

        subtitle_welcome = tb.Label(frame_title, text="Aplikasi Pintar untuk Memudahkan Anak Belajar Mengaji\ndan Mengenal Dasar-dasar Huruf Hijaiyah dengan Kreativitas dan Kesenangan", font=("comic sans ms",20),justify='center', anchor='center')
        subtitle_welcome.pack(pady=(0,138))

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

        # Menjalankan animasi
        self.animated_label = SmoothMoveImageLabel(root)
        self.animated_label.place(x=1550, y=540)

    def clicked_menu(self, menu_type):
        if menu_type == "Belajar":
            self.main_frame.pack_forget()
            self.animated_label.place_forget()
            BelajarHijaiyah(self.root).open_main_display()
            self.background_label.place_forget()
        elif menu_type == "Acak":
            self.main_frame.pack_forget()
            self.animated_label.place_forget()
            AcakHuruf(self.root)
            self.background_label.place_forget()
        elif menu_type == "Quiz":
            self.main_frame.pack_forget()
            self.animated_label.place_forget()
            QuizHijaiyah(self.root)
            self.background_label.place_forget()

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
import ttkbootstrap as tb
from PIL import ImageTk
import pygame
from configure.funcs import resize_image

from menu.home import MainMenu

def play_welcome_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("sound/others/welcome.mp3")  # Ganti dengan path file suara yang diinginkan
    pygame.mixer.music.play()

class WelcomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Selamat Datang!")

        # Setup suara dan animasi di sini
        play_welcome_sound()
        self.show_animation()

    def show_animation(self):
        # Tambahkan animasi di sini menggunakan modul Pillow (PIL)
        # Contoh: Menampilkan gambar selamat datang
        image_path = "images/others/welcome.png" 
        scale_percent = 80  # Persentase ukuran baru (80% dari ukuran original)

        resized_image = resize_image(image_path, scale_percent)
        photo = ImageTk.PhotoImage(resized_image)

        label = tb.Label(self.root, image=photo)
        label.image = photo
        label.pack(pady=30)

        # Setelah beberapa detik, nonaktifkan gambar
        self.root.after(3000, lambda: (label.pack_forget(), MainMenu(self.root)))
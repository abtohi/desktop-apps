import ttkbootstrap as tb
from PIL import Image, ImageTk
import pygame

from belajar_hijaiyah import BelajarHijaiyah

def play_welcome_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("sound/welcome.mp3")  # Ganti dengan path file suara yang diinginkan
    pygame.mixer.music.play()

class WelcomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Selamat Datang!")

        # Setup suara dan animasi di sini
        play_welcome_sound()
        self.show_animation()

    def resize_image(self, image_path, scale_percent):
        original_image = Image.open(image_path) # Buka gambar
        width, height = original_image.size # Ambil ukuran gambar original

        # Hitung ukuran baru berdasarkan persentase
        new_width = int(width * scale_percent / 100)
        new_height = int(height * scale_percent / 100)
        resized_image = original_image.resize((new_width, new_height)) # Ubah ukuran gambar
        return resized_image

    def show_animation(self):
        # Tambahkan animasi di sini menggunakan modul Pillow (PIL)
        # Contoh: Menampilkan gambar selamat datang
        image_path = "images/welcome.jpg"  # Ganti dengan path gambar yang diinginkan
        scale_percent = 80  # Persentase ukuran baru (80% dari ukuran original)

        resized_image = self.resize_image(image_path, scale_percent)
        photo = ImageTk.PhotoImage(resized_image)

        label = tb.Label(self.root, image=photo)
        label.image = photo
        label.pack(pady=100)

        # Setelah beberapa detik, nonaktifkan gambar
        self.root.after(4000, lambda: (label.pack_forget(), BelajarHijaiyah(self.root).open_main_display()))
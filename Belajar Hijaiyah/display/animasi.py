import tkinter as tk
from PIL import Image, ImageTk

class SmoothMoveImageLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.image = self.load_image()
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.configure(image=self.image_tk)
        self.animation_speed = 5  # Ubah angka ini untuk mengatur kecepatan animasi
        self.move_direction = 2  # 1 untuk bergerak ke kanan, -1 untuk bergerak ke kiri
        self.animate()

    def load_image(self):
        # Ganti dengan path dan nama file gambar PNG Anda
        image_file = "images/others/animasi.jpg"
        return Image.open(image_file)

    def animate(self):
        width, height = self.image.size
        x_offset = self.move_direction * self.animation_speed

        # Crop dan pindahkan gambar
        cropped_image = self.image.crop((0, 0, width, height))
        self.image = Image.new("RGBA", (width, height))
        self.image.paste(cropped_image, (x_offset, 0))

        # Konversi gambar ke format yang dapat ditampilkan oleh Tkinter
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.configure(image=self.image_tk)

        # Bergeser gambar dan mulai animasi lagi
        self.move_direction *= -1  # Memutar arah setelah mencapai batas tertentu
        self.after(800, self.animate)  # Ubah angka ini untuk mengatur kecepatan animasi



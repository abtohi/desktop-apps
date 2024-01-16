import ttkbootstrap as tb
from PIL import Image, ImageTk
import pygame

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
        self.root.after(4000, lambda: (label.pack_forget(), MainWindow().open_main_display()))

class MainWindow:
    def __init__(self):
        self.img_label = None

    def resize_image(self, image_path, scale_percent):
        original_image = Image.open(image_path) # Buka gambar
        width, height = original_image.size # Ambil ukuran gambar original

        # Hitung ukuran baru berdasarkan persentase
        new_width = int(width * scale_percent / 100)
        new_height = int(height * scale_percent / 100)
        resized_image = original_image.resize((new_width, new_height)) # Ubah ukuran gambar
        return resized_image
    
    def btn_format(self, frame, frame2, image, r, c):
        r_alif = self.resize_image(f'images/{image}.jpg', 15)
        alif = ImageTk.PhotoImage(r_alif)
        l_alif = tb.Button(frame, image=alif, style="secondary", command=lambda: (self.play_sound(image),self.open_image(frame2, image)))
        l_alif.image = alif
        l_alif.grid(row=r, column=c, padx=5, pady=5)

    def play_sound(self, huruf):
        pygame.mixer.init()
        pygame.mixer.music.load(f"sound/{huruf}.mp3")  # Ganti dengan path file suara yang diinginkan
        pygame.mixer.music.play()

    def open_image(self, frame, image):
        r_img = self.resize_image(f'images/{image}.jpg', 200)
        img = ImageTk.PhotoImage(r_img)

        # Jika img_label sudah ada, ubah gambar di dalamnya
        if self.img_label:
            self.img_label.config(image=img)
            self.img_label.image = img
        else:
            # Jika img_label belum ada, buat label baru dan simpan referensinya
            self.img_label = tb.Label(frame, image=img)
            self.img_label.image = img
            self.img_label.pack()
    
    def open_main_display(self):
        #Button
        frame3 = tb.Frame(root)
        frame3.pack()
        r_img = self.resize_image(f'images/000.jpg', 200)
        img = ImageTk.PhotoImage(r_img)
        # Jika img_label sudah ada, ubah gambar di dalamnya
        if self.img_label:
            self.img_label.config(image=img)
            self.img_label.image = img
        else:
            # Jika img_label belum ada, buat label baru dan simpan referensinya
            self.img_label = tb.Label(frame3, image=img)
            self.img_label.image = img
            self.img_label.pack()


        frame1 = tb.Frame(root)
        frame1.pack()
        frame2 = tb.Frame(root)
        frame2.pack()
        
        alphabets1 = ["001-alif","002-ba","003-taa","004-tha","005-jeem","006-haa","007-khaa","008-dal","009-dhal","010-raa","011-jaa","012-seen","013-sheen","014-saad","015-dhaad"]
        self.btn_format(frame1, frame3, alphabets1[14],0,0)
        self.btn_format(frame1, frame3, alphabets1[13],0,1)
        self.btn_format(frame1, frame3, alphabets1[12],0,2)
        self.btn_format(frame1, frame3, alphabets1[11],0,3)
        self.btn_format(frame1, frame3, alphabets1[10],0,4)
        self.btn_format(frame1, frame3, alphabets1[9],0,5)
        self.btn_format(frame1, frame3, alphabets1[8],0,6)
        self.btn_format(frame1, frame3, alphabets1[7],0,7)
        self.btn_format(frame1, frame3, alphabets1[6],0,8)
        self.btn_format(frame1, frame3, alphabets1[5],0,9)
        self.btn_format(frame1, frame3, alphabets1[4],0,10)
        self.btn_format(frame1, frame3, alphabets1[3],0,11)
        self.btn_format(frame1, frame3, alphabets1[2],0,12)
        self.btn_format(frame1, frame3, alphabets1[1],0,13)
        self.btn_format(frame1, frame3, alphabets1[0],0,14)

        alphabets2 = ["016-toa","017-dhaa","018-ain","019-ghain","020-faa","021-qaaf","022-kaaf","023-laam","024-meem","025-noon","026-waw","027-ha","028-hamza","029-yaa"]
        self.btn_format(frame2, frame3, alphabets2[13],0,0)
        self.btn_format(frame2, frame3, alphabets2[12],0,1)
        self.btn_format(frame2, frame3, alphabets2[11],0,2)
        self.btn_format(frame2, frame3, alphabets2[10],0,3)
        self.btn_format(frame2, frame3, alphabets2[9],0,4)
        self.btn_format(frame2, frame3, alphabets2[8],0,5)
        self.btn_format(frame2, frame3, alphabets2[7],0,6)
        self.btn_format(frame2, frame3, alphabets2[6],0,7)
        self.btn_format(frame2, frame3, alphabets2[5],0,8)
        self.btn_format(frame2, frame3, alphabets2[4],0,9)
        self.btn_format(frame2, frame3, alphabets2[3],0,10)
        self.btn_format(frame2, frame3, alphabets2[2],0,11)
        self.btn_format(frame2, frame3, alphabets2[1],0,12)
        self.btn_format(frame2, frame3, alphabets2[0],0,13)

        frame3 = tb.Frame(root)
        frame3.pack()

if __name__ == "__main__":
    root = tb.Window()
    #welcome_screen = WelcomeScreen(root)
    MainWindow().open_main_display()
    resw = root.winfo_screenwidth()
    resh = root.winfo_screenheight()
    root.geometry(f'{resw}x{resh}')
    root.mainloop()

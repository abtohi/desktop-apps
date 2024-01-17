import ttkbootstrap as tb
from PIL import Image, ImageTk
import pygame

class BelajarHijaiyah:
    def __init__(self, root):
        self.img_label = None
        self.root = root
        self.hurufsaatini = tb.StringVar()
        self.frame3 = tb.Frame(self.root)
        self.frame3.pack()

        self.frame4 = tb.Frame(self.root)
        self.frame4.place(x=935, y=650)

        self.frame1 = tb.Frame(self.root)
        self.frame1.place(x=250,y=800)
        self.frame2 = tb.Frame(self.root)
        self.frame2.place(x=300, y=890)

        self.alphabet = [
            {"id":0, "img":"001-alif"},
            {"id":1, "img":"002-ba"},
            {"id":2, "img":"003-taa"},
            {"id":3, "img":"004-tha"},
            {"id":4, "img":"005-jeem"},
            {"id":5, "img":"006-haa"},
            {"id":6, "img":"007-khaa"},
            {"id":7, "img":"008-dal"},
            {"id":8, "img":"009-dhal"},
            {"id":9, "img":"010-raa"},
            {"id":10, "img":"011-jaa"},
            {"id":11, "img":"012-seen"},
            {"id":12, "img":"013-sheen"},
            {"id":13, "img":"014-saad"},
            {"id":14, "img":"015-dhaad"},
            {"id":15, "img":"016-toa"},
            {"id":16, "img":"017-dhaa"},
            {"id":17, "img":"018-ain"},
            {"id":18, "img":"019-ghain"},
            {"id":19, "img":"020-faa"},
            {"id":20, "img":"021-qaaf"},
            {"id":21, "img":"022-kaaf"},
            {"id":22, "img":"023-laam"},
            {"id":23, "img":"024-meem"},
            {"id":24, "img":"025-noon"},
            {"id":25, "img":"026-waw"},
            {"id":26, "img":"027-ha"},
            {"id":27, "img":"028-hamza"},
            {"id":28, "img":"029-yaa"}
            ]

    def resize_image(self, image_path, scale_percent):
        original_image = Image.open(image_path) # Buka gambar
        width, height = original_image.size # Ambil ukuran gambar original

        # Hitung ukuran baru berdasarkan persentase
        new_width = int(width * scale_percent / 100)
        new_height = int(height * scale_percent / 100)
        resized_image = original_image.resize((new_width, new_height)) # Ubah ukuran gambar
        return resized_image
    
    def btn_format(self, frame, image, id, r, c):
        r_img = self.resize_image(f'images/{image}.jpg', 15)
        img = ImageTk.PhotoImage(r_img)
        l_img = tb.Button(frame, image=img, style="dark-outline", command=lambda: self.play_and_open(image, id))
        l_img.image = img
        l_img.grid(row=r, column=c, padx=5, pady=5)

    def play_and_open(self, image, id):
        #self.play_sound(image)
        self.open_image(self.frame3, image, id)

    def play_sound(self, huruf):
        pygame.mixer.init()
        pygame.mixer.music.load(f"sound/{huruf}.mp3")  # Ganti dengan path file suara yang diinginkan
        pygame.mixer.music.play()

    def on_left_arrow(self):
        curr = self.hurufsaatini.get()
        moveto = int(curr)+1
            
        image = self.alphabet[moveto].get("img")
        #self.play_sound(image)
        self.open_image(self.frame3, image, moveto)

    def on_right_arrow(self):
        curr = self.hurufsaatini.get()
        moveto = int(curr)-1
        image = self.alphabet[moveto].get("img")
        #self.play_sound(image)
        self.open_image(self.frame3, image, moveto)
    
    def on_updown_pressed(self):
        curr = self.hurufsaatini.get()
        image = self.alphabet[int(curr)].get("img")
        self.play_sound(image)
        
    def open_image(self, frame, image, id):
        r_img = self.resize_image(f'images/{image}.jpg', 180)
        img = ImageTk.PhotoImage(r_img)

        r_left = self.resize_image(f'images/left-arrow.png', 20)
        left = ImageTk.PhotoImage(r_left)

        r_right = self.resize_image(f'images/right-arrow.png', 20)
        right = ImageTk.PhotoImage(r_right)

        r_play = self.resize_image(f'images/play.jpg', 13)
        play = ImageTk.PhotoImage(r_play)

        img_left = tb.Button(frame, image=left, style="dark-outline", command=self.on_left_arrow)
        img_left.image = left
        img_left.grid(row=0, column=0)

        img_right = tb.Button(frame, image=right, style="dark-outline", command=self.on_right_arrow)
        img_right.image = right
        img_right.grid(row=0, column=2)

        img_play = tb.Button(self.frame4, image=play, style="dark-outline", command=lambda: self.play_sound(image))
        img_play.image = play
        img_play.grid(row=1, column=1)

        # Jika img_label sudah ada, ubah gambar di dalamnya
        if self.img_label:
            self.img_label.config(image=img)
            self.img_label.image = img
            if id == 28:
                self.hurufsaatini.set(-1)
            else:
                self.hurufsaatini.set(id)

        else:
            # Jika img_label belum ada, buat label baru dan simpan referensinya
            self.img_label = tb.Label(frame, image=img)
            self.img_label.image = img
            self.img_label.grid(row=0, column=1)

        self.root.bind("<Left>", lambda event:self.on_left_arrow())
        self.root.bind("<Right>", lambda event:self.on_right_arrow())
        self.root.bind("<Up>", lambda event:self.on_updown_pressed())
        self.root.bind("<Down>", lambda event:self.on_updown_pressed())
    
    def open_main_display(self):
        r_img = self.resize_image(f'images/000.jpg', 150)
        img = ImageTk.PhotoImage(r_img)

        self.img_label = tb.Label(self.frame3, image=img)
        self.img_label.image = img
        self.img_label.grid(row=0, column=1)
        
        alphabet = self.alphabet
        for i in range(0,15):
            self.btn_format(self.frame1, alphabet[14-i].get("img"), alphabet[14-i].get("id"),0,i)

        for i in range(0,14):
            nilai = 28-i
            self.btn_format(self.frame2, alphabet[nilai].get("img"), alphabet[nilai].get("id"),0,i)
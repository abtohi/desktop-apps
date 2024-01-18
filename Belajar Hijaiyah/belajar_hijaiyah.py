import ttkbootstrap as tb
from PIL import ImageTk
import pygame
from alphabet import alphabet
from funcs import resize_image, home_icon

class BelajarHijaiyah:
    def __init__(self, root):
        self.img_label = None
        self.root = root
        self.hurufsaatini = tb.StringVar()

        self.main_frame = tb.Frame(self.root)
        self.main_frame.pack()
        self.frame3 = tb.Frame(self.main_frame)
        self.frame3.pack(pady=(50,0))

        self.frame4 = tb.Frame(self.main_frame)
        self.frame4.place(x=680, y=590)

        self.frame1 = tb.Frame(self.main_frame)
        self.frame1.pack(pady=(70,10))
        self.frame2 = tb.Frame(self.main_frame)
        self.frame2.pack()
    
    def btn_format(self, frame, image, id, r, c):
        r_img = resize_image(f'images/alphabet/{image}.jpg', 15)
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
            
        image = alphabet[moveto].get("img")
        #self.play_sound(image)
        self.open_image(self.frame3, image, moveto)

    def on_right_arrow(self):
        curr = self.hurufsaatini.get()
        moveto = int(curr)-1
        image = alphabet[moveto].get("img")
        #self.play_sound(image)
        self.open_image(self.frame3, image, moveto)
    
    def on_updown_pressed(self):
        curr = self.hurufsaatini.get()
        image = alphabet[int(curr)].get("img")
        self.play_sound(image)
        
    def open_image(self, frame, image, id):
        r_img = resize_image(f'images/alphabet/{image}.jpg', 150)
        img = ImageTk.PhotoImage(r_img)

        r_left = resize_image(f'images/icon/left-arrow.png', 13)
        left = ImageTk.PhotoImage(r_left)

        r_right = resize_image(f'images/icon/right-arrow.png', 13)
        right = ImageTk.PhotoImage(r_right)

        r_play = resize_image(f'images/icon/play.jpg', 13)
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

        title = tb.Label(self.main_frame, text="Belajar Huruf Hijaiyah", font=("Helvetica",40))
        title.place(x=445, y=10)

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
        r_img = resize_image(f'images/others/000.png', 150)
        img = ImageTk.PhotoImage(r_img)

        self.img_label = tb.Label(self.frame3, image=img)
        self.img_label.image = img
        self.img_label.grid(row=0, column=1)

        home_icon(self.root, self.main_frame)
        
        for i in range(0,15):
            self.btn_format(self.frame1, alphabet[14-i].get("img"), alphabet[14-i].get("id"),0,i)

        for i in range(0,14):
            nilai = 28-i
            self.btn_format(self.frame2, alphabet[nilai].get("img"), alphabet[nilai].get("id"),0,i)
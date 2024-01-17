import ttkbootstrap as tb
import random
from PIL import ImageTk
from alphabet import alphabet
from funcs import *

class AcakHuruf:
    def __init__(self, root):
        self.root = root

        self.main_frame = tb.Frame(root)
        self.main_frame.pack()
        self.img_label = None
        
        self.frame1 = tb.Frame(self.main_frame)
        self.frame1.pack()

        self.frame2 = tb.Frame(self.main_frame)
        self.frame2.pack()

        self.title = tb.Label(self.frame1, text="Acak Huruf Hijaiyah", font=("Helvetica",40))
        self.title.pack(pady=(60,100))

        r_img = resize_image(f'images/icon/random.jpg', 17)
        img = ImageTk.PhotoImage(r_img)
        btn_img = tb.Button(root, image=img, style="dark-outline", command=self.acak_gambar)
        btn_img.image = img
        btn_img.place(x=925, y=650)
        
        home_icon(self.root, self.main_frame, btn_img, "place")
        self.acak_gambar()
        
    def acak_gambar(self):
        listangka = []
        counter = 0
        
        while counter < 4:
            selected_number = self.acakangka()
            if selected_number not in listangka:
                listangka.append(selected_number)
                image = alphabet[selected_number].get("img")
                imagepath = f'images/alphabet/{image}.jpg'
                dp_label_grid(self.frame2, imagepath, 100, 0, counter)
                counter+=1
        
    def acakangka(self):
        angkarandom = random.choice(range(1, 29))
        return angkarandom
    

        
        
import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox
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
        self.title.pack(pady=(60,150))

        self.limit = tb.BooleanVar()
        self.limit.set(False)

        self.checklimit = tb.Checkbutton(self.main_frame, variable=self.limit, text="Limitasi", bootstyle="secondary-outline-toolbutton", command=self.oncheck_limit)
        self.checklimit.place(x=640, y=150, width=80, height=35)

        self.spinbox1 = tb.Spinbox(self.main_frame,from_=1, to=29, font=("Helvetica",13), state="disable")
        self.spinbox1.place(x=730,y=150, width=60)
        self.spinbox1.set(1)

        self.to = tb.Label(self.main_frame, text="to", font=("Helvetica",13))
        self.to.place(x=820, y=150)

        self.spinbox2 = tb.Spinbox(self.main_frame,from_=1, to=29, font=("Helvetica",13), state="disable")
        self.spinbox2.place(x=870,y=150, width=60)
        self.spinbox2.set(29)

        r_img = resize_image(f'images/icon/random.jpg', 17)
        img = ImageTk.PhotoImage(r_img)
        btn_img = tb.Button(root, image=img, style="dark-outline", command=self.acak_gambar)
        btn_img.image = img
        btn_img.place(x=925, y=690)
        
        home_icon(self.root, self.main_frame, btn_img, "place")
        self.acak_gambar()
    
    def oncheck_limit(self):
        value = self.limit.get()
        if value == True:
            self.spinbox1.set(1)
            self.spinbox2.set(29)
            self.spinbox1.config(state="enable")
            self.spinbox2.config(state="enable")
        else:
            self.spinbox1.config(state="disable")
            self.spinbox2.config(state="disable")
        
    def acak_gambar(self):
        listangka = []
        counter = 0
        bottom = int(self.spinbox1.get())
        top = int(self.spinbox2.get())

        if top-bottom >=3:
            try:
                while counter < 4:
                    selected_number = self.acakangka(bottom, top)
                    if selected_number not in listangka:
                        listangka.append(selected_number)
                        image = alphabet[selected_number].get("img")
                        imagepath = f'images/alphabet/{image}.jpg'
                        dp_label_grid(self.frame2, imagepath, 100, 0, counter)
                        counter+=1
            except Exception as e:
                Messagebox.show_error(title="Pesan Error",message="Silahkan masukkan angka limitasi yang valid", parent=self.main_frame)
        else:
            Messagebox.show_error(title="Pesan Error",message="Silahkan masukkan angka limitasi yang valid", parent=self.main_frame)
     
    def acakangka(self, bottom, top):
        limitstatus = self.limit.get()
        if limitstatus == True:
            angkarandom = random.choice(range(bottom-1, top))
        else:
            angkarandom = random.choice(range(0, 29))
        return angkarandom
    

        
        
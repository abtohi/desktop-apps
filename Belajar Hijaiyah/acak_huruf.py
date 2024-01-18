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
        play_sound('/effects/btn-open')
        self.root.after(1000, stop_sound())
        self.open_display()

    def open_display(self):
        title = tb.Label(self.frame1, text="Acak Huruf Hijaiyah", font=("comic sans ms",40))
        title.pack(pady=(30,200))

        self.limit = tb.BooleanVar()
        self.limit.set(False)

        style = tb.Style()
        style.configure('secondary.Outline.TButton', font=("comic sans ms",10))

        checklimit = tb.Checkbutton(self.main_frame, variable=self.limit, text="Limitasi", style="secondary.Outline.TButton", command=self.oncheck_limit)
        checklimit.place(x=740, y=150, width=100, height=38)

        self.spinbox1 = tb.Spinbox(self.main_frame,from_=1, to=29, font=("comic sans ms",13), state="disable")
        self.spinbox1.place(x=850,y=150, width=60)
        self.spinbox1.set(1)

        to = tb.Label(self.main_frame, text="to", font=("comic sans ms",13))
        to.place(x=930, y=150)

        self.spinbox2 = tb.Spinbox(self.main_frame,from_=1, to=29, font=("comic sans ms",13), state="disable")
        self.spinbox2.place(x=970,y=150, width=60)
        self.spinbox2.set(29)

        r_img = resize_image(f'images/icon/random.jpg', 17)
        img = ImageTk.PhotoImage(r_img)
        btn_img = tb.Button(self.root, image=img, style="dark-outline", command=self.acak_gambar)
        btn_img.image = img
        btn_img.place(x=925, y=790)
        
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
        lbl_img = None

        if top-bottom >=3:
            try:
                while counter < 4:
                    selected_number = self.acakangka(bottom, top)
                    if selected_number not in listangka:
                        listangka.append(selected_number)
                        image = alphabet[selected_number].get("img")
                        imagepath = f'images/alphabet/{image}.jpg'
                        r_img = resize_image(imagepath, 100)
                        img = ImageTk.PhotoImage(r_img)
                        lbl_img = tb.Button(self.frame2, image=img, command=lambda img=image: play_sound(img), bootstyle="secondary-outline")
                        lbl_img.image = img
                        lbl_img.grid(row=0, column=counter, padx=10)
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
    

        
        
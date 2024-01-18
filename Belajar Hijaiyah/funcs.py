from PIL import Image, ImageTk
import ttkbootstrap as tb
import pygame

def resize_image(image_path, scale_percent):
    original_image = Image.open(image_path) # Buka gambar
    width, height = original_image.size # Ambil ukuran gambar original

    # Hitung ukuran baru berdasarkan persentase
    new_width = int(width * scale_percent / 100)
    new_height = int(height * scale_percent / 100)
    resized_image = original_image.resize((new_width, new_height)) # Ubah ukuran gambar
    return resized_image

def home_icon(root, main_frame, need_to_close=None,tipe=None):
    r_home = resize_image(f'images/icon/home.jpg', 15)
    home = ImageTk.PhotoImage(r_home)
    img_home = tb.Button(root, image=home, style="dark-outline", command=lambda: (destroy(root, main_frame), img_home.place_forget(), close_opsional(need_to_close, tipe), disable_bind(root)))
    img_home.image = home
    img_home.place(x=30, y=30)

def disable_bind(root):
    root.unbind("<Left>")
    root.unbind("<Right>")
    root.unbind("<Up>")
    root.unbind("<Down>")

def close_opsional(obj, tipe):
    if tipe == "grid":
        obj.grid_forget()
    elif tipe == "place":
        obj.place_forget()
    elif tipe == "pack":
        obj.pack_forget()

def destroy(root, main_frame):
    main_frame.pack_forget()
    from home import MainMenu
    MainMenu(root)

def dp_button_grid(frame, path, scale, r, c, comm=None):
    r_img = resize_image(path, scale)
    img = ImageTk.PhotoImage(r_img)
    btn_img = tb.Button(frame, image=img, style="dark-outline", command=comm)
    btn_img.image = img
    btn_img.grid(row=r, column=c)

def dp_label_grid(frame, path, scale, r, c):
    r_img = resize_image(path, scale)
    img = ImageTk.PhotoImage(r_img)
    lbl_img = tb.Label(frame, image=img)
    lbl_img.image = img
    lbl_img.grid(row=r, column=c)
        
def dp_button_place(frame, path, scale, xnum, ynum, comm):
    r_img = resize_image(path, scale)
    img = ImageTk.PhotoImage(r_img)
    btn_img = tb.Button(frame, image=img, style="dark-outline", command=comm)
    btn_img.image = img
    btn_img.place(x=xnum, y=ynum)

def play_sound(huruf):
    pygame.mixer.init()
    pygame.mixer.music.load(f"sound/{huruf}.mp3")  # Ganti dengan path file suara yang diinginkan
    pygame.mixer.music.play()
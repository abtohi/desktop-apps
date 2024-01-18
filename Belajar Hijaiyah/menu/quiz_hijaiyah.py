import ttkbootstrap as tb
from configure.funcs import *

class QuizHijaiyah:
    def __init__(self, root):
        self.root = root
        self.main_frame = tb.Frame(self.root)
        self.main_frame.pack()
        home_icon(self.root, self.main_frame)
        play_sound('effects/btn-open')
        self.root.after(1000, stop_sound())
        

    
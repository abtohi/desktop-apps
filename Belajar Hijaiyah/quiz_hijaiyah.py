import ttkbootstrap as tb
from funcs import *

class QuizHijaiyah:
    def __init__(self, root):
        self.root = root
        self.main_frame = tb.Frame(self.root)
        self.main_frame.pack()
        home_icon(self.root, self.main_frame)
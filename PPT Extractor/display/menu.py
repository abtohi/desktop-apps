import os
import ttkbootstrap as tb
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.constants import *
from functools import partial
import datetime
import shutil

class Menu:
    def __init__(self, app, root, var_new_project, frame4, style, scaled, labelproject):
        self.app = app
        self.root = root
        self.var_new_project = var_new_project
        self.frame4 = frame4
        self.style = style
        self.scaled = scaled
        self.labelproject = labelproject

    def new_project(self):
        path = f'{os.getcwd()}\projects'
        if not os.path.exists(path):
            os.makedirs(path)
        npframe = tb.Frame(self.root, border=1, relief="solid")
        npframe.place(x=self.scaled(40), y=self.scaled(100), width=530, height=200)

        labeltitle = tb.Label(npframe, text="Create New Project", font=("Arial Bold",15), bootstyle="primary")
        labeltitle.place(x=self.scaled(170), y=self.scaled(20))

        labelproject = tb.Label(npframe, text="Input Project Name",font=("Arial",11), bootstyle="primary")
        labelproject.place(x=self.scaled(15), y=self.scaled(73))

        inputproject = tb.Entry(npframe, textvariable=self.var_new_project)
        inputproject.place(x=self.scaled(155), y=self.scaled(70), width=self.scaled(340))

        createbtn = tb.Button(npframe, text="Create", command=lambda: (self.create_project(npframe)))
        createbtn.place(x=self.scaled(170), y=self.scaled(120), width=90)

        cancelbtn = tb.Button(npframe, text="Cancel", bootstyle="danger", command=lambda: (npframe.destroy()))
        cancelbtn.place(x=self.scaled(280), y=self.scaled(120), width=90)

    def create_project(self,frame):
        path = os.getcwd()
        path = f'{str(path)}/projects/{self.var_new_project.get()}'
        if not os.path.exists(path):
            os.makedirs(f'projects/{self.var_new_project.get()}')
            frame.destroy()
            Messagebox.ok(message="Your project has been successfully created", parent=self.frame4)
            self.labelproject.config(text=f"Project Name : {self.var_new_project.get()}")
        else:
            Messagebox.show_warning(message="Project name already exists",parent=self.frame4)

    def open_project(self):
        current = f'{os.getcwd()}\projects'
        if not os.path.exists(current):
            os.makedirs(current)
        opframe = tb.Frame(self.root, border=1, relief="solid")
        opframe.place(x=self.scaled(40), y=self.scaled(60), width=530, height=600)

        labeltitle = tb.Label(opframe, text="Open The Project Folder", font=("Arial Bold",15), bootstyle="primary")
        labeltitle.place(x=self.scaled(150), y=self.scaled(20))

        #Project Table
        coldata = [
            {"text": "Project Name", "stretch": False},
            {"text": "Creation Date", "stretch":False},
            {"text": "Last Modified", "stretch": False},
            ]
        
        path = os.getcwd()
        path = f'{str(path)}\projects'

        colors = self.root.style.colors

        data_project = []

        proj_list = os.listdir(path)
        for proj in proj_list:
            creation_date = datetime.datetime.fromtimestamp(os.path.getctime(f'{path}\{proj}')).strftime('%Y-%m-%d %H:%M:%S')
            last_modified = datetime.datetime.fromtimestamp(os.path.getmtime(f'{path}\{proj}')).strftime('%Y-%m-%d %H:%M:%S')
            data_project.append((proj,creation_date,last_modified))

        dt = Tableview(
            master=opframe,
            coldata=coldata,
            rowdata=data_project,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(colors.light, None),
        )
        dt.place(x=10, y=60, width=507, height=450)

        openebtn = tb.Button(opframe, text="Open Project", command=lambda: (self.select_project(opframe, dt.get_rows(selected=True)[0].values[0])))
        openebtn.place(x=self.scaled(70), y=self.scaled(540), width=120)

        deletebtn = tb.Button(opframe, text="Delete Project", bootstyle="danger", command=lambda: (self.delete_project(opframe, dt.get_rows(selected=True)[0].values[0])))
        deletebtn.place(x=self.scaled(210), y=self.scaled(540), width=120)

        cancelbtn = tb.Button(opframe, text="Cancel", bootstyle="warning", command=lambda: (opframe.destroy()))
        cancelbtn.place(x=self.scaled(350), y=self.scaled(540), width=120)
    
    def select_project(self, opframe, selected_project):
        self.var_new_project.set(selected_project)
        self.labelproject.config(text=f"Project Name : {selected_project}")
        opframe.destroy()
        Messagebox.show_info(message=f"Your project {selected_project} has been successfully selected", parent=self.frame4)

    def delete_project(self, opframe, selected_project):
        path = os.getcwd()
        path = f'projects\{selected_project}'

        listproject = os.listdir(path)
        if listproject == []:
            try:
                os.rmdir(path)
                opframe.destroy()
                Messagebox.show_info(message="Your project has been successfully deleted",parent=self.frame4)
            except Exception as e:
                msg = str(e)
                Messagebox.show_error(message=msg,parent=self.frame4)
        else:
            confirm = Messagebox.yesno(message="Your project folder contains file(s) that you might be working on, are you sure you want to delete them?", parent=self.frame4)
            if confirm == 'Yes':
                try:
                    shutil.rmtree(path)
                    opframe.destroy()
                    Messagebox.show_info(message="Your project has been successfully deleted",parent=self.frame4)
                except Exception as e:
                    msg = str(e)
                    Messagebox.show_error(message=msg,parent=self.frame4)
   
    def select_theme(self, themeselected):
        self.style.theme_use(themeselected)

    def exitapp(self):
        self.root.destroy()

    def menu(self):
        menubar = tb.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tb.Menu(menubar)
        menubar.add_separator()
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Project",command=self.new_project) 
        file_menu.add_command(label="Open Project", command=self.open_project)
        file_menu.add_command(label="Exit", command=self.exitapp)

        display_menu = tb.Menu(menubar)
        menubar.add_cascade(label="Display", menu=display_menu)

        theme_menu = tb.Menu(display_menu, tearoff=False)
        display_menu.add_cascade(label="Select Theme", menu=theme_menu)
        themes = sorted(self.style.theme_names())

        for th in themes:
            theme_menu.add_command(label=th,command=partial(self.select_theme, th))

        about_menu = tb.Menu(menubar)
        menubar.add_cascade(label="Help", menu=about_menu)  
        about_menu.add_command(label="About")
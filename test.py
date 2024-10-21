from tkinter import PhotoImage
# command for exe: pyinstaller --noconfirm --windowed --icon "photos\icon.ico" --add-data "GUImath.py;." --add-data "photos;photos/" --add-data "customtkinter;customtkinter/"  "test.py"
import customtkinter
import GUImath
import os
basedir = os.path.dirname(__file__)


test = 1

#test
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_appearance_mode("System")
        # Themes: "blue" (standard), "green", "dark-blue"
        customtkinter.set_default_color_theme("blue")
        def run():
            answer.configure(text_color="grey")
            if combobox.get() == "slope from two points":
                if box1.get() ==""  or box2.get()  == "":
                    answer.configure(text="Both boxes must be filled in",text_color="red")
                else:
                    GUImath.findSlopeFromPoint(box1.get(), box2.get())
                    answer.configure(text=GUImath.solved,text_color=GUImath.color)
            elif combobox.get() == "point slope to slope intercept":
                if box1.get() ==""  or box2.get()  == "":
                    answer.configure(text="Both boxes must be filled in",text_color="red")
                else:
                    GUImath.pointSlopeToSlopeIntercept(box1.get(), box2.get())
                    answer.configure(text=GUImath.solved,text_color=GUImath.color)
        def combobox_callback(choice):
            answer.configure(text="")
            box1.delete(0,100000)
            box2.delete(0,100000)
            if choice == "slope from two points":
                label1.grid(row=2, column=0)
                box1.grid(row=3, column=0, pady=5)
                label2.grid(row=4, column=0)
                box2.grid(row=5, column=0, pady=5)
                label1.configure(text="First Point")
                box1.configure(placeholder_text="1,2")
                label2.configure(text="Second Point")
                box2.configure(placeholder_text="-4,0")
            elif choice == "point slope to slope intercept":
                label1.grid(row=2, column=0)
                box1.grid(row=3, column=0, pady=5)
                label2.grid(row=4, column=0)
                box2.grid(row=5, column=0, pady=5)
                label1.configure(text="Point")
                box1.configure(placeholder_text="1,2")
                label2.configure(text="Slope")
                box2.configure(placeholder_text="1/3")

            else:
                label1.grid_remove()
                box1.grid_remove()
                label2.grid_remove()
                box2.grid_remove()

        # Window/App Customization
        self.geometry("250x400")
        self.title("Starter Code Example")
        self.attributes('-topmost',True)
        self.iconbitmap(os.path.join(basedir,"photos", "icon.ico"))
        self.resizable(False, False)
        combobox_var = customtkinter.StringVar(value="slope from two points")
        # Grid Configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_rowconfigure(6, weight=0)
        self.grid_rowconfigure(7, weight=0)



        title = customtkinter.CTkLabel(self,
                                       text="Algebra Calculator",
                                       font=("Arial", 25),
                                       anchor="center")
        combobox = customtkinter.CTkComboBox(master=self,
                                             width=140,
                                             values=["slope from two points", "point slope to slope intercept"],
                                             command=combobox_callback,
                                             variable=combobox_var
                                             )
        label1 = customtkinter.CTkLabel(self,
                                        text="First Point",
                                        font=("Arial", 13),
                                        anchor="w",
                                        width=140,
                                        text_color="white")

        box1 = customtkinter.CTkEntry(self, placeholder_text="1,2")

        label2 = customtkinter.CTkLabel(self,
                                        text="Second Point",
                                        font=("Arial", 13),
                                        anchor="w",
                                        width=140,
                                        text_color="white")

        box2 = customtkinter.CTkEntry(self, placeholder_text="-4,0")

        runButton = customtkinter.CTkButton(self, text="Run",command=run )

        answer = customtkinter.CTkLabel(self,
                                        text="",
                                        font=("Arial", 20),
                                        anchor="center",
                                        text_color="grey")

        title.grid(row=0, column=0,pady=10,)
        combobox.grid(row=1,column=0,pady=20)
        label1.grid(row=2, column=0)
        box1.grid(row=3, column=0, pady=5)
        label2.grid(row=4, column=0)
        box2.grid(row=5, column=0, pady=5)
        runButton.grid(row=6,column=0,pady=20)
        answer.grid(row=7, column=0,pady=10,sticky="nsew")

app = App()
app.mainloop()
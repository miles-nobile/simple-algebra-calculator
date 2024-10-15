import customtkinter
import GUImath
  # set initial value
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
            if combobox.get() == "slope from two points":
                if not firstPoint.get() ==""  and not secondPoint.get()  == "":
                    answer.configure(text_color="red")
                    answer.configure(text="Both boxes must be filled in")
                else:
                    GUImath.findSlopeFromPoint(firstPoint.get(), secondPoint.get())
                    answer.configure(text=GUImath.solved)
        def combobox_callback(choice):
            answer.configure(text="")
            if choice == "slope from two points":
                firstPointText.grid(row=2, column=0)
                firstPoint.grid(row=3, column=0, pady=5)
                secondPointText.grid(row=4, column=0)
                secondPoint.grid(row=5, column=0, pady=5)

            else:
                firstPointText.grid_remove()
                firstPoint.grid_remove()
                secondPointText.grid_remove()
                secondPoint.grid_remove()

        # Window/App Customization
        self.geometry("250x400")
        self.title("Starter Code Example")
        self.attributes('-topmost',True)
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
        firstPointText = customtkinter.CTkLabel(self,
                                        text="First Point",
                                        font=("Arial", 13),
                                        anchor="w",
                                        width=140,
                                        text_color="white")

        firstPoint = customtkinter.CTkEntry(self, placeholder_text="1,2")

        secondPointText = customtkinter.CTkLabel(self,
                                        text="Second Point",
                                        font=("Arial", 13),
                                        anchor="w",
                                        width=140,
                                        text_color="white")

        secondPoint = customtkinter.CTkEntry(self, placeholder_text="-4,0")

        runButton = customtkinter.CTkButton(self, text="Run",command=run )

        answer = customtkinter.CTkLabel(self,
                                        text="",
                                        font=("Arial", 20),
                                        anchor="center",
                                        text_color="grey")

        title.grid(row=0, column=0,pady=10,)
        combobox.grid(row=1,column=0,pady=20)
        firstPointText.grid(row=2, column=0)
        firstPoint.grid(row=3, column=0, pady=5)
        secondPointText.grid(row=4, column=0)
        secondPoint.grid(row=5, column=0, pady=5)
        runButton.grid(row=6,column=0,pady=20)
        answer.grid(row=7, column=0,pady=10,sticky="nsew")

app = App()
app.mainloop()
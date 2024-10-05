import customtkinter
import GUImath
  # set initial value
test = 1


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_appearance_mode("System")
        # Themes: "blue" (standard), "green", "dark-blue"
        customtkinter.set_default_color_theme("blue")
        def run():
            if combobox.get() == "point slope to slope intercept":
                GUImath.findSlopeFromPoint(firstPoint.get(), secondPoint.get())
                answer.configure(text=GUImath.solved)
        def combobox_callback(choice):
            if choice == "point slope to slope intercept":
                firstPoint.grid(row=3, column=0, pady=5)
                secondPoint.grid(row=4, column=0, pady=5)

            else:
                firstPoint.grid_remove()
                secondPoint.grid_remove()

        # Window/App Customization
        self.geometry("250x400")
        self.title("Starter Code Example")
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



        title = customtkinter.CTkLabel(self,
                                       text="Algebra Calculator",
                                       font=("Arial", 25),
                                       anchor="center")
        combobox = customtkinter.CTkComboBox(master=self,
                                             values=["slope from two points", "point slope to slope intercept"],
                                             command=combobox_callback,
                                             variable=combobox_var)
        firstPointText = customtkinter.CTkLabel(self,
                                        text="First Point",
                                        font=("Arial", 13),
                                        anchor="w",
                                        text_color="white")

        firstPoint = customtkinter.CTkEntry(self, placeholder_text="First Point")

        secondPoint = customtkinter.CTkEntry(self, placeholder_text="Second Point")

        runButton = customtkinter.CTkButton(self, text="Run",command=run )

        answer = customtkinter.CTkLabel(self,
                                        text="",
                                        font=("Arial", 20),
                                        anchor="center",
                                        text_color="grey")

        title.grid(row=0, column=0,pady=10)
        combobox.grid(row=1,column=0,pady=20)
        firstPointText.grid(row=2, column=0,sticky="w",padx=60)
        runButton.grid(row=5,column=0,pady=20)
        answer.grid(row=6, column=0,pady=10,sticky="nsew")

app = App()
app.mainloop()
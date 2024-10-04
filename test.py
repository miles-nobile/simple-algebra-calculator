import customtkinter
  # set initial value



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        global mode
        # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_appearance_mode("System")
        # Themes: "blue" (standard), "green", "dark-blue"
        customtkinter.set_default_color_theme("blue")

        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)
            mode = choice
        # Window/App Customization
        self.geometry("250x400")
        self.title("Starter Code Example")
        combobox_var = customtkinter.StringVar(value="option 2")
        # Grid Configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=1)


        title = customtkinter.CTkLabel(self,
                                       text="Algebra Calculator",
                                       font=("Arial", 25),
                                       anchor="center")
        combobox = customtkinter.CTkComboBox(master=self,
                                             values=["option 1", "option 2"],
                                             command=combobox_callback,
                                             variable=combobox_var)
        entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        title.grid(row=0, column=0)
        combobox.grid(row=1,column=0)
        entry.grid(row=2,column=0)

app = App()
app.mainloop()
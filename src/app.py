import customtkinter as ctk
from PIL import Image


# Hauptfenster
ctk.set_appearance_mode("dark")  # Setze das Erscheinungsbild auf "dark"
ctk.set_default_color_theme("./config/theme/custom.json")  # Setze das Standardfarbschema
root = ctk.CTk()  # Erstelle das Hauptfenster
root.title('Meine Musik Empfehlung')
root.geometry('800x600')
root.resizable(width=False, height=False)  # Fenstergröße ist fix/unveränderbar
root.configure()


# Hintergrundbild laden und skalieren
bild_path = r"assetes/image/SL.123119.26540.04.jpg"
bild = Image.open(bild_path)

# CTkImage erstellen und auf Fenstergröße skalieren
hintergrundbild = ctk.CTkImage(bild, size=(800, 600))

# CTkLabel für das Hintergrundbild erstellen
label_hintergrund = ctk.CTkLabel(root, image=hintergrundbild, text="")
label_hintergrund.place(relwidth=1, relheight=1)



# Genre Dropdown
genre_ver = ctk.StringVar(value="Genre")
genres = ["Rock", "Dance/Electronic", "Latin", "Trap", "Country", "House", "Reggaeton",
          "Boy_Band", "Bolero", "Reggae", "Jazz", "Opm"]
genre_dropdown = ctk.CTkOptionMenu(root, variable=genre_ver, values=genres)
genre_dropdown.grid(column=0, row=0, padx=20, pady=10)

# Interpreten Dropdown
interpret_ver = ctk.StringVar(value="Interpret")
interpret = ["schreib ne for schleife", "und iteriere über die db"]
interpret_dropdown = ctk.CTkOptionMenu(root, variable=interpret_ver, values=interpret)
interpret_dropdown.grid(column=0, row=1, padx=20, pady=10)

# Rating Dropdown
rating_ver = ctk.StringVar(value="Rating")
rating = ["Rating Funktion schreiben"]
rating_dropdown = ctk.CTkOptionMenu(root, variable=rating_ver,values=rating, bg_color="transparent")
rating_dropdown.grid(column=0, row=2, padx=20, pady=10 )

# Extras Lable
label = ctk.CTkLabel(root, text="Extras")
label.grid(row=0, column=1, padx=20, pady=10)

# Radio-Buttons (Ja/Nein)
radio_btn = ctk.IntVar(value=-1)
chooice = ["Yes", "No"]
for index, gender in enumerate(chooice):
    ctk.CTkRadioButton(root, text=gender, value=index, variable=radio_btn).grid(row=index+1, column=1, padx=20, pady=10)

# Start-Button
start_btn = ctk.CTkButton(root, text="Start",)
start_btn.grid(row=3, column=0, columnspan=2, padx=20, pady=10)





# Hauptschleife starten
root.mainloop()

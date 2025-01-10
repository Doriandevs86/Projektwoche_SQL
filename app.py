import customtkinter as ctk
from PIL import Image

class Farben:
    # Grundfarben
    black = '#000000'
    white = '#FFFFFF'
    gray = '#808080'
    light_gray = '#D3D3D3'
    dark_gray = '#A9A9A9'

    # Grün-Töne
    green = '#0e793c'
    dark_green = '#006400'
    light_green = '#90EE90'

    # Blau-Töne
    blue = '#0000FF'
    dark_blue = '#00008B'
    light_blue = '#ADD8E6'
    sky_blue = '#87CEEB'

    # Rot-Töne
    red = '#f31260'
    dark_red = '#8B0000'
    light_red = '#FF6347'

    # Gelb-Töne
    yellow = '#FFFF00'
    dark_yellow = '#FFD700'
    light_yellow = '#FFFFE0'

    # Orange-Töne
    orange = '#FFA500'
    dark_orange = '#FF8C00'
    light_orange = '#FFDAB9'

    # Violett-Töne
    purple = '#800080'
    dark_purple = '#4B0082'
    light_purple = '#D8BFD8'

    # Pink-Töne
    pink = '#FFC0CB'
    hot_pink = '#FF69B4'
    deep_pink = '#FF1493'

    # Braun-Töne
    brown = '#A52A2A'
    dark_brown = '#654321'
    light_brown = '#D2B48C'

    # Andere UI-freundliche Farben
    light_blue_gray = '#B0E0E6'
    light_cyan = '#E0FFFF'
    lavender = '#E6E6FA'
    mint_cream = '#F5FFFA'
    ivory = '#FFFFF0'


# Hauptfenster
ctk.set_appearance_mode("dark")  # Setze das Erscheinungsbild auf "dark"
ctk.set_default_color_theme("blue")  # Setze das Standardfarbschema
root = ctk.CTk()  # Erstelle das Hauptfenster
root.title('Meine Musik Empfehlung')
root.geometry('800x600')
root.resizable(width=False, height=False)  # Fenstergröße ist fix/unveränderbar
root.configure(bg=Farben.black)


# Hintergrundbild laden und skalieren
bild_path = r"C:\Users\Admin\Desktop\Projektwoche_SQL\data\database\SL.123119.26540.04.jpg"
bild = Image.open(bild_path)

# CTkImage erstellen und auf Fenstergröße skalieren
hintergrundbild = ctk.CTkImage(bild, size=(800, 600))

# CTkLabel für das Hintergrundbild erstellen
label_hintergrund = ctk.CTkLabel(root, image=hintergrundbild, text="")
label_hintergrund.place(relwidth=1, relheight=1)



# Genre Dropdown
genre_ver = ctk.StringVar(value="Genre")
genres = ["Rock", "Dance/Electronic", "Latin", "Trap", "Country", "House", "Reggaeton", "Boy_Band", "Bolero", "Reggae", "Jazz", "Opm"]
genre_dropdown = ctk.CTkOptionMenu(root, variable=genre_ver, values=genres, fg_color=Farben.black)
genre_dropdown.grid(column=0, row=0, padx=20, pady=10)

# Interpreten Dropdown
interpret_ver = ctk.StringVar(value="Interpret")
interpret = ["schreib ne for schleife", "und iteriere über die db"]
interpret_dropdown = ctk.CTkOptionMenu(root, variable=interpret_ver, values=interpret, fg_color=Farben.black)
interpret_dropdown.grid(column=0, row=1, padx=20, pady=10)

# Rating Dropdown
rating_ver = ctk.StringVar(value="Rating")
rating = ["Rating Funktion schreiben"]
rating_dropdown = ctk.CTkOptionMenu(root, variable=rating_ver, values=rating, fg_color=Farben.black)
rating_dropdown.grid(column=0, row=2, padx=20, pady=10)

# Extras Lable
label = ctk.CTkLabel(root, text="Extras", bg_color=Farben.black, text_color=Farben.green , text_color_disabled=Farben.dark_orange)
label.grid(row=0, column=1, padx=20, pady=10)

# Radio-Buttons (Ja/Nein)
radio_btn = ctk.IntVar(value=-1)
chooice = ["Yes", "No"]
for index, gender in enumerate(chooice):
    ctk.CTkRadioButton(root, text=gender, bg_color=Farben.black, value=index, variable=radio_btn).grid(row=index+1, column=1, padx=20, pady=10)

# Start-Button
start_btn = ctk.CTkButton(root, text="Start", fg_color=Farben.dark_red)
start_btn.grid(row=3, column=0, columnspan=2, padx=20, pady=10)





# Hauptschleife starten
root.mainloop()

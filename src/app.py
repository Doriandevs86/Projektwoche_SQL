import customtkinter as ctk
from PIL import Image
from customtkinter import CTkFrame
from sqlalchemy import column

from Projektwoche_SQL.src.dropdown_funktionen import connect_to_db
from dropdown_funktionen import get_genres_from_db
from dropdown_funktionen import get_interpreten_from_db
from dropdown_funktionen import get_subgenres_from_db


### Hauptfenster ###
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("./config/theme/custom.json") # Setze das Standardfarbschema

root = ctk.CTk()  # Erstelle das Hauptfenster
root.title('Meine Musik Empfehlung')
root.geometry('800x600')
root.resizable(width=False, height=False)
root.configure()


### Hintergrundbild laden ###

bild_path = r"assetes/image/SL.123119.26540.04.jpg"
bild = Image.open(bild_path)

# CTkImage erstellen und auf Fenstergröße skalieren
hintergrundbild = ctk.CTkImage(bild, size=(800, 600))

# CTkLabel für das Hintergrundbild erstellen
label_hintergrund = ctk.CTkLabel(root, image=hintergrundbild, text="")
label_hintergrund.place(relwidth=1, relheight=1)


### Buttons und Menüs ###

# Genre Dropdown
genre_ver = ctk.StringVar(value="Genre")
genres = get_genres_from_db(connection=connect_to_db())
genre_dropdown = ctk.CTkOptionMenu(root, variable=genre_ver, values=genres)
genre_dropdown.grid(column=0, row=0, padx=20, pady=10)

# Sub_Genre Dropdown
sub_genre_ver = ctk.StringVar(value="Sub_Genres")
sub_genres = get_subgenres_from_db(connection=connect_to_db())
sub_genre_dropdown = ctk.CTkOptionMenu(root, variable=sub_genre_ver, values=sub_genres)
sub_genre_dropdown.grid(column=0, row=1, padx=20, pady=10)

# Interpreten Dropdown
interpret_ver = ctk.StringVar(value="Interpret")
interpret = get_interpreten_from_db(connection=connect_to_db())
interpret_dropdown = ctk.CTkOptionMenu(root, variable=interpret_ver, values=interpret)
interpret_dropdown.grid(column=1, row=0, padx=20, pady=10)

# Extras Dropdown
extras_ver = ctk.StringVar(value="Extras")
extras = ["ja", "Nein"]
extras_dropdown = ctk.CTkOptionMenu(root, variable=extras_ver,values=extras, bg_color="transparent")
extras_dropdown.grid(column=1, row=1, padx=20, pady=10 )

def info():
   infofenster = ctk.CTkTextbox(root)
   infofenster.grid(row=6, column=1)


#Start-Button
start_btn = ctk.CTkButton(root, text="Start", command=info)
start_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10)


root.mainloop()

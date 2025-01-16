import customtkinter as ctk
from PIL import Image
from dropdown_funktionen import (connect_to_db,
                                get_genres_from_db,
                                get_subgenres_from_db,
                                get_interpreten_from_db
                                )

# Verbindung einmalig herstellen
connection = connect_to_db()

def info():
    infofenster = ctk.CTkLabel(root, text= '################################\n'
                                           '\n'
                                           'Hier stehen deine 5 Musikvorschläge \n'
                                           '\n'
                                           '\n'
                                           ' mit allen wichtigen Infos\n'
                                           '\n'
                                           '################################')
    infofenster.grid(row=4, column=0, columnspan=3)

def extra_info():
    infofenster = ctk.CTkLabel(root, text= '################################\n'
                                           '\n'
                                           'Hier stehen deine 5 Musikextras \n'
                                           '\n'
                                           '\n'
                                           ' Bsp. Release_Date, Top_Album, Rating\n'
                                           '\n'
                                           '################################')
    infofenster.grid(row=7, column=0, columnspan= 3)


def check_extras_input(event):
    if hasattr(check_extras_input, "error_label"): # entfernt die fehlermeldung
        check_extras_input.error_label.grid_forget()

    user_input = extras_ver.get()

    if user_input == "Y" or user_input == "y":
        extra_info()
    elif user_input == "N" or user_input == "n":
        info()
    else:
        check_extras_input.error_label = ctk.CTkLabel(root, text="Ungültige Eingabe! Bitte nur 'Y' oder 'N' eingeben.", text_color="red")
        check_extras_input.error_label.grid(row=3, column=0, columnspan=3)


# Abhängigkeiten der Dropdowns
def update_subgenres(selected_genre):
    subgenres = get_subgenres_from_db(connection=connection, genre=selected_genre)
    sub_genre_dropdown.configure(values=subgenres)

    interpret_dropdown.configure(values=[])
    interpret_ver.set("Interpret")

def update_interpreten(selected_genre, selected_subgenre):
    interpreten = get_interpreten_from_db(connection=connection, genre=selected_genre, subgenre=selected_subgenre)
    interpret_dropdown.configure(values=interpreten)




### Hauptfenster ###
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("./config/theme/custom.json")
root = ctk.CTk()
root.title('Meine Musik Empfehlung')
root.geometry('800x600')
root.resizable(width=False, height=False)
root.configure()

### Hintergrundbild laden ###
bild_path = r"assetes/image/SL.123119.26540.04.jpg"
bild = Image.open(bild_path)
hintergrundbild = ctk.CTkImage(bild, size=(800, 600))
label_hintergrund = ctk.CTkLabel(root, image=hintergrundbild, text="")
label_hintergrund.place(relwidth=1, relheight=1)

### Dropdown-Menüs ###
# Genre Dropdown
genre_ver = ctk.StringVar(value="Genre")
genres = get_genres_from_db(connection=connection)
genre_dropdown = ctk.CTkOptionMenu(root, variable=genre_ver, values=genres,
                                   command=lambda value: update_subgenres(value))
genre_dropdown.grid(column=1, row=0, padx=20, pady=10)

# Sub_Genre Dropdown
sub_genre_ver = ctk.StringVar(value="Sub_Genres")
sub_genre_dropdown = ctk.CTkOptionMenu(root, variable=sub_genre_ver, values=[],
                                       command=lambda value: update_interpreten(genre_ver.get(), value))
sub_genre_dropdown.grid(column=1, row=1, padx=20, pady=10)

# Interpreten Dropdown
interpret_ver = ctk.StringVar(value="Interpret")
interpret_dropdown = ctk.CTkOptionMenu(root, variable=interpret_ver, values=[])
interpret_dropdown.grid(column=0, row=0, padx=20, pady=10)

# Extras_Header
extra_header = ctk.CTkLabel(root, text="Extra Infos: Y/N", bg_color="gray")
extra_header.grid(column=0, row=1)

# Eingabefeld für "Extras Y/N" erstellen
extras_ver = ctk.StringVar(value="")
extras_entry = ctk.CTkEntry(root, textvariable=extras_ver, placeholder_text='Hallo Welt', placeholder_text_color="gray" , width=140)
extras_entry.grid(column=0, row=2, padx=20, pady=10)
extras_entry.bind("<Return>", check_extras_input)

# Start-Button
start_btn = ctk.CTkButton(root, text="Start", command=info)
start_btn.grid(row=2, column=1, padx=20, pady=10)

root.mainloop()

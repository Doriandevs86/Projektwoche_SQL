import customtkinter as ctk
from PIL import Image

from dropdown_funktionen import connect_to_db
from dropdown_funktionen import get_genres_from_db
from dropdown_funktionen import get_interpreten_from_db
from dropdown_funktionen import get_subgenres_from_db


### Hauptfenster ###
# Fenstersettings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("./config/theme/custom.json")
# Fenster erstellen
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
genres = get_genres_from_db(connection=connect_to_db())
genre_dropdown = ctk.CTkOptionMenu(root, variable=genre_ver, values=genres,
                                    command=lambda value: update_subgenres(value))
genre_dropdown.grid(column=0, row=0, padx=20, pady=10)

# Sub_Genre Dropdown
sub_genre_ver = ctk.StringVar(value="Sub_Genres")
sub_genre_dropdown = ctk.CTkOptionMenu(root, variable=sub_genre_ver, values=[],
                                        command=lambda value: update_interpreten(genre_ver.get(), value))
sub_genre_dropdown.grid(column=0, row=1, padx=20, pady=10)

# Interpreten Dropdown
interpret_ver = ctk.StringVar(value="Interpret")
interpret_dropdown = ctk.CTkOptionMenu(root, variable=interpret_ver, values=[])
interpret_dropdown.grid(column=1, row=0, padx=20, pady=10)

# Extras Dropdown
extras_ver = ctk.StringVar(value="Extras")
extras = ["ja", "Nein"]
extras_dropdown = ctk.CTkOptionMenu(root, variable=extras_ver, values=extras, bg_color="transparent")
extras_dropdown.grid(column=1, row=1, padx=20, pady=10)

#Abhängigkeiten der Dropdowns

def update_subgenres(selected_genre):
    subgenres = get_subgenres_from_db(connection=connect_to_db(), genre=selected_genre)
    sub_genre_dropdown.configure(values=subgenres)

def update_interpreten(selected_genre, selected_subgenre):
    interpreten = get_interpreten_from_db(connection=connect_to_db(), genre=selected_genre, subgenre=selected_subgenre)
    interpret_dropdown.configure(values=interpreten)



# Info_Label
def info():
   infofenster = ctk.CTkLabel(root, text= '################################\n'
                                          '\n'
                                          'Hier steht dein Musikvorschlag \n'
                                          '\n'
                                          '\n'
                                          ' mit allen wichtigen Infos\n'
                                          '\n'
                                          '################################')
   infofenster.grid(row=3, column=0, columnspan=3)

# Start-Button
start_btn = ctk.CTkButton(root, text="Start", command=info)
start_btn.grid(row=2, column=0, columnspan=2, padx=20, pady=10)


root.mainloop()

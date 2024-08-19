
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Fael.LCI\Desktop\tkdesigner\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("577x730")
window.configure(bg = "#3C91E6")


canvas = Canvas(
    window,
    bg = "#3C91E6",
    height = 730,
    width = 577,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    42.999999999999886,
    83.0,
    anchor="nw",
    text="Bem Vindo !",
    fill="#FAFFFD",
    font=("Boogaloo Regular", 64 * -1)
)

canvas.create_text(
    42.999999999999886,
    167.0,
    anchor="nw",
    text="Realize seu Login",
    fill="#FAFFFD",
    font=("Boogaloo Regular", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    224.9999999999999,
    304.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=50.999999999999886,
    y=281.0,
    width=348.0,
    height=44.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    224.9999999999999,
    418.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=50.999999999999886,
    y=395.0,
    width=348.0,
    height=44.0
)

canvas.create_text(
    42.999999999999886,
    246.0,
    anchor="nw",
    text="usuario ou email",
    fill="#FAFFFD",
    font=("Boogaloo Regular", 18 * -1)
)

canvas.create_text(
    42.999999999999886,
    365.0,
    anchor="nw",
    text="senha",
    fill="#FAFFFD",
    font=("Boogaloo Regular", 18 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=29.999999999999886,
    y=509.0,
    width=158.0,
    height=46.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=29.999999999999886,
    y=509.0,
    width=158.0,
    height=46.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=248.9999999999999,
    y=509.0,
    width=158.0,
    height=46.0
)
window.resizable(False, False)
window.mainloop()

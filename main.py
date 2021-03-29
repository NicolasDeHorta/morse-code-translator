from tkinter import *
from PIL import ImageTk, Image
import json

## ====================================== READ JSONS DATA ======================================

with open("morse-code.json") as file:
    text_to_morse_dic = json.load(file)

# morse_to_text_data = {value : key for (key, value) in morse.items()}
# print(morse_to_text_data)
# with open("morse-to-text.json", "w") as file:
#     json.dump(morse_to_text_data, file)


with open("morse-to-text.json") as file:
    morse_to_text_dic = json.load(file)


## ====================================== TRANSLATOR FUNCTIONS ======================================

def text_to_morse():
    text = text_entry.get(1.0, "end-1c")
    global text_to_morse_dic
    translation = ""

    for letter in text:
        if letter != " ":
            translation += text_to_morse_dic[letter.lower()]
            translation += " | "
        else:
            translation += " | "
            
    morse_entry.delete(1.0, "end") #borro lo que haya en la textbox
    morse_entry.insert(INSERT, translation)


def morse_to_text():
    morse = morse_entry.get(1.0, "end-1c")
    global morse_to_text_dic
    morse = morse.split(" ")
    translation = ""

    for letter in morse:
        if letter == "|":
            translation += " "
        elif letter in [key for (key, value) in morse_to_text_dic.items()]:
            translation += morse_to_text_dic[letter]
        else:
            pass
            
    text_entry.delete(1.0, "end") #borro lo que haya en la textbox
    text_entry.insert(INSERT, translation)

def reset():
    text_entry.delete(1.0, "end")
    morse_entry.delete(1.0, "end")



## ====================================== TKINTER GUI ======================================
BACKGROUND_COLOR="#777777"
win = Tk()
win.config(bg=BACKGROUND_COLOR)
win.title("Morse Code Hacker")
win.geometry("800x800")
win.resizable(0,0)

canvas = Canvas(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=0)
img = Image.open("morseimg.png")
img = img.resize((200, 200))
image = ImageTk.PhotoImage(img)
canvas.create_image(100, 100, image=image)
canvas.place(x=300,y=50)

text_label = Label(text="Alphanumeric Text:", font='Helvetica 10 bold')
text_label.config( bg=BACKGROUND_COLOR, fg = "#fff")
text_label.place(x=40, y=350)
text_entry = Text()
text_entry.place(x=200, y=290, height= 150, width = 400)
button_text = Button(text="Translate to Morse", command=text_to_morse)
button_text.place(x=630, y=350)

text_label = Label(text="Morse code characters have to be separated by spaces, spaces are marked with this | symbol ", font='Helvetica 8 bold')
text_label.config( bg=BACKGROUND_COLOR, fg = "#fff")
text_label.place(x=150, y=500)

morse_label = Label(text="Morse Code:", font='Helvetica 10 bold')
morse_label.config( bg=BACKGROUND_COLOR, fg = "#fff")
morse_label.place(x=40, y=600)
morse_entry = Text()
morse_entry.place(x=200, y=540, height= 150, width = 400)
button_morse = Button(text="Translate to Text", command=morse_to_text)
button_morse.place(x=630, y=600)

button_reset = Button(text="RESET", command=reset)
button_reset.place(x=380, y=750)

win.mainloop()

from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO #помогает работать с байтами из интернета


def loade_image():
    try:
        response=requests.get(url)
        response.raise_for_status()
        image_data=BytesIO(response.content)
        img=Image_open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


window=Tk()
window.title("cats")
window.geometry("600x480")

label=Label()
label.pack()

url="httds://cataas.com/cat"
img=load_image(url)

if img:
    label.config(image=img)
    label.image=img

window.mainloop()
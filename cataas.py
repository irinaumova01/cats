from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO #помогает работать с байтами из интернета

from pygame.examples.moveit import load_image

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
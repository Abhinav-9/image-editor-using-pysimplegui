import PySimpleGUI as sg
from PIL import Image,ImageEnhance,ImageFilter, ImageTk, ImageDraw, ImageFont
import matplotlib.pyplot as plt

first_line = [sg.FileBrowse(),sg.Input(key="filepath")]
image_line=[sg.Image(key="showimage"), sg.Image(key="edit_image")]
second_line = [sg.Button("Original Image", key = "Original Image", size = (15,1)),
               sg.Button("Resize",key="resize", size=(15,1)),
               sg.Button("Rotate",key="rotate", size=(15,1)),
               sg.Button("Blur",key="blur", size=(15,1))]
third_line = [sg.Save(key = "save"),sg.Cancel()]


layout = [first_line, image_line,second_line, third_line]
Title = "Image Editor"

window = sg.Window(Title,layout)

while True:
    event,value = window.read()
    im_path = value["filepath"]
    
    
    if event == "Original Image":
        im = Image.open(im_path)
        window["showimage"].update(data=ImageTk.PhotoImage(im))
    
    if event == "resize":
        width,height=im.size
        width=(int(width))/2
        height=(int(height))/2
        size=(int(width),int(height)) 
        new_im=im.resize(size)
        window["edit_image"].update(data=ImageTk.PhotoImage(new_im))
    
    if event == "rotate":
        #im = Image.open(im_path)
        new_im=im.rotate(45)
        window["edit_image"].update(data=ImageTk.PhotoImage(new_im))
    
    if event == "blur":
        new_im=im.filter(ImageFilter.BLUR)
        window["edit_image"].update(data=ImageTk.PhotoImage(new_im))
    
    
        
    if event == "save":
        im.save('new_im.jpg')
    
    if event=="Cancel" or event == sg.WIN_CLOSED:
        break
window.close()


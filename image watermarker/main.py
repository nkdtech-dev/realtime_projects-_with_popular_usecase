from tkinter import *
from tkinter import ttk, filedialog,font
from PIL import  ImageTk,ImageDraw,Image


def upload_file():
    global img
    f_types = [('image Files', ['*.png','*.jpg','*.jpeg'])]
    upload_file.filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=upload_file.filename)

    upload_image.configure(image=img)
    upload_image.grid(row=0, column=0,)

    watermark=ttk.Button(main_frame, text='add watermark', command=add_watermark)
    watermark.grid(row=0,column=1)
    
    new_file=ttk.Button(main_frame, text='upload deferent file', command=upload_file)
    new_file.grid(row=0, column=1,sticky='N')



def add_watermark():
    my_font=font.Font('times new roman', size=18, weight='bold')
    my_image=Image.open(upload_file.filename)
    edit=ImageDraw.Draw(my_image)
    edit.text(xy=(0,0), text="hello", align='center',fill="#00f", font=my_font)
    watermarked= ImageTk.PhotoImage(my_image)
    upload_image.configure(image=watermarked)
    upload_image.grid(row=0,column=0)
    upload_image.image = watermarked


root=Tk()
root.title('image water marker')
root.geometry('800x500')
main_frame=ttk.Frame(root)
main_frame.grid(row=1,column=1, sticky=(N, W, E, S))
upload_image=ttk.Button(main_frame, text='upload image', command=upload_file)
upload_image.grid(row=0, column=0)

root.mainloop()

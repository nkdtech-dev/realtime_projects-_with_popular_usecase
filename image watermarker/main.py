from tkinter import *
from tkinter import ttk, filedialog,colorchooser, simpledialog, messagebox
from PIL import  ImageTk,ImageDraw,Image,ImageFont
from tkinterdnd2 import DND_FILES, TkinterDnD

light_theme='#ECF2FF'
dark_theme='#000000'


default_font=('Ubuntu', 9,)
fontfile=('Ubuntu Bold', 'arial','FurrySack',
          'Indoo BT W01 Italic','This is Electronik',
          'Okay Cotton W00 Regular','Gothix Fate',
          'Fetish-HTF-No338','Distant Galaxy Alternate Italic V2',
          'Darrians Sexy Silhouettes 2','LinotypeZootype Water',
          'AIxDARBOTZCUMI','Action of the Time UPPER CASE')

def colors():
    colors.color=colorchooser.askcolor(title='choose color',)

def save_image():
    file_name_erro=['/','.','~','-','^','*','+','`']

    file_name=simpledialog.askstring(title='save image as',prompt="image name",parent=root)
    for letter in file_name_erro:
        if letter in file_name.split() or letter == ' ':
            messagebox.showwarning(title='warninn',message=f' empty strings are not aloud {letter}   \n please try again'  )
        else:
            add_watermark.my_image.save(f'{file_name}.png', '')
            messagebox.showinfo(title='saved',message=f'image saved as {file_name}.png')
            break
        


# def themes():
#     main_frame.configure(bg=dark_theme)
#     theme.configure(image=light_image,bg=dark_theme)
def drag_drop(event):
    dragvar.set(event.data)
    upload_file()




def upload_file():
    global img
    root.draged_image=dragvar.get()
    if root.draged_image !='':
        upload_file.filename=root.draged_image
        open_image=Image.open(str(root.draged_image)).resize((546, 515),Image.Resampling.LANCZOS)
    else:
        f_types = [('image Files', ['*.png','*.jpg','*.jpeg'])]
        upload_file.filename = filedialog.askopenfilename(filetypes=f_types)
        open_image=Image.open(upload_file.filename).resize((546, 515),Image.Resampling.LANCZOS)
    root.draged_image=''
    img = ImageTk.PhotoImage(open_image)
    image_view.configure(image=img)
    image_view.grid(row=0, column=0)
    watermark=ttk.Button(root, text='add watermark', command=add_watermark)
    watermark.place(x=565, y=180)
    new_file=ttk.Button(root, text='upload deferent image', command=upload_file, width=27)
    new_file.place(x=565, y=0)

    editting_menu()



def add_watermark():
    font = ImageFont.truetype(f"fonts/{editting_menu.font_dropdown.get()}.ttf", int(editting_menu.font_entry.get()))
    add_watermark.my_image=Image.open(upload_file.filename).resize((546, 515),Image.Resampling.LANCZOS)
    edit=ImageDraw.Draw(add_watermark.my_image)
    edit.text(xy=(100,400), text=f"{editting_menu.mark_text.get()}", align='center',fill=f"{colors.color[1]}", font=font)
    add_watermark.watermarked= ImageTk.PhotoImage(add_watermark.my_image)
    image_view.configure(image=add_watermark.watermarked)
    image_view.grid(row=0,column=0,)
    image_view.image = add_watermark.watermarked
    save_photo=Button(root,text='save image', command=save_image)
    save_photo.place(x=700,y=180)

def editting_menu():
    global default_font
    global fontfile
    font_label=ttk.Label(root, text='Font size', font=default_font)
    font_label.place(x=720,y=100)
   
    editting_menu.fontspin=StringVar()
    editting_menu.font_entry=ttk.Spinbox(root, from_= 15, to = 100, width=4,textvariable=editting_menu.fontspin,)
    editting_menu.font_entry.set(20)
    editting_menu.font_entry.place(x=720,y=120)
    
    font_dropdown_label=ttk.Label(root, text='Font Type', font=default_font)
    font_dropdown_label.place(x=565,y=100)
    defaultfont=StringVar()
    editting_menu.font_dropdown=ttk.Combobox(root, textvariable= defaultfont, width=15, height=5,)
    editting_menu.font_dropdown['values']=fontfile
    editting_menu.font_dropdown.place(x=565, y=120)
    editting_menu.font_dropdown.set(fontfile[0])

    mark_text_label=ttk.Label(root, text='water mark', font=default_font)
    mark_text_label.place(x=565,y=45)
    editting_menu.mark_text=ttk.Entry(root,font=default_font, width=18)
    editting_menu.mark_text.insert(0, '@Nkdtech')
    editting_menu.mark_text.place(x=565,y=65)

    editting_menu.text_color=ttk.Button(root, text='text color', width=8,command=colors)
    editting_menu.text_color.place(x=720,y=55)
    # editting_menu.fonttype=defaultfont.get()


root=TkinterDnD.Tk()
root.title('image water marker')
root.geometry('800x500')
root.maxsize(800,500)
root.minsize(800,500)
root.configure(bg=light_theme)

drag_lable=Label(root, text='Drop The Image', bg=light_theme, font=('Ubuntu Bold', 20))
drag_lable.place(x=160,y=200)
dragvar=StringVar()
droped_image=Entry(root, textvariable=dragvar,width=26,bg=light_theme,font=('Ubuntu Bold', 20))
droped_image.place(x=50,y=250)
droped_image.drop_target_register(DND_FILES)
droped_image.dnd_bind('<<Drop>>', drag_drop)

upload_image=Button(root, text='upload image', command=upload_file)
upload_image.place(x=195,y=300)
image_view=Label(root, text='',bg=light_theme)
image_view.grid(row=0, column=1)
split=Frame(root, height=500,width=5,)
split.place(x=557,y=0)



#TODO change editor background color button
# light_image=PhotoImage('images/light.png')
# dark_image=PhotoImage('images/dark.png')
# theme=Button(root,image=light_image ,command=themes)
# theme.place(x=1, y=100)




root.mainloop()






#TODO try to implement drag and drop photo upload method

#TODO implement upload progress bar


#TODO create a resize function to crop all photos to fit the screen




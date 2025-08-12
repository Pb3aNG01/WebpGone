'''
from tkinter import *
from tkinter import filedialog, messagebox, Label
from tkinter.ttk import Combobox
from PIL import ImageTk, Image

def openimg(fpath):
    #fileTypes = [("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.webp;")]
    fileTypes = [("Image files", "*.webp;")]
    imgpath = filedialog.askopenfilename(filetypes=fileTypes)
    
    if len(imgpath):
        img = Image.open(imgpath)
        img = img.resize((450, 350))
        pic = ImageTk.PhotoImage(img)

        main_win.geometry("600x500")
        label.config(image=pic)
        label.image = pic
        messagebox.showinfo("Image Loaded", imgpath)
    else:
        messagebox.showerror("Error", "No image selected")

    fpath = imgpath

def convertfromWebp(ftype):
    imgpath = filedialog.askopenfilename()
    img = Image.open(imgpath)
    expconvert = filedialog.asksaveasfilename(defaultextension=ftype)
    img.save(expconvert)
    img.close()

if __name__ == "__main__":
    main_win = Tk()
    main_win.geometry("600x500")
    top_frame = Frame()
    mid_frame = Frame()
    bot_frame = Frame()

    label = Label(main_win)
    label.pack(pady=10)

    localimg = ""
    fformat = StringVar()
    ftype = [".png", ".jpg", ".jpeg", ".gif"]

    convertoptions = Combobox(mid_frame, values=ftype, textvariable=fformat) 
    convertoptions.set("Convert to")
    convertoptions.pack(side="top")

    opbutton = Button(mid_frame, text="Open Image", command=openimg(localimg))
    opbutton.pack(side="left")

    convertbutton = Button(mid_frame, text="Convert", command=convertfromWebp(fformat.get()))#command=convertfromWebp(localimg,fformat.get()))
    convertbutton.pack(side="right") #when converted say it is successful

    quitbutton = Button(bot_frame, text="Quit", command=main_win.destroy)
    quitbutton.pack(side="right")

    top_frame.pack()
    mid_frame.pack()
    bot_frame.pack()
    main_win.mainloop()
'''
import os
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox
from PIL import ImageTk, Image

class ImageConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x500")
        self.master.title("WebP Image Converter")

        # Instance variable to store image path
        self.imgpath = ""

        # Set up frames
        self.top_frame = Frame()
        self.mid_frame = Frame()
        self.bot_frame = Frame()

        self.label = Label(self.master)
        self.label.pack(pady=10)

        # Supported formats
        self.ftype = [".png", ".jpg", ".jpeg"]
        self.fformat = StringVar()
        self.convertoptions = Combobox(self.mid_frame, values=self.ftype, textvariable=self.fformat)
        self.convertoptions.set("Convert to")
        self.convertoptions.pack(side="top")

        # Buttons
        Button(self.mid_frame, text="Open Image", command=self.open_image).pack(side="left", padx=10)
        Button(self.mid_frame, text="Convert", command=self.convert_image).pack(side="right", padx=10)
        Button(self.bot_frame, text="Quit", command=self.master.destroy).pack(side="right", padx=10)

        # Layout
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()

    def open_image(self):
        filetypes = [("WebP Images", "*.webp")]
        path = filedialog.askopenfilename(filetypes=filetypes)
        if path:
            self.imgpath = path
            img = Image.open(self.imgpath)
            img = img.resize((450, 350))
            pic = ImageTk.PhotoImage(img)

            self.label.config(image=pic)
            self.label.image = pic  # Keep a reference
            messagebox.showinfo("Image Loaded", self.imgpath)
        else:
            messagebox.showerror("Error", "No image selected.")

    def convert_image(self):
        if not self.imgpath:
            messagebox.showerror("Error", "No image loaded. Please open a WebP image first.")
            return

        target_format = self.fformat.get()
        if target_format not in self.ftype:
            messagebox.showerror("Error", "Please select a valid format from the dropdown.")
            return

        try:
            img = Image.open(self.imgpath)
            save_path = filedialog.asksaveasfilename(defaultextension=target_format,
                                                     filetypes=[("Target file", f"*{target_format}")],initialfile=os.path.basename(self.imgpath).split(".")[0])
            if save_path:
                img.save(save_path)
                img.close()
                messagebox.showinfo("Success", f"Image saved as: {save_path}")
            else:
                messagebox.showwarning("Cancelled", "Save operation was cancelled.")
        except Exception as e:
            messagebox.showerror("Conversion Error", f"An error occurred:\n{e}")

if __name__ == "__main__":
    root = Tk()
    app = ImageConverterApp(root)
    root.mainloop()

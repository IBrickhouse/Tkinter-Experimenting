import tkinter as tk
from PIL import ImageTk,Image  


window = tk.Tk()
#canvas = tk.Canvas(window, width = 1000, height = 1000)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("IMG_3209.JPG"))
canvas.create_image(20, 20, image=img)



# window.title('Testing Window')
# window.geometry('500x500+50+50')
# window.resizable(False, False)

#message = tk.Label(window, text="Hello, World!")
#message.pack()


window.mainloop()
import tkinter
from PIL import Image, ImageTk
import webbrowser

def open_github():
    url = "https://github.com/Hell13Cat/book-parsers"
    webbrowser.open(url, new=2, autoraise=True)

def go_url():
    url = url_input.get()
    text_info.configure(text="Подождите...")  

root = tkinter.Tk()
root.resizable(width=False, height=False)
root.title("Book parser")
root.geometry('500x250')
main_window = tkinter.Frame(root)
main_window.grid()

#label = tkinter.Label(main_window, text="Book parser").grid(row=1,column=1)
global url_input
global text_info
url_input = tkinter.Entry(main_window, width=50)
url_input.grid(row=1, column=1)
button_go = tkinter.Button(main_window, text="GO", command=go_url)
button_go.grid(row=1, column=2)
text_info = tkinter.Label(main_window, text="  ", font=("Arial Bold", 12))
text_info.grid(row=2,column=1)
button_update = tkinter.Button(main_window, text="GitHub", command=open_github).grid(row=1, column=3)


#canvas = tkinter.Canvas(root, height=400, width=700)
#image = Image.open("test.png")
#photo = ImageTk.PhotoImage(image)
#image = canvas.create_image(0, 0, anchor='nw',image=photo)
#canvas.grid(row=2,column=1)
root.mainloop()
import tkinter
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import webbrowser
import gen_data
gen_data.gen_parsers()
gen_data.clear_cache()
import gate_pars

def open_github():
    url = "https://github.com/Hell13Cat/book-parsers"
    webbrowser.open(url, new=2, autoraise=True)

def go_url():
    url = url_input.get()
    text_info.configure(text="Подождите...")
    gate_pars.main(url)

def search():
    query = url_input.get()
    text_info.configure(text="Подождите...")
    site = sites.get()
    search_data = gate_pars.search(query, site)
    if search_data["code"] == 1:
        text_info.configure(text="OK")
    if search_data["code"] == 0:
        text_res = "Error - " + search_data["desce"]
        text_info.configure(text=text_res)

root = tkinter.Tk()
root.resizable(width=False, height=False)
root.title("Book parser")
root.geometry('500x50')
main_window = tkinter.Frame(root)
main_window.grid()

#label = tkinter.Label(main_window, text="Book parser").grid(row=1,column=1)
url_input = tkinter.Entry(main_window, width=50)
url_input.grid(row=1, column=1)
button_go = tkinter.Button(main_window, text="Поиск", command=search).grid(row=1, column=3)
#text_info = tkinter.Label(main_window, text="  ", font=("Arial Bold", 12))
text_info = tkinter.Label(main_window, text="  ")
text_info.grid(row=2,column=1)
button_update = tkinter.Button(main_window, text="GitHub", command=open_github).grid(row=1, column=4)
#formats = Combobox(main_window, width=10)
sites = Combobox(main_window, width=10)
sites['values'] = gate_pars.name_list()
sites.current(0)
sites.grid(row=1, column=2) 
#formats['values'] = ("fb2", "epub", "txt")
#formats.current(0)  # установите вариант по умолчанию  
#formats.grid(row=1, column=2)  


#canvas = tkinter.Canvas(root, height=400, width=700)
#image = Image.open("test.png")
#photo = ImageTk.PhotoImage(image)
#image = canvas.create_image(0, 0, anchor='nw',image=photo)
#canvas.grid(row=2,column=1)
root.mainloop()
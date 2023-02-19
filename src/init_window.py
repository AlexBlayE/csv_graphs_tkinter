from tkinter import filedialog, Tk, Frame, Label, Button, mainloop, Entry, StringVar, Menu, messagebox, BooleanVar
from webbrowser import open

class InitWindow:
    
    def __init__(self):       
        #Root
        self._root = Tk()
        self._root.title("CSV GRAFIKATOR")
        self._root.iconbitmap("icons\icon.ico")
        self._root.resizable(False, False)
        
        #Variables
        self._csv_path = StringVar(value="C:\\")
        self._is_csv_selected = BooleanVar(value=False)
        
        #Frame
        _frame = Frame(self._root, width="720", height="480")
        _frame.pack()
        
        #Widgets root
        _menu_bar = Menu(self._root)
        self._root.config(menu=_menu_bar)
        
        _menu_info = Menu(_menu_bar, tearoff=False)
                
        _menu_bar.add_cascade(label="Info", menu=_menu_info)
        _menu_info.add_cascade(label="GitHub Repository", command=lambda: open("https://github.com/AlexBlayE/CSVGRAFIKATOR"),)
        
        #Widgets frame        
        Label(_frame, text="CSV Path: ").grid(row=0, column=1, pady=5)
        
        _text_box = Entry(_frame, justify="center", state="readonly", textvariable=self._csv_path)
        _text_box.grid(row=1, column=1, padx=80, ipadx=150)#110
        
        _button_path = Button(_frame, text="Search path", justify="left", command=lambda: InitWindow._search_path(self._csv_path),)
        _button_path.grid(row=2, column=1, padx=20, pady=10, sticky="w", ipadx=50)
        
        _button_go = Button(_frame, text="   Go   ", justify="right", command=lambda: InitWindow._quit_window(self._root, self._is_csv_selected, self._csv_path),) 
        _button_go.grid(row=2, column=1, padx=20, pady=10, sticky="e", ipadx=50)
        
        #mainloop
        self._root.mainloop()
        
    def _search_path(path):
        accepted_files = [("CSV Files", "*.csv")]
        file_path = filedialog.askopenfile(filetypes=accepted_files)
        if file_path == None:
            file_path = "C:\\"
        else:
            path.set(file_path.name)
        
    def _is_path_accept(path):# return true if path is a .csv
        string = path.get()
        length = len(string)
        if string[length - 4:] == ".csv":
            return True
        else:
            return False
        
    def _quit_window(self, csvboolean, path):
        if InitWindow._is_path_accept(path) == True:
            csvboolean.set(value=True)
            self.destroy()
        else:
            messagebox.showinfo("ALERT", "NEED A CSV FILE")
    
    def get_path(self):
        return self._csv_path.get()
    
    def get_is_csv_path(self):
        return self._is_csv_selected.get()
                
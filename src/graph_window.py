from tkinter import Tk, Frame, BooleanVar, StringVar, Menu, OptionMenu, Button, filedialog, messagebox
from matplotlib.pyplot import figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import read_csv

class GraphWindow():

    def __init__(self, path):
        #Root
        self._root = Tk()
        self._root.title("Graphs")
        self._root.iconbitmap("icons\\icon.ico")
        self._root.resizable(False, False)
        self._root.columnconfigure(0, weight=3)
        self._root.columnconfigure(1,weight=1)
        
        #Frames
        _left_frame = Frame(self._root)
        _left_frame.grid(row=0, column=0)
        
        _right_frame = Frame(self._root)
        _right_frame.grid(row=0, column=4)
        
        #Variables
        self._return = BooleanVar(value=False)
        _df = GraphWindow._load_csv(path)
        
        #
        _menu_options = GraphWindow._what_name_columns(_df)
        _var_menuX = StringVar(value=_menu_options[0])
        _var_menuY = StringVar(value=_menu_options[1])
        
        #
        _graph_options = ["Plot", "Bar", "Scatter"]
        _var_graph = StringVar(value=_graph_options[0])
        
        #dataframes
        _x = _df[_var_menuX.get()]
        _y = _df[_var_menuY.get()]
        
        #Widgets root
        _menu_bar = Menu(self._root)
        self._root.config(menu=_menu_bar)
        
        _menu_window = Menu(_menu_bar, tearoff=False)
        _menu_info = Menu(_menu_bar, tearoff=False)
        
        _menu_bar.add_cascade(label="Window", menu=_menu_window)     
        _menu_window.add_cascade(label="Return to Initial Window", command=lambda:GraphWindow._change_return_initial(self._return, self._root),)
        
        _menu_bar.add_cascade(label="Tools", menu=_menu_info)
        _menu_info.add_cascade(label="Download JPG", command=lambda:GraphWindow._download_jpg(self._canvas),)
        
        #Widgets frame
        _data_menuX = OptionMenu(_right_frame, _var_menuX, *_menu_options,)
        _data_menuX.grid()
        
        _data_menuY = OptionMenu(_right_frame, _var_menuY, *_menu_options,)
        _data_menuY.grid()
        
        _option_menu= OptionMenu(_right_frame, _var_graph, *_graph_options,)
        _option_menu.grid()
        
        Button(_right_frame, text="Change", command=lambda: GraphWindow._update_graph(_ax, self._canvas, _var_graph.get(),
                                                                                       _df[_var_menuX.get()], _df[_var_menuY.get()]),).grid()
        #graph options
        _fig = figure()
        _ax = _fig.add_subplot(111)#111
        _ax.plot(_x, _y)# plot scatter bar fill_between
        self._canvas = FigureCanvasTkAgg(_fig, _left_frame)
        self._canvas.get_tk_widget().pack()

        #Exit button events
        self._root.protocol("WM_DELETE_WINDOW",lambda: self._canvas.destroy())
        self._root.protocol("WM_DELETE_WINDOW", lambda: self._root.quit())
        
        #mainloop
        self._root.mainloop()
        
    def _load_csv(doc_path):
        return read_csv(doc_path)
    
    def _what_name_columns(dataframe):
        name_columns = dataframe.columns
        return name_columns
                
    def _update_graph(ax, canvas, option, x, y):
        if option == "Plot":
            ax.clear()
            ax.plot(x, y)
            canvas.draw()
        elif option == "Bar":
            ax.clear()
            ax.bar(x, y)
            canvas.draw()
        elif option == "Scatter":
            ax.clear()
            ax.scatter(x, y)
            canvas.draw()
   
    def _download_jpg(grafic):
        accepted_files = [("JPG Image", "*.jpg")]
        directory = filedialog.asksaveasfilename(filetypes=accepted_files)
        if directory == None:
            return 0
        else:
            grafic.print_jpg(directory + ".jpg")
            messagebox.showinfo("ALERT", "JPG DOWNLOADED IN:   " + directory + ".jpg")
    
    def _change_return_initial(var, root):
        var.set(value=True)
        root.destroy()
            
    def get_return_initial(self):
        return self._return.get()
        

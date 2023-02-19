import init_window as iniw
import graph_window as gw

def main():
    
    while(True):
        first_window = iniw.InitWindow()
        
        #                    
        path = first_window.get_path()
        is_csv = first_window.get_is_csv_path()
        
        if is_csv == True:
            graph_window = gw.GraphWindow(path=path)
            
            return_initial = graph_window.get_return_initial()
            
        if not return_initial:
            break
        
        return_initial = False
        
    return 0 

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        e.add_note("ERROR")
        quit()
    
    
    
    
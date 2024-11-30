#!/usr/bin/env python3

import enum
import tkinter as tk

APP_TITLE: str = "app title here"


class MainContentFrame(tk.Frame):


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
       
class MainAppWindow(tk.Tk):

    def __init__(self, content_frame_factory, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(APP_TITLE)
        self.bind('<Visibility>', self.center)
        
        self.content_frame = content_frame_factory(self)
        self.content_frame.grid(row=0, column=0, padx=5, pady=5)

    def center(self, event) -> None:
        
        window_height = self.winfo_height()
        window_width = self.winfo_width()
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        top = (screen_height - window_height) // 2
        left = (screen_width - window_width) // 2
        
        self.geometry(f'{window_width}x{window_height}+{left}+{top}')
        self.resizable(False, False)

def create_main_content_frame(parent: tk.Tk) -> MainContentFrame:
    return MainContentFrame(parent)

def main():

    MainAppWindow(create_main_content_frame).mainloop()

if __name__ == '__main__':
    main()

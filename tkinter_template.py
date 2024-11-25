#!/usr/bin/env python3

import tkinter as tk

APP_TITLE: str = "app title here"

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)


def main():
    App().mainloop()

if __name__ == '__main__':
    main()

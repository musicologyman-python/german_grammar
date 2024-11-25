#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk

from icecream import ic

import enum

APP_TITLE: str = "Tab Test"

class TabOrder(enum.Enum):
    TOP_BOTTOM_LEFT_RIGHT = enum.auto()
    LEFT_RIGHT_TOP_BOTTOM = enum.auto()
    

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.variables = []
        self.controls = []

        self._tab_order = TabOrder.TOP_BOTTOM_LEFT_RIGHT

        main_frame = tk.Frame(self)
        main_frame.grid(row=0, column=0, padx=5, pady=5)

        for i in range(9):
            var = tk.StringVar(main_frame, value=i)
            # var.set(str(i))
            self.variables.append(var)
            ctl = ttk.Entry(main_frame, 
                            textvariable=var, 
                            width=2, 
                            justify='right')
            ctl.grid(row=i // 3, column=i % 3)
            self.controls.append(ctl)

        set_taborder_button = ttk.Button(main_frame, 
                                         text='Toggle Tab Order',
                                         command=self._toggle_tab_order)

        set_taborder_button.grid(row=3, column=0, columnspan=3) 
        

        self.title(APP_TITLE)
        for v in self.variables:
            ic(v.get())

    def _toggle_tab_order(self):
        if self._tab_order == TabOrder.TOP_BOTTOM_LEFT_RIGHT:
            for i in range(len(self.controls)):
                self.controls[(i // 3) + (i % 3) * 3].lift() 
            self._tab_order = TabOrder.LEFT_RIGHT_TOP_BOTTOM
        else:
            for i in range(len(self.controls)):
                self.controls[i].lift()
            self._tab_order = TabOrder.TOP_BOTTOM_LEFT_RIGHT


def main():
    App().mainloop()

if __name__ == '__main__':
    main()

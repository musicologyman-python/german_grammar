#!/usr/bin/env python3

import enum
import tkinter as tk

from icecream import ic

APP_TITLE: str = "German Definite Articles"

class GenderCaseEnum(enum.Enum):

    NOMINATIVE_MASCULINE = 0
    NOMINATIVE_FEMININE  = 1
    NOMINATIVE_NEUTER    = 2
    NOMINATIVE_PLURAL    = 3
    ACCUSATIVE_MASCULINE = 4
    ACCUSATIVE_FEMININE  = 5
    ACCUSATIVE_NEUTER    = 6
    ACCUSATIVE_PLURAL    = 7
    DATIVE_MASCULINE     = 8
    DATIVE_FEMININE      = 9
    DATIVE_NEUTER        = 10
    DATIVE_PLURAL        = 11
    GENITIVE_MASCULINE   = 12
    GENITIVE_FEMININE    = 13
    GENITIVE_NEUTER      = 14
    GENITIVE_PLURAL      = 15


answers = 'der die das die den die das die dem der dem den des der des der'.split()

class MainContentFrame(tk.Frame):

    # region constants 

    _SHOW_ANSWERS_CAPTION = 'Show answers'
    _HIDE_ANSWERS_CAPTION = 'Hide answers'

    _FONT_NAME = 'Arial'
    _FONT_SIZE = 14
    _DEFAULT_FONT = (_FONT_NAME, _FONT_SIZE, 'normal')
    _BOLD_FONT = (_FONT_NAME, _FONT_SIZE, 'bold')
    
    # endregion

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        GENDERS = ['Masculine', 'Feminine', 'Neuter', 'Plural']
        CASES = ['Nominative', 'Accusative', 'Dative', 'Genitive']

        for i, case_ in enumerate(CASES, start=1):
            tk.Label(self, 
                     text=case_,
                     font=self.__class__._BOLD_FONT).grid(row=0, column=i)

        for i, gender in enumerate(GENDERS, start=1):
            tk.Label(self, 
                     text=gender,
                     font=self.__class__._BOLD_FONT).grid(row=i, column=0, sticky=tk.W)

        self.answer_variables = [tk.StringVar(self) for _ in range(16)]

        self.answer_entries = [tk.Entry(self,
                                   textvariable = self.answer_variables[i],
                                   relief=tk.SUNKEN,
                                   borderwidth=3,
                                   width=4) for i in range(16)]
        for i, answer_entry in enumerate(self.answer_entries):
            answer_entry.grid(row=(i % 4)+1, column=(i // 4)+1, 
                              sticky=None)
        
        for i in range(0,5):
            self.columnconfigure(i, uniform="entries")

        self.button_frame = tk.Frame(self)
        self.button_frame.grid(row=5, column=0, columnspan=5)
        
        self.show_hide_answers_button_caption = tk.StringVar(self)
        self.show_hide_answers_button_caption.set(
            self.__class__._SHOW_ANSWERS_CAPTION)
        self.show_hide_answers_button = \
                tk.Button(self.button_frame,
                          textvariable=self.show_hide_answers_button_caption,
                          command=self._show_hide_answers)
        self.show_hide_answers_button.pack(side='left')

        self.check_answers_button = tk.Button(self.button_frame,
                                              text='Check answers',
                                              command=self._check_answers)
        self.check_answers_button.pack(side='left')

        self.clear_answers_button = tk.Button(self.button_frame,
                                              text='Clear answers',
                                              command=self._clear_answers)
        self.clear_answers_button.pack(side='left')

        self._set_tab_order()
        
        self.bind('<Visibility>', self._on_visibility)
        
    def _on_visibility(self, event):
        self.answer_entries[0].focus()

    def _show_hide_answers(self):
        if (self.show_hide_answers_button_caption.get() == 
                self.__class__._SHOW_ANSWERS_CAPTION):
            self.show_hide_answers_button_caption.set(
                self.__class__._HIDE_ANSWERS_CAPTION)
            for i, answer in enumerate(answers):
                self.answer_variables[i].set(answer)
        else:
            self.show_hide_answers_button_caption.set(
                self.__class__._SHOW_ANSWERS_CAPTION)
            self._clear_answers()

    def _check_answers(self):
        for i, answer_variable in enumerate(self.answer_variables):
            if answer_variable.get().strip().lower() != answers[i]:
                ic(answer_variable.get().strip().lower(), answers[i])
                self.answer_entries[i].configure(fg='red', 
                    font=self.__class__._BOLD_FONT)
            else:
                self.answer_entries[i].configure(fg='blue', 
                                                 font=self.__class__._BOLD_FONT)
    
    def _clear_answers(self):
        for answer_var in self.answer_variables:
            answer_var.set('')
        for answer_entry in self.answer_entries:
            answer_entry.configure(fg='black', 
                font=self.__class__._DEFAULT_FONT)

    def _set_tab_order(self):
        for i in range(len(self.answer_entries)):
            self.answer_entries[(i // 4) + (i % 4) * 4].lift() 



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

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

class App(tk.Tk):

    _SHOW_ANSWERS_CAPTION = 'Show answers'
    _HIDE_ANSWERS_CAPTION = 'Hide answers'

    _FONT_NAME = 'Arial'
    _FONT_SIZE = 14
    _DEFAULT_FONT = (_FONT_NAME, _FONT_SIZE, 'normal')
    _BOLD_FONT = (_FONT_NAME, _FONT_SIZE, 'bold')

    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)

        GENDERS = ['Masculine', 'Feminine', 'Neuter', 'Plural']
        CASES = ['Nominative', 'Accusative', 'Dative', 'Genitive']

        main_content_frame = tk.Frame(self, padx=5, pady=5)
        main_content_frame.pack()

        for i, gender in enumerate(GENDERS, start=1):
            tk.Label(main_content_frame, 
                     text=gender,
                     font=App._BOLD_FONT).grid(row=i, column=0, sticky=tk.W)

        for i, case_ in enumerate(CASES, start=1):
            tk.Label(main_content_frame, 
                     text=case_,
                     font=App._BOLD_FONT).grid(row=0, column=i)

        self.answer_variables = [tk.StringVar(self) for _ in range(16)]

        self.answer_entries = [tk.Entry(main_content_frame,
                                   textvariable = self.answer_variables[i],
                                   relief=tk.SUNKEN,
                                   borderwidth=3,
                                   width=4) for i in range(16)]
        for i, answer_entry in enumerate(self.answer_entries):
            answer_entry.grid(row=(i % 4)+1, column=(i // 4)+1, 
                              sticky=None)
        
        for i in range(0,5):
            main_content_frame.columnconfigure(i, weight=1)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=5)
        
        self.show_hide_answers_button_caption = tk.StringVar(self)
        self.show_hide_answers_button_caption.set(App._SHOW_ANSWERS_CAPTION)
        self.show_hide_answers_button = \
                tk.Button(button_frame,
                          textvariable=self.show_hide_answers_button_caption,
                          command=self._show_hide_answers)
        self.show_hide_answers_button.pack(side='left')

        self.check_answers_button = tk.Button(button_frame,
                                              text='Check answers',
                                              command=self._check_answers)
        self.check_answers_button.pack(side='left')

        self.clear_answers_button = tk.Button(button_frame,
                                              text='Clear answers',
                                              command=self._clear_answers)
        self.clear_answers_button.pack(side='left')

    def _show_hide_answers(self):
        if self.show_hide_answers_button_caption.get() == App._SHOW_ANSWERS_CAPTION:
            self.show_hide_answers_button_caption.set(App._HIDE_ANSWERS_CAPTION)
            for i, answer in enumerate(answers):
                self.answer_variables[i].set(answer)
        else:
            self.show_hide_answers_button_caption.set(App._SHOW_ANSWERS_CAPTION)
            self._clear_answers()

    def _check_answers(self):
        for i, answer_variable in enumerate(self.answer_variables):
            if answer_variable.get().strip().lower() != answers[i]:
                ic(answer_variable.get().strip().lower(), answers[i])
                self.answer_entries[i].configure(fg='red', font=App._BOLD_FONT)
            else:
                self.answer_entries[i].configure(fg='blue', 
                                                 font=App._BOLD_FONT)
    
    def _clear_answers(self):
        for answer_var in self.answer_variables:
            answer_var.set('')
        for answer_entry in self.answer_entries:
            answer_entry.configure(fg='black', font=App._DEFAULT_FONT)



def main():
    App().mainloop()

if __name__ == '__main__':
    main()

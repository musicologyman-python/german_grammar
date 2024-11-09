import inspect
from pathlib import Path
from pprint import pprint
import tkinter as tk
import tkinter.filedialog as fd

from toolz.functoolz import compose_left

docit = compose_left(inspect.getdoc, print)

def browse_for_file():
    return fd.askopenfilename()

def browse_for_folder():
    return fd.askdirectory(initialdir=Path.cwd())



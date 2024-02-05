from tkinter import filedialog
import pandas as pd
from src.algorithms.perceptron import execute_perceptron
from src.interfaces.graphics_view import graphic_norm, graphic_w
from src.interfaces.output_view import option_button_output

file = ""


def read_csv():
    global file
    csv = filedialog.askopenfilename(filetypes=[('CSV Files', '*csv')])
    if csv:
        file_read = pd.read_csv(csv, delimiter=";")
        file = file_read
    else:
        print("Invalid file")


def execute(frame, frame_graphics, canvas_graphics, eras, eta, tolerance):
    data = {"matrix": get_matrix(),
            "eras": int(eras.get()),
            "eta": float(eta.get()),
            "tolerance": float(tolerance.get())}
    errors, w_eras, info = execute_perceptron(data)
    for w in frame_graphics.winfo_children():
        w.destroy()
    graphic_norm(frame_graphics, canvas_graphics, errors)
    graphic_w(frame_graphics, canvas_graphics, w_eras)
    option_button_output(frame, info)


def get_matrix():
    x = []
    values = []
    [values.append(float(v)) for v in file.columns]
    x.append(values)
    [x.append(list(row)) for row in file.values]
    return x

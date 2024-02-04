import csv
from tkinter import filedialog
import tkinter as tk
import pandas as pd
import numpy as np
import glob
import random

window = tk.Tk()
window.title("Inteligencia artificial")
# window.geometry("500x600")
window.config(bg='#2e2e2e')
window.resizable(False, False)

frame = tk.Frame(window)
frame.pack(expand=True)


def read_csv():
    x = []
    values = []
    file = filedialog.askopenfilename(filetypes=[('CSV Files', '*csv')])
    if file:
        file_read = pd.read_csv(file, delimiter=";")
        [values.append(float(v)) for v in file_read.columns]
        x.append(values)
        [x.append(list(row)) for row in file_read.values]
        matrix = np.array(x)
        matrix_2 = np.insert(matrix, 0, 1, axis=1)
        print(matrix_2)
        yd = np.array(matrix[:, -1]).astype(int).reshape(-1, 1)
        w = initializer_w(matrix)
        u = get_u(w, matrix)
        yc = function_activation_step(u)
        e = calculate_error(yd, yc)
        delta_w = calculate_delta_w(1, e, matrix)
        norm = calculate_norm(e)
        print(norm)
        w = update_w(w, delta_w)
        print(w)
    else:
        print("Not Found CSV")


def initializer_w(matrix):
    return np.random.random((1, matrix.shape[1] - 1))
    # return [[random.random()] for _ in range(matrix.shape[1] - 1)]


def get_u(w, matrix):
    x = matrix[:, :(matrix.shape[1] - 1)]
    return np.dot(x, w.T)


def function_activation_step(u):
    return np.where(u >= 0, 1, 0).astype(int)


def calculate_error(yd, yc):
    # yd == yc
    # yd ^ yc
    return yd - yc


def calculate_norm(e):
    return np.linalg.norm(e)


def calculate_delta_w(eta, e, matrix):
    x = matrix[:, :(matrix.shape[1] - 1)]
    return (-eta) * np.dot(e.T, x)


def update_w(w, delta_w):
    return w + delta_w


def option_read_csv():
    text = tk.Label(frame, text="Select file '.csv'")
    text.pack()
    open_button = tk.Button(frame, text="Open file", command=lambda: read_csv())
    open_button.pack()


option_read_csv()

window.mainloop()

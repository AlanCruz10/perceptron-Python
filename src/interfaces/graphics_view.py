import random
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import mplcursors
import os
import numpy as np


def graphic_norm(frame, canvas, errors):
    output_folder = 'graphics/'
    os.makedirs(output_folder, exist_ok=True)
    eras = list(range(0, len(errors)))
    fig, ax = plt.subplots(figsize=(12, 5.9), dpi=60)
    ax.spines['left'].set_position('zero')
    ax.spines['left'].set_color('gray')
    ax.spines['bottom'].set_position('zero')
    ax.spines['bottom'].set_color('gray')
    ax.plot(eras, errors, label='Errores', marker='s', linestyle='-', color='red')
    ax.set_xlim((0 - 1), (len(eras) + 1))
    if min(errors) >= 0:
        ax.set_ylim((0 - 1), (max(errors) + 1))
    else:
        ax.set_ylim((min(errors) - 1), (max(errors) + 1))
    ax.set_xticks(range(len(errors)), labels=eras, rotation=30)
    ax.set_title('Evolución de la norma del error')
    ax.set_xlabel('Época')
    ax.set_ylabel('norm (|E|)')
    ax.legend(loc='upper right', bbox_to_anchor=(1, 1))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    filename = os.path.join(output_folder, 'evolucion_norma_error.png')
    fig.savefig(filename)
    mplcursors.cursor(hover=True)
    canvas_figure = FigureCanvasTkAgg(fig, master=frame)
    canvas_figure.draw()
    canvas_figure_widget = canvas_figure.get_tk_widget()
    canvas_figure_widget.pack()
    toolbar = NavigationToolbar2Tk(canvas_figure, frame)
    toolbar.zoom(10)
    toolbar.place(x=2000, y=0)
    frame.update_idletasks()
    bbox = canvas.bbox(tk.ALL)
    canvas.configure(scrollregion=bbox)


def graphic_w(frame, canvas, w_eras):
    output_folder = 'graphics/'
    os.makedirs(output_folder, exist_ok=True)
    eras = list(range(0, len(w_eras)))
    w = np.array([v[0] for v in w_eras])
    fig, ax = plt.subplots(figsize=(12, 5.9), dpi=60)
    ax.spines['left'].set_position('zero')
    ax.spines['left'].set_color('gray')
    ax.spines['bottom'].set_position('zero')
    ax.spines['bottom'].set_color('gray')
    marks = ['s', 'o', '^']
    for i in range(w.shape[1]):
        ax.plot(range(w.shape[0]), w[:, i], label=f'Peso {i}', marker=random.choice(marks), linestyle='-')
    ax.set_xlim((0 - 1), (len(w_eras) + 1))
    if np.min(w) >= 0:
        ax.set_ylim((0 - 1), (np.max(w) + 1))
    else:
        ax.set_ylim((np.min(w) - 1), (np.max(w) + 1))
    ax.set_xticks(range(len(w_eras)), labels=eras, rotation=30)
    ax.set_title('Evolución de los pesos')
    ax.set_xlabel('Época')
    ax.set_ylabel('Pesos (w)')
    ax.legend(loc='upper right', bbox_to_anchor=(1, 1))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    filename = os.path.join(output_folder, 'evolucion_de_pesos.png')
    fig.savefig(filename)
    mplcursors.cursor(hover=True)
    canvas_figure = FigureCanvasTkAgg(fig, master=frame)
    canvas_figure.draw()
    canvas_figure_widget = canvas_figure.get_tk_widget()
    canvas_figure_widget.pack()
    toolbar = NavigationToolbar2Tk(canvas_figure, frame)
    toolbar.zoom(10)
    toolbar.place(x=2000, y=0)
    frame.update_idletasks()
    bbox = canvas.bbox(tk.ALL)
    canvas.configure(scrollregion=bbox)

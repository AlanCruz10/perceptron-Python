import tkinter as tk
from initialize import read_csv, execute


def option_read_csv(frame):
    text = tk.Label(frame, text="Selecciona el archivo '.csv'", bg='black', fg='white')
    text.pack()
    open_button = tk.Button(frame, text="Abrir archivo", fg='white', bg='green', command=read_csv)
    open_button.pack()


def option_eta(frame):
    eta_title = tk.Label(frame, text='Eta', bg='black', fg='white')
    eta_title.pack()
    eta_entry = tk.Entry(frame, justify=tk.CENTER)
    eta_entry.pack()
    return eta_entry


def option_tolerance(frame):
    tolerance_title = tk.Label(frame, text='Tolerancia', bg='black', fg='white')
    tolerance_title.pack()
    tolerance_title = tk.Entry(frame, justify=tk.CENTER)
    tolerance_title.pack()
    return tolerance_title


def option_eras(frame):
    eras_title = tk.Label(frame, text='Épocas', bg='black', fg='white')
    eras_title.pack()
    eras_title = tk.Entry(frame, justify=tk.CENTER)
    eras_title.pack()
    return eras_title


def option_button_calculate(frame, frame_graphics, canvas_graphics, eras, eta, tolerance):
    calculate_button = tk.Button(frame, text="Ejecutar", fg='white', bg='red', command=lambda: execute(frame, frame_graphics, canvas_graphics, eras, eta, tolerance))
    calculate_button.pack(pady=3)
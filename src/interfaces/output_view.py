import tkinter as tk
from tkinter import messagebox


def option_button_output(frame, info):
    calculate_button = tk.Button(frame, text="Salidas", fg='white', bg='blue', command=lambda: output(frame, info))
    calculate_button.place(x=150, y=60)


def output(frame, info):
    output_frame = tk.Frame(frame, bg='black')
    output_frame.place(width=275, height=200, x=450, y=0)
    info_text = f"Peso inicial: {info['w_initial']} \n\n" \
                f"Peso final: {info['w_final']} \n\n" \
                f"Eta: {info['eta']} \n" \
                f"Épocas: {info['eras']}\n" \
                f"Tolerancia: {info['tolerance']}\n"
    scrollbar = tk.Scrollbar(output_frame, orient=tk.VERTICAL)
    output_text = tk.Text(output_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, bg='black', fg='white')
    output_text.insert(tk.END, info_text)
    output_text.config(width=30, height=10)
    scrollbar.config(command=output_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    output_text.pack(expand=True, fill=tk.BOTH)
    messagebox.showinfo("Salidas", info_text)

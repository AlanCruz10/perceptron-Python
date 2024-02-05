import tkinter as tk
from src.interfaces.options_view import option_read_csv, option_eras, option_eta, option_tolerance, \
    option_button_calculate


def main():
    window = tk.Tk()
    window.title("Inteligencia artificial")
    window.geometry("742x578")
    window.config(bg='#2e2e2e')
    window.resizable(False, False)
    frame = tk.Frame(window, bg="#9C9292")
    frame.pack(fill='both', expand=True)
    option_read_csv(frame)
    eras = option_eras(frame)
    eta = option_eta(frame)
    tolerance = option_tolerance(frame)
    canvas_graphics = tk.Canvas(frame, bg="#525252")
    scrollbar_vertical = tk.Scrollbar(canvas_graphics, orient=tk.VERTICAL, command=canvas_graphics.yview)
    canvas_graphics.configure(yscrollcommand=scrollbar_vertical.set)
    frame_graphics = tk.Frame(canvas_graphics)
    canvas_graphics.create_window((0, 0), window=frame_graphics, anchor="nw")
    option_button_calculate(frame, frame_graphics, canvas_graphics, eras, eta, tolerance)
    canvas_graphics.pack(fill="both", expand=True)
    scrollbar_vertical.pack(side="right", fill="y")
    canvas_graphics.pack()
    window.mainloop()


if __name__ == "__main__":
    main()

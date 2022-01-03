import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()


def main():
    main_window = MainWindow()
    main_window.mainloop()


if __name__ == "__main__":
    main()

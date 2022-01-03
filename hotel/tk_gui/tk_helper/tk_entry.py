import tkinter as tk


def change_entry(entry: tk.Entry, string: str) -> None:
    entry.delete(0, "end")
    entry.insert(0, string)

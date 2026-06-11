import json
import tkinter as tk
from tkinter import ttk

def load_json(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def save_json(file_path: str, data: dict) -> None:
    with open(file_path, "w") as file:
        json.dump(data, file)

# loaded_data = load_json("Data/shohei_ohtani_goal_matrix.json")
# print(loaded_data)

# Initialize the main application window
root = tk.Tk()
root.title("My First Python GUI")
root.geometry("400x200")

# Add a text label
label = ttk.Label(root, text="Hello, World!", font=("Arial", 16))
label.pack(pady=20)

# Add a clickable button
def on_click():
    label.config(text="Button Clicked!")

button = ttk.Button(root, text="Click Me", command=on_click)
button.pack(pady=10)

# Start the application's persistent event loop
root.mainloop()

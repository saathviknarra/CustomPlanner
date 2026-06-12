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

def populating_load_list(leftcorner: tuple, key: str, data: dict, load_list: list) -> None:
    x, y = leftcorner
    for i in range(3):
        for j in range(3):
            list_idx = i * 3 + j
            print(f"data key : {data[key]}")
            print(f"list index : {list_idx}")
            if list_idx < 4:
                load_list[x + i][y + j] = data[key][list_idx]
            elif list_idx == 4:
                print(f"key without suffix : {key[:-9]}")
                load_list[x + i][y + j] = data[key[:-9]]
            elif list_idx < 8:
                load_list[x + i][y + j] = data[key][list_idx-1]

def populating_middle_of_load_list(leftcorner: tuple, key: str, data: dict, load_list: list) -> None:
    x, y = leftcorner
    for i in range(3):
        for j in range(3):
            list_idx = i * 3 + j
            if list_idx < 4:
                load_list[x + i][y + j] = data[key.rstrip() + " " + str(list_idx + 1)]
            elif list_idx == 4:
                load_list[x + i][y + j] = data["Main Goal"]
            else:
                load_list[x + i][y + j] = data[key.rstrip() + " " + str(list_idx)]

loaded_data = load_json("Data/shohei_ohtani_goal_matrix.json")

load_list = [[0 for _ in range(9)] for _ in range(9)]
populating_middle_of_load_list((3, 3), "Supporting Improvements", loaded_data, load_list)

# for i in range(3):
#     for j in range(3):
#         list_idx = i * 3 + j
#         if list_idx < 4:
#             populating_load_list((i * 3, j * 3), f"Supporting Improvements {list_idx} subgoals", loaded_data, load_list)
#         elif list_idx == 4:

print(load_list)


# # Initialize the main application window
# root = tk.Tk()
# root.title("My First Python GUI")
# root.geometry("400x200")

# # Add a text label
# label = ttk.Label(
#     root,
#     text="Hello, World!",
#     font=("Arial", 16),
#     foreground="white",
#     background="black",
#     anchor="center",
# )
# label.pack(pady=20, fill=tk.BOTH, expand=True)


# # Add a clickable button
# def on_click():
#     label.config(text="Button Clicked!")


# button = ttk.Button(root, text="Click Me", command=on_click)
# button.pack(pady=10)

# # Start the application's persistent event loop
# root.mainloop()

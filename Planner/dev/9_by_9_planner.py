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


def populating_load_list(
    leftcorner: tuple, key: str, data: dict, load_list: list
) -> None:
    x, y = leftcorner
    for i in range(3):
        for j in range(3):
            list_idx = i * 3 + j
            # print(f"data key : {data[key]}")
            # print(f"list index : {list_idx}")
            if list_idx < 4:
                load_list[x + i][y + j] = data[key][list_idx]
            elif list_idx == 4:
                # print(f"key without suffix : {key[:-9]}")
                load_list[x + i][y + j] = data[key[:-9]]
            else:
                load_list[x + i][y + j] = data[key][list_idx - 1]


def populating_middle_of_load_list(
    leftcorner: tuple, key: str, data: dict, load_list: list
) -> None:
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


def populate_load_list(loaded_data: dict, load_list: list) -> None:
    for x in range(3):
        for y in range(3):
            list_idx = x * 3 + y
            if list_idx < 4:
                populating_load_list(
                    (x * 3, y * 3),
                    f"Supporting Improvements {list_idx+1} subgoals",
                    loaded_data,
                    load_list,
                )
            elif list_idx == 4:
                populating_middle_of_load_list(
                    (x * 3, y * 3), "Supporting Improvements", loaded_data, load_list
                )
            else:
                populating_load_list(
                    (x * 3, y * 3),
                    f"Supporting Improvements {list_idx} subgoals",
                    loaded_data,
                    load_list,
                )


populate_load_list(loaded_data, load_list)


# Initialize the main application window
root = tk.Tk()
root.title("Planner GUI")
root.geometry("1000x600")

# Create a 9x9 grid of labels and populate from `load_list`
# make the grid responsive so labels resize with the window
labels = [[None for _ in range(9)] for _ in range(9)]
for i in range(9):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

supporting_impr = [
    (1, 1),
    (1, 4),
    (1, 7),
    (4, 1),
    (4, 7),
    (7, 1),
    (7, 4),
    (7, 7),
    (3, 3),
    (3, 4),
    (3, 5),
    (4, 3),
    (4, 5),
    (5, 3),
    (5, 4),
    (5, 5),
]

for i in range(9):
    for j in range(9):
        text = str(load_list[i][j])
        if (i, j) in supporting_impr:
            forground_clr = "black"
            background_clr = "gray"
            font = ("Arial", 10, "bold")
        elif (i, j) == (4, 4):
            forground_clr = "black"
            background_clr = "yellow"
            font = ("Arial", 10, "bold")
        else:
            forground_clr = "black"
            background_clr = "white"
            font = ("Arial", 10)
        lbl = tk.Label(
            root,
            text=text,
            font=font,
            fg=forground_clr,
            bg=background_clr,
            borderwidth=1,
            relief="solid",
            anchor="center",
            wraplength=100,
        )
        lbl.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
        labels[i][j] = lbl


# Add a refresh button to reload label texts from `load_list`
def refresh_labels():
    for i in range(9):
        for j in range(9):
            labels[i][j].config(text=str(load_list[i][j]))


refresh_btn = tk.Button(root, text="Refresh", command=refresh_labels)
refresh_btn.grid(row=9, column=0, columnspan=9, sticky="ew", pady=(5, 0))

# # Create a semi-transparent overlay using a borderless Toplevel so the arrow
# # appears translucent over the target cell (4,2).
# overlay = tk.Toplevel(root)
# overlay.overrideredirect(True)
# overlay.attributes("-topmost", True)
# # Adjust this alpha (0.0-1.0) to change translucency
# overlay.attributes("-alpha", 0.5)

# arrow_label = tk.Label(
#     overlay, text="\u2190", font=("Arial", 48), fg="black", bg=labels[4][2].cget("bg")
# )
# arrow_label.pack(expand=True, fill="both")


# def place_overlay(event=None):
#     # Ensure geometry info is up to date
#     root.update_idletasks()
#     # Calculate absolute position of the target cell
#     cell_x = root.winfo_rootx() + labels[4][2].winfo_x()
#     cell_y = root.winfo_rooty() + labels[4][2].winfo_y()
#     cell_w = labels[4][2].winfo_width()
#     cell_h = labels[4][2].winfo_height()
#     if cell_w > 0 and cell_h > 0:
#         overlay.geometry(f"{cell_w}x{cell_h}+{cell_x}+{cell_y}")


# # Initial placement and dynamic updates on resize/move
# place_overlay()
# root.bind("<Configure>", place_overlay)
# labels[4][2].bind("<Configure>", place_overlay)

# Start the application's persistent event loop
root.mainloop()

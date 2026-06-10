import json


def load_json(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def save_json(file_path: str, data: dict) -> None:
    with open(file_path, "w") as file:
        json.dump(data, file)

loaded_data = load_json("Data/shohei_ohtani_goal_matrix.json")
print(loaded_data)

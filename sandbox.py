import json


def load_json(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def save_json(file_path: str, data: dict) -> None:
    with open(file_path, "w") as file:
        json.dump(data, file)


data = {
    "Main Goal": "Get drafted 1st overall (8 teams)",
    "Supporting Improvements 1": "Body",
    "Supporting Improvements 2": "Control",
    "Supporting Improvements 3": "Sharpness",
    "Supporting Improvements 4": "Mental Toughness",
    "Supporting Improvements 5": "Speed 100mph",
    "Supporting Improvements 6": "Personality",
    "Supporting Improvements 7": "Karma",
    "Supporting Improvements 8": "Pitch Variance",
    "Supporting Improvements 1 subgoals": [
        "Body Care",
        "Take Supplements",
        "FSQ^2 90kg",
        "Flexibility",
        "RSQ^2 130kg",
        "Stamina",
        "Range of Motion",
        "Meals^3 PM: 7 bowls AM: 3 bowls",
    ],
}
save_json("data.json", data)
loaded_data = load_json("data.json")
print(loaded_data)

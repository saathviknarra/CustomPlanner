import json


def load_json(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def save_json(file_path: str, data: dict) -> None:
    with open(file_path, "w") as file:
        json.dump(data, file)


# data = {
#     "Main Goal": "Get drafted 1st overall (8 teams)",
#     "Supporting Improvements 1": "Body",
#     "Supporting Improvements 2": "Control",
#     "Supporting Improvements 3": "Sharpness",
#     "Supporting Improvements 4": "Mental Toughness",
#     "Supporting Improvements 5": "Speed 100mph",
#     "Supporting Improvements 6": "Personality",
#     "Supporting Improvements 7": "Karma",
#     "Supporting Improvements 8": "Pitch Variance",
#     "Supporting Improvements 1 subgoals": [
#         "Body Care",
#         "Take Supplements",
#         "FSQ^2 90kg",
#         "Flexibility",
#         "RSQ^2 130kg",
#         "Stamina",
#         "Range of Motion",
#         "Meals^3 PM: 7 bowls AM: 3 bowls",
#     ],
#     "Supporting Improvements 2 subgoals": [
#         "Improve instep",
#         "Core Strength",
#         "Maintain Body Axis",
#         "Consistent Release Point",
#         "Remove Insecurities",
#         "Lower Body Strength",
#         "Don't Open Up Body",
#         "Control Mental State",
#     ],
#     "Supporting Improvements 3 subgoals": [
#         "Create Angle of Delivery",
#         "\"Hit\" the Ball from Above",
#         "Wrist Strength",
#         "Don't Overpower",
#         "Lead with Lower Body",
#         "Release the Ball in Front",
#         "Increase Spin Rate",
#         "Range of Motion",
#     ],
#     "Supporting Improvements 4 subgoals": [
#         "Set Clear Goals",
#         "Don't Let Plays Affect Emotions",
#         "Calm Mind, Burning Heart",
#         "Thrive on Adversity",
#         "Don't get Caught Up in the Flow",
#         "Don't make Waves",
#         "Dedication to Winning",
#         "Be Considerate of Teammates",
#     ],
#     "Supporting Improvements 5 subgoals": [
#         "Turn Along Body Axis",
#         "Lower Body Strength",
#         "Increase Body Weight",
#         "Core Strength",
#         "Shoulder Strength",
#         "Range of Motion",
#         "Practice Catching Liners",
#         "Pitch More",
#     ],
#     "Supporting Improvements 6 subgoals": [
#         "Emotions",
#         "Likeability",
#         "Planning",
#         "Consideration",
#         "Thankfulness",
#         "Politeness",
#         "Reliability",
#         "Persistence",
#     ],
#     "Supporting Improvements 7 subgoals": [
#         "Greetings",
#         "Pick Up Trash",
#         "Keep Room Clean",
#         "Take Care of Equipment",
#         "Show Respect to Umpires",
#         "Be Positive",
#         "Be Someone People Want to Support",
#         "Read Books",
#     ],
#     "Supporting Improvements 8 subgoals": [
#         "Increase Ball Count",
#         "Perfect the Forkball",
#         "Sharpness of Slider",
#         "Slow, Dropping Curveball",
#         "Pitch for Finishing Batters",
#         "Use Fastball Form for All Pitches",
#         "Strike/Ball Control",
#         "\"Deep\" Image",
#     ],
# }
# save_json("Data/shohei_ohtani_goal_matrix.json", data)
loaded_data = load_json("Data/shohei_ohtani_goal_matrix.json")
print(loaded_data)

import os
import json

# Make sure the data folder exists
def check_data_folder():
    if not os.path.exists("data"):
        os.makedirs("data")

# Read a json file safely
def read_json_file(filename):
    check_data_folder()
    path = os.path.join("data", filename)
    if not os.path.exists(path):
        # Create an empty file with an empty list if it doesn't exist
        with open(path, "w") as f:
            json.dump([], f)
        return []
    
    with open(path, "r") as f:
        try:
            data = json.load(f)
            return data
        except:
            return []

# Save data back to the json file
def write_json_file(filename, data):
    check_data_folder()
    path = os.path.join("data", filename)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

# Simple helper to take a clean positive integer from the user
def ask_int(prompt):
    while True:
        val = input(prompt).strip()
        if val.isdigit():
            return int(val)
        print("Please enter a valid positive number.")

# Simple helper to take a float number
def ask_float(prompt):
    while True:
        val = input(prompt).strip()
        try:
            num = float(val)
            if num >= 0:
                return num
            print("Number must be positive.")
        except:
            print("Please enter a valid decimal number.")
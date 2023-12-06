import os
import json
from play import prompt

directory_path = "./dataset/1"
output_path = "./prompts/1"

files = os.listdir(directory_path)

def log(message):
    print(message)
    with open("error.txt", 'a') as file:
        file.write(message + "\n")

# Loop through the list of files and read each file
for filename in files:
    file_path = os.path.join(directory_path, filename)
    txt_filename = os.path.splitext(filename)[0] + ".txt"
    output_file_path = os.path.join(output_path, txt_filename)

    # Check if the path is a file (not a directory)
    if os.path.isfile(file_path):
        try:
            data = ""
            with open(file_path, "r") as file:
                file_content = json.load(file)
                data = prompt(file_content)

            if data == "":
                raise Exception(f"Prompt is empty")

            # Write prompt to file
            log("Writing to file: " + output_file_path)
            with open(output_file_path, 'w') as file:
                file.write(data)   
        except Exception as e:
            message = f"Error reading file {filename}: {str(e)}"
            log(message)

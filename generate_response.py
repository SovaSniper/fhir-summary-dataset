import g4f
import os
import json

directory_path = "./prompts/1"
output_path = "./responses/1"

files = os.listdir(directory_path)

def log(message):
    print(message)
    with open("error.txt", "a") as file:
        file.write(message + "\n")

for filename in files:
    file_path = os.path.join(directory_path, filename)
    output_file_path = os.path.join(output_path, filename)

    if os.path.exists(output_file_path):
        print(f"File {output_file_path} already exists")
        continue

    # Check if the path is a file (not a directory)
    if os.path.isfile(file_path):
        try:
            response = ""
            with open(file_path, "r") as file:
                file_content = file.read()
                tries = 0
                while tries < 20 and response == "":
                    tries += 1
                    try:
                        response = g4f.ChatCompletion.create(
                            model=g4f.models.gpt_4,
                            provider=g4f.Provider.Acytoo,
                            messages=[{"role": "user", "content": file_content}],
                        )
                        # print(response)
                        # print(response.count('\n'))
                        if response.count("\n") <= 20:
                            raise Exception("Response too less")
                    except Exception as e:
                        message = f"Error with CHATGPT for file {filename}: {str(e)}"
                        log(message)
                        response = ""

            if response == "":
                raise Exception(f"Response is empty")

            # Write prompt to file
            log("Writing to file: " + output_file_path)
            with open(output_file_path, "w") as file:
                file.write(response)
        except Exception as e:
            message = f"Error reading file {filename}: {str(e)}"
            log(message)

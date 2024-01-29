# file_io.py

def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w") as f:
        f.write(file_content)


def append_file(file_name, append_content):
    with open(f"{file_name}.txt", "a") as f:
        f.write(append_content)

import os

def read_file(file_name):
    if os.path.exists(f"{file_name}.txt"):
        with open(f"{file_name}.txt", 'r') as f:
            file_content = f.read()
        return file_content
    else:
        return None




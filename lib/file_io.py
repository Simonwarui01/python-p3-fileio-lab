def write_file(file_name, file_content):
    # Add .txt extension
    txt_file = file_name.with_suffix(".txt")
    with open(txt_file, "w") as f:
        f.write(file_content)

def append_file(file_name, append_content):
    # Add .txt extension
    txt_file = file_name.with_suffix(".txt")
    with open(txt_file, "a") as f:
        f.write(append_content)

def read_file(file_name):
    # Add .txt extension
    txt_file = file_name.with_suffix(".txt")
    with open(txt_file, "r") as f:
        return f.read()

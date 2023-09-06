import os

def get_files(dir_path):
    file_list  = []
    for path, dirs, files in os.walk(dir_path):
        for file in files:
            file_list.append(dir_path + "/" + file)
    return file_list 

def lines_to_array(file_path):
    file = open(file_path, 'r')

    out = []
    for line in file:
        stripped_line = line.strip()
        if len(stripped_line) > 0:
            out.append(stripped_line)
    return out



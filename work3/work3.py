import os
from pprint import pprint
import glob

files_dir = 'work3'
files = [os.path.join(files_dir, f) for f in os.listdir(files_dir) if f.endswith('.txt')]

files_lines = {}
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.readlines()
        files_lines[file] = len(content)

sorted_files = sorted(files_lines.items(), key=lambda x: x[1])

with open('./work3/result.txt', 'w', encoding='utf-8') as output_file:
    for file, lines in sorted_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            output_file.write(f"Содержимое файла {os.path.basename(file)} содержит {lines} строк: \n =======================================")
            output_file.write(f"\n{content}\n\n")
pprint(output_file)            
        


import os
import shutil

source_file = 'README.md'
current_dir = os.getcwd()

for root, dirs, files in os.walk(current_dir):
    for dir in dirs:
        dest_path = os.path.join(root, dir)
        if os.path.join(current_dir, source_file):
            shutil.copy(source_file, dest_path)

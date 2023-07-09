import os

source_file = 'README.md'
current_dir = os.getcwd()

for root, dirs, files in os.walk(current_dir):
    for file in files:
        if file == source_file:
            os.remove(os.path.join(root, file))

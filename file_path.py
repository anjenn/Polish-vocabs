import os

# Get the absolute file path
file_path_1 = os.path.abspath('filter.py')

# Replace backslashes with double backslashes
file_path_2 = file_path_1.replace('\\', '\\\\')

print(f'file path: {file_path_1}')
print(f'file path: {file_path_2}')
# print(file_path_2)
# Use the file path in the code
csv_file_path = file_path_1
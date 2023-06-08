# -*- coding: utf-8 -*-

## for duplicate words in the entry
import csv
import os

def check_duplicate_entries(csv_file):
    duplicates = []
    words_set = set()
    
    # with open(csv_file, 'r', newline='', encoding='utf-8') as file:
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present
        
        for row in reader:
            entry = row[0]
            
            # Split the entry string into words
            words = entry.split()
            
            # Check for duplicate words in the entry
            for word in words:
                if word in words_set:
                    duplicates.append(entry)
                    break  # Stop checking if duplicate word found
            
            # Add words to the set for future comparison
            words_set.update(words)
    
    return duplicates

# Get the absolute file path
file_path = os.path.abspath('filter.py')

# Replace backslashes with double backslashes
file_path = file_path.replace('\\', '\\\\')

# Use the file path in the code
csv_file_path = file_path

# Specify the path to the CSV file
csv_file_path = r'C:\Users\anjen\Documents\Github\Polish-vocabs\File_name.csv'

# Call the function to check for duplicate entries
duplicate_entries = check_duplicate_entries(csv_file_path)

# Print the duplicate entries
for entry in duplicate_entries:
    print(entry)



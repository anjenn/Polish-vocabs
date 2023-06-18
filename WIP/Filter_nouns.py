# function to store all entries get the same base word

# If the file is large and memory usage is a concern,
# you can write the merged entries to a new file and then replace the original file
# with the new file. This approach ensures that
# you're not keeping both the original and merged entries in memory at the same time.

import csv


def read_csv(): #1. Read the CSV file and store them in a list
    entries_list = []
    csv_file = r'C:\Users\anjen\Documents\Github\Polish-vocabs\WIP\Nouns_Test.csv'
    # csv_file = r'C:\Users\anjen\Documents\Github\Polish-vocabs\WIP\Nouns.csv'

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader: # administracja (f) - administration, optional (f)
            entry = row[0]  # (Word1, Classifier, Word2)
            word1 = entry.split('-')[0].strip()
            word2 = entry.split('-')[1].strip().split('(')[0].strip() # adding a comma makes it a tuple
            entries_list.append((word1, word2))
    return entries_list

def merge_by_base(): #2. Merge the entries with the same base word (Word1)
    entries_list = read_csv()
    counter = 0
    final_ent_dict = {}
    seen_entries = {} # dictionary to store the entries that have been seen

    for index, entry in enumerate(entries_list):
        key = entry[0]  # Assuming the first element of each tuple is the key
        rest = entry[1:] # word2
        word2 = "".join(rest).strip()

        if key in seen_entries:
            # Handle the duplicate key
            print(f"Duplicate key found: {key}")
            merged_entry = final_ent_dict[key] + ", " + word2 
            print(f"Rest - Existing: {final_ent_dict[key]}")
            final_ent_dict[key] = merged_entry
            counter += 1
            print(f"Rest - Current (new): {word2}")
            print(f"Merged entry: {final_ent_dict[key]}")
            print(f"Counter: {counter}")
            print(f"-----\n")
        else:
            seen_entries[key] = word2 # Store the key and rest of elements in the dictionary
            # Process the data and add it to the dictionary
            final_ent_dict[key] = seen_entries[key] # (classifier, word2)
    print(f"Total merged entries: {len(final_ent_dict)}")
    print(f"Counter: {counter}")
    return final_ent_dict

# function to replace the unecessary entries in the original file
def write_to_csv(filename):
    final_ent_dict = merge_by_base() # key: (classifier, word2)
    data = []
    for key in final_ent_dict:
        entry = [key] + list(final_ent_dict[key])
        data.append(entry)  

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Example usage
# data = [
#     ['Name', 'Age', 'City'],
#     ['John', '25', 'New York'],
#     ['Alice', '30', 'London'],
#     ['Bob', '35', 'Paris']
# ]

# write_to_csv(data, 'output.csv')

merge_by_base()
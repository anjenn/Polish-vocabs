## Polish words were generated based on english word => polish may have duplicates
# String structure: Abandoned - Opuszczony # word1 - word2
# For any multiple entries sharing the same base words word1, merged them and write them to a new file

import csv

def read_csv(): #1. Read the CSV file and store them in a list
    entries_list = []
    csv_file = r'C:\Users\anjen\Documents\Github\Polish-vocabs\Simpler\Adjectives.csv'

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader: # Abandoned - Opuszczony
            entry = row[0].lower()
            word1 = entry.split('-')[0].strip()
            word2 = entry.split('-')[1].strip()
            entries_list.append((word1, word2))
    return entries_list

def merge_by_base(): #2. Merge the entries with the same base word (Word1)
    entries_list = read_csv()
    counter = 0
    final_ent_dict = {}
    seen_entries = {} # dictionary to store the entries that have been seen

    for entry in entries_list:
        # make the second word a key, as the second word can appear multiple times
        key = entry[1]  # assuming the second element is a key
        value = entry[0] # word1

        if key in seen_entries:
            # Handle the duplicate key
            print(f"Duplicate key found: {key}")
            if (final_ent_dict[key] != value):
                merged_entry = final_ent_dict[key] + ", " + value 
                final_ent_dict[key] = merged_entry
                counter += 1
                print(f"Merged entry: {final_ent_dict[key]}")
            else:
                print(f"Duplicate entry found: {final_ent_dict[key]}")
                print(f"Duplicate entry: {value}, {final_ent_dict[key]}")
            print(f"-----")
        else:
            seen_entries[key] = value
            final_ent_dict[key] = seen_entries[key]

    print(f"Total number of entries before merge: {len(entries_list)}")
    print(f"Total number of entries without duplicates: {len(seen_entries)}")
    print(f"Total number of final entries: {len(final_ent_dict)}")
    print(f"Duplicates: {counter}")
    return final_ent_dict

# function to replace the unecessary entries in the original file
def write_to_file(filename):
    init_data = merge_by_base() # format: translation - init_data[key]

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        for key in init_data:
            final_entry = f'{key} - {init_data[key]}\n'
            file.write(final_entry)

write_to_file('Filtered_adjectives.txt')

# merge_by_base()
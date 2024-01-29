# String structure: i - and # word1 - word2
## Polish words were generated based on english word => polish may have duplicates
## In thie particular file, there were multiple (and duplicative words) for the translation part
## Which required a set to be used to remove duplicates
# For any multiple entries sharing the same base words word1, merged them and write them to a new file

import csv

def read_csv(): #1. Read the CSV file and store them in a list
    entries_list = []
    csv_file = r'C:\Users\anjen\Documents\Github\Polish-vocabs\Phrasal_verbs\phVerbs.csv'

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader: # "natomiast - however, whereas"
            entry = row[0].replace('"', '').lower()
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
        key = entry[0]
        value_list = [word.strip() for word in entry[1].split(',')]
    
        if key in seen_entries:
            # Handle the duplicate key
            print(f"Duplicate key found: {key}")
            if(type(final_ent_dict[key]) == str): # this is required because when we store merged list into the final dictionary, we make it a string
                old_value_list = final_ent_dict[key].split(', ')
            elif(type(final_ent_dict[key]) == list):
                old_value_list = final_ent_dict[key]
            merged_value_set = set(old_value_list + value_list)
            merged_list = list(merged_value_set) # important to convert into list first instead of directly coverting to string to ensure that the order is preserved
            merged_string = ', '.join(merged_list)
            final_ent_dict[key] = merged_string
            counter += 1
            print(f"Merged entry: {final_ent_dict[key]}")
            print(f"-----")
        else:
            seen_entries[key] = value_list
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
            if(type(init_data[key]) == list):
                init_data[key] = ', '.join(init_data[key])
            final_entry = f'{key} - {init_data[key]}\n'
            file.write(final_entry)

write_to_file('Filtered_phVerbs.txt')

merge_by_base()
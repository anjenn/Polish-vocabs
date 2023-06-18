# String structure: Noun (classifier) - Translation (classifier)
# For a string '# administracja (f) - administration, optional (f)', extracts base word (administracja (f))
# and the next word (administration, optional (f)) for checking for duplicates
# For any multiple entries sharing the same base words, merged them and write them to a new file

import csv


def read_csv(): #1. Read the CSV file and store them in a list
    entries_list = []
    csv_file = r'C:\Users\anjen\Documents\Github\Polish-vocabs\Nouns\Nouns.csv'
    # csv_file = r'C:\Users\anjen\Documents\Github\Polish-vocabs\WIP\Nouns.csv'

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader: # administracja (f) - administration, optional (f)
            entry = row[0]
            word1 = entry.split('-')[0].strip()
            word2 = entry.split('-')[1].strip().split('(')[0].strip()
            entries_list.append((word1, word2))
    return entries_list

def merge_by_base(): #2. Merge the entries with the same base word (Word1)
    entries_list = read_csv()
    counter = 0
    final_ent_dict = {}
    seen_entries = {} # dictionary to store the entries that have been seen

    for entry in entries_list:
        key = entry[0]  # Assuming the first element of each tuple is the key
        rest = entry[1:] # word2
        word2 = "".join(rest).strip()

        if key in seen_entries:
            # Handle the duplicate key
            print(f"Duplicate key found: {key}")
            if (final_ent_dict[key] != word2):
                merged_entry = final_ent_dict[key] + ", " + word2 
                final_ent_dict[key] = merged_entry
                counter += 1
                print(f"Merged entry: {final_ent_dict[key]}")
            else:
                print(f"Duplicate entry found: {final_ent_dict[key]}")
                print(f"Duplicate entry: {word2}, {final_ent_dict[key]}")
            print(f"-----")
        else:
            seen_entries[key] = word2 # Store the key and rest of elements in the dictionary
            # Process the data and add it to the dictionary
            final_ent_dict[key] = seen_entries[key] # (classifier, word2)

    print(f"Total number of entries before merge: {len(entries_list)}")
    print(f"Total number of entries without duplicates: {len(seen_entries)}")
    print(f"Total number of final entries: {len(final_ent_dict)}")
    print(f"Duplicates: {counter}")
    return final_ent_dict

# function to replace the unecessary entries in the original file
def write_to_file(filename):
    init_data = merge_by_base() # init_data[key]: (classifier, word2)
    # final_data = []

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        # writer = csv.writer(file, dialect='excel')
        # writer.writerows(final_data)

        for key in init_data:
            classifier = key.split(' ')[1].strip()
            final_entry = f'{key} - {init_data[key]} {classifier}\n'
            file.write(final_entry)

            ## final_entry string contains unexpected characters being written to the file => makes csv file generation harder
            # final_entry = key + " - " + init_data[key] + " " + classifier
            # formatted_key = key.replace(',', '').replace('"', "'")
            # formatted_value = init_data[key].replace(',', '').replace('"', "'")
            # formatted_classifier = classifier.replace(',', '').replace('"', "'")
            # final_entry = f'{formatted_key} - {formatted_value} {formatted_classifier}'
            # print(final_entry)
            # final_data.append(final_entry)

write_to_file('Filtered_nouns.txt')

# merge_by_base()
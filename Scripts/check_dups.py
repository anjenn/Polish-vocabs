# function to store all entries get the same base word

# If the file is large and memory usage is a concern,
# you can write the merged entries to a new file and then replace the original file
# with the new file. This approach ensures that
# you're not keeping both the original and merged entries in memory at the same time.

import csv


def read_csv(): #1. Read the CSV file and store them in a list
    entries_list = []
    csv_file = r'C:\Users\anjen\Documents\Github\Polish-vocabs\Verbs\Verbs.csv'

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader: # "akceptować - akceptuję (imp.), to accept (imp.)"
            entry = row[0].replace('"', '')  # akceptować - akceptuję (imp.), to accept (imp.)
            word1 = entry.split(',')[0].strip()
            word2 = entry.split(',')[1].strip()
            entries_list.append((word1, word2))
    
    return entries_list

def merge_by_base(): #2. Merge the entries with the same base word (Word1)
    entries_list = read_csv()
    counter = 0
    final_ent_dict = {}
    seen_entries = {} # dictionary to store the entries that have been seen

    for index, entry in enumerate(entries_list):
        key = entry[0]  # Assuming the first element of each tuple is the key
        word2 = entry[1]

        if key in seen_entries:
            # Handle the duplicate key
            print(f"Duplicate key found: {key}")
            # merged_entry = final_ent_dict[key] + ", " + word2 
            # final_ent_dict[key] = merged_entry
            counter += 1
            # print(f"Merged entry: {final_ent_dict[key]}")
            # print(f"-----")
        else:
            seen_entries[key] = word2 # Store the key and rest of elements in the dictionary
            # Process the data and add it to the dictionary
            # final_ent_dict[key] = seen_entries[key] # (classifier, word2)

    print(f"Total number of entries before merge: {len(entries_list)}")
    print(f"Total number of entries without duplicates: {len(seen_entries)}")
    # print(f"Total number of final entries: {len(final_ent_dict)}")
    # print(f"Duplicates: {counter}")
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

# write_to_file('output1.txt')

merge_by_base()
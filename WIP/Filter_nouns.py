# function to store all entries get the same base word

# 3. Counter function to count the number of merged entries. Using dictionary, this can be done by counting the number of keys in the dictionary.
# 4. Replace the unecessary entries in the original file
## Iterate over the original file, and check whether each entry is present in the merged entries dictionary
## Writing to the original file => This approach avoids creating a new file and allows you to update the original file in place.

# If the file is large and memory usage is a concern,
# you can write the merged entries to a new file and then replace the original file
# with the new file. This approach ensures that
# you're not keeping both the original and merged entries in memory at the same time.

import csv

entries_list = []
counter = 0
def read_csv(csv_file): #1
    # 1. Read the CSV file and store them in a list
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader: # administracja (f) - administration, optional (f)
            entry = row[0]  # (Word1, Classifier, Word2)
            word1 = entry.split('(')[0].strip()
            word2 = entry.split('-')[1].strip().split('(')[0].strip(), # adding a comma makes it a tuple
            classifier = entry.split(' ')[1]

            entries_list.append((word1, classifier, word2))

# function to merge entries with the same base word
def merge_overlaps(occurrences, entries_set): #2
# 2. Merge the entries with the same base word (Word1)
## Create a function that takes the list of entries and performs the merging operation
## Iterate through the list of entries and use the base word as the key to a dictionary (dictionary cannot have duplicate keys)
## For each group of base words (duplicative), combine the word2's, and eventually create merged entries.

    ##sth like:
    # def merge_entries(entries):
    # merged_entries = {}
    # for entry in entries:
    #     attribute_a, attribute_b, attribute_c = entry
    #     if attribute_a in merged_entries:
    #         merged_entries[attribute_a] = (merged_entries[attribute_a][0] + attribute_b,
    #                                         merged_entries[attribute_a][1] + attribute_c)
    #     else:
    #         merged_entries[attribute_a] = (attribute_b, attribute_c)
    # return merged_entries


    merged_entries = [] # list requires declaration

    for triplet in occurrences: # involves unecessary iterations making the code inefficient. Use dictionary instead
        base = triplet[0]
        word2 = triplet[2]
        for triplet in occurrences:
            if (triplet[0] == base and triplet[2] not in (word2,)):
                updated_triplet = (triplet[0], triplet[1], triplet[2] + (word2,))
                merged_entry = f"{triplet[0]} - {triplet[2]} {triplet[1]}"
                merged_entries.append(merged_entry)
                break
    return merged_entries

# function to replace the unecessary entries in the original file
def replace_entries(entries_set, merged_entries):
    for entry in entries_set:
        to_be_checked = entry.split('-')[0].strip()
        word2 = entry.split('-')[1].strip().split('(')[0].strip() # entry.split('-')[1].strip() => 'administration, optional (f)'

        for merged_entry in merged_entries:
            if (to_be_checked == merged_entry.split('-')[0].strip() and word2 not in merged_entry.split('-')[1].strip()):
                print(f"Replacing {entry} with {merged_entry}") # DEBUGGING - 2nd condition to be fixed
                entries_set.remove(entry)
                if (merged_entry not in entries_set):
                    entries_set.add(merged_entry)
                break

    return entries_set # OR write to the CSV file, but first, check the results without modifying the original file
        # replace old_entry with new_entry in csv_file



csv_file = r'C:\Users\anjen\Documents\Github\Polish-vocabs\WIP\Nouns.csv'
occurrences, merged_entries = merge_duplicates(csv_file)

print("Merged Entries:")
for entry in merged_entries:
    print(entry)

print(f"Total merged entries: {len(merged_entries)}")
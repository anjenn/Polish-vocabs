import csv

# function to store all entries get the same base word
def init_process(csv_file):
    occurrences = {} # dictionary requires declaration
    entries_set = set()
    counter = 0

    # 1. Read the CSV file and store them in a list
    ## Create a fnction that reads the CSV file and extracts the entries, storing them in a list. Each entry should be represented as a tuple. (Word1, Classifier, Word2)
    # 2. Merge the entries with the same base word (Word1)
    ## Create a function that takes the list of entries and performs the merging operation
    ## Iterate through the list of entries and use the base word as the key to a dictionary (dictionary cannot have duplicate keys)
    ## For each group of base words (duplicative), combine the word2's, and eventually create merged entries.

sth like:
def merge_entries(entries):
    merged_entries = {}
    for entry in entries:
        attribute_a, attribute_b, attribute_c = entry
        if attribute_a in merged_entries:
            merged_entries[attribute_a] = (merged_entries[attribute_a][0] + attribute_b,
                                           merged_entries[attribute_a][1] + attribute_c)
        else:
            merged_entries[attribute_a] = (attribute_b, attribute_c)
    return merged_entries


    # 3. Counter function to count the number of merged entries. Using dictionary, this can be done by counting the number of keys in the dictionary.
    # 4. Replace the unecessary entries in the original file
    ## Iterate over the original file, and check whether each entry is present in the merged entries dictionary
    ## Writing to the original file => This approach avoids creating a new file and allows you to update the original file in place.

    # If the file is large and memory usage is a concern,
    # you can write the merged entries to a new file and then replace the original file
    # with the new file. This approach ensures that
    # you're not keeping both the original and merged entries in memory at the same time.

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            entry = row[0] # administracja (f) - administration, optional (f)
            word1 = entry.split('(')[0].strip()
            word2 = entry.split('-')[1].strip().split('(')[0].strip() # entry.split('-')[1].strip() => 'administration, optional (f)'
            classifier = entry.split(' ')[1]

            to_be_checked = f"{word1} {classifier}"

            if to_be_checked in entries_set:
                # for triplet in occurrences:
                    # if (triplet[0] !== to_be_checked):
                    #     occurrences.add((to_be_checked, classifier, (word2,)))
                    #     print(f"Base word '{triplet[0]}' has multiple occurrences.")
                    ## the above code was to add all 'duplicative' entries to the occurrences set
                    ## but it is not required as the entries_set already contains all the duplicative entries
                    ## the below code instead checks if the base word has multiple occurrences, and replaces the old entry with the new entry right away
                for key in occurrences
                    counter += 1
                    if (key == to_be_checked and word2 != occurrences[key][1][0]):
                        print(f"Base word '{to_be_checked}' has multiple occurrences.")
                        # but there can be a case wherer the new word2 is either a superset or a subset of the old word2
                        occurrences[key] = [classifier, (word2,)]
                    else if (key == to_be_checked and word2 == occurrences[key][1][0]):
                        print(f"Base word '{to_be_checked}' has duplicative occurrences.")
                        break
                        # I need to add an entry to the occurrences set only if the new word2 is not a superset or a subset of the old word2
                        # But it has to have a collection of multiple duplicative entries at the first place in order to be able to filter them
            else:
                entries_set.add(to_be_checked)
        print(f"Counter: {counter}")
    return occurrences, entries_set

# function to merge entries with the same base word
def merge_overlaps(occurrences, entries_set):
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
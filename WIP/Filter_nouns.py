import csv

# function to store all entries get the same base word
def init_process(csv_file):
    occurrences = set() # Change this to a dictionary, using 'base_word' as the key, triplet as the value
    entries_set = set()
    counter = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            entry = row[0] # administracja (f) - administration, optional (f)
            word1 = entry.split('(')[0].strip()
            word2 = entry.split('-')[1].strip().split('(')[0].strip() # entry.split('-')[1].strip() => 'administration, optional (f)'
            classifier = entry.split(' ')[1]

            to_be_checked = f"{word1} {classifier}"

            if to_be_checked in entries_set:
                for triplet in occurrences:
                    counter += 1
                    if (triplet[0] !== to_be_checked):
                        occurrences.add((to_be_checked, classifier, (word2,)))
                        print(f"Base word '{triplet[0]}' has multiple occurrences.")
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
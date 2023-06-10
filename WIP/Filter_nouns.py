import csv

# function to store all entries get the same base word
def init_process(csv_file):
    occurrences = set() # set requires declaration
    entries_set = set()

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            entry = row[0] # administracja (f) - administration, optional (f)
            word1 = entry.split('(')[0].strip()
            # .split('(') is used to split the 'entry' string into a list of substrings based on the occurences of '(')
            # [0] is used to select the first element of the list
            # In this case entry.split('(')[0] will return the substring before the first '('
            # .strip() is used to remove any leading or trailing whitespaces

            word2 = entry.split('-')[1].strip().split('(')[0].strip() # entry.split('-')[1].strip() => 'administration, optional (f)'
            # entry.split('-')[1].strip().split('(')[0].strip() => 'administration, optional'
            classifier1 = entry.split(' ')[1]

            to_be_checked = f"{word1} {classifier1}"

            if to_be_checked in entries_set:
                for triplet in occurrences:
                    if (triplet[0] !== to_be_checked):
                        occurrences.add((to_be_checked, classifier1, (word2,)))
                        print(f"Base word '{triplet[0]}' has multiple occurrences.")
                    else:
                        # add occurences
            else:
                entries_set.add(to_be_checked)

    return occurrences, entries_set


# function to merge entries with the same base word
def merge_overlaps():
    merged_entries = [] # list requires declaration
    occurrences, entries_set = init_process(csv_file)
    counter = 0

    for triplet in occurrences:
        base = triplet[0]
        word2 = triplet[2]
        for triplet in occurrences:
            if (triplet[0] == base and triplet[2] not in (word2,)):
                counter += 1
                updated_triplet = (triplet[0], triplet[1], triplet[2] + (word2,))
                merged_entry = f"{triplet[0]} - {triplet[2]} {triplet[1]}"
                merged_entries.append(merged_entry)
                break

    return merged_entries


    counter = 0
    for triplet in occurrences:
        counter += 1
        print(f"Base word '{triplet[0]}' has multiple occurrences.")

    print(f"Counter: {counter}")


# function to replace the unecessary entries in the original file
def merge_overlaps():


csv_file = r'C:\Users\anjen\Documents\Github\Polish-vocabs\WIP\Nouns.csv'
occurrences, merged_entries = merge_duplicates(csv_file)

print("Merged Entries:")
for entry in merged_entries:
    print(entry)

print(f"Total merged entries: {len(merged_entries)}")
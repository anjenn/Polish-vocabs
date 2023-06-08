import csv

def merge_duplicates(csv_file):
    occurrences = set() # set requires declaration
    entries_set = set()
    merged_entries = [] # list requires declaration

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

            overlapping_part = f"{word1} {classifier1}"

            # function to merge entries
            # function to remove old entries
            # function to add merged entries

            def check_overlapping_part():
                if overlapping_part in entries_set:
                    for triplet in occurrences:
                        if (triplet[0] == overlapping_part and triplet[2] not in (word2,)):
                            updated_triplet = (triplet[0], triplet[1], triplet[2] + (word2,))
                            # (word2,) syntax indicates that the element is a tuple
                            occurrences.remove(triplet)
                            occurrences.add(updated_triplet)
                            break
                    else:
                        occurrences.add((overlapping_part, classifier1, (word2,)))
                else:
                    entries_set.add(overlapping_part)

            check_overlapping_part()

    for triplet in occurrences:
        merged_entry = f"{triplet[0]} - {triplet[2]} {triplet[1]}"
        merged_entries.append(merged_entry)

    counter = 0
    for triplet in occurrences:
        counter += 1
        print(f"Base word '{triplet[0]}' has multiple occurrences.")

    print(f"Counter: {counter}")
    return occurrences, merged_entries


csv_file = r'C:\Users\anjen\Documents\Github\Polish-vocabs\WIP\Nouns.csv'
occurrences, merged_entries = merge_duplicates(csv_file)

print("Merged Entries:")
for entry in merged_entries:
    print(entry)

print(f"Total merged entries: {len(merged_entries)}")
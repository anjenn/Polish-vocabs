import csv

def merge_duplicates(csv_file):
    occurrences = {}
    entries_set = set()
    merged_entries = []

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            entry = row[0]
            word1 = entry.split('(')[0].strip()
            # .split('(') is used to split the 'entry' string into a list of substrings based on the occurences of '(')
            # [0] is used to select the first element of the list
            # In this case entry.split('(')[0] will return the substring before the first '('
            # .strip() is used to remove any leading or trailing whitespaces

            word2 = entry.split('-')[1].strip().split('(')[0].strip() #extracts the substring after the first '-' and then the substring before the first '('
            classifier1 = entry.split('(')[1].strip().split(')')[0].strip() #extracts the substring after the first '(' and then the substring before the first ')'
            classifier2 = entry.split('(')[2].strip().split(')')[0].strip()

            overlapping_part = f"{word1} {classifier1}"

            if overlapping_part in entries_set:
                if overlapping_part in occurrences:
                    occurrences[overlapping_part].append(word2)
                else:
                    occurrences[overlapping_part] = [word2]
            else:
                entries_set.add(overlapping_part)

    for base_word, words in occurrences.items():
        merged_word2 = ', '.join(words)
        merged_entry = f"{base_word} - {merged_word2} {classifier2}"
        merged_entries.append(merged_entry)

    for entry, words in occurrences.items():
        print(f"Base word '{entry}' has {len(words)+1} occurrences.")

    return occurrences, merged_entries

csv_file = r'C:\Users\anjen\Documents\Github\Polish-vocabs-processing\Tester\Nouns.csv'
occurrences, merged_entries = merge_duplicates(csv_file)

print("Merged Entries:")
for entry in merged_entries:
    print(entry)

print(f"Total merged entries: {len(merged_entries)}")
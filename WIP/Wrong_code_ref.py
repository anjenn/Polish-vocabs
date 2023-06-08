import csv

def merge_duplicates(csv_file):
    occurrences = set()
    entries_set = set()
    merged_entries = []

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            entry = row[0]
            word1 = entry.split('(')[0].strip()
            word2 = entry.split('-')[1].strip().split('(')[0].strip()
            classifier1 = entry.split(' ')[1]
            overlapping_part = f"{word1} {classifier1}"

            if overlapping_part in entries_set:
                for triplet in occurrences:
                    if triplet[0] == overlapping_part and word2 not in triplet[2]:
                        triplet[2].append(word2)
                        break
                else:
                    occurrences.add([overlapping_part, classifier1, [word2]])
            else:
                entries_set.add(overlapping_part)

    for triplet in occurrences:
        merged_entry = f"{triplet[0]} - {', '.join(triplet[2])} {triplet[1]}"
        merged_entries.append(merged_entry)

    return occurrences, merged_entries

csv_file = r'C:\Users\anjen\Documents\Github\Polish-vocabs\WIP\Nouns.csv'
occurrences, merged_entries = merge_duplicates(csv_file)

print("Merged Entries:")
for entry in merged_entries:
    print(entry)

print(f"Total merged entries: {len(merged_entries)}")
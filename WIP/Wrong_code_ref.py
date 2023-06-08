#csv_file = r'C:\Users\anjen\Documents\Github\Polish-vocabs-processing\Nouns.csv'
import csv

def merge_duplicates(csv_file):
    occurrences = {}
    entries_set = set()
    merged_entries = []

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            entry = row[0]
            word1 = entry.split('(')[0].strip().split('-')[0].strip()
            word2 = entry.split('-')[1].strip().split('(')[0].strip()
            classifier1 = entry.split('(')[1].strip().split(')')[0].strip()
            classifier2 = entry.split('(')[2].strip().split(')')[0].strip()

            overlapping_part = f"{word1} {classifier1}"

            if overlapping_part in entries_set:
                if overlapping_part in occurrences:
                    occurrences[overlapping_part].append(word2)
                else:
                    occurrences[overlapping_part] = [word2]
            else:
                entries_set.add(overlapping_part)

    print("Detected entries with multiple occurrences:")
    for entry, words in occurrences.items():
        print(f"{entry} - {', '.join(words)}")

    print("\nMerged Entries:")
    for base_word, words in occurrences.items():
        merged_word2 = ', '.join(words)
        merged_entry = f"{base_word} - {merged_word2} {classifier2}"
        merged_entries.append(merged_entry)

    print('\n'.join(merged_entries))
    print(f"\nTotal merged entries: {len(merged_entries)}")

    return occurrences, merged_entries

csv_file = r'C:\Users\anjen\Documents\Github\Polish-vocabs-processing\Tester\Nouns.csv'
occurrences, merged_entries = merge_duplicates(csv_file)
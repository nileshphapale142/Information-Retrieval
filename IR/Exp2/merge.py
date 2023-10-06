import csv
import os

# Function to read a CSV file and create a dictionary
def create_dict_from_csv(filename):
    data_dict = {}
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            termid, docid = int(row[0]), int(row[1])
            if termid not in data_dict:
                data_dict[termid] = [docid]
            else:
                data_dict[termid].append(docid)
    return data_dict

# Function to merge two dictionaries into one
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for termid, docids in dict2.items():
        if termid in merged_dict:
            merged_dict[termid].extend(docids)
        else:
            merged_dict[termid] = docids
    return merged_dict

# Read and create dictionaries from all CSV files
data_dicts = []
for i in range(10):
    data_dicts.append(create_dict_from_csv(f'data_{i + 1}.csv'))

# Merge all dictionaries into a single inverted index
inverted_index = {}
for data_dict in data_dicts:
    inverted_index = merge_dicts(inverted_index, data_dict)

# Sort the docid lists in the inverted index
for termid, docids in inverted_index.items():
    inverted_index[termid] = sorted(docids)

# Print the inverted index
# for termid, docids in inverted_index.items():
    # print(f"{termid}: {docids}")

# Optionally, save the inverted index to a CSV file
inverted_index = dict(sorted(inverted_index.items(), key=lambda x:x[0]))
with open('inverted_index.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['termid', 'docids'])
    for termid, docids in inverted_index.items():
        writer.writerow([termid, ' '.join(map(str, docids))])

print("Inverted index created successfully.")


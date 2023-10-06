import os

# Read the Cranfield collection file
with open('cran/cran_all.txt', 'r') as collection_file:
    documents = collection_file.read().split('.I ')

# Create a directory to store the text files
# if not os.path.exists('cran'):
os.mkdir('cranfield_collection')

# Iterate through the documents and save them as separate text files
for i, document in enumerate(documents[1:], start=1):  # Skip the first empty entry
    with open(f'cranfield_collection/document_{i}.txt', 'w') as output_file:
        output_file.write(document)

print(f'{len(documents) - 1} documents extracted and saved as text files.')

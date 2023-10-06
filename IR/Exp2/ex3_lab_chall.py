import csv
import random

# Function to generate a random pair of termid and docid
def generate_random_pair():
    termid = random.randint(1, 5000)
    docid = random.randint(1, 10000)
    return termid, docid

# Function to create a CSV file with random data
def create_csv_file(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow(['termid', 'docid'])

        # Generate and write 500 random pairs
        for _ in range(500):
            termid, docid = generate_random_pair()
            writer.writerow([termid, docid])

# Function to sort a CSV file based on termid
def sort_csv_file(filename):
    with open(filename, mode='r') as file:
        data = list(csv.reader(file))
    
    # Sort the rows based on termid
    sorted_data = sorted(data[1:], key=lambda x: int(x[0]))
    
    # Rewrite the sorted data to the file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['termid', 'docid'])
        writer.writerows(sorted_data)

# Create 10 CSV files
for file_number in range(1, 11):
    filename = f'data_{file_number}.csv'
    create_csv_file(filename)

print("CSV files created successfully.")

# Sort all CSV files
for file_number in range(1, 11):
    filename = f'data_{file_number}.csv'
    sort_csv_file(filename)

print("CSV files sorted successfully.")



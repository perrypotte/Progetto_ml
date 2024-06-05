import os
import csv

def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for _ in file)

def process_text_files(directory):
    csv_rows = []

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            line_count = count_lines_in_file(file_path)
            new_filename = os.path.splitext(filename)[0] + '.jpg'
            csv_rows.append([new_filename, line_count])

    return csv_rows

def write_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Path', 'Label'])
        csvwriter.writerows(data)

# Directory contenente i file di testo
directory = 'purogetto/euro_dataset/valid/labels'
# Path del file CSV di output
csv_output_path = 'purogetto/valid.csv'

# Processa i file di testo e crea i dati per il CSV
csv_data = process_text_files(directory)
# Scrivi i dati nel file CSV
write_csv(csv_output_path, csv_data)

print(f"CSV file has been created at {csv_output_path}")

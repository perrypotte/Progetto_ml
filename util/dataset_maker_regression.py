import os
import csv
from dotenv import load_dotenv

load_dotenv(override=True)

#*******QUESTO SCRIPT SERVE A RICAVARE DEI CSV A PARTIRE DAL DATASET IN FORMATO YOLO**********
#*******IN PARTICOLARE CONTA IL NUMERO DI BOUNDING BOX NELLE IMMAGINI PER RICAVARE  **********
#*******IL NUMERO DI MONETE DA UTILIZZARE COME G.T. NEL CASO DELLA REGRESSIONE.     **********


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
directory = [os.getenv("PATH_VALID_LABELS"),os.getenv("PATH_TRAIN_LABELS"),os.getenv("PATH_TEST_LABELS")]
# Path del file CSV di output
csv_output_path = [os.getenv("PATH_VALID_CSV"),os.getenv("PATH_TRAIN_CSV"),os.getenv("PATH_TEST_CSV")]

# Processa i file di testo e crea i dati per il CSV
for i in range(0,3):
    csv_data = process_text_files(directory[i])
    # Scrivi i dati nel file CSV
    write_csv(csv_output_path[i], csv_data)

print(f"CSV creati in percorsi del tipo: "+os.getenv("PATH_TRAIN_CSV"))

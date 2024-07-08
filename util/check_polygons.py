import os
from dotenv import load_dotenv

load_dotenv(override=True)
#*******QUESTO SCRIPT SERVE A FARE UN CHECK AI BOUNDING BOX, SE QUALCUNO HA DIMENTICATO**********
#*******DEI POLIGONI DURANTE L'ETICHETTAMENTO QUESTO LI RILEVA E LI ELENCA.            **********

def contains_segmentation_mask(annotation_file):
    with open(annotation_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            # Se ci sono più di 5 valori nella riga allora non si tratta di bounding box ma di un poligono
            if len(parts) > 5:
                return True
    return False

def check_for_segmentation_masks(path):
    if not os.path.exists(path):
        print(f"Path inesistente: {path}")
        return

    # Elenca tutti i file della directory
    all_files = os.listdir(path)

    # Filtra solo i file .txt
    annotation_files = [f for f in all_files if f.lower().endswith('.txt')]

    print("Contenenti poligoni:")

    # Cerca maschere di segmentazione (Poligoni)
    for annotation_file in annotation_files:
        full_path = os.path.join(path, annotation_file)
        if contains_segmentation_mask(full_path):
            print(annotation_file)

paths = [os.getenv("PATH_TRAIN_LABELS"),os.getenv("PATH_VALID_LABELS"),os.getenv("PATH_TEST_LABELS")]
# Run
for i in range(0,3):
    print(paths[i])
    check_for_segmentation_masks(paths[i])
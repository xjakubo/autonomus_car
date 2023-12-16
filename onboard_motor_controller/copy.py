import os
import shutil
from datetime import datetime

def get_latest_file_date(directory):
    # Pobierz listę plików w katalogu
    files = os.listdir(directory)

    # Utwórz pełną ścieżkę dla każdego pliku
    full_paths = [os.path.join(directory, file) for file in files]

    # Pobierz daty modyfikacji dla wszystkich plików
    modification_dates = [os.path.getmtime(file) for file in full_paths]

    # Znajdź indeks najnowszego pliku
    latest_index = modification_dates.index(max(modification_dates))

    # Pobierz datę modyfikacji najnowszego pliku
    latest_date = datetime.fromtimestamp(modification_dates[latest_index])

    return latest_date

def copy_newer_files(source_dir, dest_dir):
    # Pobierz datę najnowszego pliku z dest_directory
    cutoff_date = get_latest_file_date(dest_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            dest_path = os.path.join(dest_dir, file)

            # Sprawdź czy kopiowany plik to nie skrypt copy.py
            if file != 'copy.py':
                # Sprawdź datę modyfikacji pliku
                modified_time = os.path.getmtime(source_path)
                modified_datetime = datetime.fromtimestamp(modified_time)

                # Kopiuj plik, jeśli został zmodyfikowany po dacie najnowszego pliku w dest_directory
                if modified_datetime > cutoff_date:
                    #shutil.copy2(source_path, dest_path)
                    print(f"Skopiowano: {source_path} -> {dest_path}")

if __name__ == "__main__":
    source_directory = "."
    dest_directory = "/pyboard"

    copy_newer_files(source_directory, dest_directory)


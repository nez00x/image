import os

def rename_weapon_files(directory):
    # Parcourt tous les fichiers dans le répertoire
    for filename in os.listdir(directory):
        # Vérifie si le fichier commence par "weapon" (insensible à la casse)
        if filename.lower().startswith("weapon"):
            # Nouveau nom en majuscules
            new_name = filename.upper()
            
            # Chemins complets pour renommage
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)

            # Renommage du fichier
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")

# Spécifiez le répertoire contenant les fichiers
directory_path = input("Enter the directory path: ").strip()

# Vérifie si le répertoire existe
if os.path.isdir(directory_path):
    rename_weapon_files(directory_path)
else:
    print(f"Invalid directory: {directory_path}")

import os
import shutil

source_folder = "D:/Test_Folder"

folders = {
    "Images": ["jpg", "jpeg", "png", "gif"],
    "Documents": ["pdf", "docx", "txt"],
    "Archives": ["zip", "rar", "tar"],
}

for folder_name in folders:
    folder_path = os.path.join(source_folder, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for file_name in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file_name)

    if os.path.isdir(file_path):
        continue

    extension = file_name.split(".")[-1].lower()
    moved = False

    for folder_name, extensions in folders.items():
        if extension in extensions:
            destination = os.path.join(source_folder, folder_name, file_name)
            shutil.move(file_path, destination)
            moved = True
            break

    if not moved:
        other_folder = os.path.join(source_folder, "Others")
        if not os.path.exists(other_folder):
            os.makedirs(other_folder)

        destination = os.path.join(other_folder, file_name)
        shutil.move(file_path, destination)

print("Test_Folder organized successfully!")





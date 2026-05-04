import os

# Folder path
folder_path = "D:/Script"
# Get all files in the folder
files = os.listdir(folder_path)

# Loop through files and rename them
for index, file_name in enumerate(files):
    old_file = os.path.join(folder_path, file_name)
    
    new_name = f"report_{index + 1}.txt"
    new_file = os.path.join(folder_path, new_name)
    
    os.rename(old_file, new_file)

print("Files renamed successfully!")
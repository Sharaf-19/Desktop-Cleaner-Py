import os
import shutil

#define desktop path
desktop_path = os.path.expanduser("~/Desktop")
#print(desktop_path)


#create a dic to store the file paths by file extension

files_by_extension = {}

#loop throough all the files on the desktop

for filename in os.listdir(desktop_path):
  #get the file path
  file_path = os.path.join(desktop_path, filename)

  #check if its a file
  if os.path.isfile(file_path):
    #get the file extension
    file_extension = os.path.splitext(filename)[1]

    #add file extension and file path to the dic

    if file_extension not in files_by_extension:
      files_by_extension[file_extension] = [file_path]
    
    files_by_extension[file_extension].append(file_path)
#print(files_by_extension)

#create a folder for each file extension and move the files to its respective folders

for file_extension, file_path in files_by_extension.items():
  #create a folder for the file extension
  folder_name = f"{file_extension[1:].upper()} Files"
  folder_path = os.path.join(desktop_path, folder_name)

  #create the folder if it doesnt exist
  if not os.path.exists(folder_path):
    os.makedirs(folder_path)
  
  #moving the files to respective folders
  for file_path in file_path:
    shutil.move(file_path, folder_path)





import os
for folder_name, sub_folders, file_names in os.walk('data'):
    print('The folder is ' + folder_name)
    print('the subfolders ' + str(sub_folders))
    print('the filenames ' + str(file_names))

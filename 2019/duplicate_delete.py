# this is to delete duplicate files

# this is the steps:
"""
#1 check if the file is the same,
#2 check if the file name is the same but with a additional number   
          like this: 
            2nd Grade P1.one (On 10-27-2019).one
            2nd Grade P1.one (On 10-27-2019 - 2).one
#3 if both of the above are true then we check the file sum to see if they are the same

if all 3 are true then they are file duplicates
if 2 are true then most likely they are the same
if 1<= are true then they are not duplicates


we will look in this folder
C:\Users\demir_20\Downloads\DeleteDuplicates\Backup

""" 
import os



input_folder = r"C:\Users\demir_20\Downloads\DeleteDuplicates\Backup"

def get_allFiles(folder_to_search):
  all_files = []
  for root,d_names,f_names in os.walk(folder_to_search):
    if "\\OneNote_RecycleBin" in root:
      continue 
    for flie_name in f_names:
      all_files.append( os.path.join(root, flie_name) )
      
  return all_files


all_files = get_allFiles(input_folder)

print all_files

# def

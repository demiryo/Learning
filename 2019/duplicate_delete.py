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
import json

def get_allFiles(folder_to_search):
  all_files = []
  for root,d_names,f_names in os.walk(folder_to_search):
    if "\\OneNote_RecycleBin" in root:
      continue 
    for flie_name in f_names:
      all_files.append( os.path.join(root, flie_name) )
      
  return all_files

#print all_files

'''
Given file names like:
            2nd Grade P1.one (On 10-27-2019).one
            2nd Grade P1.one (On 10-27-2019 - 2).one

We want to extrack unique name like:
            2nd Grade P1.one
            2nd Grade P1.one
'''
def get_unique_name(file_name):
  last_index = file_name.rfind(" (On")
  return  file_name[0:last_index]

'''
this funtion is going to take a list of all the files in a directory tree, and use 3 dictionaries. 
  Level l we will group by folder
  level 2 we will group by unique file name
  level 3 we will group by the file size 
'''
def group_file(all_files):
  duplicates = {}
  for full_filepath in all_files:
    folder_name = os.path.dirname(full_filepath) 
    file_name = os.path.basename(full_filepath) 
    # print folder_name, file_name
    if duplicates.get(folder_name) is None:
      duplicates[folder_name] = {}
    clean_file_name = get_unique_name(file_name)
    if duplicates[folder_name].get(clean_file_name) is None:
      duplicates[folder_name][clean_file_name] = {}
    file_size = os.path.getsize(full_filepath) 
    if duplicates[folder_name][clean_file_name].get(file_size) is None:
      duplicates[folder_name][clean_file_name][file_size] = []
    duplicates[folder_name][clean_file_name][file_size].append(full_filepath)

  return duplicates


# main
input_folder = r"C:\Users\demir_20\Downloads\DeleteDuplicates\Backup"
all_files = get_allFiles(input_folder)
duplicates = group_file(all_files)
# print get_unique_name("Coding.one (On 10-27-2019 - 2).one") # expect "Coding.one"
print json.dumps(duplicates, indent=4, sort_keys=True) 

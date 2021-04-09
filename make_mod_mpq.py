import os
import configparser
import subprocess

from convert_all_bins_to_txt import files_and_structs


target_files = list(files_and_structs.keys())

# extract bins from patch mpq
def mpq_extract_bin(filename_txt):
    filename_bin = os.path.basename(filename_txt)[:-3] + 'bin'
    path_in_mpq = 'data\\global\\excel\\' + filename_bin
    code = subprocess.call(r'cd WinMPQ && .\\WinMPQ.exe e ..\\mpqOrig\\Patch_D2.mpq ' + path_in_mpq + ' ..\\BinFiles\\', shell=True)
    print(f'code: {code}')
    print(f"Extracted {filename_bin} to BinFiles\\")

for file in target_files:
    mpq_extract_bin(file)


# convert bins to txt
subprocess.call(["python", "convert_all_bins_to_txt.py"])


# read in settings.ini
config = configparser.ConfigParser()
config.read('settings.ini')


def get_filelines(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


### TODO: if the [section] is commented out in the ini file, config.items(section) will error below
# Monster Density corresponds to file TxtFiles/Levels.txt
section = 'Monster Density'
# TODO filenames can be gotten from target_files
filename = os.path.join('TxtFiles', 'Levels.txt')
lines = get_filelines(filename)

col_names = lines[0].split('\t')
idx_monden, idx_monden_n, idx_monden_h = col_names.index('MonDen'), col_names.index('MonDenN'), col_names.index('MonDenH')
col_level_name = col_names.index('LevelName')

for key, val in config.items(section):
    found = False
    for i in range(len(lines)):
        line_split = lines[i].split('\t')

        if key.lower() == line_split[col_level_name].lower():
            # Swampy Pit Level 2 also contains 'Pit level 2' as a substring. Should be careful
            line_split[idx_monden], line_split[idx_monden_n], line_split[idx_monden_h] = val, val, val
            lines[i] = '\t'.join(line_split)
            found = True
            print(f'For "{key}" the edited "{section}" value is: {val}')
            break
    if not found:
        print(f'***WARNING: Key "{key}" not found in the txt file columns!')

# once done with edits to the txt lines write the file.  then use txt_to_bin to create bins, and WinMPQ to add to mpq
with open(filename, 'w') as f:
    f.write("\n".join(lines) + "\n")


# Unique Items corresponds to file TxtFiles/UniqueItems.txt
section = 'Unique Items'
filename = os.path.join('TxtFiles', 'UniqueItems.txt')
lines = get_filelines(filename)

col_names = lines[0].split('\t')
idx_enabled = col_names.index('enabled')
col_index_name = col_names.index('index')
col_index_lvl = col_names.index('lvl')
col_index_lvlreq = col_names.index('lvl_req')
col_index_rarity = col_names.index('rarity')

for key, val in config.items(section):
    # The first occurrence of the item will be modified (so the crystal sword for Azurewrath)
    found = False
    for i in range(len(lines)):
        line_split = lines[i].split('\t')

        if key.lower() == line_split[col_index_name].lower():
            line_split[idx_enabled] = val

            if key.lower() == "constricting ring":
                line_split[col_index_lvl] = '53'
                line_split[col_index_lvlreq] = '45'
                line_split[col_index_rarity] = '20'

            lines[i] = '\t'.join(line_split)
            found = True
            print(f'For "{key}" the edited "{section}" value is: {val}')
            break
    if not found:
        print(f'***WARNING: Key "{key}" not found in the txt file columns!')

# once done with edits to the txt lines write the file.  then use txt_to_bin to create bins, and WinMPQ to add to mpq
with open(filename, 'w') as f:
    f.write("\n".join(lines) + "\n")


# Treasure Class corresponds to file TxtFiles/TreasureClassEx.txt
section = 'Treasure Class'
filename = os.path.join('TxtFiles', 'TreasureClassEx.txt')
lines = get_filelines(filename)

col_names = lines[0].split('\t')
idx_prob2, idx_prob3 = col_names.index('Prob2'), col_names.index('Prob3')
col_treasureclass = col_names.index('TreasureClass')

for key, val in config.items(section):
    found = False
    for i in range(len(lines)):
        line_split = lines[i].split('\t')

        if key.lower() == line_split[col_treasureclass].lower():
            if "runes 17" in key.lower():
                line_split[idx_prob2] = val
            else:
                line_split[idx_prob3] = val
            lines[i] = '\t'.join(line_split)
            found = True
            print(f'For "{key}" the edited "{section}" value is: {val}')
            break
    if not found:
        print(f'***WARNING: Key "{key}" not found in the txt file columns!')

# once done with edits to the txt lines write the file.  then use txt_to_bin to create bins, and WinMPQ to add to mpq
with open(filename, 'w') as f:
    f.write("\n".join(lines) + "\n")


# Skills corresponds to file TxtFiles/Skills.txt
section = 'Skills'
filename = os.path.join('TxtFiles', 'Skills.txt')
lines = get_filelines(filename)

col_names = lines[0].split('\t')
idx_delay = col_names.index('delay')
col_id = col_names.index('Id')

for key, val in config.items(section):
    found = False
    for i in range(len(lines)):
        line_split = lines[i].split('\t')

        if key.lower() == line_split[col_id].lower():
            line_split[idx_delay] = val
            lines[i] = '\t'.join(line_split)
            found = True
            print(f'For "{key}" the edited "{section}" value is: {val}')
            break
    if not found:
        print(f'***WARNING: Key "{key}" not found in the txt file columns!')

# once done with edits to the txt lines write the file.  then use txt_to_bin to create bins, and WinMPQ to add to mpq
with open(filename, 'w') as f:
    f.write("\n".join(lines) + "\n")


# Item Ratio corresponds to file TxtFiles/ItemRatio.txt
section = 'Item Ratio'
filename = os.path.join('TxtFiles', 'ItemRatio.txt')
lines = get_filelines(filename)

col_names = lines[0].split('\t')
idx_unique = col_names.index('Unique')
idx_unique_min = col_names.index('UniqueMin')
unique_min_val = '1'

# change all rows to the value from settings.ini
for key, val in config.items(section):
    for i in range(1, len(lines)):
        line_split = lines[i].split('\t')

        line_split[idx_unique] = val
        line_split[idx_unique_min] = unique_min_val
        lines[i] = '\t'.join(line_split)

# once done with edits to the txt lines write the file.  then use txt_to_bin to create bins, and WinMPQ to add to mpq
with open(filename, 'w') as f:
    f.write("\n".join(lines) + "\n")


# convert txt to bins
subprocess.call(["python", "convert_all_txt_to_bin.py"])

# copy orig mpq to mpqModded dir
os.system(r'copy mpqOrig\\patch_d2.mpq mpqModded\\patch_d2.mpq')


def mpq_add_bin(filename):
    filename_bin = os.path.basename(filename)[:-3] + 'bin'
    path_in_mpq = 'data\\global\\excel\\' + filename_bin
    code = subprocess.call(r'cd WinMPQ && .\\WinMPQ.exe add ..\\mpqModded\\Patch_D2.mpq ..\\BinFilesModded\\' + filename_bin + ' ' + path_in_mpq, shell=True)
    print(f'code: {code}')
    print(f"Added {filename_bin} to mpqModded\\patch_d2.mpq")

for filename in target_files:
    mpq_add_bin(filename)


# clean up
for filename in target_files:
    txtpath = os.path.join('TxtFiles', filename.replace('.bin', '.txt'))
    if os.path.isfile(txtpath):
        os.remove(txtpath)
os.removedirs('TxtFiles')

from os import path

from binstructs import *

files_and_structs = {
    "ItemRatio.txt": ItemRatio_struct,
    "Levels.txt": Levels_struct,
    "Skills.txt": Skills_struct,
    "TreasureClassEx.txt": TreasureClassEx_struct,
    "UniqueItems.txt": UniqueItems_struct,
}

def convert_tsv_to_bin(basefilename):
    # e.g. 'TsvFiles\\TreasureClassEx.txt'
    filename_tsv = path.join('TsvFiles', basefilename)

    # get the byteheader from the original .bin
    filename_bin_orig = path.join('BinFiles', basefilename[:-3] + 'bin')
    with open(filename_bin_orig, "rb") as f:
        byteheader = f.read(4)

    # read in tsv lines
    with open(filename_tsv, 'r') as f:
        contents = f.read()
        lines = contents.splitlines()

    # store all hex data in a list
    lines_hex_all = [byteheader]

    # convert tsv strings/ints to binary
    for line in lines[1:]:
        # e.g. ['0', 'Hadriels Hand', '100' ... ]
        parts = line.split('\t')

        counter = 0
        for val in files_and_structs[basefilename].values():
            if val['type'] == 'w':
                if 'tsv_to_bin_format' in val:
                    # if custom formatting, take the combined string/list (e.g. '0001'/['0', '0', '0', '1']) and create hex
                    str_input_list = parts[counter: counter + len(val['expand_to_cols'])]
                    hexvalue = val['tsv_to_bin_format'](str_input_list)

                    # increment counter to jump to correctly go to next hex value
                    counter += len(val['expand_to_cols']) - 1

                else:
                    intvalue = int(parts[counter])
                    # words and dwords will have number of bytes equal to the size of the field
                    sign = val['signed'] if 'signed' in val else True
                    hexvalue = intvalue.to_bytes(val['size'], byteorder='little', signed=sign)
                    ### TODO: check if signed=False ever comes up in the .bin and tsv files.   d2bin2txt c files have signed & unsigned ints
            else:
                # val['type'] is 'c', chars. create bytes that have the same size as the field. zero pad on the right
                charsvalue = parts[counter]
                hexvalue = bytes(charsvalue, 'utf-8') + bytes(val['size'] - len(charsvalue))

            lines_hex_all.append(hexvalue)
            counter += 1

    filename_bin_modded = path.join('BinFilesModded', basefilename[:-3] + 'bin')
    with open(filename_bin_modded, 'wb') as f:
        f.writelines(lines_hex_all)
    print(f"Completed: {filename_bin_modded}")


if __name__ == "__main__":
    # convert all tsv files to bins
    for name in files_and_structs:
        convert_tsv_to_bin(name)

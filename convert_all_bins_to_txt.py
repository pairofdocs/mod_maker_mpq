from os import path

from binstructs import *

files_and_structs = {
    "ItemRatio.bin": ItemRatio_struct,
    "Levels.bin": Levels_struct,
    "Skills.bin": Skills_struct,
    "TreasureClassEx.bin": TreasureClassEx_struct,
    "UniqueItems.bin": UniqueItems_struct,
}


def convert_bin_to_txt(basefilename):
    struct = files_and_structs[basefilename]

    row_size = sum([x['size'] for x in struct.values()])
    print(f'row_size: {row_size}')


    lines_txt_all = ['']
    for key in struct.keys():
        if 'expand_to_cols' in struct[key]:
            # expand to specified columns
            lines_txt_all[0] += '\t'.join(struct[key]['expand_to_cols']) + '\t'
        else:
            lines_txt_all[0] += key + '\t'

    filename_bin_orig = path.join('BinFiles', basefilename)
    with open(filename_bin_orig, "rb") as f:
        byteheader = f.read(4)

        while row_bytes := f.read(row_size):
            line_txt = ""

            current_pos = 0
            for key, value in struct.items():
                # print(f'key- column name: {key}')
                value['bytes'] = row_bytes[current_pos:current_pos + value['size']]
                current_pos += value['size']

                if value['type'] == 'w':
                    if 'bin_to_txt_format' in value:
                        # do custom formatting/splitting
                        line_txt += value['bin_to_txt_format'](value['bytes'])
                    else:
                        # default to 'signed' numbers
                        sign = value['signed'] if 'signed' in value else True
                        int_value = int.from_bytes(value['bytes'], byteorder='little', signed=sign)
                        # would this work for '255' FF? -1?  int.from_bytes(b'\xFF\xFF', 'little', signed=True) --> -1 works.
                        line_txt += str(int_value) + '\t'
                else:
                    # print(value['bytes'])

                    try:
                        line_txt += value['bytes'].decode('utf-8').replace('\x00','') + '\t'
                        # print()
                    except:
                        print(f'key- column name: {key}')
                        print(value['bytes'])
                        print('***Error decoding char bytes***')
                        print()
                        # break out of key,value loop for the row
                        break

            lines_txt_all.append(line_txt)

    filename_txt = path.join('TxtFiles', basefilename[:-3] + 'txt')
    with open(filename_txt, 'w') as f:
        f.write("\n".join(lines_txt_all) + "\n")
    print(f"Completed: {filename_txt}")
    print()


if __name__ == "__main__":
    for name in files_and_structs:
        print(f'Starting: {name}')
        convert_bin_to_txt(name)

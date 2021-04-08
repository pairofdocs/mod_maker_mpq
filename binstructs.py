
# row size 68 bytes
ItemRatio_struct = {
    "Unique" : {"size": 4, "type": "w"},
    "UniqueDivisor" : {"size": 4, "type": "w"},
    "UniqueMin" : {"size": 4, "type": "w"},

    "Rare" : {"size": 4, "type": "w"},
    "RareDivisor" : {"size": 4, "type": "w"},
    "RareMin" : {"size": 4, "type": "w"},

    "Set" : {"size": 4, "type": "w"},
    "SetDivisor" : {"size": 4, "type": "w"},
    "SetMin" : {"size": 4, "type": "w"},

    "Magic" : {"size": 4, "type": "w"},
    "MagicDivisor" : {"size": 4, "type": "w"},
    "MagicMin" : {"size": 4, "type": "w"},

    "HiQuality" : {"size": 4, "type": "w"},
    "HiQualityDivisor" : {"size": 4, "type": "w"},

    "Normal" : {"size": 4, "type": "w"},
    "NormalDivisor" : {"size": 4, "type": "w"},

    "Version" : {"size": 2, "type": "w"},
    "Uber" : {"size": 1, "type": "w"},
    "Class_Specific" : {"size": 1, "type": "w"},
}

# using the struct from  d2bin2txt/bin2txt/levels.c,  removing 'iPadding' areas and following order of code 'VALUE_MAP_DEFINE(pstValueMap, pstLineInfo, Id, USHORT);'
# also found that OpenDiablo2 has a struct for their txts: OpenDiablo2/d2core/d2records/level_details_loader.go but it's not the 'bin order'
# 155 rows in levels.txt - converted by d2bin2txt.
# 84,320 total bytes in levels.bin  -->  544 bytes per row.    alignment works in HxD -v'
# byte header is 4bytes: 9B 00 00 00
Levels_struct = {  # 185/6 fields  (end fields of levels.c were not used because the row size limit was reached
    "Id": {"size": 2, "type": "w"},
    "Pal": {"size": 1, "type": "w"},      # **these should be int** not char
    "Act": {"size": 1, "type": "w"},

    "Teleport": {"size": 1, "type": "w"},
    "Rain": {"size": 1, "type": "w"},
    "Mud": {"size": 1, "type": "w"},
    "NoPer": {"size": 1, "type": "w"},

    "IsInside": {"size": 1, "type": "w"},
    "DrawEdges": {"size": 1, "type": "w"},
    "iPadding2": {"size": 2, "type": "w"},

    "WarpDist": {"size": 4, "type": "w"},

    "MonLvl1": {"size": 2, "type": "w"},
    "MonLvl2": {"size": 2, "type": "w"},

    "MonLvl3": {"size": 2, "type": "w"},
    "MonLvl1Ex": {"size": 2, "type": "w"},

    "MonLvl2Ex": {"size": 2, "type": "w"},
    "MonLvl3Ex": {"size": 2, "type": "w"},

    "MonDen": {"size": 4, "type": "w"},
    "MonDenN": {"size": 4, "type": "w"},
    "MonDenH": {"size": 4, "type": "w"},

    "MonUMin": {"size": 1, "type": "w"},         #   **these should be int** not char
    "MonUMinN": {"size": 1, "type": "w"},
    "MonUMinH": {"size": 1, "type": "w"}, # 04

    "MonUMax": {"size": 1, "type": "w"},
    "MonUMaxN": {"size": 1, "type": "w"},
    "MonUMaxH": {"size": 1, "type": "w"},
    "MonWndr": {"size": 1, "type": "w"},
    "MonSpcWalk": {"size": 1, "type": "w"},         #  41

    "Quest": {"size": 1, "type": "w"},
    "rangedspawn": {"size": 1, "type": "w"},         #  ss    55    offset 49 (50 bytes, since 0base index)
    "NumMon": {"size": 2, "type": "w"},        # 33  (# key)

    "iPadding13": {"size": 2, "type": "w"},        #2 bytes always zero   (byte offset 52-53)
    "mon1": {"size": 2, "type": "w"},   #//MonStats   offset 54
    "mon2": {"size": 2, "type": "w"},
    "mon3": {"size": 2, "type": "w"},
    "mon4": {"size": 2, "type": "w"},
    "mon5": {"size": 2, "type": "w"},
    "mon6": {"size": 2, "type": "w"},
    "mon7": {"size": 2, "type": "w"},
    "mon8": {"size": 2, "type": "w"},
    "mon9": {"size": 2, "type": "w"},
    "mon10": {"size": 2, "type": "w"},

    "mon11": {"size": 2, "type": "w"},     # offset 74
    "mon12": {"size": 2, "type": "w"},
    "mon13": {"size": 2, "type": "w"},
    "mon14": {"size": 2, "type": "w"},
    "mon15": {"size": 2, "type": "w"},
    "mon16": {"size": 2, "type": "w"},
    "mon17": {"size": 2, "type": "w"},
    "mon18": {"size": 2, "type": "w"},
    "mon19": {"size": 2, "type": "w"},
    "mon20": {"size": 2, "type": "w"},

    "mon21": {"size": 2, "type": "w"},   # offset 94
    "mon22": {"size": 2, "type": "w"},
    "mon23": {"size": 2, "type": "w"},
    "mon24": {"size": 2, "type": "w"},
    "mon25": {"size": 2, "type": "w"},

    "nmon1": {"size": 2, "type": "w"},   #//MonStats   # offset 104
    "nmon2": {"size": 2, "type": "w"},
    "nmon3": {"size": 2, "type": "w"},
    "nmon4": {"size": 2, "type": "w"},
    "nmon5": {"size": 2, "type": "w"},
    "nmon6": {"size": 2, "type": "w"},
    "nmon7": {"size": 2, "type": "w"},
    "nmon8": {"size": 2, "type": "w"},
    "nmon9": {"size": 2, "type": "w"},
    "nmon10": {"size": 2, "type": "w"},

    "nmon11": {"size": 2, "type": "w"},    # offset 124
    "nmon12": {"size": 2, "type": "w"},
    "nmon13": {"size": 2, "type": "w"},
    "nmon14": {"size": 2, "type": "w"},
    "nmon15": {"size": 2, "type": "w"},
    "nmon16": {"size": 2, "type": "w"},
    "nmon17": {"size": 2, "type": "w"},
    "nmon18": {"size": 2, "type": "w"},
    "nmon19": {"size": 2, "type": "w"},
    "nmon20": {"size": 2, "type": "w"},

    "nmon21": {"size": 2, "type": "w"},  # offset 144
    "nmon22": {"size": 2, "type": "w"},
    "nmon23": {"size": 2, "type": "w"},
    "nmon24": {"size": 2, "type": "w"},
    "nmon25": {"size": 2, "type": "w"},

    "umon1": {"size": 2, "type": "w"},  #//monstats    # offset 154.    value5, value28 (cold plains).  looks right--comparing to LoD umon1 column
    "umon2": {"size": 2, "type": "w"},
    "umon3": {"size": 2, "type": "w"},
    "umon4": {"size": 2, "type": "w"},  #//40
    "umon5": {"size": 2, "type": "w"},
    "umon6": {"size": 2, "type": "w"},
    "umon7": {"size": 2, "type": "w"},
    "umon8": {"size": 2, "type": "w"},
    "umon9": {"size": 2, "type": "w"},
    "umon10": {"size": 2, "type": "w"},

    "umon11": {"size": 2, "type": "w"},    # offset 174
    "umon12": {"size": 2, "type": "w"},
    "umon13": {"size": 2, "type": "w"},
    "umon14": {"size": 2, "type": "w"},
    "umon15": {"size": 2, "type": "w"},
    "umon16": {"size": 2, "type": "w"},
    "umon17": {"size": 2, "type": "w"},
    "umon18": {"size": 2, "type": "w"},
    "umon19": {"size": 2, "type": "w"},
    "umon20": {"size": 2, "type": "w"},

    "umon21": {"size": 2, "type": "w"},   # offset 194
    "umon22": {"size": 2, "type": "w"},
    "umon23": {"size": 2, "type": "w"},
    "umon24": {"size": 2, "type": "w"},
    "umon25": {"size": 2, "type": "w"},

    "cmon1": {"size": 2, "type": "w"},  #//monstats    # offset 204   .  this matches LoD cmon1 column -v'
    "cmon2": {"size": 2, "type": "w"},
    "cmon3": {"size": 2, "type": "w"},
    "cmon4": {"size": 2, "type": "w"},

    "cpct1": {"size": 2, "type": "w"},    # offset 212          this matches LoD col cpct1
    "cpct2": {"size": 2, "type": "w"},
    "cpct3": {"size": 2, "type": "w"},
    "cpct4": {"size": 2, "type": "w"},

    "camt4": {"size": 2, "type": "w"},      #220 start dec offset         sum() -- size = 222 -v'
    "iPadding55": {"size": 2, "type": "w"},    #222 start offset
    "iPadding56": {"size": 4, "type": "w"},      #56 4 bytes   (could be 2 shorts here. unk cols)

    "Waypoint": {"size": 1, "type": "w"},     #offset 228/   valeus 1,2,3 for cold plains, stony, darkwood. matches .txt
                                                # ***error*** found for type. waypoint is int. not a char (like levels.c has)
                                                # make int 1 byte
    "ObjGrp0": {"size": 1, "type": "w"},
    "ObjGrp1": {"size": 1, "type": "w"},
    "ObjGrp2": {"size": 1, "type": "w"},

    "ObjGrp3": {"size": 1, "type": "w"},
    "ObjGrp4": {"size": 1, "type": "w"},     #####  *** error found *** this are also not chars.  they are int values
    "ObjGrp5": {"size": 1, "type": "w"},     #####  *** error found *** this are also not chars.  they are int values
    "ObjGrp6": {"size": 1, "type": "w"},

    "ObjGrp7": {"size": 1, "type": "w"}, #offset 236
    "ObjPrb0": {"size": 1, "type": "w"},

    "ObjPrb1": {"size": 1, "type": "w"},
    "ObjPrb2": {"size": 1, "type": "w"},
    "ObjPrb3": {"size": 1, "type": "w"},
    "ObjPrb4": {"size": 1, "type": "w"},
    "ObjPrb5": {"size": 1, "type": "w"},           #####  *** error found *** this are also not chars.  they are int values
    "ObjPrb6": {"size": 1, "type": "w"},
    "ObjPrb7": {"size": 1, "type": "w"},  # offset 244

    "LevelName": {"size": 40, "type": "c"},  #245 start offset.  hex 88
    "LevelWarp": {"size": 40, "type": "c"},   #285 offset
    "EntryFile": {"size": 39, "type": "c"},    #325 offset    ~A1L7 chars

    "iPadding91": {"size": 4, "type": "w"},        #364 offset.   all zeros for mant columns
    "iPadding92": {"size": 4, "type": "w"},
    "iPadding93": {"size": 4, "type": "w"},
    "iPadding94": {"size": 4, "type": "w"},
    "iPadding95": {"size": 4, "type": "w"},
    "iPadding96": {"size": 4, "type": "w"},
    "iPadding97": {"size": 4, "type": "w"},
    "iPadding98": {"size": 4, "type": "w"},
    "iPadding99": {"size": 4, "type": "w"},
    "iPadding100": {"size": 4, "type": "w"},

    "iPadding101": {"size": 4, "type": "w"},   # offset 404
    "iPadding102": {"size": 4, "type": "w"},
    "iPadding103": {"size": 4, "type": "w"},
    "iPadding104": {"size": 4, "type": "w"},
    "iPadding105": {"size": 4, "type": "w"},
    "iPadding106": {"size": 4, "type": "w"},
    "iPadding107": {"size": 4, "type": "w"},
    "iPadding108": {"size": 4, "type": "w"},
    "iPadding109": {"size": 4, "type": "w"},
    "iPadding110": {"size": 4, "type": "w"},

    "iPadding111": {"size": 4, "type": "w"},  # offset 444
    "iPadding112": {"size": 4, "type": "w"},
    "iPadding113": {"size": 4, "type": "w"},
    "iPadding114": {"size": 4, "type": "w"},
    "iPadding115": {"size": 4, "type": "w"},
    "iPadding116": {"size": 4, "type": "w"},
    "iPadding117": {"size": 4, "type": "w"},
    "iPadding118": {"size": 4, "type": "w"},
    "iPadding119": {"size": 4, "type": "w"},
    "iPadding120": {"size": 4, "type": "w"},

    "iPadding121": {"size": 4, "type": "w"},  #offset 484
    "iPadding122": {"size": 4, "type": "w"},
    "iPadding123": {"size": 4, "type": "w"},
    "iPadding124": {"size": 4, "type": "w"},
    "iPadding125": {"size": 4, "type": "w"},
    "iPadding126": {"size": 4, "type": "w"},
    "iPadding127": {"size": 4, "type": "w"},
    "iPadding128": {"size": 4, "type": "w"},
    "iPadding129": {"size": 4, "type": "w"},
    "iPadding130": {"size": 4, "type": "w"},

    "iPadding131": {"size": 4, "type": "w"},  #offset 524
    "Themes": {"size": 4, "type": "w"},        #offset 528      hex 77.     values '8'  matches .txt  -v
    "FloorFilter": {"size": 4, "type": "w"},
    "BlankScreen": {"size": 4, "type": "w"},   #offset 536
    "SoundEnv": {"size": 4, "type": "w"},      #offset 540.   and end is 544
}

# row size 572 bytes
Skills_struct = {
    "Id" : {"size": 4, "type": "w", "signed": False},

    # bit processing needed here. using vBitCombined, vBitCombined2 from d2bin2txt's skills.c
    "BitCombined" : {"size": 4, "type": "w", "signed": False},
    "BitCombined2" : {"size": 4, "type": "w", "signed": False},
    # these fields are populated from the two bytes above
    # "interrupt" : {"size": 4, "type": "w"},
    # "leftskill" : {"size": 4, "type": "w"},
    # "ItemTgtDo" : {"size": 4, "type": "w"},
    # "AttackNoMana" : {"size": 4, "type": "w"},
    # "TargetItem" : {"size": 4, "type": "w"},
    # "TargetAlly" : {"size": 4, "type": "w"},
    # "TargetPet" : {"size": 4, "type": "w"},
    # "TargetCorpse" : {"size": 4, "type": "w"},
    # "SearchOpenXY" : {"size": 4, "type": "w"},
    # "SearchEnemyNear" : {"size": 4, "type": "w"},
    # "SearchEnemyXY" : {"size": 4, "type": "w"},
    # "TargetableOnly" : {"size": 4, "type": "w"},
    # "UseAttackRate" : {"size": 4, "type": "w"},
    # "durability" : {"size": 4, "type": "w"},
    # "enhanceable" : {"size": 4, "type": "w"},
    # "noammo" : {"size": 4, "type": "w"},
    # "immediate" : {"size": 4, "type": "w"},
    # "weaponsnd" : {"size": 4, "type": "w"},
    # "stsounddelay" : {"size": 4, "type": "w"},
    # "stsuccessonly" : {"size": 4, "type": "w"},
    # "repeat" : {"size": 4, "type": "w"},
    # "InGame" : {"size": 4, "type": "w"},
    # "Kick" : {"size": 4, "type": "w"},
    # "InTown" : {"size": 4, "type": "w"},
    # "prgstack" : {"size": 4, "type": "w"},
    # "periodic" : {"size": 4, "type": "w"},
    # "aura" : {"size": 4, "type": "w"},
    # "passive" : {"size": 4, "type": "w"},
    # "finishing" : {"size": 4, "type": "w"},
    # "progressive" : {"size": 4, "type": "w"},
    # "lob" : {"size": 4, "type": "w"},
    # "decquant" : {"size": 4, "type": "w"},
    # "warp" : {"size": 4, "type": "w"},
    # "usemanaondo" : {"size": 4, "type": "w"},
    # "scroll" : {"size": 4, "type": "w"},
    # "general" : {"size": 4, "type": "w"},
    # "ItemCltCheckStart" : {"size": 4, "type": "w"},
    # "ItemCheckStart" : {"size": 4, "type": "w"},
    # "TgtPlaceCheck" : {"size": 4, "type": "w"},

    "charclass" : {"size": 1, "type": "w", "signed": False},
    "padding1" : {"size": 3, "type": "w", "signed": False},

    "anim" : {"size": 1, "type": "w", "signed": False},   # start offset 16
    "monanim" : {"size": 1, "type": "w", "signed": False},
    "seqtrans" : {"size": 1, "type": "w", "signed": False},
    "seqnum" : {"size": 1, "type": "w", "signed": False},
    "range" : {"size": 1, "type": "w", "signed": False},
    "SelectProc" : {"size": 1, "type": "w", "signed": False},

    "seqinput" : {"size": 2, "type": "w", "signed": False},  # start offset 22
    "itypea1" : {"size": 2, "type": "w", "signed": False},
    "itypea2" : {"size": 2, "type": "w", "signed": False},
    "itypea3" : {"size": 2, "type": "w", "signed": False},
    "itypeb1" : {"size": 2, "type": "w", "signed": False},
    "itypeb2" : {"size": 2, "type": "w", "signed": False},
    "itypeb3" : {"size": 2, "type": "w", "signed": False},
    "etypea1" : {"size": 2, "type": "w", "signed": False},
    "etypea2" : {"size": 2, "type": "w", "signed": False},
    "etypeb1" : {"size": 2, "type": "w", "signed": False},
    "etypeb2" : {"size": 2, "type": "w", "signed": False},
    "srvstfunc" : {"size": 2, "type": "w", "signed": False},
    "srvdofunc" : {"size": 2, "type": "w", "signed": False},
    "srvprgfunc1" : {"size": 2, "type": "w", "signed": False},
    "srvprgfunc2" : {"size": 2, "type": "w", "signed": False},
    "srvprgfunc3" : {"size": 2, "type": "w", "signed": False},
    "padding13" : {"size": 2, "type": "w", "signed": False},

    "prgcalc1" : {"size": 4, "type": "w", "signed": False},  # start offset 56       # should this be signed: True?  (tsv value is 4294967295)
    "prgcalc2" : {"size": 4, "type": "w", "signed": False},
    "prgcalc3" : {"size": 4, "type": "w", "signed": False},
    "prgdam" : {"size": 2, "type": "w", "signed": False},

    "srvmissile" : {"size": 2, "type": "w", "signed": False}, # start offset 70
    "srvmissilea" : {"size": 2, "type": "w", "signed": False},
    "srvmissileb" : {"size": 2, "type": "w", "signed": False},
    "srvmissilec" : {"size": 2, "type": "w", "signed": False},
    "srvoverlay" : {"size": 2, "type": "w", "signed": False},
    "aurafilter" : {"size": 4, "type": "w", "signed": False},
    "aurastat1" : {"size": 2, "type": "w", "signed": False},
    "aurastat2" : {"size": 2, "type": "w", "signed": False},
    "aurastat3" : {"size": 2, "type": "w", "signed": False},
    "aurastat4" : {"size": 2, "type": "w", "signed": False}, # offset 92
    "aurastat5" : {"size": 2, "type": "w", "signed": False},
    "aurastat6" : {"size": 2, "type": "w", "signed": False},

    "auralencalc" : {"size": 4, "type": "w", "signed": False},  # offset 96
    "aurarangecalc" : {"size": 4, "type": "w", "signed": False},
    "aurastatcalc1" : {"size": 4, "type": "w", "signed": False},
    "aurastatcalc2" : {"size": 4, "type": "w", "signed": False},
    "aurastatcalc3" : {"size": 4, "type": "w", "signed": False},
    "aurastatcalc4" : {"size": 4, "type": "w", "signed": False},
    "aurastatcalc5" : {"size": 4, "type": "w", "signed": False},
    "aurastatcalc6" : {"size": 4, "type": "w", "signed": False},

    "aurastate" : {"size": 2, "type": "w", "signed": False},    # offset 128
    "auratargetstate" : {"size": 2, "type": "w", "signed": False},
    "auraevent1" : {"size": 2, "type": "w", "signed": False},
    "auraevent2" : {"size": 2, "type": "w", "signed": False},
    "auraevent3" : {"size": 2, "type": "w", "signed": False},
    "auraeventfunc1" : {"size": 2, "type": "w", "signed": False},
    "auraeventfunc2" : {"size": 2, "type": "w", "signed": False},
    "auraeventfunc3" : {"size": 2, "type": "w", "signed": False},
    "auratgtevent" : {"size": 2, "type": "w", "signed": False},
    "auratgteventfunc" : {"size": 2, "type": "w", "signed": False},

    "passivestate" : {"size": 2, "type": "w", "signed": False},
    "passiveitype" : {"size": 2, "type": "w", "signed": False},
    "passivestat1" : {"size": 2, "type": "w", "signed": False},
    "passivestat2" : {"size": 2, "type": "w", "signed": False},
    "passivestat3" : {"size": 2, "type": "w", "signed": False},
    "passivestat4" : {"size": 2, "type": "w", "signed": False},
    "passivestat5" : {"size": 2, "type": "w", "signed": False},
    "padding40" : {"size": 2, "type": "w", "signed": False},

    "passivecalc1" : {"size": 4, "type": "w", "signed": False},  # offset 164
    "passivecalc2" : {"size": 4, "type": "w", "signed": False},
    "passivecalc3" : {"size": 4, "type": "w", "signed": False},
    "passivecalc4" : {"size": 4, "type": "w", "signed": False},
    "passivecalc5" : {"size": 4, "type": "w", "signed": False},

    "passiveevent" : {"size": 2, "type": "w", "signed": False},     # offset 184
    "passiveeventfunc" : {"size": 2, "type": "w", "signed": False},
    "summon" : {"size": 2, "type": "w", "signed": False},

    "pettype" : {"size": 1, "type": "w", "signed": False},   # offset 190
    "summode" : {"size": 1, "type": "w", "signed": False},
    "petmax" : {"size": 4, "type": "w", "signed": False},

    "sumskill1" : {"size": 2, "type": "w", "signed": False},  # offset 196
    "sumskill2" : {"size": 2, "type": "w", "signed": False},
    "sumskill3" : {"size": 2, "type": "w", "signed": False},
    "sumskill4" : {"size": 2, "type": "w", "signed": False},
    "sumskill5" : {"size": 2, "type": "w", "signed": False},
    "padding51" : {"size": 2, "type": "w", "signed": False},

    "sumsk1calc" : {"size": 4, "type": "w", "signed": False},  # offset 208
    "sumsk2calc" : {"size": 4, "type": "w", "signed": False},
    "sumsk3calc" : {"size": 4, "type": "w", "signed": False},
    "sumsk4calc" : {"size": 4, "type": "w", "signed": False},
    "sumsk5calc" : {"size": 4, "type": "w", "signed": False},

    "sumumod" : {"size": 2, "type": "w", "signed": False},   # offset 228
    "sumoverlay" : {"size": 2, "type": "w", "signed": False},

    "cltmissile" : {"size": 2, "type": "w", "signed": False},  # offset 232
    "cltmissilea" : {"size": 2, "type": "w", "signed": False},
    "cltmissileb" : {"size": 2, "type": "w", "signed": False},
    "cltmissilec" : {"size": 2, "type": "w", "signed": False},
    "cltmissiled" : {"size": 2, "type": "w", "signed": False},
    "cltstfunc" : {"size": 2, "type": "w", "signed": False},
    "cltdofunc" : {"size": 2, "type": "w", "signed": False},
    "cltprgfunc1" : {"size": 2, "type": "w", "signed": False},
    "cltprgfunc2" : {"size": 2, "type": "w", "signed": False},
    "cltprgfunc3" : {"size": 2, "type": "w", "signed": False},

    "stsound" : {"size": 2, "type": "w", "signed": False},   # offset 252
    "stsoundclass" : {"size": 2, "type": "w", "signed": False},
    "dosound" : {"size": 2, "type": "w", "signed": False},
    "dosound a" : {"size": 2, "type": "w", "signed": False},
    "dosound b" : {"size": 2, "type": "w", "signed": False},
    "castoverlay" : {"size": 2, "type": "w", "signed": False},
    "tgtoverlay" : {"size": 2, "type": "w", "signed": False},
    "tgtsound" : {"size": 2, "type": "w", "signed": False},
    "prgoverlay" : {"size": 2, "type": "w", "signed": False},
    "prgsound" : {"size": 2, "type": "w", "signed": False},

    "cltoverlaya" : {"size": 2, "type": "w", "signed": False},  # offset 272
    "cltoverlayb" : {"size": 2, "type": "w", "signed": False},

    "cltcalc1" : {"size": 4, "type": "w", "signed": False},   # offset 276
    "cltcalc2" : {"size": 4, "type": "w", "signed": False},
    "cltcalc3" : {"size": 4, "type": "w", "signed": False},


    "ItemTarget" : {"size": 1, "type": "w", "signed": False},  # offset 288
    "Padding72" : {"size": 1, "type": "w", "signed": False},

    "ItemCastSound" : {"size": 2, "type": "w", "signed": False},
    "ItemCastOverlay" : {"size": 2, "type": "w", "signed": False},
    "Padding73" : {"size": 2, "type": "w", "signed": False},

    "perdelay" : {"size": 4, "type": "w"},   # offset 296

    "maxlvl" : {"size": 2, "type": "w", "signed": False},     # offset 300
    "ResultFlags" : {"size": 2, "type": "w", "signed": False},

    "HitFlags" : {"size": 4, "type": "w", "signed": False},   # offset 304
    "HitClass" : {"size": 4, "type": "w", "signed": False},

    "calc1" : {"size": 4, "type": "w", "signed": False},   # offset 312
    "calc2" : {"size": 4, "type": "w", "signed": False},
    "calc3" : {"size": 4, "type": "w", "signed": False},
    "calc4" : {"size": 4, "type": "w", "signed": False},
    "Param1" : {"size": 4, "type": "w"},
    "Param2" : {"size": 4, "type": "w"},
    "Param3" : {"size": 4, "type": "w"},
    "Param4" : {"size": 4, "type": "w"},
    "Param5" : {"size": 4, "type": "w"},
    "Param6" : {"size": 4, "type": "w"},
    "Param7" : {"size": 4, "type": "w"},
    "Param8" : {"size": 4, "type": "w"},

    "weapsel" : {"size": 2, "type": "w", "signed": False},     # offset 360
    "ItemEffect" : {"size": 2, "type": "w", "signed": False},
    "ItemCltEffect" : {"size": 2, "type": "w", "signed": False},
    "Padding91" : {"size": 2, "type": "w", "signed": False},

    "skpoints" : {"size": 4, "type": "w", "signed": False},  # offset 368

    "reqlevel" : {"size": 2, "type": "w", "signed": False},  # offset 372
    "reqstr" : {"size": 2, "type": "w", "signed": False},
    "reqdex" : {"size": 2, "type": "w", "signed": False},
    "reqint" : {"size": 2, "type": "w", "signed": False},
    "reqvit" : {"size": 2, "type": "w", "signed": False},
    "reqskill1" : {"size": 2, "type": "w", "signed": False},
    "reqskill2" : {"size": 2, "type": "w", "signed": False},
    "reqskill3" : {"size": 2, "type": "w", "signed": False},
    "startmana" : {"size": 2, "type": "w", "signed": False},
    "minmana" : {"size": 2, "type": "w", "signed": False},
    "manashift" : {"size": 2, "type": "w", "signed": False},
    "mana" : {"size": 2, "type": "w", "signed": False},

    "lvlmana" : {"size": 2, "type": "w"},     # offset 396
    "attackrank" : {"size": 1, "type": "w", "signed": False},
    "LineOfSight" : {"size": 1, "type": "w", "signed": False},

    # delay seems to have another layer of coding to it. LoD hex has 53 00 (83 decimal) and txt has 15 frames
    "delay" : {"size": 4, "type": "w"},      # offset 400
    "skilldesc" : {"size": 2, "type": "w", "signed": False},
    "Padding101" : {"size": 2, "type": "w", "signed": False},

    "ToHit" : {"size": 4, "type": "w", "signed": False},     # offset 408
    "LevToHit" : {"size": 4, "type": "w", "signed": False},
    "ToHitCalc" : {"size": 4, "type": "w", "signed": False},

    "HitShift" : {"size": 1, "type": "w", "signed": False},  # offset 420
    "SrcDam" : {"size": 1, "type": "w", "signed": False},          # signed: False works here -v'
    "Padding105" : {"size": 2, "type": "w", "signed": False},


    "MinDam" : {"size": 4, "type": "w", "signed": False},     # offset 424
    "MaxDam" : {"size": 4, "type": "w", "signed": False},
    "MinLevDam1" : {"size": 4, "type": "w", "signed": False},
    "MinLevDam2" : {"size": 4, "type": "w", "signed": False},
    "MinLevDam3" : {"size": 4, "type": "w", "signed": False},
    "MinLevDam4" : {"size": 4, "type": "w", "signed": False},
    "MinLevDam5" : {"size": 4, "type": "w", "signed": False},
    "MaxLevDam1" : {"size": 4, "type": "w", "signed": False},
    "MaxLevDam2" : {"size": 4, "type": "w", "signed": False},
    "MaxLevDam3" : {"size": 4, "type": "w", "signed": False},
    "MaxLevDam4" : {"size": 4, "type": "w", "signed": False},
    "MaxLevDam5" : {"size": 4, "type": "w", "signed": False},
    "DmgSymPerCalc" : {"size": 4, "type": "w", "signed": False},

    "EType" : {"size": 2, "type": "w", "signed": False},       # offset 476
    "Padding119" : {"size": 2, "type": "w", "signed": False},

    "EMin" : {"size": 4, "type": "w", "signed": False},        # offset 480
    "EMax" : {"size": 4, "type": "w", "signed": False},
    "EMinLev1" : {"size": 4, "type": "w", "signed": False},
    "EMinLev2" : {"size": 4, "type": "w", "signed": False},
    "EMinLev3" : {"size": 4, "type": "w", "signed": False},
    "EMinLev4" : {"size": 4, "type": "w", "signed": False},
    "EMinLev5" : {"size": 4, "type": "w", "signed": False},
    "EMaxLev1" : {"size": 4, "type": "w", "signed": False},
    "EMaxLev2" : {"size": 4, "type": "w", "signed": False},
    "EMaxLev3" : {"size": 4, "type": "w", "signed": False},
    "EMaxLev4" : {"size": 4, "type": "w", "signed": False},
    "EMaxLev5" : {"size": 4, "type": "w", "signed": False},

    "EDmgSymPerCalc" : {"size": 4, "type": "w", "signed": False},  # offset 528
    "ELen" : {"size": 4, "type": "w", "signed": False},
    "ELevLen1" : {"size": 4, "type": "w", "signed": False},
    "ELevLen2" : {"size": 4, "type": "w", "signed": False},
    "ELevLen3" : {"size": 4, "type": "w", "signed": False},
    "ELenSymPerCalc" : {"size": 4, "type": "w", "signed": False},

    "restrict" : {"size": 2, "type": "w", "signed": False},   # offset 552
    "State1" : {"size": 2, "type": "w", "signed": False},
    "State2" : {"size": 2, "type": "w", "signed": False},
    "State3" : {"size": 2, "type": "w", "signed": False},

    "aitype" : {"size": 2, "type": "w", "signed": False},
    "aibonus" : {"size": 2, "type": "w"},

    "costmyspmult" : {"size": 4, "type": "w", "signed": False},  # offset 564
    "costmyspadd" : {"size": 4, "type": "w", "signed": False},
}

TreasureClassEx_struct = {
    "TreasureClass" : {"size": 32, "type": "c"},  # c for char         -- this uses bytes.decode()
    "Picks" : {"size": 4, "type": "w"},           # w for WORD, DWORD  -- this type uses int.from_bytes()

    "group" : {"size": 2, "type": "w"},
    "level" : {"size": 2, "type": "w"},
    "Magic" : {"size": 2, "type": "w"},
    "Rare" : {"size": 2, "type": "w"},
    "Set" : {"size": 2, "type": "w"},
    "Unique" : {"size": 2, "type": "w"},

    "filler" : {"size": 4, "type": "w"},
    "NoDrop" : {"size": 4, "type": "w"},

    "Item1" : {"size": 64, "type": "c"},
    "Item2" : {"size": 64, "type": "c"},
    "Item3" : {"size": 64, "type": "c"},
    "Item4" : {"size": 64, "type": "c"},
    "Item5" : {"size": 64, "type": "c"},
    "Item6" : {"size": 64, "type": "c"},
    "Item7" : {"size": 64, "type": "c"},
    "Item8" : {"size": 64, "type": "c"},
    "Item9" : {"size": 64, "type": "c"},
    "Item10" : {"size": 64, "type": "c"},

    "Prob1" : {"size": 4, "type": "w"},
    "Prob2" : {"size": 4, "type": "w"},
    "Prob3" : {"size": 4, "type": "w"},
    "Prob4" : {"size": 4, "type": "w"},
    "Prob5" : {"size": 4, "type": "w"},
    "Prob6" : {"size": 4, "type": "w"},
    "Prob7" : {"size": 4, "type": "w"},
    "Prob8" : {"size": 4, "type": "w"},
    "Prob9" : {"size": 4, "type": "w"},
    "Prob10" : {"size": 4, "type": "w"}
}

def uniqueitems_bin_to_tsv(byte_in):
    # '05 00 00 00' --> bin(5) --> 00\t  01\t  00\t  01\t
    # default to signed numbers
    string_bits = '{0:04b}'.format(int.from_bytes(byte_in, byteorder='little'))
    return "\t".join(list(string_bits)) + "\t"

def uniqueitems_tsv_to_bin(str_in_list):
    # the reverse formatting of the above function
    # 0 1 0 1 -->  '05 00 00 00' hex
    # input is a list. e.g.  ['0', '0', '0', '1']
    int_base2 = int(''.join(str_in_list), 2)        # '0001' --> int1
    return int_base2.to_bytes(4, byteorder='little')

# row size 332 bytes
UniqueItems_struct = {
    "unknown" : {"size": 2, "type": "w"}, # w for WORD, DWORD  -- this type uses int.from_bytes()
    "index" : {"size": 34, "type": "c"},  # c for char         -- this uses bytes.decode()
    "version": {"size": 4, "type": "w"},
    "code": {"size": 4, "type": "c"},

    # this DWORD represents 4 columns (ladder, carry1, nolimit, enabled)
    "itemflags": {"size": 4, "type": "w",
                  "expand_to_cols": ["ladder", "carry1", "nolimit", "enabled"],
                  "bin_to_tsv_format": uniqueitems_bin_to_tsv,
                  "tsv_to_bin_format": uniqueitems_tsv_to_bin,},

    "rarity": {"size": 4, "type": "w"},
    "lvl": {"size": 2, "type": "w"},
    "lvl_req": {"size": 2, "type": "w"},

    "chartransform": {"size": 1, "type": "w"},
    "invtransform": {"size": 1, "type": "w"},
    "flippyfile": {"size": 32, "type": "c"},
    "invfile": {"size": 34, "type": "c"},

    "cost_mult": {"size": 4, "type": "w"},
    "cost_add": {"size": 4, "type": "w"},
    "dropsound": {"size": 2, "type": "w"},
    "usesound": {"size": 2, "type": "w"},
    "dropsfxframe": {"size": 4, "type": "w"},

    "prop1": {"size": 4, "type": "w"},
    "par1": {"size": 4, "type": "w"},
    "min1": {"size": 4, "type": "w"},
    "max1": {"size": 4, "type": "w"},
    "prop2": {"size": 4, "type": "w"},
    "par2": {"size": 4, "type": "w"},
    "min2": {"size": 4, "type": "w"},
    "max2": {"size": 4, "type": "w"},
    "prop3": {"size": 4, "type": "w"},
    "par3": {"size": 4, "type": "w"},
    "min3": {"size": 4, "type": "w"},
    "max3": {"size": 4, "type": "w"},
    "prop4": {"size": 4, "type": "w"},
    "par4": {"size": 4, "type": "w"},
    "min4": {"size": 4, "type": "w"},
    "max4": {"size": 4, "type": "w"},
    "prop5": {"size": 4, "type": "w"},
    "par5": {"size": 4, "type": "w"},
    "min5": {"size": 4, "type": "w"},
    "max5": {"size": 4, "type": "w"},
    "prop6": {"size": 4, "type": "w"},
    "par6": {"size": 4, "type": "w"},
    "min6": {"size": 4, "type": "w"},
    "max6": {"size": 4, "type": "w"},
    "prop7": {"size": 4, "type": "w"},
    "par7": {"size": 4, "type": "w"},
    "min7": {"size": 4, "type": "w"},
    "max7": {"size": 4, "type": "w"},
    "prop8": {"size": 4, "type": "w"},
    "par8": {"size": 4, "type": "w"},
    "min8": {"size": 4, "type": "w"},
    "max8": {"size": 4, "type": "w"},
    "prop9": {"size": 4, "type": "w"},
    "par9": {"size": 4, "type": "w"},
    "min9": {"size": 4, "type": "w"},
    "max9": {"size": 4, "type": "w"},
    "prop10": {"size": 4, "type": "w"},
    "par10": {"size": 4, "type": "w"},
    "min10": {"size": 4, "type": "w"},
    "max10": {"size": 4, "type": "w"},
    "prop11": {"size": 4, "type": "w"},
    "par11": {"size": 4, "type": "w"},
    "min11": {"size": 4, "type": "w"},
    "max11": {"size": 4, "type": "w"},
    "prop12": {"size": 4, "type": "w"},
    "par12": {"size": 4, "type": "w"},
    "min12": {"size": 4, "type": "w"},
    "max12": {"size": 4, "type": "w"}
}

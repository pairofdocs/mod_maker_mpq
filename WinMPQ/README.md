## WinMPQ Tool from Shadowflare
from https://sfsrealm.hopto.org/downloads/WinMPQ.html

## Install
Visual Basic 4 runtime files: run `WinMPQ\Vbr4\setup.exe`

Runtime Files Pack 3: run `WinMPQ\RunPack3\setup.exe`

## Usage
To add a .bin file to a target mpq: go to folder `py_converter\WinMPQ` and shift+right click `Open Powershell window here` then run in powershell
```
.\WinMPQ.exe add .\my_mpq\Patch_D2.mpq ..\BinFilesModded\DifficultyLevels.bin data\global\excel\DifficultyLevels.bin
```

where a folder `my_mpq` contains the target Patch_D2 mpq and DifficultyLevels.bin is, for example, the name of a modded .bin file in folder `py_converter\BinFilesModded`

The template for using WinMPQ'a `add` command is:

```
WinMPQ.exe add <MPQFile> <SourceFile> [DestinationFilePath In the MPQ]
```

## Usage in a Script
Windows batch file `add_all_bins_to_mpq.bat`

```
for %%i in (..\BinFilesModded\*) do (
    .\WinMPQ.exe add .\my_mpq\Patch_D2.mpq ..\BinFilesModded\%%~nxi data\global\excel\%%~nxi
)
```

Double clicking or executing `add_all_bins_to_mpq.bat` adds all .bin files from `BinFilesModded\` into `my_mpq\Patch_D2.mpq`


## Documentation
`WinMPQ\WinMPQ.rtf`

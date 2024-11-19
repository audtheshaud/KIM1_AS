# KIM1_AS
This is a project to create a VS Code environment for ECE 287: KIM-1 Design Project

## Installion and Use of Python Script:
### Prerequisites: 
1. Install the Retroassembler VS Code extension
2. Download the current Retroassembler version from https://enginedesigns.net/retroassembler/ and unzip
3. Set the file path of the retroassembler.exe or retroassembler.dll in VS Code extension settings for Retroassembler by going to VS Code's settings and searching Retroassembler
4. Follow this guide from Retroassembler to install .NET Runtime/SDK https://enginedesigns.net/post/2021/01/how_to_install_dotnet_on_linux_and_macos/

### Using the Python Script:
1. Download the Python Script from this Repository by clicking the file and choosing download RAW file in the top right of the file viewer
2. Place this file into the same folder as where you are writing your assembly code file
3. Make sure your Assembly code file is named *(Your file name)*.6502.asm
4. Open a terminal in VS Code
5. Run Retroassembler on Windows by doing this: *(Your File path)*\retroassembler.exe -O=txt *(Your File path)*\*(Your file name)**.6502.asm
   On MacOS and Linux run Retroassembler by doing this: dotnet *(Your File path)*/retroassembler.dll -O=txt *(Your File path)*/*(Your file name)*.6502.asm
6. Now run the KIM1_TXT2HEX.py
7. Copy the generated ouput from the VS Code Terminal

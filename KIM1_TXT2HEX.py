'''
Adrian Nelson ECE 287 Intel Hex Formatter for KIM-1 Development Board 11/19/2024

'''

print('''
This program is an Intel Hex Formatter that uses the text file generated by Retroassembler and translates it into
a KIM-1 Readable format. The max amount of data per line is 0x10 or 16 bytes of data. After each address, you will
notice that there is a 00 which marks the beginning of the data. The end of each line is a checksum which is the
sum of all the bytes starting from the semicolon to the last piece of data.
      ''')

input_file = input("Enter the name of the text file generated by the Retroassembler (Omit the .txt): ")
print("\n")

# Open the text file generated by Retroassembler and read the lines into the lines array, then close the file
with open(f"{input_file}.txt") as f:
    lines = f.read().splitlines()
    f.close()

# Flatten the lines into one array of arguments: The addresses and the data
args = [arg for line in lines for arg in line.split()]

# Clean the input args from the file by removing any addresses that are not % 10, this leaves 0200, 0210, 0220, etc.
i = 0
while i < len(args):
    if len(args[i]) == 4 and int(args[i]) % 10 != 0:
        args.pop(i)  # Remove invalid address
        # Do not increment i; stay at the same index to check the next element
    else:
        i += 1  # Move to the next element if no removal

# Insert 00 to mark data being input into the address of the KIM-1
i = 0
while i < len(args):
    if len(args[i]) == 4:
        args.insert(i + 1, "00")  # Insert "00" after the address
        i += 2  # Skip past the address and the newly inserted "00"
    else:
        i += 1  # Move to the next element

# Insert the number of bytes per line, it is in the range of 0x10-0x01
i = 0
while i < len(args):
    if len(args[i]) == 4:  # Check if the current item is an address
        # Calculate the number of data bytes until the next address or end of list
        start_index = i + 2  # Start counting data bytes after the address and the "00"
        end_index = min(len(args), start_index + 16)  # Max 16 bytes per line
        byte_count = end_index - start_index
        
        # If we are handling an address like 0220, it has a count excluding the "00" byte
        byte_count_marker = f":{byte_count:02X}"
        
        # Insert the marker before the address
        args.insert(i, byte_count_marker)
        i += 2  # Move past the newly inserted marker and address (skip "00")
    else:
        i += 1  # Move to the next element

lines = []
current_line = []

for arg in args:
    if arg.startswith(":") and current_line:
        # Append the completed line and start a new one
        lines.append(current_line)
        current_line = []
    current_line.append(arg)

# Append the last line if any
if current_line:
    lines.append(current_line)

for line in lines:
    checksum = 0
    byte_count = line[0]
    start_addr = line[1]
    checksum += int(byte_count[1:], 16) + int(start_addr[0:2],16) + int(start_addr[2:],16)
    for x in range(2,len(line)):
            checksum += int(line[x].upper(),16)
    checksum = (0x100 - (checksum % 0x100)) & 0xFF
    line.append(f"{checksum:02X}")

kim1_lines = ""

for line in lines:
    kim1_lines += ''.join(line).upper()  # Join the line and convert to uppercase
    kim1_lines += "\n"
    
kim1_lines += ":00000001FF"


print("Please copy and paste this formatted Intel Hex into your terminal using paste special:\n")
print(f"{kim1_lines}\n")
# Convert the input to KIM-1 sendable format
# output_data = convert_to_kim1_format(args)

# Check is pasted from ASM80's .Hex file
# check = ":10020000A9AA8D0040A2FFA0FF88D0FDCAD0F8A9FE\n:10021000558D0040A2FFA0FF88D0FDCAD0F84C0049\n:0202200002EAF0\n:00000001FF"

# print(check + "\n")

# Print the formatted output
'''if check == kim1_lines:
    print("Correct output\n")
else:
    print("Incorrect output\n")'''
def convert_to_kim1_format(args):

    kim1_intel_hex = ''''''

    origin_addr = args[2]
    line = ""
    j=17
    checksum = 16 + int(origin_addr[0:2], 16) + int(origin_addr[2:], 16)

    for x in range(1,j):
        if len(args[x]) == 2:
            line += args[x].upper()
            checksum += int(args[x],16)
        else:
            x+=1
    checksum = hex(0x100 - (checksum % 0x100))[2:].upper()
    line += checksum
    kim1_intel_hex += f"{line}\n"
    return kim1_intel_hex


# Open the text file generated by Retroassembler and read the lines into the lines array, then close the file
with open("Nov12.txt") as f:
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
        # Calculate the number of bytes until the next address or end of list
        start_index = i + 1
        end_index = min(len(args), start_index + 16)
        byte_count = end_index - start_index
        
        # Convert byte count to a two-digit hex value
        byte_count_marker = f":{byte_count:02X}"
        
        # Insert the marker before the address
        args.insert(i, byte_count_marker)
        i += 1  # Move past the newly inserted marker
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

# Output
print(f"{lines}\n")

for line in lines:
    # Extract byte count (from ':xx')
    byte_count = int(line[0][1:], 16)  # Removing the colon and converting to int
    address = int(line[1], 16)  # Address in hexadecimal

    # Split the address into high and low bytes
    address_high = address >> 8  # High byte (shift right by 8 bits)
    address_low = address & 0xFF  # Low byte (mask the lower 8 bits)

    # Extract data bytes (excluding checksum placeholder at the end of the line)
    data_bytes = [int(byte, 16) for byte in line[2:-1]]

    # Calculate checksum: byte count + address high + address low + data bytes
    checksum = byte_count + address_high + address_low + sum(data_bytes)
    checksum = (0x100 - (checksum % 0x100)) & 0xFF  # Two's complement checksum

    # Append the checksum as a two-character hex string
    line.append(f"{checksum:02X}")


# Convert the input to KIM-1 sendable format
# output_data = convert_to_kim1_format(args)

check = """
:10020000A9AA8D0040A2FFA0FF88D0FDCAD0F8A9FE
:10021000558D0040A2FFA0FF88D0FDCAD0F84C0049
:0102200002DB
:00000001FF
"""

print(check + "\n")

# Print the formatted output
print(output_data + "\n")
if check == output_data:
    print("Correct output\n")
else:
    print("Incorrect output\n")
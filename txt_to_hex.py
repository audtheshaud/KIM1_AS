def convert_to_kim1_format(args):
    origin_addr = args[0]
    print(origin_addr)
    
    line = ""
    x=2
    j=17
    (":10" + "origin_addr" + "00").join(line)
    print(origin_addr[:2])
    sum = hex(16)[2:] + hex(int(origin_addr[0:2], 16))[2:] + hex(int(origin_addr[2:], 16))[2:]
    for x in range(j):
        str(args[x]).join(line)
        sum += hex(int(str(args[x]),16))[2:].upper()
    print(sum)

    return line
        

# The input data as provided
with open("Nov12.txt") as f:
    lines = f.read().splitlines()
    f.close()
# Split each line into arguments and flatten into a single list
args = [arg for line in lines for arg in line.split()]

# Convert the input to KIM-1 sendable format
print(args)

output_data = convert_to_kim1_format(args)

check = """
:10020000A9AA8D0040A2FFA0FF88D0FDCAD0F8A9FE
:10021000558D0040A2FFA0FF88D0FDCAD0F84C0049
:0102200002DB
:00000001FF
"""

print(check)
print("\n")

# Print the formatted output
print(output_data + "\n")
if check == output_data:
    print("Correct output\n")
else:
    print("Incorrect output\n")


'''
# Clean and split the input text into rows of hex bytes
    hex_lines = lines

    # Initialize an empty list to store formatted lines
    kim1_lines = []
    
    # Start with the provided origin address
    org = int(args[0], 16)  # Treat the first argument as hex
    
    for arg in hex_lines:
        # Remove spaces and concatenate the hexadecimal bytes
        hex_data = arg.replace(" ", "")
        
        # Calculate the length of the data in this line (each pair of hex digits is 1 byte)
        length = len(hex_data) // 2  # Divide by 2 since each byte is represented by 2 hex digits
        
        # Prepare the line in the KIM-1 format with explicit length
        formatted_line = f":{length:02X}{org:04X}{hex_data.upper()}"
        
        # Calculate checksum as the sum of the bytes (excluding the checksum byte)
        checksum = 0
        for i in range(1, len(formatted_line), 2):  # Start at 1 to skip the ':' character
            checksum += int(formatted_line[i:i+2], 16)
        
        checksum = checksum % 256
        checksum = (256 - checksum) % 256  # Two's complement to get the correct checksum
        
        formatted_line += f"{checksum:02X}"
        
        # Add this formatted line to the list
        kim1_lines.append(formatted_line)
        
        # Increment address for next data block
        org += length
    
    # Add the final line to mark the end
    kim1_lines.append(":00000001FF")
    
    # Join all lines into a single string with newlines
    return "\n".join(kim1_lines)

'''
def convert_to_kim1_format(args):

    kim1_intel_hex = ''''''

    origin_addr = args[0]
    line = ""
    j=18
    line += f":10{origin_addr}00"
    checksum = 16 + int(origin_addr[0:2], 16) + int(origin_addr[2:], 16)

    for x in range(1,j):
        if len(args[x]) == 2:
            line += args[x].upper()
            checksum += int(args[x],16)
        else:
            x+=1
        if(x==j):
            checksum = hex(0x100 - (checksum % 0x100))[2:].upper()
            line += checksum
            kim1_intel_hex += f"{line}\n"
            origin_addr =
            break
    return kim1_intel_hex


# The input data as provided
with open("Nov12.txt") as f:
    lines = f.read().splitlines()
    f.close()

# Extract the address and data from the lines
args = [arg for line in lines for arg in line.split()]

# Convert the input to KIM-1 sendable format
output_data = convert_to_kim1_format(args)

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
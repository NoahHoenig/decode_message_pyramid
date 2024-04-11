def decode(message_file):
    position = 0
    step = 1
    result = ""
    with open(message_file,'r') as file:
        line_list = file.readlines()
        
    line_list.sort(key=lambda x: int(x.split()[0]))
        
    while position < len(line_list):
        step += 1
        result += line_list[position].split()[1] + " "
        position += step
    return result[:-1]
        
print(decode("coding_qual_input.txt"))


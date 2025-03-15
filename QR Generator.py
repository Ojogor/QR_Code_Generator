def converter(string):
    binary_array=[]
    for char in string:
        binary_array.append(format(ord(char), '08b'))
    return " ".join(binary_array)
string = "www.google.com"
binary_list = converter(string)
for binary in binary_list:
    row_output = ""
    for bit in binary:
        if bit == "1":
            row_output += u"\u25A0"
        elif bit == "0":
            row_output += " "      
    print(row_output)
def qr_mode(mode):
    if mode == "numeric":
        return "0001"
    elif mode == "alphanumeric":
        return "0010"
    elif mode == "byte":
        return "0100"
    elif mode == "kanji":
        return "1000"
    else:
        return "0010"
def qr_character_count(string):
    return format(len(string), '08b')

string = "www.google.com"
mode = "alphanumeric"
print(qr_mode(mode))
print(qr_character_count(string))
binary_list = converter(string)
mode = "alphanumeric"
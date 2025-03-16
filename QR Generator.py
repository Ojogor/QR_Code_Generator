import matplotlib.pyplot as plt
import numpy as np
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


G = np.zeros((25,25,3))

def draw_square(starting_pos, length, color):
    for i in range(length):
        if(starting_pos[1]>=0):
            G[starting_pos[0]+i] [starting_pos[1]] = color
        if(starting_pos[1]+length<=25):
            G[starting_pos[0]+i] [starting_pos[1]+length-1] = color
        if(starting_pos[0]>=0):
            G[starting_pos[0]] [starting_pos[1]+i] = color
        if(starting_pos[0]+length<=25):
            G[starting_pos[0]+length-1] [starting_pos[1]+i] = color

draw_square((1,1), 5, [1, 1, 1])
draw_square((1,19), 5, [1, 1, 1])
plt.matshow(G)
plt.show()
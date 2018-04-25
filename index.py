#!/usr/bin/Python3

import binascii
from PIL import Image
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

img = Image.open("testImage.png")
pxl = img.load()

beginning_of_text = 12 #This is set to 12 so that when right_most is taken to start entering text into image, it will start at the correct position.
beginning_of_number = 11 # This will allow the number defining the length of the text to start at the right_most - 11th pixel

string_to_use = "Fluffer puppers3!"
string_size = len(string_to_use)
string_size_bin = str(bin(string_size))
converted_string = str(bin(string_size))
#conv_string_tot = bin(string_to_use)

right_most, bottom = img.size

j = len(string_size_bin) - 1
i = right_most
text_length = ""
cnt = 0
for i in range ((right_most-1),(right_most-12),-1):
    text_length += str(pxl[i,(bottom-1)][0]%2)
    text_length += str(pxl[i,(bottom-1)][1]%2)
    text_length += str(pxl[i,(bottom-1)][2]%2)
    #print(i,bottom-1,(pxl[i,(bottom-1)][0]%2),(pxl[i,(bottom-1)][1]%2),(pxl[i,(bottom-1)][2]%2))
#print(text_length)
text_length_bin = ((int(text_length,base = 2)))/2
#print(text_length_bin)
text_len_utf = (text_length_bin)

act_str = ""
full_txt= ""
letter = ""
act_txt = ""
act_let = ""

for i in range (right_most-12, -1, -1):
    #print(i,bottom-1)
    if (cnt < text_len_utf):
        act_str += str((pxl[i,(bottom-1)][0])%2)
        cnt+=1
        if (cnt < text_len_utf):
            act_str += str((pxl[i,(bottom-1)][1])%2)
            cnt+=1
            if (cnt < text_len_utf):
                act_str += str((pxl[i,(bottom-1)][2])%2)
                cnt+=1

bot = bottom - 2

for k in range (bot,-1,-1):
    for i in range ((right_most - 1),-1,-1):
            #print(i,k)
            if (cnt < text_len_utf):
                act_str += str((pxl[i,k][0])%2)
                cnt+=1

                if (cnt < text_len_utf):
                    act_str += str((pxl[i,k][1])%2)
                    cnt+=1
                    if (cnt < text_len_utf):
                        act_str += str((pxl[i,k][2])%2)
                        cnt+=1

#print(text_len_utf, cnt, len(act_str), cnt/8)

it = 0
for l in range (0,(len(act_str))):

    letter += (act_str[l])
    it = it+1
    #print(it)
    if(it == 8):
        rdy = (int(letter,2))
        #print(chr(rdy))

        act_let = chr(rdy)
        #print(letter , act_let)
        full_txt += act_let
        letter=""
        it = 0


print("The secret message is: ",full_txt)


'''
#print(string_size_bin[1])
right_most, bottom = img.size

j = len(string_size_bin) - 1
i = right_most
for i in range ((right_most-1),(right_most-12), -1):

    if j > 1:
        color = tuple(pxl[i,bottom-1])
        r, g, b = color
        #This will clear the bits and make the lsb 0.
        r >> 1
        r << 1
        g >> 1
        g << 1
        b >> 1
        b << 1

        #print("This processing the r string: ", bottom-1, i, int(string_size_bin[j]))
        b += int(string_size_bin[j])
        j -=1
        if j > 1:
            #print("This processing the g string: ", bottom-1, i, int(string_size_bin[j]))
            g += int(string_size_bin[j])
            j -=1

            if j > 1:
                #print("This processing the b string: ", bottom-1, i, int(string_size_bin[j]))
                r += int(string_size_bin[j])
                pxl[i,bottom-1] = (r,g,b)
                #img[i,bottom-1] = pxl[i,bottom-1]
                j -=1

            else:
                pxl[i,bottom-1] = (r,g,b)
                #img[i,bottom-1] = pxl[i,bottom-1]


        else:
            pxl[i,bottom-1] = (r,g,b)
            #img[i,bottom-1] = pxl[i,bottom-1]
            #print("This processing the string: ", bottom-1, i)
    else:
        color = tuple(pxl[i,bottom-1])
        r, g, b = color
        r >> 1
        r << 1
        g >> 1
        g << 1
        b >> 1
        b << 1
        pxl[i,bottom-1] = (r,g,b)
        #img[i,bottom-1] = pxl[i,bottom-1]
        #print('r: ',pxl[i,bottom-1][0],"g: ",pxl[i,bottom-1][1],"b: ",pxl[i,bottom-1][2], i)

i = right_most
for i in range ((right_most-1),(right_most-12), -1):
    print(i, 'r: ',pxl[i,bottom-1][0],"g: ",pxl[i,bottom-1][1],"b: ",pxl[i,bottom-1][2])
    '''
print (string_to_use, string_size, "This is a garbage line to show that the program actually got this far.", right_most, bottom)

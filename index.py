#!/usr/bin/Python3

from PIL import Image

img = Image.open("Mario_meme.jpg")
pxl = img.load()

beginning_of_text = 12 #This is set to 12 so that when right_most is taken to start entering text into image, it will start at the correct position.
beginning_of_number = 11 # This will allow the number defining the length of the text to start at the right_most - 11th pixel

string_to_use = "security is fun"
string_size = len(string_to_use)#This will be used to encode the text into the image.
string_size_bin = str(bin((string_size*16)+1))
conv_string_len = len(str(bin(string_size)))
if string_size_bin.startswith("0b"):
        string_size_bin = string_size_bin[2:]
for i in range (conv_string_len,31):
    string_size_bin = "0" + string_size_bin
conv_string_len = len(string_size_bin)


right_most, bottom = img.size

#beginning of encode()

#encode text length

j = 0
for i in range ((right_most-1),(right_most-12),-1):

    color = tuple(pxl[i,bottom-1])
    r, g, b = color

    #This will clear the bits and make the lsb 0.
    if ((pxl[i,(bottom-1)][0]%2) == 1):
        r -= 1
    if ((pxl[i,(bottom-1)][1]%2) == 1):
        g -= 1
    if ((pxl[i,(bottom-1)][2]%2) == 1):
        b -= 1

    if j < conv_string_len:
        r += int(string_size_bin[j])
        j += 1

        if j < conv_string_len:
            g += int(string_size_bin[j])
            j += 1

            if j < conv_string_len:
                b += int(string_size_bin[j])
                pxl[i,bottom-1] = (r,g,b)
                j += 1

            else:
                pxl[i,bottom-1] = (r,g,b)

        else:
            pxl[i,bottom-1] = (r,g,b)
    else:
        pxl[i,bottom-1] = (r,g,b)

#end encode text length

#Begin code insertion
cnt = 0
en_st =""
for i in range (0,string_size):
    tString = bin(ord(string_to_use[i]))
    if tString.startswith("0b"):
        tString = tString[2:]

    tString = str(tString).zfill(8)
    en_st += tString

for i in range (right_most-12, -1, -1):

    color = tuple(pxl[i,bottom-1])
    r, g, b = color

    if ((pxl[i,(bottom-1)][0]%2) == 1):
        r -= 1
    if ((pxl[i,(bottom-1)][1]%2) == 1):
        g -= 1
    if ((pxl[i,(bottom-1)][2]%2) == 1):
        b -= 1

    if (cnt < (len(en_st)-1)):
        if (en_st[cnt] == "1"):
            r += 1
            cnt += 1
        else:
            cnt+=1

        if (cnt < (len(en_st)-1)):
            if (en_st[cnt] == "1"):
                g += 1
                cnt += 1
            else:
                cnt+=1

            if (cnt < (len(en_st)-1)):
                if (en_st[cnt] == "1"):
                    b += 1
                    cnt += 1
                else:
                    cnt+=1

    pxl[i,bottom-1] = (r,g,b)

bot = bottom - 2

for k in range (bot,-1,-1):
    for i in range ((right_most - 1),-1,-1):
            color = tuple(pxl[i,k])
            r, g, b = color
            if ((pxl[i,k][0]%2) == 1):
                r -= 1
            if ((pxl[i,k][1]%2) == 1):
                g -= 1
            if ((pxl[i,k][2]%2) == 1):
                b -= 1

            if (cnt < (len(en_st)-1)):
                if (en_st[cnt] == "1"):
                    #print("r",i,k,"before",r)
                    r += 1
                    #print("r",i,k,"after",r)
                    cnt += 1
                else:
                    cnt+=1

                if (cnt < (len(en_st)-1)):
                    if (en_st[cnt] == "1"):
                        g += 1
                        cnt += 1
                    else:
                        cnt+=1

                    if (cnt < (len(en_st)-1)):
                        if (en_st[cnt] == "1"):
                            b += 1
                            cnt += 1
                        else:
                            cnt+=1

            pxl[i,k] = (r,g,b)

#end of endcode()


#beginning of decode()
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

            if (cnt < text_len_utf):
                act_str += str((pxl[i,k][0])%2)
                cnt+=1

                if (cnt < text_len_utf):
                    act_str += str((pxl[i,k][1])%2)
                    cnt+=1
                    if (cnt < text_len_utf):
                        act_str += str((pxl[i,k][2])%2)
                        cnt+=1

it = 0
for l in range (0,(len(act_str))):

    letter += (act_str[l])
    it = it+1

    if(it == 8):
        rdy = (int(letter,2))


        act_let = chr(rdy)

        full_txt += act_let
        letter=""
        it = 0
#end of decode()

print("The secret message is: ",full_txt)

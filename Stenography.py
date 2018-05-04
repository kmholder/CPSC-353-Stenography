from PIL import Image

def encode(rImage):
	#encode(rImage) preprocessing work
    img = Image.open(rImage+".jpg")
    pxl = img.load()
    txt_file = open("Stenography.py","r")

    string_to_use = txt_file.read()
    string_size = len(string_to_use)#This will be used to encode the text into the image.

    string_size_bin = str(bin((string_size*16)+1)) #This will allow the encoded string size to match that of the length of the string in binary.
    conv_string_len = len(str(bin(string_size)))
    if string_size_bin.startswith("0b"):
        string_size_bin = string_size_bin[2:] #This removes "0b" from the string.
    for i in range (conv_string_len,31):
        string_size_bin = "0" + string_size_bin #This will prepend the string so that the correct lenght is inserted into the image.
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

		#This will set the bits that are being encoded.
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

            pxl[i,k] = (r,g,b)
    img.save(rImage+".png")
#end of endcode()

def decode(rImage):
    img = Image.open(rImage)
    pxl = img.load()
    right_most, bottom = img.size
    #beginning of decode()

    text_length = ""
    cnt = 0
    for i in range ((right_most-1),(right_most-12),-1):
        text_length += str(pxl[i,(bottom-1)][0]%2)
        text_length += str(pxl[i,(bottom-1)][1]%2)
        text_length += str(pxl[i,(bottom-1)][2]%2)

    text_length_bin = ((int(text_length,base = 2)))/2
    text_len_utf = (text_length_bin)

    act_str  = "" #This is used for the string in bits.
    full_txt = "" #This is used for the text version of the string.
    letter   = "" #This is used to keep track of the letter in binary as it is being created by every 8 bits being read in.
    act_let  = "" #This will hold the actual ascii letter to be added to full_txt.

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

    print ("The secret message is:") 
    print (full_txt)
	#end of decode()

# CPSC-353-Stenography

This program can store and read text hidden in an image starting from the bottom right pixel.
This is done by storing the length of the text in bits in the last eleven pixels
and the text in the remaining pixels.
The text will be written from the bottom right-most corner (starting with the 12th to last pixel) to the
top left-most corner.

Running this program:

    1. Download repository
    2. Navigate to repository in terminal
    3. To encode, run the following command:
        "python -c 'import index; index.encode("Mario_meme")'"
    4. To decode, run the following command:
        "python -c 'import index; index.decode("Mario_meme.png")'"
        
As of April 27, 2018 2:14 am: the encode and decode functions work properly and can be called through the command line.

# CPSC-353-Stenography

This program can store and read text hidden in an image starting from the bottom right pixel.
This is done by storing the length of the text in bits in the last eleven pixels
and the text in the remaining pixels.
The text will be written from the bottom right-most corner (starting with the 12th to last pixel) to the
top left-most corner.

As of April 26, 2018 12:31 am: the encode and decode functions work properly

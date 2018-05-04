# CPSC-353-Stenography
# Keenan Holder
# CWID:891048423

This program can store and read text hidden in an image starting from the bottom right pixel.
This is done by storing the length of the text in bits in the last eleven pixels
and the text in the remaining pixels.
The text will be written from the bottom right-most corner (starting with the 12th to last pixel) to the
top left-most corner.


Running this program:

    1. Download the repository.
    2. Navigate to the repository in terminal
	3. Install Python and Python pillow if it has not been previously installed.
    3. To encode, run the following command:
        python -c 'import Stenography; Stenography.encode("forest")'

		#forest.jpg is the file used in the testing of this program. Any file can be used as long as its extention is .jpg. When typing the function into terminal, exclude ".jpg" from the command, as the program will append it.
		# forest provided by: https://www.pexels.com/photo/road-landscape-nature-forest-39811/

    4. To decode, run the following command:
        
		python -c 'import Stenography; Stenography.decode("forest.png")'
 
		#As mentioned above, forest.jpg, as well as the encoded foret.png are the files used for testing this program. Any file can be read as long as its extension is .png. Note: ".png" is required here to be sure to distinguish the files.


Implemenation notes:

	- The python file was opened and read in to create the string with source code to be encoded.

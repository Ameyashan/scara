#!/usr/bin/python

from sys import argv
import zbar
from PIL import Image
import image_generator as img
LETTER=['None']*20
number_of_images=20


#if len(argv) < 2: exit(1)

# create a reader
def check_letter():
	print 'entering check letter'

	scanner = zbar.ImageScanner()

	# configure the reader
	#scanner.parse_config('enable')

	# obtain image data
	#pil = Image.open(argv[1]).convert('L'
	img.image_gen(number_of_images) #call image_generator
	for i in range(number_of_images):
		pil=Image.open(img.IMAGE_SAVING_PATH + 'test_image' + str(i) + ".png").convert('L')
		#pil = Image.open("C:\Users\Akash\Desktop\zbar-0.10\\test\\barcode.png")
		width, height = pil.size
		raw = pil.tobytes()

		# wrap image data
		image = zbar.Image(width, height, 'Y800', raw)
		#print(image)

		# scan the image for barcodes
		scanner.scan(image)

		# extract results
		print (i)

		for symbol in image:
			# do something useful with results
			#print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
			LETTER[i]=symbol.data


	return LETTER
# clean up
# del(image)
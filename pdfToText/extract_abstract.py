import os.path
import sys
pdf = 'd.pdf'

os.system('python "storing pic of first page of pdf.py" '+pdf)

if os.path.exists('out.jpg') == False :
	print("Error in taking pic of the first page of the pdf")
	sys.exit()


os.system('python "drawing boxes and storing.py"')

if os.path.exists('img_1.jpg') == False :
	print("Error in Drawing bounding box")
	sys.exit()


os.system('python "recognize text from image.py"')	
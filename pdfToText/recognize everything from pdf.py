from PIL import Image
import pytesseract
import sys


filelimit = int(sys.argv[1])

outfile = "out_text.txt"
f=open(outfile, "a")
for i in range(1,filelimit+1):
	
	filename = "out_"+str(i)+".jpg"
		
	text = str(((pytesseract.image_to_string(Image.open(filename)))))

	text = text.replace('—\n', '')
	text = text.replace('-\n', '')
	#text = text.replace('\n', ' ')

	
	
	

	final = text
	f.write(final)
f.close()

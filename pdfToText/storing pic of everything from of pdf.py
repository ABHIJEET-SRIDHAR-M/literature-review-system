from pdf2image import convert_from_path
import sys
import os


file = sys.argv[1]
pages = convert_from_path(file, 500)
i=1

for page in pages:
    filename = "out_"+str(i)+".jpg"
    page.save(filename, 'JPEG')
    i = i + 1	

i-=1

os.system('python3 "recognize everything from pdf.py" ' + str(i))

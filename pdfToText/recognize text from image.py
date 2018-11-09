from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
text = str(((pytesseract.image_to_string(Image.open('img_1.jpg'))).encode('utf-8')))
text = text.replace('-\\n', '')
text = text.replace('\\n', ' ')


f=open("abstract.txt", "r+")
f.write(text[2:len(text)-1])

f.close()

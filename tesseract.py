'''This is an optical character recognition tool to be used by businesses in converting physical sign up sheets to digital
records. Google tesseract pyhton wrapper is used for this implementation.'''

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

print(pytesseract.image_to_string(Image.open('test2.jpg')))

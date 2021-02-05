# install pip3 via command - sudo apt install pip3
# install PyPDF2 via command - pip install PyPDF2
# importing required modules 
import PyPDF2 
  
# creating a pdf file object 
# Enter filename instead of Your_filename.pdf
pdfFileObj = open('Your_fliename.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
print(pdfReader.numPages) 
  
# creating a page object 
pageObj = pdfReader.getPage(0) 
  
# extracting text from page 
print(pageObj.extractText()) 
  
# closing the pdf file object 
pdfFileObj.close() 
# Save this file in the folder in which your pdf is saved 

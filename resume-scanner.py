import PyPDF2 
import re
    
# creating a pdf file object 
pdfFileObj = open('resume.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

numPages = pdfReader.getNumPages()
# printing number of pages in pdf file 
print(pdfReader.numPages) 
    
# creating a page object 
page = pdfReader.getPage(0) 
    
# extracting text from page 
page_content = page.extractText()
#print(page_content.encode('utf-8'))

prog = re.compile("\s*(Name|name|nick).*")
result = prog.match("Name: James Loh")

if result:
    print (result.group(0))

result = prog.match("University: Rice")

if result:
    print (result.group(0))

page_content.splitlines()

    
# closing the pdf file object 
pdfFileObj.close() 
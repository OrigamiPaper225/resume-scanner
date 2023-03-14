import PyPDF2 
import re
import openpyxl
import pandas as pd

wb = openpyxl.load_workbook('excel2.xlsx')
sheet_obj = wb.active
count = 1
# creating a pdf file object 
pdfFileObj = open('stanfordresume.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
numPages = pdfReader.getNumPages()
print(numPages)
print(type(numPages))
# printing number of pages in pdf file  
    
# creating a page object 
for x in range(numPages):
    page = pdfReader.getPage(count) 
    # extracting text from page 
    page_content = page.extractText()
    print(type(page_content))
    prog = re.compile("((?:http*s*[:\/\/www]*\.*)*linkedin\.com\/in\/[a-zA-Z]+\S*\/*)")
    try:
        result = prog.findall(page_content)[0]
        print(type(result))
    except:
        result = str(prog.findall(page_content))
    if result:
        print(count)
        print('LinkedIn: ' + result)
        print(type(result))
        sheet_obj['A' + str(count)].value  = result
        print(sheet_obj['A' + str(count)].value)
        wb.save('excel2.xlsx')
    else:
        sheet_obj['A' + str(count)].value  = 'No LinkedIn'
        wb.save('excel2.xlsx')
    count += 1
# result = prog.match("University: Rice")

# if result:
#     print (result.group(0))

# page_content.splitlines()

wb.save('excel2.xlsx')
wb.close()
# closing the pdf file object 
pdfFileObj.close() 
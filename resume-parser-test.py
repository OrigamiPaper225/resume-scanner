from resume_parser import resumeparse
import openpyxl
import pandas as pd
import PyPDF2 
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import regexp_tokenize
from collections import Counter
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import gensim
from gensim.corpora.dictionary import Dictionary
from gensim import corpora
from pprint import pprint
from pdfminer.high_level import extract_text

from gensim.utils import simple_preprocess
from smart_open import smart_open
import os

# extract text, use regex to find:
# match with "LinkedIn", get the next word which is a link.
# split pdf with Adobe Acrobat
# Make bash script, using move to rename to resume1-486
# make for loop search where it reads file based on count

count = 65
resumefilepath = './stanfordresumes/stanfordresume_Part' + str(count) + '.pdf'
originalresumefilepath = 'stanfordresume.pdf'
excelfilepath = 'excel2.xlsx'
separator = ' '
#modelData = pd.read_excel("MBA Book Summary 2022") # Change to my own excel model data later

#PyPDF2
pdfFileObj = open(originalresumefilepath, 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
numPages = pdfReader.getNumPages()

stopwords = nltk.corpus.stopwords.words('english')
stopwords.append('\n')



# Extract model answers
# modelName = modelData.loc['name']
# modelEducation = modelData.loc['university']
# modelDesig = modelData.loc['designition']
# modelSkills = modelData.loc['skills']

# Resume Parser


# OpenPyxl
wb = openpyxl.load_workbook(excelfilepath)
#wb = wb.to_excel("test.xlsx", engine='xlsxwriter')

sheet_obj = wb.active
all_text = []

for x in range(5):
    #Try using Index for the Excel
    resumefilepath = './stanfordresumes/stanfordresume_Part' + str(count) + '.pdf'
    #print(count)
    token = extract_text(resumefilepath)
    tokens = extract_text(resumefilepath)
    tokens2 = [r for r in word_tokenize(tokens.lower()) if r.isalpha()]
    no_stops = [t for t in tokens2 if t not in stopwords]
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
    #print(token)
    all_text.append(lemmatized)
    #print(all_text)
    count += 1
# dictionary = Dictionary(all_text)
# # dictionary = corpora.Dictionary(
# # simple_preprocess(line, deacc =True) for line in lemmatized
# # )   
# corpus = [dictionary.doc2bow(text) for text in all_text]
# print(corpus[3][:10])

count = 65

for x in range(5):
    resumefilepath = './stanfordresumes/stanfordresume_Part' + str(count) + '.pdf'
    data = resumeparse.read_file(resumefilepath)
    #print(data)
    #Add name
    name = str(data['name']).lower().capitalize()
    sheet_obj['A' + str(count)].value = name
    print(name)

    def addColumn(column, newDataColumn, splice=None, separatorStatus=False):
        if splice == None:
            columnData = data[str(column)]
        else:
            try:
                columnData = data[str(column)][int(splice)]
            except:
                columnData = data[str(column)]
        # print(column)
        print('Column Data: ' + str(columnData))
        if separatorStatus==True:
            try:
                columnName = ' '.join(str(l) for l in columnData)
            except:
                columnName = columnData
        else:
            try:
                columnName = ''.join(str(l) for l in columnData)
            except:
                columnName = columnData
        
        #print(columnName)
        try:
            capitalizedColumnName = separator.join(word[0].capitalize()+word[1:] for word in columnName.split(separator))
            sheet_obj[str(newDataColumn) + str(count)].value  = capitalizedColumnName
        except:
            sheet_obj[str(newDataColumn) + str(count)].value  = columnName
        #print('Capitalized Column Name' + capitalizedColumnName)
        
        #print(sheet_obj[str(newDataColumn) + str(count)].value)

    #Add University
    addColumn('university','B','0',False)
    # try:
    #     firstCollegeName = str(data['university'][0])
    #     new_firstCollegeName = separator.join(word[0].capitalize()+word[1:] for word in firstCollegeName.split(separator))
    #     sheet_obj['B' + str(count)].value  = new_firstCollegeName
    # except:
    #     sheet_obj['B' + str(count)].value  = str(data['university'])
    
    #Add Total Experience
    addColumn('total_exp','C')
    # sheet_obj['C' + str(count)].value = data['total_exp']

    #Add Designation
    addColumn('designition','D')
    # try:
    #     designition = str(separator.join(data['designition']))
    #     new_designition = separator.join(word[0].capitalize()+word[1:] for word in designition.split(separator))
    #     sheet_obj['D' + str(count)].value = new_designition
    # except:
    #     sheet_obj['D' + str(count)].value = str(separator.join(data['designition']))

    #Add Total Experience
    addColumn('skills','E')
    # try:
    #     skills = data[['skills']]
    #     new_skills = separator.join(str(word[0]).capitalize()+word[1:] for word in skills.split(separator))
    #     sheet_obj['E' + str(count)].value = new_skills
    # except:
    #     #sheet_obj['E' + str(count)].value = str(data['skills'])
    #     sheet_obj['E' + str(count)].value = str(separator.join(data['skills']))
    #     #print(type(str(separator.join(data['skills']))))


    tokens = extract_text(resumefilepath)
    tokens2 = [r for r in word_tokenize(tokens.lower()) if r.isalpha()]
    no_stops = [t for t in tokens2 if t not in stopwords]
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
    bow = Counter(lemmatized)

    # dictionary = corpora.Dictionary(
    # simple_preprocess(line, deacc =True) for line in lemmatized
    # )   
    # corpus = [dictionary.doc2bow(x) for x in all_text]
    # print(corpus[4][:10])

    def skillAppend(compiler):
        try:
            compilerResult = compiler.findall(tokens)
        except:
            compilerResult = str(compiler.findall(tokens))
        if result:
            return industries.append(' '.join(compilerResult))

    prog = re.compile("((?:http*s*[:\/\/www]*\.*)*linkedin\.com\/in\/[a-zA-Z]+\S*\/*)")
    try:
        result = prog.findall(tokens)
    except:
        result = str(prog.findall(tokens))
    if result:
        sheet_obj['F' + str(count)].value  = result[0]
    else:
        sheet_obj['F' + str(count)].value  = 'No LinkedIn'
    
    industries = []

    consulting = re.compile('[cC]onsult(?:ant|ing)')
    analyst= re.compile('(?:\w+\s+)[aA]nalyst')
    engineer= re.compile('(?:\w+\s+)[eE]ngineer')
    associate= re.compile('(?:\w+\s+)[aA]ssociate')
    strategy= re.compile('(?:\w+\s+)[sS]trateg(?:y|ist)')
    product= re.compile('(?:\w+\s+)[pP]roduct\s*(?:[mM]anag(?:er|ement)|[oO]wner)')
    skillAppend(consulting)
    skillAppend(analyst)
    skillAppend(engineer)
    skillAppend(associate)
    skillAppend(strategy)
    skillAppend(product)
    
    # founder= re.compile('\w*\s*\w*-*[fF]ounder')
    # CEO= re.compile('CEO')
    print(industries)
    
    sheet_obj['G' + str(count+1)].value  = str(', '.join(industries))
    count += 1
    print(count)
    wb.save(excelfilepath)
wb.save(excelfilepath)





#Other Universities
# secondCollegeName = str(data['university'][1])
# new_secondCollegeName = separator.join(word[0].capitalize()+word[1:] for word in secondCollegeName.split(separator))
# sheet_obj['D' + str(count)].value  = new_secondCollegeName

# thirdCollegeName = str(data['university'][2])
# new_thirdCollegeName = separator.join(word[0].capitalize()+word[1:] for word in thirdCollegeName.split(separator))
# sheet_obj['E' + str(count)].value  = new_thirdCollegeName

wb.save(excelfilepath)
wb.close()

print(data)

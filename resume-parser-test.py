from resume_parser import resumeparse
import openpyxl

count = 1
resumefilepath = 'resume.pdf'
excelfilepath = 'excel.xlsx'
separator = ' '

data = resumeparse.read_file(resumefilepath)
print(data['name'])
wb = openpyxl.load_workbook(excelfilepath)
sheet_obj = wb.active

#Add name
sheet_obj['A' + str(count)].value = data['name']
#Add University
firstCollegeName = str(data['university'][0])
new_firstCollegeName = separator.join(word[0].capitalize()+word[1:] for word in firstCollegeName.split(separator))
print(new_firstCollegeName)

sheet_obj['B' + str(count)].value  = new_firstCollegeName

#Add Total Experience
sheet_obj['C' + str(count)].value = data['total_exp']

#Add Designation
designition = str(separator.join(data['designition']))
new_designition = separator.join(word[0].capitalize()+word[1:] for word in designition.split(separator))
sheet_obj['D' + str(count)].value = new_designition

#Add Total Experience
skills = str(data['skills'])
new_skills = separator.join(word[0].capitalize()+word[1:] for word in skills.split(separator))
sheet_obj['E' + str(count)].value = new_skills

#sheet_obj['E' + str(count)].value = separator.join(data['skills'])



#Other Universities
# secondCollegeName = str(data['university'][1])
# new_secondCollegeName = separator.join(word[0].capitalize()+word[1:] for word in secondCollegeName.split(separator))
# print(new_secondCollegeName)
# sheet_obj['D' + str(count)].value  = new_secondCollegeName

# thirdCollegeName = str(data['university'][2])
# new_thirdCollegeName = separator.join(word[0].capitalize()+word[1:] for word in thirdCollegeName.split(separator))
# print(new_thirdCollegeName)
# sheet_obj['E' + str(count)].value  = new_thirdCollegeName

wb.save(excelfilepath)
wb.close()

print(data)

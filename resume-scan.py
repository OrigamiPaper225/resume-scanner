from pdfminer.high_level import extract_text
import docx2txt
import nltk

# def extract_text_from_pdf(pdf_path):
#     return extract_text(pdf_path)

# if __name__ == '__main__':
#     print(extract_text_from_pdf('./resume.pdf'))  # noqa: T001

text = extract_text('stanfordresume.pdf')
print(repr(text))

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
 
 
# def extract_text_from_docx(docx_path):
#     txt = docx2txt.process(docx_path)
#     if txt:
#         return txt.replace('\t', ' ')
#     return None
 
 
# def extract_names(txt):
#     person_names = []
 
#     for sent in nltk.sent_tokenize(txt):
#         for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
#             if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
#                 person_names.append(
#                     ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
#                 )
 
#     return person_names
 
 
# if __name__ == '__main__':
#     text = extract_text_from_docx('resume.docx')
#     names = extract_names(text)
 
#     if names:
#         print(names[0])  # noqa: T001
 
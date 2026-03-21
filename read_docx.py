import zipfile
import xml.etree.ElementTree as ET

try:
    with zipfile.ZipFile('C:/Users/malikjb/Downloads/Chapter_1_v2_Introduction.docx') as docx:
        tree = ET.XML(docx.read('word/document.xml'))
    paragraphs = []
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    for paragraph in tree.iter(f'{{{ns["w"]}}}p'):
        texts = [node.text for node in paragraph.iter(f'{{{ns["w"]}}}t') if node.text]
        if texts:
            paragraphs.append(''.join(texts))
            
    with open('C:/Users/malikjb/.gemini/antigravity/scratch/SDLC/chapter1_extracted.txt', 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(paragraphs))
    print("Extracted successfully with absolute path.")
except Exception as e:
    print('ERROR:', str(e))

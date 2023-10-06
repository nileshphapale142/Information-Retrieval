from bs4 import BeautifulSoup

xml_file_path = '/home/hadoop/Downloads/simplewiki-20211001-pages-articles-multistream.xml'
output_file_path = 'rough.txt'

# Create a generator expression to extract text from 'text' elements
def extract_text():
    with open(xml_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
        for p in soup.find_all('text'):
            yield p.get_text()

# Write the extracted text to the output file
with open(output_file_path, 'w', encoding='utf-8') as file:
    for text_content in extract_text():
        file.write(text_content)

print('Extraction and writing completed.')

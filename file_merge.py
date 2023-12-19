import docx
import pandas as pd
import re
import os

# 저장한 docx 파일 위치 경로 
docx_directory = 'output'

# 파일 결합할 리스트 생성 
index_list = []
text_list = []

# 리스트에 185개의 docx 파일 추가하기 
for filename in os.listdir(docx_directory):
    if filename.endswith('.docx'):
        file_path = os.path.join(docx_directory, filename)
    
        doc = docx.Document(file_path)

        # list에 존재하는 185개의 docx파일 결합 
        for x, paragraph in enumerate(doc.paragraphs):
            index_list.append(x)
            text_list.append(paragraph.text)


# Index, Text로 구성된 데이터 프레임으로 df로 설정하여 생성
df = pd.DataFrame({'Index': index_list, 'Text': text_list})

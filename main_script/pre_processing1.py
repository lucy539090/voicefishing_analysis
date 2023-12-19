import docx
import pandas as pd
import re

# 불용어 제거 과정
# 화자1, 화자2 제거 
df['Text'] = df['Text'].apply(lambda x: re.sub(r'화자 \d+ | \d+:\d+', '', x, flags=re.IGNORECASE))

# 통화 시간 제거 
df['Text'] = df['Text'].apply(lambda x: re.sub(r'\d{2}:\d{2}|\n', '', x))

# docx 파일로 변환할 때 첫번째 행에 생긴 필요없는 문구 제거 
df = df[~df['Text'].str.startswith('Evaluation Only. Created with Aspose.Words.')]
df.reset_index(drop=True, inplace=True)

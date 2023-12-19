import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import font_manager

# CSV 파일 경로 및 파일명 설정
csv_file_path = 'ytdata.csv'

# CSV 파일에서 데이터 읽기
df = pd.read_csv(csv_file_path, encoding='cp949')
column_name = 'description'

# 특정 컬럼의 값들을 하나의 문자열로 합치기
text_data = ' '.join(df[column_name].astype(str))

# 한글 폰트 설정 (맑은 고딕 폰트 사용)
font_path = "C:/Windows/Fonts/malgun.ttf"
font_prop = font_manager.FontProperties(fname=font_path)

# 워드 클라우드 생성
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    font_path=font_path  # 한글 폰트 지정
).generate(text_data)

# 워드 클라우드 시각화
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

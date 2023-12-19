# 워드 클라우드 라이브러리 불러오기
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt

# 상위 100개 단어만 추출 
top_words = text_count.most_common(100)

# 상위 100개 단어를 사전으로 생성 
wordcloud_dict = dict(top_words)

# 상위 100개 단어 사전을 기반으로 워드 클라우드 생성
wordcloud = WordCloud(font_path='NanumGothic.ttf', background_color='white', width=800, height=400, max_words=100).generate_from_frequencies(wordcloud_dict)

# 설정한 워드 클라우드 나타내기
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

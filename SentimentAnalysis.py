import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# 데이터 읽기
df = pd.read_csv('ytdata.csv', encoding='cp949')

# 감성 분석
analyzer = SentimentIntensityAnalyzer()
df['compound'] = df['description'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

# 감성 점수 시각화
plt.hist(df['compound'], bins=20, edgecolor='black')
plt.title('Distribution of Sentiment Scores')
plt.xlabel('Compound Sentiment Score')
plt.ylabel('Frequency')
plt.show()

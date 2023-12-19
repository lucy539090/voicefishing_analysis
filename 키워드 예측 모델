import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.feature_extraction.text import TfidfVectorizer

# 데이터 읽기
df = pd.read_csv('ytdata.csv', encoding='cp949')

# 특성과 타겟 설정
features = df[['title', 'author', 'publish_date', 'description']]
target = df['keywords']  # 수정 필요

# 텍스트 데이터를 벡터화
vectorizer_title = TfidfVectorizer()
X_title = vectorizer_title.fit_transform(features['title'])

vectorizer_author = TfidfVectorizer()
X_author = vectorizer_author.fit_transform(features['author'])

vectorizer_keywords = TfidfVectorizer()
X_keywords = vectorizer_keywords.fit_transform(features['keywords'])

# 데이터 결합
X_combined = pd.concat([pd.DataFrame(X_title.toarray()), pd.DataFrame(X_author.toarray()), pd.DataFrame(X_keywords.toarray())], axis=1)

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X_combined, target, test_size=0.2, random_state=42)

# 회귀 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 모델 평가
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

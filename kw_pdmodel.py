import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 데이터 로드
data = pd.read_csv("ytdata.csv", encoding='latin1')

# Features와 Labels 분리
X = data[['title', 'author', 'keywords', 'description']]
y = data[['publish_date']]

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ColumnTransformer 정의
preprocessor = ColumnTransformer(
    transformers=[
        ('title', TfidfVectorizer(), 'title'),
        ('author', TfidfVectorizer(), 'author'),
        ('keywords', TfidfVectorizer(), 'keywords'),
        ('description', TfidfVectorizer(), 'description')
    ],
    remainder='passthrough'
)

# 전체 파이프라인 구성
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', MultiOutputClassifier(RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)))
])

# 모델 학습
pipeline.fit(X_train, y_train)

# 예측
y_pred = pipeline.predict(X_test)

# 성능 평가
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_rep)

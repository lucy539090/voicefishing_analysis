# konlpy 이용하여 자연어 처리
from konlpy.tag import Okt
from collections import Counter

okt = Okt()

# 한글 정규식
df['Text'] = df['Text'].apply(lambda x: re.sub(r'[^a-zA-Zㄱ-ㅎㅏ-ㅣ가-힣\s]', '', x))

# 불용어 set 설정해서 제거 
stopwords = set(['안녕하세요', '이', '있', '하', '것', '들', '그', '되', '수', '이', '보', '않', '없', '나', '사람', '주', '아니', '등', '같', '우리', '때', '년', '가', '한', '지', '대하', '오', '말', '일', '그렇', '위하', '때문', '그것', '두'])
df['Text'] = df['Text'].apply(lambda x: ' '.join([word for word in okt.morphs(x) if word not in stopwords]))

# 필요없는 1음절 단어 제거 
df['Text'] = df['Text'].apply(lambda x: ' '.join([word for word in okt.morphs(x) if len(word) > 1 and word not in stopwords]))

# 명사 추출을 위한 과정 
# 모든 문장을 하나의 문장으로 합치기 
text_corpus = ''.join(df['Text'])

# 명사만 추출 
tagger = Okt()
nouns = tagger.nouns(text_corpus)

# 각 단어 빈도수 계산 
text_count = Counter(nouns)
print(text_count)

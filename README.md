# voicefishing_analysis

## youtube Data

- SentimentAnalysis.py
  : Pandas와 VaderSentiment 패키지를 사용하여 유튜브 크롤링 데이터에 대한 감성 분석을 수행하고, 그 결과를 히스토그램으로 시각화한다.
- dc_wordcloud.py
  : 유튜브 크롤링 데이터에서 'description'(유튜브 영상의 설명란) 열의 텍스트 데이터를 추출하여 Word Cloud를 생성하고 시각화한다.
- kw_wordcloud.py
  : 유튜브 크롤링 데이터에서 'keywords'(유튜브 영상의 핵심 키워드) 열의 텍스트 데이터를 추출하여 Word Cloud를 생성하고 시각화한다.
- kw_pdmodel.py
  : YouTube 동영상 데이터를 사용하여 날짜를 예측하는 다중 출력(MultiOutput) 분류 모델을 구축하는 파이프라인이다.

# voicefishing_analysis

## 데이터 수집 
- youtube data
  - 크롤링 통해 진행
- script data
  - 보이스피싱 사례 영상에서 음성 변환하여 185개의 doc 파일 수집

---
## 캡스톤 연계 실습을 통해 발전시킨 내용 
### Script Data 
  - Pre_processing
    - docx 파일로, 파일 형식 변환
    - 하나의 데이터 프레임으로 병합
    - 불용어 제거
    - 자연어 처리 통한 명사 추출
  - Visualization
    - 상위 100개 명사 사전 통해 워드 클라우드 

#### 파일 설명 
- doc_docx.py
    - doc파일을 docx파일로 변환 
- file_merge.py
    - 변환한 docx파일을 하나의 데이터프레임으로 병합
- pre_processing1.py
  - 병합한 데이터프레임에서 불용어 제거, 한글 정제 등 전처리 과정 진행 
- pre_processing2.py
  - 정제된 데이터를 konlpy 라이브러리를 이용해 자연어 처리 진행
  - 명사 추출 
- wordcloud.py
  - 추출된 상위 100개의 명사를 사전으로 생성하여 워드 클라우드로 시각화 진행 

- cleaned_output.csv
    - 모든 전처리를 완료한 csv 최종 파일 
- wordcloud_result
  - 상위 100개 명사를 통해 워드 클라우드 시각화 진행한 결과
- docx wordcloud
  - docx 개별 파일들을 워드 클라우드 시각화 진행

---
### youtube Data 
  - crawling
  - doc 파일 워드클라우드
  - 키워드 추출 워드클라우드
  - 감성분석
  - 키워드 예측 모델

#### 파일 설명 
- SentimentAnalysis.py
  : Pandas와 VaderSentiment 패키지를 사용하여 유튜브 크롤링 데이터에 대한 감성 분석을 수행하고, 그 결과를 히스토그램으로 시각화한다.
- dc_wordcloud.py
  : 유튜브 크롤링 데이터에서 'description'(유튜브 영상의 설명란) 열의 텍스트 데이터를 추출하여 Word Cloud를 생성하고 시각화한다.
- kw_wordcloud.py
  : 유튜브 크롤링 데이터에서 'keywords'(유튜브 영상의 핵심 키워드) 열의 텍스트 데이터를 추출하여 Word Cloud를 생성하고 시각화한다.
- kw_pdmodel.py
  : YouTube 동영상 데이터를 사용하여 날짜를 예측하는 다중 출력(MultiOutput) 분류 모델을 구축하는 파이프라인이다.




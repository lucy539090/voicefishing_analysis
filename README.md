# voicefishing_analysis
### Script Data 
- 보이스피싱 사례의 영상을 한글로 변환한 doc파일 185개 수집 

#### 발전시킨 내용 
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

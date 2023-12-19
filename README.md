# voicefishing_analysis
## 데이터 수집 
- youtube data
  - 크롤링 통해 진행
- script data
  - 보이스피싱 사례 영상에서 음성 변환하여 185개의 doc 파일 수집 

--- 
## 캡스톤 연계 실습을 통해 발전시킨 내용 
- youtube_data
  - crawling
  - doc 파일 워드클라우드
  - 키워드 추출 워드클라우드
  - 감성분석
  - 키워드 예측 모델

- script_data
  - pre_processing
    - docx 파일로, 파일 형식 변환
    - 하나의 데이터 프레임으로 병합
    - 불용어 제거
    - 자연어 처리 통한 명사 추출
  - Visualization
    - 상위 100개 명사 사전 통해 워드 클라우드  

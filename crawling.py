from pytube import YouTube
#pytube 라이브러리 호출

url = "https://www.youtube.com/watch?v=ohnDEG alG8"
#크롤링 할 유튜브 영상 url 입력

yt = YouTube(url)
#yt 변수 생성

print("title : ", yt.title)
#해당 동영상의 제목을 크롤링하여 출력
print("author : ", yt.author)
#해당 동영상의 유튜브 채널명을 크롤링하여 출력
print ("publish_date : " , yt.publish_date)
#해당 동영상의 게시 날짜를 크롤링하여 출력
print("keywords : ", yt.keywords)
#해당 동영상과 관련된 키워드를 크롤링하여 출력
print("description : ", yt.description)
#해당 동영상의 상세설명을 크롤링하여 출력

save_path = r'C:/Users/lucy5'
#csv 저장 경로 입력

#results = [[yt.title. yt.author. yt.publish_date, yt.keywords, yt.description]]

import pandas as pd
#pandas 라이브러리 호출
from csv import writer
from csv import DictWriter
#csv 모듈 불러오기, writer, DictWriter 호출

headersCSV = ['title', 'author', 'publish_date', 'keywords', 'description']
#csv 컬럼명 지정

dict = {'title' : yt.title, 'author' : yt.author, 'publish_date' : yt.publish_date, 'keyvords' : yt.keywords, 'description' : yt.description}
#csv 컬럼 지정

with open('유튜브 크롤링.csv', 'a', newline='') as f_object:
	dictwriter_object = DictWriter(f_object, fieldnames = headersCSV)
	dictwriter_object.writerow(dict)
	f_object .close()
#DictWriter 함수와 writerow 함수를 이용하여 csv 작성

print('저장 완료')
#저장 성공 시 '저장 완료' 출력

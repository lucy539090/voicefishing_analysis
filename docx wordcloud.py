from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from docx import Document

def read_docx(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + " "
    return text

def generate_wordcloud(text):
    wordcloud = WordCloud(font_path= 'NanumGothic.ttf', width=800, height=400, background_color='white').generate_from_frequencies(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def main():
    file_path = "NR3178.docx"  # 대상 파일 경로, 저 파일 name은 예시

    # Word 파일에서 텍스트 추출
    script_text = read_docx(file_path)

    # 단어 빈도수 계산
    word_counts = Counter(script_text.split())

    # 가장 많이 나오는 단어 n개 선택
    top_words = dict(word_counts.most_common(10))

    # 워드 클라우드 생성 및 출력
    generate_wordcloud(top_words)

if __name__ == "__main__":
    main()

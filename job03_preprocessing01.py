#한글, 띄어쓰기 빼고 다 버리기
#한글자, 불용어, 영어 등 다 버리기

import pandas as pd
from konlpy.tag import Okt    #terminal - pip install konlpy
import re

df = pd.read_csv('crawling_data/reviews_2021.csv')
#df.info()

#형태소 분리
okt = Okt()

#stopwords 리스트로 형태 변환
df_stopwords = pd.read_csv('./crawling_data/stopwords.csv')
stopwords = list(df_stopwords['stopword'])

# #pos
# token = okt.pos(df.reviews[0], stem=True)
# #형태소로 분리후 품사까지 알려줌(튜플형태-형태소&품사 쌍으로 묶음)
# #morphs는 형태소 분리만 해줌!(리스트형태)
# print(token)
# exit()

#한글만 남기기
cleaned_sentences = []

for review in df.reviews:
    review = re.sub('[^가-힣 ]', ' ', review)  #문자열 review에서 [가-힣]빼고 공백으로 대체
    token = okt.pos(review, stem=True)

    df_token = pd.DataFrame(token, columns=['word', 'class'])  #튜플형태 >> 컬럼 두개짜리 데이터프레임 으로 변환
    df_token = df_token[(df_token['class']=='Noun') | (df_token['class']=='Verb') | (df_token['class']=='Adjective') | (df_token['class']=='Adverb')]

    words =[]
    for word in df_token.word:
        if len(word) > 1 :
            if word not in stopwords :
                words.append(word)
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)

df['cleaned_sentences'] = cleaned_sentences
df = df[['title', 'cleaned_sentences']]
df.dropna(inplace=True)

df.to_csv('./crawling_data/cleaned_review_2021.csv', index=False)
df.info()
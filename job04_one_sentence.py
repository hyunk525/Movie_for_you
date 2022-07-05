#같은 영화 리뷰끼리 묶기

import pandas as pd

df = pd.read_csv('./crawling_data/cleaned_review_2021.csv')
df.dropna(inplace=True)

one_sentences = []

for title in df['title'].unique():
    temp = df[df['title']==title]
    if len(temp) > 30:  # 리뷰가 너무 많을 수 있으니 제한
        temp = temp.iloc[:30, :]  # 30개보다 크면 30개까지만 사용
    one_sentence = ' '.join(temp['cleaned_sentences'])
    one_sentences.append(one_sentence)
df_one = pd.DataFrame({'titles': df['title'].unique(), 'review': one_sentences})
print(df_one.head())

df_one.to_csv('./crawling_data/cleaned_review_one_2021.csv', index=False)

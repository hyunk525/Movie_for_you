import pandas as pd
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from matplotlib import font_manager, rc
import matplotlib as mpl

font_path = './malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
mpl.rcParams['axes.unicode_minus'] = False
rc('font', family=font_name)

embedding_model = Word2Vec.load('./models/word2vec_2017_2022_movies.model')

key_word = '사랑'
sim_word = embedding_model.wv.most_similar(key_word, topn=10)
print(sim_word)


vectors = []
labels = []

for label, _ in sim_word:
    labels.append(label)
    vectors.append(embedding_model.wv[label])

df_vectors = pd.DataFrame(vectors)

tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500)
new_value = tsne_model.fit_transform(df_vectors)
df_xy = pd.DataFrame({'words':labels, 'x':new_value[:, 0], 'y':new_value[:, 1]})
print(df_xy)
print(df_xy.shape)
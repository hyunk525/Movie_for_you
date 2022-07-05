# import pandas as pd
#
# df = pd.DataFrame()
# for i in range(1, 39):
#     df_temp = pd.read_csv('/crawling_2021/reviews_2021_{}page.csv'.format(i))
#     df_temp.dropna(inplace=True)
#     df_temp.drop_duplicates(inplace=True)
#     df = pd.concat([df, df_temp], ignore_index=True)
# df.drop_duplicates(inplace=True)
# df.info()
#
# my_year = 2021
# df.to_csv('./crawling_2021/reviews_{}page.csv'.format(my_year))



import glob
import pandas as pd

df = pd.DataFrame()
data_paths = glob.glob('crawling_data/MR_2021/*')

for path in data_paths:
    df_temp = pd.read_csv(path)
    df_temp.dropna(inplace=True)
    df_temp.drop_duplicates(inplace=True)
    df = pd.concat([df, df_temp], ignore_index=True)
df.drop_duplicates(inplace=True)
df.info()

my_year = 2021
df.to_csv('./crawling_data/reviews_{}.csv'.format(my_year), index=False)
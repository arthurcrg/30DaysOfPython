import pandas as pd

url = "https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/hacker_news.csv"
df = pd.read_csv(url)

print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)
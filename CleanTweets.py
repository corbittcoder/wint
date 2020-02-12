quotes = open(r"C:\Users\scttc\AppData\Local\Programs\Python\Python36-32\TrumpTweets.txt", encoding='utf-8')
contents = quotes.read()
# print(contents)
quotes.close()

##eliminate all URLS in tweets
import pandas as pd
import re
filtered = re.sub(r'^https?:\/\/.*[\r\n]*', '', contents, flags=re.MULTILINE)
df = pd.DataFrame(filtered.split('\n'), columns=['text'])
delete = 'http'
remove = df['text'].str.contains(delete)
df = df[~remove]
print(df.size)
# print(df[1:10])

#write to file
series = pd.Series(df['text'])
fname = "C:\\Users\\scttc\\PycharmProjects\\wint\\TrumpFilteredTweets.txt"
f = open(fname, 'a')
output = series.str.cat(sep='\n')
with open(fname, "w", encoding="utf-8") as f:
    f.write(output)
f.close()
# print(series.str.cat(sep='\n'))


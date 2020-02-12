quotes = open(r"C:\Users\scttc\AppData\Local\Programs\Python\Python36-32\TrumpTweets.txt", encoding='ISO-8859-1')
contents = quotes.read()
print(contents)
quotes.close()

##eliminate all URLS in tweets
import pandas as pd

print(contents.split('\n')[1])
df = pd.DataFrame(contents.split('\n'))
print(df.size)


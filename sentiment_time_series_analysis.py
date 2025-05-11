import pandas as pd
from textblob import TextBlob
import datetime
import matplotlib.pyplot as plt
from multiprocessing import Process

def get_sentiment_timeseries(comments):
    data = []
    for c in comments:
        dt = datetime.datetime.utcfromtimestamp(c.created_utc).date()
        polarity = TextBlob(c.body).sentiment.polarity
        data.append((dt, polarity))
    df = pd.DataFrame(data, columns=["date", "polarity"])
    return df.groupby("date").mean()

def create_sentiment_plot(df):
    plt.figure(figsize=(8, 4))
    plt.plot(df.index, df['polarity'], marker='o', linestyle='-', color='purple')
    plt.title("Sentiment Over Time")
    plt.xlabel("Date")
    plt.ylabel("Average Sentiment")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("static/sentiment_plot.png")

if __name__ == "__main__":
    p = Process(target=get_sentiment_timeseries)
    p.start()
    p.join()


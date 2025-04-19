from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from rake_nltk import Rake

# Sentiment analysis
vader_analyzer = SentimentIntensityAnalyzer()  # VADER initialization :contentReference[oaicite:14]{index=14}
rake = Rake()  # RAKE initialization :contentReference[oaicite:15]{index=15}

def analyze_sentiment(text):
    """Return combined VADER and TextBlob sentiment scores."""
    vader_scores = vader_analyzer.polarity_scores(text)
    tb = TextBlob(text)
    return {
        'vader': vader_scores,
        'textblob': {'polarity': tb.sentiment.polarity, 'subjectivity': tb.sentiment.subjectivity}
    }  # TextBlob usage :contentReference[oaicite:16]{index=16}

def extract_keywords(text, num_phrases=10):
    """Return top keyword phrases using RAKE."""
    rake.extract_keywords_from_text(text)
    return rake.get_ranked_phrases()[:num_phrases]  # RAKE get_ranked_phrases :contentReference[oaicite:17]{index=17}

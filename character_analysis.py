from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from rake_nltk import Rake


vader_analyzer = SentimentIntensityAnalyzer()  # VADER initialization :contentReference[oaicite:14]{index=14}
# Libary used for keyword extraction
rake = Rake()  

def analyze_sentiment(text):
    """Return combined VADER and TextBlob sentiment scores."""
    vader_scores = vader_analyzer.polarity_scores(text)
    compound_value = vader_scores['compound']
    user_polarity = ''
    if compound_value < -0.05:
        user_polarity = 'negative'
    elif compound_value <= 0.05:
        user_polarity = 'neutral'
    else:
        user_polarity = 'positive'

    tb = TextBlob(text)
    subjectivity_value = tb.sentiment.subjectivity

    if subjectivity_value < 0.3:
        user_subjectivity = "objective"
    elif 0.3 <= subjectivity_value < 0.7:
        user_subjectivity = "mixed"
    else:
        user_subjectivity = "subjective"

    return user_polarity, user_subjectivity

def get_characteristic_type_and_character(polarity, subjectivity):
    characteristics = {
        ('positive', 'objective'): ("The Idealistic Strategist", "Armin Arlert (Attack on Titan)"),
        ('positive', 'mixed'): ("The Hopeful Dreamer", "Naruto Uzumaki (Naruto)"),
        ('positive', 'subjective'): ("The Purehearted Idealist", "Tohru Honda (Fruits Basket)"),
        ('neutral', 'objective'): ("The Detached Analyst", "Saber (Fate/Stay Night)"),
        ('neutral', 'mixed'): ("The Reserved Mediator", "Ginko (Mushishi)"),
        ('neutral', 'subjective'): ("The Stoic Empath", "Violet Evergarden"),
        ('negative', 'objective'): ("The Cynical Realist", "Light Yagami (Death Note)"),
        ('negative', 'mixed'): ("The Tormented Rebel", "Eren Yeager (Attack on Titan)"),
        ('negative', 'subjective'): ("The Broken Idealist", "Homura Akemi (Madoka Magica)")
    }
    key = (polarity.lower(), subjectivity.lower())
    return characteristics.get(key, ("Unknown Type", "Unknown Character"))

def extract_keywords(text, num_phrases=30):
    rake.extract_keywords_from_text(text)
    return rake.get_ranked_phrases()[:num_phrases]  


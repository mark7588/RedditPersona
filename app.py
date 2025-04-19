from flask import Flask, render_template, request
from reddit_client import fetch_user_data
from nlp import analyze_sentiment, extract_keywords

app = Flask(__name__)  # Flask app initialization :contentReference[oaicite:18]{index=18}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        posts, comments = fetch_user_data(username)
        text_blob = " ".join([p.title for p in posts] + [c.body for c in comments])
        sentiment = analyze_sentiment(text_blob)
        keywords = extract_keywords(text_blob)
        return render_template('result.html', user=username, sentiment=sentiment, keywords=keywords)
    return render_template('index.html')  # render_template usage :contentReference[oaicite:19]{index=19}

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask server :contentReference[oaicite:20]{index=20}

from flask import Flask, render_template, request
from reddit_client import fetch_user_data
from nlp import analyze_sentiment, extract_keywords

app = Flask(__name__)  

# Render main page and the page after user submit Reddit user id
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        user, posts, comments = fetch_user_data(username)

        link_karma = user.link_karma
        comment_karma = user.comment_karma
        account_created = user.created_utc
        comments_count = len(comments)
        posts_count = len(posts)

        text_blob = " ".join([p.title for p in posts] + [c.body for c in comments])
        user_polarity, user_subjectivity = analyze_sentiment(text_blob)
        keywords = extract_keywords(text_blob)

        return render_template('result.html', comments_count = comments_count, posts_count = posts_count, 
        user = user, username = username, user_polarity = user_polarity, user_subjectivity = user_subjectivity, keywords = keywords)
    return render_template('index.html')  

if __name__ == '__main__':
    app.run(debug=True)  

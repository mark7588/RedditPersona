import praw
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT

def init_reddit():
    """Initialize PRAW Reddit client."""
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )
    return reddit  # Quick Start with PRAW :contentReference[oaicite:12]{index=12}

def fetch_user_data(username, limit=50):
    """Retrieve submissions and comments for a given Reddit user."""
    reddit = init_reddit()
    user = reddit.redditor(username)
    posts = list(user.submissions.new(limit=limit))
    comments = list(user.comments.new(limit=limit))
    
    return posts, comments  # Example pattern for user.posts/comments :contentReference[oaicite:13]{index=13}

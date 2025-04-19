# 🧠 Reddit User Analyzer

A simple and interactive web application that allows users to analyze a Reddit user's profile and activity using Reddit's API and Natural Language Processing (NLP). Built with Flask and PRAW (Python Reddit API Wrapper), the app fetches posts and comments, then applies sentiment analysis and keyword extraction to provide meaningful insights.

---

## 🚀 Purpose

The purpose of this application is to:
- Analyze the behavior, tone, and interests of a Reddit user.
- Explore sentiment trends and recurring topics in their posts and comments.
- Serve as a foundation for building more advanced Reddit data analytics tools.

This is useful for:
- Social media researchers and analysts.
- Data science and NLP learning projects.
- General Reddit users curious about content behavior.

---

## 🔍 Key Features

1. **User ID Input**  
   Users can input a Reddit username via a clean web interface.

2. **Data Retrieval via Reddit API**  
   The app uses [PRAW](https://praw.readthedocs.io/) to collect:
   - User profile metadata (karma, creation date, etc.)
   - Recent posts and comments

3. **NLP Analysis**  
   It performs:
   - **Sentiment Analysis** (using VADER or TextBlob)
   - **Keyword Extraction** (using RAKE or NLTK)

4. **Insights Display**  
   Output includes:
   - User karma stats
   - Sentiment scores (positive, neutral, negative)
   - Common keywords used
   - Account metadata and profile info

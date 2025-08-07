import feedparser
import re
import random

# RSS Feeds
espncricinfo_rss = "https://www.espncricinfo.com/rss/content/story/feeds/0.xml"
google_news_tech_rss = "https://news.google.com/rss/search?q=technology&hl=en-IN&gl=IN&ceid=IN:en"
google_news_politics_rss = "https://news.google.com/rss/search?q=politics&hl=en-IN&gl=IN&ceid=IN:en"

# Feed sources mapped to categories
rss_sources = {
    "sports": espncricinfo_rss,
    "technology": google_news_tech_rss,
    "politics": google_news_politics_rss
}

def clean_title(title):
    """Clean special characters from titles."""
    return re.sub(r'[^\w\s\-\'\",.:!?]', '', title)

def fetch_feed_articles(feed_url, category, max_items=5):
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries[:max_items]:
        title = clean_title(entry.title)
        articles.append({
            "title": title,
            "category": category
        })
    return articles

# Fetch and compile news
final_news_items = []
for category, url in rss_sources.items():
    final_news_items.extend(fetch_feed_articles(url, category))

# Optional: Shuffle for randomness
random.shuffle(final_news_items)

# Print output
for i, item in enumerate(final_news_items, 1):
    print(f"{i}. 📰 [{item['category'].capitalize()}] {item['title']}")

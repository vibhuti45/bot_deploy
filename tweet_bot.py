import tweepy

# Replace with your actual keys
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAOHe3QEAAAAA2DSLh4SQw7OqFUBYYqFL5AnT63U%3DLA1lQbIwzC6HSSZLxPIjsbt6QpCSfDmFyAWFdzsUs69PmuM04B"
API_KEY = "AlzejWTbX3V3vFYeK5i7GR0Gw"
API_SECRET = "a22ZdwdESKvwkd4klWKKzhq7d4muZpixnFthjNejhHNjyEZ6Ww"
ACCESS_TOKEN = "1953524743677595648-l5b2IEAN9oz9jyqyuTr8jAdgLAXzRN"
ACCESS_SECRET = "h4zO0m3nxFwya2waehucZJpV0ZKgI3IUCcuZ5UiCKFpRc"


# Authenticate using tweepy.Client (API v2)
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

# Post a tweet
try:
    response = client.create_tweet(text="Next post coming soon! Stay tuned for updates. 🚀")
    print("✅ Tweet posted! Tweet ID:", response.data["id"])
except Exception as e:
    print("❌ Error while posting tweet:", e)

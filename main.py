import subprocess
import google.generativeai as genai
import tweepy
import os

# === CONFIG ===
GEMINI_API_KEY = "AIzaSyA2ilH4ZcZUnxGWiuNDnpOuUCG9zvs_Gew"
genai.configure(api_key=GEMINI_API_KEY)


# === Step 1: Get Headlines from fetch_news.py ===
print("🚀 Fetching headlines...")
result = subprocess.run(["python3", "fetch_news.py"], capture_output=True, text=True)
headlines = result.stdout.strip()

# === Step 2: Prepare prompt for Gemini ===
prompt = f"""
These are the latest news headlines:

{headlines}

From these:
1. Pick top 3 important or India-related headlines
2. For each, give:
   - One-line summary
   - An image prompt idea for illustration
3. Keep the summaries concise and impactful under 50 characters each.

4. Keep the summary in line with "Summary:" and image prompt in line with "Image Prompt:" in the next line. Nothing should be in bold.

Format:
[Headline]
Summary: ...
Image Prompt: ...

"""

# === Step 3: Run Gemini ===
model = genai.GenerativeModel(model_name="gemini-2.5-pro")
response = model.generate_content(prompt)
filtered_output = response.text.strip()
print("✅ Gemini Output:\n", filtered_output)

# === Step 4: Extract text to post ===
# You can choose to post only the summaries or include the headlines too.
# For now, just tweet the summaries
# === Step 4: Extract only summaries ===
# === Step 4: Extract only summaries ===
summary_lines = []

for line in filtered_output.splitlines():
    line = line.strip()
    if line.startswith("Summary:") or line.startswith("**Summary:**"):
        summary_text = line.replace("Summary:" or "**Summary:**", "").strip()
        summary_lines.append("• " + summary_text)

tweet_text = "📰 Daily India News Digest 🇮🇳\n\n" + "\n".join(summary_lines)

print("📄 Prepared Tweet Text:\n", tweet_text)
# Truncate if over Twitter limit (280 characters)
if len(tweet_text) > 280:
    tweet_text = tweet_text[:270] + "..."

# === Step 5: Tweet ===
print("📤 Posting to X (Twitter)...")

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
    response = client.create_tweet(text=tweet_text)
    print("✅ Tweet posted! Tweet ID:", response.data["id"])
except Exception as e:
    print("❌ Error while posting tweet:", e)

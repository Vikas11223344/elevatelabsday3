import requests
from bs4 import BeautifulSoup

# Step 1: Website URL
URL = "https://www.hindustantimes.com"

# Step 2: Fetch the HTML content
response = requests.get(URL)
if response.status_code != 200:
    print(" Failed to retrieve webpage")
    exit()

# Step 3: Parse HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract headlines
# BBC often uses <h3> tags for headlines
headlines = []

for tag in soup.find_all(['h2', 'h3']):  # Search both h2 and h3
    text = tag.get_text(strip=True)
    if text and len(text) > 10:  # Ignore empty/short texts
        headlines.append(text)

# Step 5: Save the results to a text file
with open("headlines.txt", "w", encoding="utf-8") as f:
    for i, headline in enumerate(headlines, start=1):
        f.write(f"{i}. {headline}\n")

print(f"successfully {len(headlines)} headlines saved to 'headlines.txt'")

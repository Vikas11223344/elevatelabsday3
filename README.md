# Headlines Scraper (Hindustan Times) — README

A small Python script that fetches the homepage of Hindustan Times and extracts headlines from <h2> and <h3> tags, then saves them to a text file.

This README documents how to run the script, required dependencies, expected output, and recommended improvements and safety/ethics considerations for web scraping.

## Files
- headlines_scraper.py (or the script you provided) — the scraper that requests the page, parses it with BeautifulSoup, extracts headlines, and writes them to `headlines.txt`.
- headlines.txt — output file produced after running the script.

## Requirements
- Python 3.7+
- pip packages:
  - requests
  - beautifulsoup4

Install dependencies:
```
pip install requests beautifulsoup4
```

## Usage
1. Save the provided script to a file, e.g. `headlines_scraper.py`.
2. Run the script:
```
python headlines_scraper.py
```
3. On success, the script will create `headlines.txt` in the same directory containing numbered headlines, e.g.:
```
1. Headline one...
2. Headline two...
...
```
The script prints a simple summary like:
```
successfully 25 headlines saved to 'headlines.txt'
```

## Script behavior (what the script does)
- Fetches HTML from https://www.hindustantimes.com using requests.
- Parses the page with BeautifulSoup (html.parser).
- Finds all <h2> and <h3> tags and collects their text (ignores short/empty texts).
- Writes each headline as a numbered line into `headlines.txt`.
- Exits with a message if the webpage retrieval fails (non-200 response).
- Handles non-200 responses by printing " Failed to retrieve webpage" and exiting.

## Error handling and limitations
- The script currently:
  - Checks response.status_code and exits on non-200.
  - Does not handle network exceptions (requests.exceptions.RequestException).
  - Does not set a custom User-Agent header.
  - Does not respect robots.txt by default.
  - Assumes headline tags are in <h2> or <h3> — site structure may change and break the scraper.

## Recommended improvements
- Add robust error handling:
  - Wrap requests.get in try/except for request-related exceptions.
  - Handle and log parsing exceptions.
- Respect site crawling rules:
  - Check `robots.txt` before scraping and obey its directives.
  - Add delays between requests (time.sleep) and/or exponential backoff.
- Use a custom User-Agent header and consider rate-limiting to avoid being blocked:
```python
headers = {"User-Agent": "YourNameHeadlinesScraper/1.0 (+https://your-site.example)"}
response = requests.get(URL, headers=headers, timeout=10)
```
- Use a more specific selector for headlines if available (CSS classes or IDs) to reduce noise.
- Save output in additional formats (CSV, JSON) if you need structured data.
- Add logging (Python logging module) instead of print statements.
- Consider using a headless browser (e.g., Playwright, Selenium) if the site renders headlines via JavaScript.
- Add unit tests (mock requests) to verify parsing logic.

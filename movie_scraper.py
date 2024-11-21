import requests
from bs4 import BeautifulSoup
import csv

# URL of IMDb's Top 250 Movies page
URL = "https://www.imdb.com/chart/top/"

# Set a user-agent to avoid being blocked
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, "html.parser")

# Find all movie entries
movies = []

# Locate the list items
movie_items = soup.find_all("li", class_="ipc-metadata-list-summary-item")

for movie in movie_items:
    try:
        # Extract title
        title = movie.find("h3", class_="ipc-title__text").text.strip()

        # Extract metadata like year, duration, or rating
        metadata = movie.find_all("span", class_="sc-5bc66c50-6 OOdsw cli-title-metadata-item")
        year = metadata[0].text.strip() if metadata else "N/A"

        # Extract IMDb rating
        rating = movie.find("span", class_="ipc-rating-star--rating").text.strip()

        # Append to list
        movies.append({"Title": title, "Year": year, "Rating": rating})
    except AttributeError as e:
        print(f"Error extracting movie: {e}")

# Write to CSV
with open("imdb_top_250_updated.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Title", "Year", "Rating"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(movies)

print(f"Scraped {len(movies)} movies.")

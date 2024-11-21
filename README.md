Here’s a `README.md` file for your movie scraper:

---

# IMDb Top 250 Movie Scraper

This project is a Python-based web scraper that extracts the IMDb Top 250 movies along with their titles, release years, and ratings. The data is saved into a CSV file for easy access and analysis.

## Features

- Fetches the **Top 250 movies** from IMDb.
- Extracts the following details for each movie:
  - Title
  - Release Year
  - IMDb Rating
- Saves the data into a CSV file (`imdb_top_250_updated.csv`).

## Prerequisites

Before running the scraper, ensure you have the following installed:

1. **Python 3.7+**
2. The following Python libraries:
   - `requests`
   - `beautifulsoup4`

Install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

### 1. Clone the Repository
Download or clone this repository to your local machine.

### 2. Run the Script
Execute the script using Python:

```bash
python movie_scraper.py
```

### 3. Output
After running the script, you will find a file named `imdb_top_250_updated.csv` in the same directory. This file contains the scraped data with the following columns:

- **Title**: Movie title.
- **Year**: Release year of the movie.
- **Rating**: IMDb rating.

### Example Output

| Title                     | Year | Rating |
|---------------------------|------|--------|
| The Shawshank Redemption  | 1994 | 9.3    |
| The Godfather             | 1972 | 9.2    |
| The Dark Knight           | 2008 | 9.0    |

## Code Overview

- **`requests`**: Used to fetch the IMDb Top 250 page.
- **`beautifulsoup4`**: Parses the HTML content to extract movie data.
- The extracted data is written to a CSV file for further use.

## Troubleshooting

### Common Issues
1. **Empty Output**: 
   - Ensure IMDb hasn’t updated its page structure. If so, update the CSS selectors in the script.
   - Check your internet connection.

2. **403 Forbidden Error**:
   - IMDb might block your IP for excessive requests. Use a valid `User-Agent` header in the script.

3. **Incomplete Data**:
   - Ensure all required HTML elements exist in the IMDb page. Debugging the `soup` object can help.

### Debugging Tips
Add the following print statements in the script to debug issues:

```python
print(soup.prettify())  # Check the entire HTML content
```

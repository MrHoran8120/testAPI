"""
Secure News Reader - Version 1: Insecure Example

This version is intentionally insecure for teaching purposes.

It shows a common mistake: storing an API key directly in source code.
Students should compare this file with news_secure.py.
"""

import requests


# WARNING: This is deliberately insecure.
#
# This key is written directly in the Python file. If this file is uploaded to
# GitHub, anyone who can view the repository can copy the key.
#
# Attackers also use automated tools to search GitHub for exposed API keys.
# This can happen very quickly after code is pushed.
#
# This approach is useful only as a classroom demonstration of what NOT to do.
# Remove any real key before sharing or committing this file.
NEWS_API_KEY = "Put your api key here, but don't commit it to GitHub!"

NEWS_API_URL = "https://newsapi.org/v2/everything"


def get_api_key():
    """Return the API key that is hard-coded in this file."""
    return NEWS_API_KEY


def fetch_headlines(api_key):
    """
    Send a request to NewsAPI and return the response as Python data.

    This function demonstrates the basic API pattern:

    1. Choose the API endpoint URL.
    2. Send parameters, including the API key.
    3. Receive JSON data from the server.

    This example uses Australian news website domains because NewsAPI's
    country=au top-headlines feed can sometimes return an empty list.
    """
    params = {
        "domains": "abc.net.au,news.com.au,smh.com.au,9news.com.au",
        "sortBy": "publishedAt",
        "pageSize": 10,
        "apiKey": api_key,
    }

    response = requests.get(NEWS_API_URL, params=params, timeout=10)

    # If NewsAPI returns an error status code, this line raises an exception.
    # For example, an invalid API key may cause a 401 Unauthorized error.
    response.raise_for_status()

    return response.json()


def display_headlines(news_data):
    """Display up to 10 news headlines in a numbered list."""
    articles = news_data.get("articles", [])

    if not articles:
        print("No headlines were returned.")
        print("The API request worked, but NewsAPI returned an empty list.")
        return

    print("\nLatest Australian News Headlines")
    print("-" * 36)

    for number, article in enumerate(articles, start=1):
        title = article.get("title") or "Untitled article"
        source = article.get("source", {}).get("name") or "Unknown source"

        print(f"{number}. {title}")
        print(f"   Source: {source}\n")


def main():
    """Run the insecure news reader."""
    api_key = get_api_key()

    if not api_key or api_key == "your_api_key_here":
        print("Missing API key.")
        print("Add a NewsAPI key to NEWS_API_KEY for this insecure demo.")
        return

    try:
        news_data = fetch_headlines(api_key)
        display_headlines(news_data)

    except requests.exceptions.HTTPError as error:
        if error.response is not None and error.response.status_code == 401:
            print("Invalid API key. NewsAPI rejected the request.")
        else:
            print(f"NewsAPI returned an error: {error}")

    except requests.exceptions.ConnectionError:
        print("Network connection error. Check your internet connection.")

    except requests.exceptions.Timeout:
        print("The request timed out. Try again later.")

    except requests.exceptions.RequestException as error:
        print(f"An unexpected request error occurred: {error}")


if __name__ == "__main__":
    main()

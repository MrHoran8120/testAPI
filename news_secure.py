"""
Secure News Reader - Version 2: Secure Example

This version keeps the API key out of the source code.

Instead of writing the key in this file, the program loads it from a .env file.
That means the code can be shared on GitHub without sharing the secret key.
"""

import os

import requests
from dotenv import load_dotenv


NEWS_API_URL = "https://newsapi.org/v2/top-headlines"


def get_api_key():
    """
    Load the NewsAPI key from the .env file.

    The .env file should contain:

        NEWS_API_KEY=your_real_api_key_here

    The .env file is listed in .gitignore so it should not be committed to
    GitHub. This is safer than writing the key directly in the Python file.
    """
    load_dotenv()
    return os.getenv("NEWS_API_KEY")


def fetch_headlines(api_key):
    """
    Send a request to NewsAPI and return the response as Python data.

    This function demonstrates the basic API pattern:

    1. Choose the API endpoint URL.
    2. Send parameters, including the API key.
    3. Receive JSON data from the server.
    """
    params = {
        "country": "au",
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
    """Run the secure news reader."""
    api_key = get_api_key()

    if not api_key:
        print("Missing API key.")
        print("Create a .env file and add:")
        print("NEWS_API_KEY=your_real_api_key_here")
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

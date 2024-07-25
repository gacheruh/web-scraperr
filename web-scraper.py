import requests
from bs4 import BeautifulSoup

def get_article_content(url):
    try:
        # Send a request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title of the article
        title = soup.find('h1').text

        # Extract the content of the article
        # This part may need to be adjusted depending on the website structure
        paragraphs = soup.find_all('p')
        content = '\n'.join([para.text for para in paragraphs])

        return title, content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

if __name__ == "__main__":
    # Example URL of a news article
    url = "https://www.nytimes.com/2020/09/02/opinionremote-learning-coronavirus.html"
    title, content = get_article_content(url)

    if title and content:
        print(f"Title: {title}")
        print(f"Content: {content}")
    else:
        print("Failed to retrieve article content.")

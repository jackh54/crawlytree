import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag, urlparse

failed = []

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure we get a valid response
        return response.content
    except requests.RequestException:
        failed.append(url)
        return None

def parse_links(url, content, visited):  # Add 'visited' as an argument
    soup = BeautifulSoup(content, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        href = urljoin(url, href)  # Handle relative URLs
        href, _ = urldefrag(href)  # Remove URL fragments
        parsed_href = urlparse(href)
        
        # Only add internal links
        if parsed_href.netloc == urlparse(url).netloc and href not in visited:
            links.append(href)
    
    return links

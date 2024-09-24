
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag, urlparse

failed = []

def fetch_page(url):
    try:
        response = requests.get(url)
        return response.content
    except requests.RequestException:
        failed.append(url)
        return None

def parse_links(url, content):
    soup = BeautifulSoup(content, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        href = urljoin(url, href)
        href, _ = urldefrag(href)
        parsed_href = urlparse(href)
        if parsed_href.netloc != urlparse(url).netloc:
            continue
        links.append(href)
    return links

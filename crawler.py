
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag
from threading import Lock
from colorama import Fore
from utils import fetch_page, parse_links

lock = Lock()
visited = set()
output_queue = []
failed = []

def crawl_website(url, depth=0):
    global visited
    with lock:
        if url in visited:
            return
        visited.add(url)

    content = fetch_page(url)
    if content is None:
        output = " " * depth * 2 + "|- " + url + " (error)"
        output_queue.append((depth, Fore.RED + output))
        return []

    output = " " * depth * 2 + "|- " + url
    output_queue.append((depth, Fore.GREEN + output))

    links = parse_links(url, content)
    return links, depth + 1

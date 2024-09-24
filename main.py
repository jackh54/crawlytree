import os
import concurrent.futures
from urllib.parse import urlparse
from colorama import init, Fore
from crawler import crawl_website
from utils import failed

init(autoreset=True)

max_workers = 200
output_content = []

def print_output(output_queue):
    output_queue.sort(key=lambda x: x[0])
    for _, output in output_queue:
        print(output)
        output_content.append(output + "\n")

def summarize_crawl(domain, visited, failed):
    success_count = len(visited)
    failed_count = len(failed)

    summary = f"\n{Fore.CYAN}{domain} - {Fore.GREEN}{success_count} domains traced"
    if failed_count > 0:
        summary += f" and {Fore.RED}{failed_count} failed"
    else:
        summary += " and 0 failed"

    print(summary)
    output_content.append(summary + "\n")

def main():
    global output_content
    visited = set()
    output_queue = []
    
    print(Fore.GREEN + "Starting the web crawler...")

    if os.getenv("CI"):
        url = "http://books.toscrape.com/"  # Replace with any valid default URL for testing
    else:
        url = input(Fore.YELLOW + "Enter the website URL to crawl: ")

    if not url.startswith('http'):
        url = 'http://' + url
    
    domain = urlparse(url).netloc
    
    print(Fore.MAGENTA + "\nCrawling the website and building tree structure...\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(crawl_website, url, 0): url}
        
        while futures:
            done, _ = concurrent.futures.wait(futures, return_when=concurrent.futures.FIRST_COMPLETED)
            
            for future in done:
                futures.pop(future)
                result = future.result()
                
                if result:
                    links, next_depth = result
                    for link in links:
                        if link not in visited:
                            futures[executor.submit(crawl_website, link, next_depth)] = link

    print_output(output_queue)
    summarize_crawl(domain, visited, failed)

if __name__ == '__main__':
    main()

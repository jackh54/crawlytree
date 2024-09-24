# CrawlyTree - Enhanced Web Crawler

## Overview
CrawlyTree is a multithreaded web crawler that recursively traces a website's structure, extracting links and organizing them into a tree-like hierarchy. It outputs the crawled structure to the console with proper indentation, showing the relationship between parent and child pages.

## Features
- Multithreaded web crawling for fast performance.
- Outputs a tree-like structure of the website, displaying parent and child pages with indentation.
- Uses color for better visual representation:
  - **Green** for successfully crawled pages.
  - **Red** for pages that encountered errors.
- Ability to save the output to a file.
- Summary at the end showing the number of successful and failed domains.
- Option to either crawl another website or quit.

## How It Works
1. The user inputs a URL to crawl.
2. The program normalizes the URL and begins crawling.
3. It uses threads to fetch pages concurrently and extracts all internal links.
4. The tree-like structure is printed to the console.
5. The user is prompted to save the output to a file.
6. After the crawl, a summary is displayed showing the total number of traced domains and any failed requests.

## Installation
1. Install required dependencies:
   ```
   pip install requests beautifulsoup4 colorama
   ```

2. Run the script:
   ```
   python crawlytree.py
   ```

## Usage
- Enter a valid website URL when prompted.
- The program will crawl the website and display the tree structure.
- You can choose to save the output to a file after the crawl.
- The program will offer you the choice to either crawl another link or quit.


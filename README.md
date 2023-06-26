# Personal ChatGPT

This Python script is a web crawler that visits a list of URLs and extracts code snippets from the HTML content of each page. It can be used to gather code examples and learn from different websites. The code snippets are saved to a file named `learned.txt` for future reference. For the code to get everything out of the links it can take HOURS to DAYS (based off the amount of links) for me to visit about 10,000 links it took about 40 minutes. NOTE THIS IS ONLY FOR CODING IT WILL ONLY GRAP CODE FROM WEBSITES NOTHING ELSE

## Features

- Crawls multiple URLs specified in the `links.txt` file.
- Extracts code snippets from HTML pages.
- Saves the learned code snippets in the `learned.txt` file.
- Avoids revisiting URLs that have already been crawled.
- Provides a progress bar to track the crawling process.
- Allows searching for specific code requests and generates Luau code based on the input.

## Requirements

- Python 3.x
- Libraries:
  - requests
  - beautifulsoup4
  - tqdm

## Usage

1. Clone the repository or download the `crawler.py` file.
2. Install the required libraries: `pip install requests beautifulsoup4 tqdm`.
3. Prepare a list of URLs to crawl and save them in a file named `links.txt`, with one URL per line.
4. Run the script: `python main.py`.
5. The script will crawl the URLs, extract code snippets, and save them in the `learned.txt` file.
6. Optionally, you can modify the code request in the `main()` function to generate specific Luau code snippets.

## Example

Here's an example of how to use the script:

1. Create a file named `links.txt` and add the URLs you want to crawl, one URL per line, or replace https://create.roblox.com/docs/reference/ (line 24) with any link and it will go to all the subdir of that link
   ```
   https://example.com/page1
   https://example.com/page2
   https://example.com/page3
   ```
2. Run the script: `python main.py`.
3. The script will crawl the provided URLs, extract code snippets, and save them in the `learned.txt` file.
4. You can view the learned code sections by running: `python crawler.py`.

## Notes

- The script will only crawl URLs that start with `https://create.roblox.com/docs/reference/`. Modify the `startswith()` condition in the `extract_urls()` function if you want to crawl URLs from a different domain.
- Adjust the number of URLs to crawl by modifying the `seed_urls` list in the `main()` function.
- To use the multithreading functionality, uncomment the corresponding lines in the `main()` function.
- The script uses the `tqdm` library to display a progress bar during crawling. If you don't want the progress bar, remove the `tqdm` references.

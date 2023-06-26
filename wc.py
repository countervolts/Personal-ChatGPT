import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from tqdm import tqdm

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    code_blocks = soup.find_all('code')
    code_snippets = [code.get_text() for code in code_blocks]
    return code_snippets

def extract_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    anchor_tags = soup.find_all('a')
    urls = []
    parsed_url = urlparse(url)
    base_url = '{}://{}'.format(parsed_url.scheme, parsed_url.netloc)

    for tag in anchor_tags:
        href = tag.get('href')
        if href:
            absolute_url = urljoin(base_url, href)
            if absolute_url.startswith('https://create.roblox.com/docs/reference/'):
                urls.append(absolute_url)

    return urls

def generate_luau_code(data, code_request):
    code_snippets = []
    for url, snippets in data.items():
        filtered_snippets = [snippet for snippet in snippets if code_request.lower() in snippet.lower()]
        code_snippets.extend(filtered_snippets)

    if code_snippets:
        code_parts = []
        for i, code in enumerate(code_snippets, start=1):
            code_parts.append('Code Part {}: {}'.format(i, code))
        code = '\n\n'.join(code_parts)
    else:
        code = 'No matching code snippets found.'

    return code

def write_learned_data(url, code_snippets):
    with open('learned.txt', 'a') as file:
        file.write('URL: {}\n'.format(url))
        for snippet in code_snippets:
            file.write('Code snippet:\n{}\n\n'.format(snippet))

def write_visited_links(links):
    with open('links.txt', 'a+') as file:
        file.seek(0)
        existing_links = file.read().splitlines()
        new_links = [link for link in links if link not in existing_links]
        if new_links:
            file.seek(0)
            file.write('\n'.join(new_links))
            file.write('\n')

def read_links_file(filename):
    with open(filename, 'r') as file:
        links = file.read().splitlines()
    return links

def print_learned_code():
    with open('learned.txt', 'r') as file:
        lines = file.readlines()
    code_sections = []
    for line in lines:
        line = line.strip()
        if line.startswith('URL:'):
            code_sections.append('')
        elif line.startswith('Code snippet:'):
            code_sections[-1] += line + '\n'
    
    print('Learned Code Sections: {}'.format(len(code_sections)))
    print('\n'.join(code_sections))

def main():
    seed_urls = read_links_file('links.txt')[:4]
    learned_data = {}
    total_urls = len(seed_urls)

    with tqdm(total=total_urls, desc='Crawling Progress') as pbar:
        for seed_url in seed_urls:
            links = [seed_url]
            while links:
                link = links.pop(0)
                if link not in learned_data:
                    code_snippets = scrape_page(link)
                    if code_snippets:
                        learned_data[link] = code_snippets
                        write_learned_data(link, code_snippets)
                    extracted_urls = extract_urls(link)
                    links.extend(extracted_urls)
                    write_visited_links(extracted_urls)
                pbar.update(1)

    print('Finished visiting {}/{} websites. Already visited {}/{} websites.'.format(len(seed_urls), total_urls, len(learned_data), total_urls))
    print_learned_code()

if __name__ == '__main__':
    main()

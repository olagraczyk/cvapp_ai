# web_scraper.py
# To run this script, paste `python web_scraper.py` in the terminal

import requests
from bs4 import BeautifulSoup

def scrape(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.select_one('h1').text
    
    # Find all big divs and get the one with the most text content
    divs = soup.find_all(['div', 'section'], recursive=True)
    main_div = max(divs, key=lambda tag: len(tag.get_text(strip=True)), default=None)
    
    if main_div:
        content = main_div.get_text(separator='\n', strip=True)
        full_text = f"{title}\n\n{content}"
    
        return title, full_text
    else:
        print("No content found")






if __name__ == '__main__':
    scrape()
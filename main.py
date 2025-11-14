from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    with open('url.txt', 'r') as f:
        url = f.read().strip()
    
    with urlopen(url) as response:
        html = response.read().decode('utf-8')
    
    soup = BeautifulSoup(html, 'html.parser')

    header = soup.find('div', class_='section__title')
    # or
    # header = soup.find_all('div', class_='section__title')[0]
    # or
    # header = soup.select_one('div.section__title')
    # or
    # header = soup.select('div.section__title')[0]

    print(header.get_text())
    
if __name__ == "__main__":
    main()

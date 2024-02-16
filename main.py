import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin


BASE_URL = "https://www.marmiton.org/"

def main():
    with requests.Session() as session:
        response = session.get(BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        categories = soup.find("li",class_="mrtn-header-menu-title").find_all("a", class_="mrtn-header-subitem-link")
        #categories = soup.select("li.mrtn-header-menu-title ul li a.mrtn-header-subitem-link")

        categories_url = [category["href"] for category in categories]
        full_url_categories = [urljoin(BASE_URL, category) for category in categories_url]

        for full_url_category in full_url_categories:
            response = session.get(full_url_category)
            soup = BeautifulSoup(response.content, 'html.parser')
            pagination = soup.find("nav", class_="af-pagination")
            if not pagination:
                return 0
            pages = pagination.find_all('a')
            pprint(pages)
            number_page = max([int(page.get_text()) for page in pages if page.get_text().isdigit()])
            pprint(number_page)
       # pprint(full_url_categories)

if __name__ == "__main__":
    main()
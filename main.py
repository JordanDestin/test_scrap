import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin


BASE_URL = "https://www.marmiton.org/"

def get_number_of_pages(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        pagination = soup.find("nav", class_="af-pagination")
        if not pagination:
            return 0
        number_pages = pagination.find_all('a')
        return max([int(page.get_text()) for page in number_pages if page.get_text().isdigit()])


def get_all_categories(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    categories = soup.find("li",class_="mrtn-header-menu-title").find_all("a", class_="mrtn-header-subitem-link")
    categories_url = [category["href"] for category in categories]
    full_url_categories = [urljoin(BASE_URL, category) for category in categories_url]
    
    return full_url_categories
   ## pprint(full_url_categories)
         

def main():
    with requests.Session() as session:
        try:
            response = session.get(BASE_URL)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f'Error{e}')
            raise requests.exceptions.RequestException from e

        list_categories = get_all_categories(BASE_URL)
        number_of_pages = get_number_of_pages(list_categories[0]) 
        get_all_categories(BASE_URL)

        """categories = soup.find("li",class_="mrtn-header-menu-title").find_all("a", class_="mrtn-header-subitem-link")
        #categories = soup.select("li.mrtn-header-menu-title ul li a.mrtn-header-subitem-link")

        categories_url = [category["href"] for category in categories]
        full_url_categories = [urljoin(BASE_URL, category) for category in categories_url]

        for full_url_category in full_url_categories:
            #response = session.get(full_url_category)
            
            number_pages = get_number_of_pages(full_url_category)
            pprint(full_url_category)"""


if __name__ == "__main__":
    main()
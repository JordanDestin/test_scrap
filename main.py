import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin
from selectolax.parser import HTMLParser
from loguru import logger
import sys

logger.remove() 
logger.add("logs.log", level="WARNING", rotation="500kb")
logger.add(sys.stderr, level="INFO")

BASE_URL = "https://www.marmiton.org/"



def get_all_categories(url):
    response = requests.get(url)
    tree = HTMLParser(response.text)
    categories = tree.css("li.mrtn-header-menu-title ul li a.mrtn-header-subitem-link")

    
    """soup = BeautifulSoup(response.text, 'html.parser')
    categories = soup.find("li",class_="mrtn-header-menu-title").find_all("a", class_="mrtn-header-subitem-link")
    categories_url = [category["href"] for category in categories]
    full_url_categories = [urljoin(BASE_URL, category) for category in categories_url]
    
    urls_categorie = [url for url in full_url_categories if "categorie" in url]
    urls_modifiees = [url.replace("?rcp=0", "") for url in urls_categorie]"""
    #return urls_modifiees[0:1]
    pprint(categories)


def get_number_of_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    pagination = soup.find("nav", class_="af-pagination")
    if not pagination:
        return 0
    number_pages = pagination.find_all('a')
    return max([int(page.get_text()) for page in number_pages if page.get_text().isdigit()])


def get_all_recipes_urls_by_category(url):
    pass

         

def get_all_recipes_name_by_category(url):
    list_recipe_names = []
  
    list_categories = get_all_categories(url)
    pprint(list_categories)
    for category in list_categories:
        number_pages = get_number_of_pages(category)
        pprint(number_pages)
        for i in range(1, number_pages+1):
            page_url = category + "/"+ str(i)
            #pprint(page_url)
            response = requests.get(page_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            recipes_name = soup.find_all("h4", class_="recipe-card__title")
            pprint(recipes_name)
            """for recipe in recipes_name:
                list_recipe_names.append(recipe.get_text().strip())"""
    #pprint(list_recipe_names)
   

def get_number_star_recipe(url):
    pass      
   

def main():
    with requests.Session() as session:
        try:
            response = session.get(BASE_URL)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f'Error{e}')
            raise requests.exceptions.RequestException from e

        #list_categories = get_all_categories(BASE_URL)
        #number_of_pages = get_number_of_pages(list_categories) 
        get_all_categories(BASE_URL)
        #get_all_recipes_name_by_category(BASE_URL)

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
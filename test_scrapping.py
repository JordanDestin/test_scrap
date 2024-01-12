import requests
from bs4 import BeautifulSoup
from pprint import pprint


url = "https://www.marmiton.org/recettes/index/categorie/aperitif-ou-buffet/"


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

def get_text_if_not_none(e):
    if e:
        return e.text.strip()
    else:
        return None

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text
    response_encoding = response.apparent_encoding
    #print(html)
   # f = open("marmiton.html", "w", encoding=response_encoding)
   # f.write(html)
    #f.close
    soup = BeautifulSoup(html, 'html5lib')

    #title = soup.find("h1").text
    #recipe = get_text_if_not_none(soup.find("div",class_ = "recipe-step-list"))

    #ingredient
    #div_ingredients = soup.find("div", class_="card-ingredient")
    #e_ingredients = div_ingredients.find_all("span", class_="card-ingredient-title")
    #for ingredient in e_ingredients:
     #   print(ingredient)
    

    def get_number_of_pages(url):
        response = requests.get(url)
        #soup = BeautifulSoup(response.content, 'html.parser')

        pagination = soup.find("nav", class_="af-pagination")
        if not pagination:
            return 0

        number_pages = pagination.find_all('a')
     
        return max([int(page.get_text()) for page in number_pages if page.get_text().isdigit()])

    def get_all_list_recipes(url):      
        list_recipe = []
        number_pages= get_number_of_pages(url)
        
        for i in range(1 ,number_pages+1):
            list_recipe.append(url+str(i))
            pprint(list_recipe)


    get_all_list_recipes(url)

else:
    print("error")



import requests
from bs4 import BeautifulSoup


my_protein_site = "https://www.myprotein.pl/clothing/outlet/womens.list?\
                   pageNumber=1&\
                   facetFilters=pl_sportsClothingtype_content:Leginsy"
response = requests.get(my_protein_site)

response_html = response.text
parsed_response_html = BeautifulSoup(response_html)

leggins = parsed_response_html.find_all(
    "div", class_="athenaProductBlock_title"
)

leggin_name_list = []

for leggin in leggins:
    leggin_name = leggin.h2.text.replace("\n", "")
    leggin_name_list.append(leggin_name)

print(leggin_name_list)

import requests
from bs4 import BeautifulSoup


def get_list_of_leggins_from_page(page_number):
    my_protein_site = "https://www.myprotein.pl/clothing/womens/gym-leggings.list"
    response = requests.get(my_protein_site, {"pageNumber": page_number})

    response_html = response.text
    parsed_response_html = BeautifulSoup(response_html)

    leggins = parsed_response_html.find_all(
        "span", class_="athenaProductBlock_hiddenElement"
    )

    leggin_name_list = []

    for leggin in leggins:
        leggin_name = leggin["data-product-title"]
        leggin_id = leggin["data-product-id"]
        leggin_name_list.append({"leggin_name": leggin_name, "leggin_id": leggin_id})

    return leggin_name_list


def get_list_of_leggins():
    page_number = 1
    list_of_leggins = []
    list_of_leggins_per_page = get_list_of_leggins_from_page(page_number)

    while list_of_leggins_per_page:
        list_of_leggins += list_of_leggins_per_page
        page_number += 1
        list_of_leggins_per_page = get_list_of_leggins_from_page(page_number)

    return list_of_leggins


print(get_list_of_leggins())

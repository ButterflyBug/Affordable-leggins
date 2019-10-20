import requests
from bs4 import BeautifulSoup


def get_list_of_leggins_from_page(page_number):
    my_protein_site = "https://www.myprotein.pl/clothing/womens/gym-leggings.list"
    response = requests.get(my_protein_site, {"pageNumber": page_number})

    response_html = response.text
    parsed_response_html = BeautifulSoup(response_html, "html")

    leggins = parsed_response_html.find_all(
        "div", class_="productListProducts_product"
    )

    leggin_name_list = []

    for leggin in leggins:
        leggin_data = leggin.find("span")
        leggin_name = leggin_data["data-product-title"]
        leggin_id = leggin_data["data-product-id"]
        leggin_price = float(
            leggin_data["data-product-price"].replace(" zł", ""))

        leggin_name_list.append({
            "leggin_name": leggin_name,
            "leggin_id": leggin_id,
            "leggin_price": leggin_price,
        })

    return leggin_name_list


def get_rrp_from_single_site(identificator):
    single_leggin_site = "https://www.myprotein.pl/" + \
        str(identificator) + ".html"
    single_response = requests.get(single_leggin_site)

    single_response_html = single_response.text
    parsed_single_response_html = BeautifulSoup(single_response_html, "html")

    leggin_rrp = float(parsed_single_response_html.find(
        "p", class_="productPrice_rrp"
    ).text.replace(" zł", "").replace("RRP: ", ""))

    return leggin_rrp


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

for element in get_list_of_leggins():
    print(element)

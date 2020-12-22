import requests
from bs4 import BeautifulSoup


def get_list_of_leggins_from_page(page_number):
    my_protein_site = "https://www.myprotein.pl/clothing/womens/gym-leggings.list"
    response = requests.get(my_protein_site, {"pageNumber": page_number})

    response_html = response.text
    parsed_response_html = BeautifulSoup(response_html, features="html.parser")

    leggins = parsed_response_html.find_all("li", class_="productListProducts_product")

    leggin_name_list = []

    for leggin in leggins:
        leggin_data = leggin.find("span")
        leggin_name = leggin_data["data-product-title"]
        leggin_id = leggin_data["data-product-id"]
        leggin_price = float(leggin_data["data-product-price"].replace(" zł", ""))

        leggin_rrp = get_rrp_from_single_site(leggin_id) or leggin_price

        leggin_name_list.append(
            {
                "leggin_name": leggin_name,
                "leggin_id": leggin_id,
                "leggin_price": leggin_price,
                "leggin_rrp": leggin_rrp,
                "sizes": find_size(leggin_id),
            }
        )

    return leggin_name_list


def get_rrp_from_single_site(identificator):
    parsed_single_response_html = get_single_leggin_page(identificator)

    if parsed_single_response_html.find("p", class_="productPrice_rrp"):
        leggin_rrp = float(
            parsed_single_response_html.find("p", class_="productPrice_rrp")
            .text.replace(" zł", "")
            .replace("RRP: ", "")
        )
    else:
        leggin_rrp = None

    return leggin_rrp


def get_single_leggin_page(identificator):
    single_leggin_site = "https://www.myprotein.pl/" + str(identificator) + ".html"
    single_response = requests.get(single_leggin_site)

    single_response_html = single_response.text
    parsed_single_response_html = BeautifulSoup(
        single_response_html, features="html.parser"
    )
    return parsed_single_response_html


def get_list_of_leggins():
    page_number = 1
    list_of_leggins = []
    list_of_leggins_per_page = get_list_of_leggins_from_page(page_number)

    while list_of_leggins_per_page:
        list_of_leggins += list_of_leggins_per_page
        page_number += 1
        list_of_leggins_per_page = get_list_of_leggins_from_page(page_number)

    return list_of_leggins


def find_size(leggin_id):
    single_leggin_page = get_single_leggin_page(leggin_id)
    sizes_box = single_leggin_page.find("div", class_="athenaProductVariations_boxes")
    if sizes_box:
        sizes_list = list(
            map(
                lambda arg: arg.text.strip().replace("\n wybrany", ""),
                sizes_box.find_all("button", class_="inStock"),
            )
        )
        return sizes_list

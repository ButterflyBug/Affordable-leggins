import json
from affordable_leggins.leggins_list import get_list_of_leggins


def store_data():
    with open("store.json", "w") as file:
        json.dump(get_list_of_leggins(), file)
        return file

import json
import os
import datetime
from affordable_leggins.leggins_list import get_list_of_leggins


def store_data():
    date_name = datetime.date.today().strftime("%d-%m-%Y")
    os.mkdir("./leggins_lists")
    with open("leggins_lists/leggins_lists_" + date_name + ".json", "w") as file:
        json.dump(get_list_of_leggins(), file)
        return file

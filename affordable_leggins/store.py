import json
import os
import datetime
from affordable_leggins.leggins_list import get_list_of_leggins
from affordable_leggins.storage.models import Leggin


def make_directory(directory_name):
    try:
        os.mkdir(directory_name)
    except FileExistsError:
        pass


def store_data(directory_name):
    date_name = datetime.date.today().strftime("%d-%m-%Y")
    make_directory(directory_name)
    with open(directory_name + "/leggins_lists_" + date_name + ".json", "w") as file:
        json.dump(get_list_of_leggins(), file)
        return file


def store_data_in_database():
    for single_leggin in get_list_of_leggins():
        leggin = Leggin()
        leggin.name = single_leggin["leggin_name"]
        leggin.price = single_leggin["leggin_price"]
        leggin.rrp = single_leggin["leggin_rrp"]
        leggin.external_id = single_leggin["leggin_id"]
        leggin.date = datetime.datetime.now()
        leggin.save()


def read_data(directory_name, day, month, year):
    file_name = (
        directory_name + "/leggins_lists_" + str(day).zfill(2) + "-" + str(month).zfill(2) + "-" + str(year) + ".json")
    with open(file_name, "r") as file:
        data_to_read = file.read()
        return json.loads(data_to_read)

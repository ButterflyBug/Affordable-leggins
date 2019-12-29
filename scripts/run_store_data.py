#!/usr/bin/env python
import sys
from datetime import date
from affordable_leggins.store import store_data
from affordable_leggins.store import read_data
from affordable_leggins.min_current_price import find_min_current_price


try:
    store_data(sys.argv[1])
    current_date = date.today()
    leggins = read_data(sys.argv[1], current_date.day, current_date.month, current_date.year)
    min_price = find_min_current_price(leggins)
    print("The cheapest product: ", min_price)
except IndexError:
    print("Please enter directory")
    print("Usage: run_store_data.py /path/to/directory")

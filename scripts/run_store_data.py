#!/usr/bin/env python
import sys
from datetime import date
from affordable_leggins.store import store_data
from affordable_leggins.store import read_data
from affordable_leggins.min_current_price import find_min_current_price
from affordable_leggins.filters import filter_size, filter_name, filter_current_price
from affordable_leggins.send_notification import (
    send_email,
    email_address,
    subject,
    message,
)


try:
    store_data(sys.argv[1])
    current_date = date.today()
    leggins = read_data(
        sys.argv[1], current_date.day, current_date.month, current_date.year
    )
    leggins = filter_size(leggins, "XS") + filter_size(leggins, "S")
    leggins = filter_name(leggins, "Bezszwowe", reject=True)
    leggins = filter_current_price(leggins, range(100))
    min_price = find_min_current_price(leggins)

    print("Number of found leggins: ", len(leggins))
    for leggin in leggins:
        print("\n", leggin)

    print("\nThe cheapest product: ", min_price)
except IndexError:
    print("Please enter directory")
    print("Usage: run_store_data.py /path/to/directory")

send_email(email_address(), subject(), message(email_address(), leggins))

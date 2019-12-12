#!/usr/bin/env python
import sys
from affordable_leggins.store import store_data


try:
    store_data(sys.argv[1])
except IndexError:
    print("Please enter directory")
    print("Usage: run_store_data.py /path/to/directory")

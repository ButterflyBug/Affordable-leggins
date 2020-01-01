def find_min_current_price(leggins):
    if leggins == []:
        return None
    else:
        min_leggin = min(leggins, key=lambda leggin: leggin["leggin_price"])

        return min_leggin

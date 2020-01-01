def filter_size(leggins, size):
    result = list(filter(lambda leggin: size in leggin["sizes"], leggins))
    if result:
        return result

def filter_size(leggins, size):
    result = list(filter(lambda leggin: size in leggin["sizes"], leggins))
    if result:
        return result


def filter_name(leggins, name, reject=False):
    if reject:
        result = list(filter(lambda leggin: name not in leggin["leggin_name"], leggins))
    else:
        result = list(filter(lambda leggin: name in leggin["leggin_name"], leggins))

    return result

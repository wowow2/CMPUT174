def unzip(some_dictionary):
    keys = []
    values = []
    for key, value in some_dictionary.items():
        keys.append(key)
        values.append(value)
    return (keys, values)

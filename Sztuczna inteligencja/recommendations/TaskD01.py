"""Zad D01"""

def load_data(fileobj, normalize=True):
    """Zad D01"""
    data = {}
    next(fileobj)
    for line in fileobj:
        items = line.split('\t')
        user = items[0]
        band = items[1]
        rating = float(items[2])
        if user not in data:
            data[user] = {}
        data[user][band] = rating

    if normalize:
        for user in data:
            max_rating = max(data[user].values())
            for band in data[user]:
                data[user][band] /= max_rating
    return data

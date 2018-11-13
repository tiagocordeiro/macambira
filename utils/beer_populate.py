import pandas as pd

import os

local = os.path.dirname(__file__)


def create_beers():
    file = str(local + '/csv_data/beers.csv')
    df = pd.read_csv(file)

    beers = []

    for beer in df.T.to_dict().values():
        beers.append(beer)

    return list(beers)


if __name__ == '__main__':
    create_beers()

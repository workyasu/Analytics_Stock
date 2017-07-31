import pandas as pd
import jsm
from pandas.io import gbq


class BigqueryWrapper:

    def __init__(self, project_name):
        self.project_name = project_name;

    def read(self, query):
        return pd.read_gbq(query, self.project_name)

    def write(self, table, query, data):
        gbq.to_gbq(data, table, query)


def main():
    print("test")


if __name__ == '__main__':
    main()




import pandas as pd

class DataAnalyzer:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def find_extremes(self, column):
        return self.dataframe[column].max(), self.dataframe[column].min()

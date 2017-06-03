import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

class TripGeneration:

    def __init__(self, data, dependent_col_name,
                 production_col_names, production_constant, production_intercepts,
                 attraction_col_names, attraction_constant, attraction_intercepts):
        self.data = data
        self.dependent_col_name = dependent_col_name
        self.production_col_names = production_col_names
        self.production_constant = production_constant
        self.production_intercepts = production_intercepts
        self.attraction_col_names = attraction_col_names
        self.attraction_constant = attraction_constant
        self.attraction_intercepts = attraction_intercepts


    # get trip production score for 'zone'
    def getTripProductionScore(self, zone):
        production_score = 0
        data = pd.read_csv(self.pathToData, index_col=0)

        # implement specific way to get sub-table(data) just for specific 'zone' i.e: all rows related to zone1
        sub_table = data.loc[:, self.production_col_names]

        length_rows = sub_table.shape(0)

        for x in (0, length_rows):
            row_values = sub_table.iloc[x, :].values
            production_score += self.production_constant
            for j in row_values:
                production_score += row_values[j]*self.production_intercepts[j]

        return production_score

    # get trip attraction score for 'zone'
    def getTripAttractionScore(self, zone):
        attraction_score = 0
        data = pd.read_csv(self.pathToData, index_col=0)

        # implement specific way to get sub-table(data) just for specific 'zone' i.e: all rows related to zone1
        sub_table = data.loc[:, self.attraction_col_names]

        length_rows = sub_table.shape(0)

        for x in (0, length_rows):
            row_values = sub_table.iloc[x, :].values
            attraction_score += self.attraction_constant
            for j in row_values:
                attraction_score += row_values[j]*self.attraction_intercepts[j]

        return attraction_score


    def doTripBalancing(self, zone):
        print("do something")


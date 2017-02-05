import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

class CollinearityChecker:
    def __init__(self, pathToData):
        self.data = pd.read_csv(pathToData, index_col=0)

    # get collinearity (r^2 value) of a pair of columns
    def getCollinearityScore(self, dependentCol, independentCol):
        df2 = self.data.iloc[:, [independentCol, dependentCol]]
        lm = smf.ols(formula='Sales ~ TV', data=df2).fit()
        return lm.rsquared

    # print collinearities (r^2 value) of each pair of columns
    def printAllCollinearities(self):
        length_col = self.data.shape[1]
        while(0 != length_col-1):
            for x in range(0, length_col-1):
                df2 = self.data.iloc[:, [x, length_col-1]]
                col_name1 = df2.columns.values[0]
                col_name2 = df2.columns.values[1]
                lm = smf.ols(formula=col_name1+" ~ "+col_name2, data=df2).fit()
                print("Collinearity for "+col_name1+" & "+col_name2+": R^2="+lm.rsquared)
            length_col -= 1

    def getInterceptValues(self, col_names, dependent_col_name):
        intercept_values = []
        # K-FOLD CROSS VALIDATION
        zone_numbers = self.data.index.values
        testing_zone_nums = []

        # implement outer loop for k-fold validation
        for zone_num in zone_numbers:
            if zone_num not in testing_zone_nums:
                df2 = self.data.loc[:, col_names]
                col_names_string = " + ".join(col_names)
                lm = smf.ols(formula=str(dependent_col_name) + " ~ " + str(col_names_string), data=df2).fit()
                intercept_values.append(lm.params.values)

        num_of_rows = len(intercept_values)
        num_of_params = len(lm.params.values)
        # avg_of_params = [0] * num_of_params
        total_sum_of_params = [sum(x) for x in zip(*intercept_values)]
        avg_of_params = [x / num_of_rows for x in total_sum_of_params]







        return lm.params.values




import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

class CollinearityChecker:
    def __init__(self, pathToData):
        self.pathToData = pathToData

    # get collinearity (r^2 value) of a pair of columns
    def getCollinearityScore(self, dependentCol, independentCol):
        data = pd.read_csv(self.pathToData, index_col=0)
        df2 = data.iloc[:, [independentCol, dependentCol]]
        lm = smf.ols(formula='Sales ~ TV', data=df2).fit()
        return lm.rsquared

    # print collinearities (r^2 value) of each pair of columns
    def printAllCollinearities(self):
        data = pd.read_csv(self.pathToData, index_col=0)
        length_col = data.shape[1]
        while(0 != length_col-1):
            for x in range(0, length_col-1):
                df2 = data.iloc[:, [x, length_col-1]]
                col_name1 = df2.columns.values[0]
                col_name2 = df2.columns.values[1]
                lm = smf.ols(formula=col_name1+" ~ "+col_name2, data=df2).fit()
                print("Collinearity for "+col_name1+" & "+col_name2+": R^2="+lm.rsquared)
            length_col -= 1

    def getInterceptValues(self, col_names, dependent_col_name):
        data = pd.read_csv(self.pathToData, index_col=0)
        df2 = data.loc[:, col_names]
        col_names_string = " + ".join(col_names)
        lm = smf.ols(formula=str(self.dependent_col_name) + " ~ " + str(col_names_string), data=df2).fit()

        return lm.params.values




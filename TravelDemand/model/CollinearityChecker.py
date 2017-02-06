import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

class CollinearityChecker:
    def __init__(self, pathToData):
        self.data = pd.read_csv(pathToData, index_col=0)

    # get collinearity (r^2 value) of a pair of columns
    def getCollinearityScore(self, dependentCol, independentCol):
        # GET SUBTABLE CONTAINING ONLY THE INDEPENDENT COLUMN AND DEPENDENT COLUMN
        df2 = self.data.iloc[:, [independentCol, dependentCol]]
        # CREATE FITTED MODEL USING ORDINARY LEAST SQUARES REGRESSION
        lm = smf.ols(formula='Sales ~ TV', data=df2).fit()
        # RETURN RSQUARED VALUE FOR THE MODEL
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

        # ASSUMING THE ZONE #s ARE THE INDICES OF THE DATAFRAME
        zone_numbers = self.data.index.values

        # STORE NUMBER OF ROWS PER SLICE FOR CROSS VALIDATION
        num_per_slice = int(len(zone_numbers)/10)

        # THE WHOLE DATAFRAME
        remaining_rows_of_data = self.data

        #START K-FOLD CROSS VALIDATION
        for testing_slice_num in range(0, 10):
            testing_slice = None
            for slice_num in range(0,10):
                # STORE THE FIRST NUM_PER_SLICE TO A TEMPORARY VARIABLE
                temp_rows_of_data = remaining_rows_of_data[:num_per_slice]
                if slice_num != testing_slice_num: # IF THE CURRENT SLICE IS NOT THE TESTING SLICE
                    if(len(temp_rows_of_data.index) < num_per_slice): # JUST IN CASE MAY BUTAL
                        print("Last slice #"+str(slice_num))
                    else:
                        print("Slice #"+str(slice_num))
                        # UPDATES THE REMAINING ROWS OF DATA BY GETTING THE SUBTABLE STARTING FROM ROW "NUM_PER_SLICE" TIL THE LAST ROW
                        # BASICALLY REMOVES/SPLICES THE USED SLICE OF DATA
                        remaining_rows_of_data = remaining_rows_of_data[num_per_slice:]

                    # Trim the unnecessary columns out from the slice
                    df2 = self.data.loc[:, col_names]
                    col_names_string = " + ".join(col_names)

                    # Fit the model using the data in the slice
                    lm = smf.ols(formula=str(dependent_col_name) + " ~ " + str(col_names_string), data=df2).fit()

                    # Put the resulting intercept values to a list para i aaverage siya later
                    intercept_values.append(lm.params.values)
                else:
                    testing_slice = temp_rows_of_data # IF IS TESTING SLICE, STORE IT TO A TEMPORARY VARIABLE

                num_of_rows = len(intercept_values)
                total_sum_of_params = [sum(x) for x in zip(*intercept_values)]
                avg_of_params = [x / num_of_rows for x in total_sum_of_params]

                # *Perform the testing part somehow against the testing slice here*







        #for zone_num in zone_numbers:
        #    if zone_num not in testing_zone_nums:
        #        df2 = self.data.loc[:, col_names]
        #        col_names_string = " + ".join(col_names)
        #        lm = smf.ols(formula=str(dependent_col_name) + " ~ " + str(col_names_string), data=df2).fit()
        #        intercept_values.append(lm.params.values)

        #num_of_rows = len(intercept_values)
        # avg_of_params = [0] * num_of_params
        #total_sum_of_params = [sum(x) for x in zip(*intercept_values)]
        #avg_of_params = [x / num_of_rows for x in total_sum_of_params]







        return lm.params.values




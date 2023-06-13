import pandas as pd
from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Creating a class to help in understanding the data
class Understand(object):
    """A class to help with some data understanding"""

    def __init__(self, df):
        self.df = df

    def inspect_df(self):
        """This prints out the summary from the inspection of the data"""

        return {"Dimensions": f"This data set has {self.df.shape[0]} rows and {self.df.shape[1]} columns",
                "Duplicates": f"The data has {self.df.duplicated().sum()} duplicated entries and {len(self.df) - self.df.duplicated().sum()} non duplicated entries",
                "Missing values (%)": f"{sum(self.df.isna().sum())/self.df.__len__() * 100} % of the data has missing values",
                "Summary statistics": self.df.describe().T,
                "Info (printed above)": self.df.info()}
        
        
class TimeSeries(object):
    """Perform Time Series Analysis
    """
    
    def __init__(self, TS, w:int):
        self.TS = TS
        self.w = w
        
    def stationarity_check(self):
        # Calculate rolling statistics
        roll_mean = self.TS.rolling(window=w, center=False).mean()
        roll_std = self.TS.rolling(window=w, center=False).std()

        # Perform the Dickey Fuller test
        dftest = adfuller(self.TS)

        # Plot rolling statistics
        fig = plt.figure(figsize=(12, 6))
        orig = plt.plot(self.TS, color='blue', label='Original')
        mean = plt.plot(roll_mean, color='red', label='Rolling Mean')
        std = plt.plot(roll_std, color='black', label='Rolling Std')
        plt.legend(loc='best')
        plt.title('Rolling Mean & Standard Deviation')
        plt.show(block=False)

        # Print Dickey-Fuller test results
        print('Results of Dickey-Fuller Test: \n')
        dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
        for key, value in dftest[4].items():
            dfoutput['Critical Value (%s)' % key] = value
        print(dfoutput)

        print()
        if dfoutput['p-value'] > 0.05:
            print("The data is non-stationary")
        else:
            print("The data is stationary")
            
        return None
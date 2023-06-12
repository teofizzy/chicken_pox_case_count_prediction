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
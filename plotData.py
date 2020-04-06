import packages

class plot_data:
    def __init__(self, ticker_name):
        ''' Function for initializing class variables. '''
        self.df   = 0
        self.tick = ticker_name + '.csv'
        
    def read_csv(self):
        ''' Function for reading data from CSV file. '''
        self.df = packages.pd.read_csv(self.tick, parse_dates=True, index_col=0)
        return self.df

    def plot_all(self):
        ''' Function for plotting Open, Close, High, Low, Adj Close, Volume. '''
        self.read_csv().plot()
        packages.plt.show()
    
    def plot_one(self, feature):
        ''' Function for plotting specific feature. '''
        self.read_csv()[feature].plot()
        packages.plt.show()
        
if __name__ == "__main__":
    ticker_name = input("Enter the ticker name for plotting.\n")
    feature     = input("Enter the feature name for plotting.\n")
    org         = plot_data(ticker_name)
    org.plot_one(feature)
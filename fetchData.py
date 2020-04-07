import packages

class fetchData:
    def __init__(self, ticker_name):
        ''' Function for initializing class variables. '''
        self.st_year = 0
        self.end_year = 0
        self.st_month = 0
        self.st_date = 0
        self.end_month = 0
        self.end_date = 0
        self.tick = ticker_name
        self.search_engine = 'yahoo'

    def set_start_date(self):
        ''' Function for setting start date. ''' 
        self.st_date = int(input("Enter start date: "))        
        self.st_month = int(input("Enter start month: "))
        self.st_year = int(input("Enter start year: "))
        
    def set_end_date(self):
        ''' Function for setting end date. '''
        self.end_date = int(input("Enter end date: "))
        self.end_month = int(input("Enter end month: "))
        self.end_year = int(input("Enter end year: "))
        
    def return_df(self):
        ''' Function for returns dataframes loaded with data. '''
        return packages.web.DataReader(self.tick, self.search_engine, self.get_start_date(), self.get_end_date())
    
    def get_start_date(self):
        ''' Function for getting start date. '''
        return packages.dt.datetime(self.st_year, self.st_month, self.st_date)
        
    def get_end_date(self):
        ''' Function for getting end date. '''
        return packages.dt.datetime(self.end_year, self.end_month, self.end_date)
    
    def save_csv(self):
        ''' Function saves stock data in CSV. '''
        file_name = self.tick + '.csv'
        self.return_df().to_csv(file_name) 

if __name__ == "__main__":        
    ticker_name = input("Enter company's ticker name for gathering data.\n")
    org = fetchData(ticker_name)
    org.set_start_date()
    org.set_end_date()
    org.save_csv()
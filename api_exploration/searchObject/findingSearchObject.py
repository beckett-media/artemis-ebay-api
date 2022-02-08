from time import strptime

# This is meant to create amn easier to understand search object to put data into. 

# searchObject is meant for the results of an eBay findItems search object. 


class findingSearchObject: 
    
    # default params
    title = 'title'
    categoryId = 1
    categoryName = 'categoryName'
    currentPrice = 0
    currencyId = 'USD'
    listingDate = strptime('2000-01-01', '%Y-%m-%d')


    def __init__(self, title, categoryId, categoryName, currentPrice, listingDate, currencyId='USD'):
        self.title = title
        self.categoryId = categoryId
        self.categoryName = categoryName
        self.currentPrice = currentPrice
        self.currencyId = currencyId
        self.listingDate = listingDate
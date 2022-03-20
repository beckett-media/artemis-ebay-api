from ebaysdk.merchandising import Connection as merchandising_connection
from ebaysdk.finding import Connection as finding_connection
from searchObject.findingSearchObject import findingSearchObject
import keyring

beckett_appid = keyring.get_password('ebay', 'beckett_appid')
api = finding_connection(appid=beckett_appid, config_file=None, siteid="EBAY-US")
responseItems = []

def save_responses(payload, response_items):
    for response in payload:
        title = response.title
        categoryId = response.primaryCategory.categoryId
        categoryName = response.primaryCategory.categoryName
        currentPrice = response.sellingStatus.currentPrice.value
        currencyId = response.sellingStatus.currentPrice._currencyId
        listingStartTime = response.listingInfo.startTime
        response_object = findingSearchObject(title, categoryId, categoryName, currentPrice, currencyId, listingStartTime)
        responseItems.append(response_object)
    return responseItems

for pageNum in range(0, 100):
    payload = {
            'keywords': 'Baseball', 
            'categoryId': ['212'],
            'itemFilter': [
                {'name': 'LocatedIn', 'value': 'US'},
            ],
            'sortOrder': 'StartTimeNewest',
            'pagination': [
                {'entriesPerPage': '100', 'pageNumber': pageNum}
            ]
    }
    unsold_items_response = api.execute('findItemsAdvanced', payload)
    responseItems = save_responses(unsold_items_response.reply.searchResult.item, responseItems) 


for listing in responseItems:
    print(listing.title)

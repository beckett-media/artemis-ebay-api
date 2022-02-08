from ebaysdk.merchandising import Connection as merchandising_connection
from ebaysdk.finding import Connection as finding_connection


# api = Connection(config_file='ebay.yaml')
api = merchandising_connection(appid='Beckett86-b7b6-45a9-ae8a-8734862ecdd', config_file=None)
most_watched = api.execute('getMostWatchedItems', {})
# print(most_watched)
# print(most_watched.reply.itemRecommendations.item)

api = finding_connection(appid='Beckett86-b7b6-45a9-ae8a-8734862ecdd', config_file=None, siteid="EBAY-US")
payload = {
        'keywords': 'Baseball', 
        'categoryId': ['212'],
        'itemFilter': [
            {'name': 'LocatedIn', 'value': 'US'},
        ],
        'sortOrder': 'StartTimeNewest',
}
response = api.execute('findItemsAdvanced', payload)
print(response)
print(dir(response.reply.searchResult))
print(response.reply.searchResult)

for response in response.reply.searchResult.item:
    print(response.title) 

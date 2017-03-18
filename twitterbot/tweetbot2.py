from twython import Twython
import csv

CONSUMER_KEY = '8nTQnIt6oSgdPQYMYzbsTKT7U'
CONSUMER_SECRET = 'WxMGfGOLpgK1RJhEILrm09Eio36M0WkVSsvNVdmhwZXtzzN78h'
ACCESS_TOKEN = '839156510487904256-IMZs9vZDRjCh6LqrdnfNZFHoGJCgNsz'
ACCESS_TOKEN_SECRET = 'QZ2z0cySm2aR4FXApnbthbrPrDRNwJniTPEIDiBg9FMWQ'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search = twitter.search(q='YOUR SEARCH TERM HERE', count="100")
tweets = search['statuses']

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('Search Term', 'Tweet Text', 'URL'))

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['AARP', result['text'].encode('utf-8'), url]]
        a.writerows((text))

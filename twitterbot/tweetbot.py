from twython import Twython, TwythonError

CONSUMER_KEY = '8nTQnIt6oSgdPQYMYzbsTKT7U'
CONSUMER_SECRET = 'WxMGfGOLpgK1RJhEILrm09Eio36M0WkVSsvNVdmhwZXtzzN78h'
ACCESS_TOKEN = '839156510487904256-IMZs9vZDRjCh6LqrdnfNZFHoGJCgNsz'
ACCESS_TOKEN_SECRET = 'QZ2z0cySm2aR4FXApnbthbrPrDRNwJniTPEIDiBg9FMWQ'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

try:
    twitter.update_status(status='See how easy this was?')
except TwythonError as e:
    print e

# read from csv

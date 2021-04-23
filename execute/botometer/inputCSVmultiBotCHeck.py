import botometer
import pandas

#REF https://github.com/IUNetSci/botometer-python

rapidapi_key = "RAPID API KEY HERE" #Enter your Rapid API key here USE "Quotations"
twitter_app_auth = {
    'consumer_key': 'CONSUMER KEY HERE', #Enter your Rapid API key here USE 'Single Quotation'
    'consumer_secret': 'CONSUMER SECRET HERE', #Enter you Consumer Secret here USE 'Single Quotation'
    'access_token': 'ACCESS TOKEN HERE', #Enter you ACCESS TOKEN here USE 'Single Quotation'
    'access_token_secret': 'ACCESS TOKEN SECRET HERE', #Enter you ACCESS TOKEN SECRET here USE 'Single Quotation'
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)


colnames = ['id',	'username',	'acctdesc',	'location',	'language',	'following',	'followers',	'usercreatedts','verified'	,'tweetcreatedts',	'retweetcount',	'favouritecount',	'text',	'hashtags',	'profilePic',	'acctdescWEB',	'textWEB','ratio']
data = pandas.read_csv('data/cleaning/cleanedA.csv', names=colnames)

names = data.username.tolist()


for screen_name, result in bom.check_accounts_in(names):
    # Do stuff with `screen_name` and `result`
    print(result)


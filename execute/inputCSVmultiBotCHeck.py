import botometer
import pandas

#REF https://github.com/IUNetSci/botometer-python

rapidapi_key = "f1b0c74185msha822cc8331a8616p1d253fjsnfdc39667967e"
twitter_app_auth = {
    'consumer_key': '2Gghe6x0e3ZGIOEe4G7b24P6Y',
    'consumer_secret': 'P6i2cOSjObR9dCGyOaSj3Kq2EiYJgkqrQ3tf3YDESAvPLQkP17',
    'access_token': '1338758125982126080-3mvp7P0CrvkrAZeolx3Uz4YsMivPYU',
    'access_token_secret': 'QUOSw2B63U60nW3rsW4u72zoVCXPPgt4ANpubJ6zFx0UC',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)


colnames = ['id',	'username',	'acctdesc',	'location',	'language',	'following',	'followers',	'usercreatedts','verified'	,'tweetcreatedts',	'retweetcount',	'favouritecount',	'text',	'hashtags',	'profilePic',	'acctdescWEB',	'textWEB','ratio']
data = pandas.read_csv('data/cleaning/cleanedA.csv', names=colnames)

names = data.username.tolist()

#accounts = ['@clayadavis', '@jplow21', '@joebiden']
for screen_name, result in bom.check_accounts_in(names):
    # Do stuff with `screen_name` and `result`
    print(result)


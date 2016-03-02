#
#	Fitbit python api
#
#	Production Template
#
#	This template is for use during production. 		
#	The initial start up requires the user to open the browser
#	
#	Aaron Fordham


#import libraries obviously
import fitbit
import ConfigParser
import time
import datetime
from dateutil.parser import parse    

#get keys from config file
parser = ConfigParser.SafeConfigParser()
parser.read('alarm.ini')

configName = 'param'

access_key = parser.get(configName, 'a_key')
consumer_secret = parser.get(configName, 'c_secret')


code = '444c183b42ff165f457dae6f17100754d071f6c7'
redirect_uri = 'http://127.0.0.1:8080/'

client = fitbit.Fitbit(access_key, consumer_secret, oauth2=True)

id = '110125576'


# Although this says expires in 86400, it uses a different authotencation system than first thought. Therefore that parameter isn't needed.
print client.client.authorize_token_url(expires_in = '86400', redirect_uri='http://127.0.0.1:8080/')

# The line above returns a code at the end of the URL. Copy and paste this into the terminal as stin. 
code = raw_input()

# This line gathers the access token and refresh token
client.client.fetch_access_token(code = code, redirect_uri = redirect_uri)

while True:

	# refresh tokens. Refresh tokens last for 14 days
	# this is compared to access tokens which last for an hour
	# Therefore, it is imperative that the tokens get refreshed at the
	# start of the loop.

	client.client.refresh_token()



	s  = '13:30+0800'
	dt = parse("13:40+0800")

	
	# DO STUFF
	#print client.sleep()
	print client.get_devices()
	test = client.get_alarms(device_id='110125576')
	print test
	test = client.add_alarm(device_id='110125576', alarm_time=dt, enabled=True, week_days=['TUESDAY'])	
	
	print test

	# Halt program for a certain time before starting the loop again.
	time.sleep(1800)



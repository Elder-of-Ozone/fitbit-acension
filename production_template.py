#
#	Prouction Template for Fitbit
#
#	If you're reading this, this is just a template
#	It serves no purpose but authenticates a fitbit api user
#	
#	You do however need to do a few things first.
#	They are written in the script but this is the TL:DR version.
#	So atleast you know.
#	
#	1.  I encourage you to read the fitbit API section on authentication	
#	2.  This script utilises a config parser. Ensure that you
#	have a config file named 'config.ini' with the following properties
#		[param]
#		a_key = [access key]
#		c_secret = [consumer secret]
#	substituting the approperiate values for the above.
#	3.  When you run the file, a link will open. Please click on the link
#	4a. In the browser, it won't open. THIS FAILURE IS TO BE EXPECTED!
#	4b. Right, in the link, it should say code=<NUMBERS OR LETTERS>
#	5a. Copy this code and paste this back into the script. 
#	5b. There is raw input that will allow the above to occur.
#	6.  The script should loop infinititely. 
#
#	This script is powered from the python-fitbit api 
#	Many thanks to Orcisgit
#	
#	Aaron Fordham


#import libraries obviously

import fitbit
import ConfigParser
import time

# get keys from config file

parser = ConfigParser.SafeConfigParser()
parser.read('config.ini')

configName = 'param'

access_key = parser.get(configName, 'a_key')
consumer_secret = parser.get(configName, 'c_secret')

code = '444c183b42ff165f457dae6f17100754d071f6c7'
redirect_uri = 'http://127.0.0.1:8080/'

client = fitbit.Fitbit(access_key, consumer_secret, oauth2=True)

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

	# DO STUFF
	#print client.sleep()
	
	
	# Halt program for a certain time before starting the loop again.
	time.sleep(1800)



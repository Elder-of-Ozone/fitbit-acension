# It All Starts With The Shebang!
#!/usr/bin/python2.7

import fitbit
import ConfigParser
import time
import shutil
import os

# Save a file named config.ini with the following contents:
# c_id      = [INSERT YOUR CLIENT ID]
# c_secret  = [INSERT YOUR CLIENT SECRET]


# first we read our config file
parser = ConfigParser.RawConfigParser()
parser.read('config.ini')

# Then we get our client id and secrets. 
configName = 'param'

client_id = parser.get(configName, 'c_id')
client_secret = parser.get(configName, 'c_secret')

# Now we check if we have already logged in.
# TO DO: Check if refresh token has expired (~ 14 days). 
try:
    refresh_token = parser.get(configName, 'r_token')
    access_token = parser.get('param', 'a_token')

    refresh_token = unicode(refresh_token, "utf-8")
    access_token =  unicode(access_token, "utf-8")
    print "Access and Refresh token already created, so let's create our model."

    # Now we create our client model. Note we have oauth2 = true 
    #since oauth1.0 is depreceiated.
    client = fitbit.Fitbit(client_id, client_secret, oauth2=True, access_token = access_token, refresh_token = refresh_token) 
    

except:

    client = fitbit.Fitbit(client_id, client_secret, oauth2=True)


    print client.client.authorize_token_url(expires_in = '86400', redirect_uri='http://127.0.0.1:8080/')
    
    code = raw_input()

    redirect_uri = 'http://127.0.0.1:8080/'
    client.client.fetch_access_token(code = code, redirect_uri = redirect_uri)

    refresh_token = client.client.token['refresh_token']
    access_token = client.client.token['access_token']

    parser.set(configName, 'r_token', refresh_token)
    parser.set(configName, 'a_token', access_token)
    
    with open('config.ini', 'wb') as configfile:
        parser.write(configfile)
    pass

while True:

        client.client.refresh_token()
	# DO STUFF
        
        print client.sleep()
       

        refresh_token = client.client.token['refresh_token']
        access_token = client.client.token['access_token']

        parser.set(configName, 'r_token', refresh_token)
        parser.set(configName, 'a_token', access_token)
       
        config = open("config.ini",'wb')
        parser.write(config)
        config.close()

        # Halt program for a certain time before starting the loop again. 
        time.sleep(30)



#------------------------------------------------
#
#	Ascending Fitbit with Google Calendar 
#	And linux.......
#
#	Written by
#	Aaron Fordham
#------------------------------------------------
#
#	This script will upload your google calendar
#	events to your fitbit. In essence, this will
#	create a silent alarm to alert you hours before
#	your event is to start.
#
#	There is a lengthy process in order to set up
#	developer apps for both google calendar and
#	fitbit. If you have any troubles feel free to
#	issue a ticket on github.
#
#
#------------------------------------------------
#
#	
#
#	HOW TO USE
#
#	This documentation is for me as much as it is for
#	you. 
#
#	Make sure you have calendarEvents.py in the working 
#	directory. CalendarEvents is simply a python script
#	to get calendar events. It is fundamental that you can
#	run this script independently of this program. 
#
#
#
#------------------------------------------------
#
#
#	SET UP
#
#
#
#
#------------------------------------------------
#
#	Class breakdown and program flow
#
#	These are just my notes. 
#
#	Arguments
#
#	-d  semi-daemon mode (just loops every hour)
#		-default is one off
#	-v  version
#	
#	
#
#	class FitbitSilentCalendar
#		functions:
#			init 	 -  
#			addAlarm -
#			getEvent - 
#			
#
#

#
import calendarEvents

import fitbit
import ConfigParser
import time, sys
import datetime


class FitbitSilentCalendar:
	"""
	This class is 

	"""
	def __init__(self):
		print "initialising class. This doesn't really do anything yet"

	def getEvents(self):
		print "Getting events"

	def addAlarm(self):
		print "Adding alarm"
		
	def debug(self, message):
		print message


test = calendarEvents.GetEvents()
events = test.events()

for event in events:
	print event['start'].get('dateTime')


if __name__ == '__main':


	print "test"

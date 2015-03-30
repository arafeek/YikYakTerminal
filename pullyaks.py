import API as pk
import pygeocoder
import requests

#The yakker api
remoteYakker = 0

# Initializes the yakker API
	# -->sets the location
	# -->sets the userID
def initYakker():
	global remoteYakker
	# Initialize Google Geocoder API
	geocoder = pygeocoder.Geocoder("AIzaSyAGeW6l17ATMZiNTRExwvfa2iuPA1DvJqM")

	# Get the location
	try:
		f = open("locationsetting", "r")
		locationInfo = f.read()
		f.close()

		#get the coords
		coords = locationInfo.split("\n")

		location = pk.Location(coords[0],coords[1])
	except fileNotFoundError:
		print("Location information could not be found, ensure 'locationsetting' exists and is non-empty")

	# Get the userID and initialize the yakker API
	try:
		f = open("userID", "r")
		userID = f.read();
		remoteYakker = pk.Yakker(userID, location, False)
	except fileNotFoundError:
		print("No user id information found. Encure 'userID' exists and contains a valid user ID.")




# Pulls all the latest yaks in the area and writes them to yaks.txt
def getNewYaks():
	# Pull down the latest yaks, save them in yaks.txt
	yaks = remoteYakker.get_yaks()
	f = open("yaks.txt","w")
	yakCount = 0
	for yak in yaks:
		f.write(yak.message+"\n")
		yakCount += 1

	f.close()
	print("Retrieved " + str(yakCount) + " yaks")


initYakker()
getNewYaks()

import urllib.request
import json
from datetime import datetime

#J'ai voler ce code de ce site https://www.datasciencelearner.com/how-to-get-json-data-from-url-in-python/
def getResponse(url):
   operUrl = urllib.request.urlopen(url)
   if(operUrl.getcode()==200):
       data = operUrl.read()
       jsonData = json.loads(data)
   else:
       print("Error receiving data", operUrl.getcode())
   return jsonData

#retourne une chaine de charactère on peu changer le format plus d'info ici https://www.programiz.com/python-programming/datetime/timestamp-datetime
def getHourFromTimestamp(timestamp):

	dt_object = datetime.fromtimestamp(timestamp)
	return dt_object.strftime("%H")

#URL hardcodé l'URL ayant un ID unique je saurais pas comment l'automatisé
LaTorcheURL = "https://services.surfline.com/kbyg/spots/forecasts/wave?spotId=5842041f4e65fad6a7708c8b&days=1"

jsonData = getResponse(LaTorcheURL)

for i in jsonData["data"]["wave"]:
	print(getHourFromTimestamp(i["timestamp"])+ 'H' + f' Hauteur : {i["swells"][0]["height"]}, optimal score : {i["swells"][0]["optimalScore"]}')

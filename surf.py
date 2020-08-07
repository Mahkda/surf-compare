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

#On ouvre le fichier avec toutes les IDs et leur noms
spotIDFile = open("spotID")
spotIDArray = []
dictSpot = {}

#On obtient toutes les lignes dans une liste
for line in spotIDFile.readlines():
			spotIDArray.append(line.strip('\n'))

#Tous les spots sont rangé dans un dictionnaire avec leur nom et leur ID
for i in range(len(spotIDArray)):

	listSpot = spotIDArray[i].split()
	dictSpot[str(i+1)] = {'name' : listSpot[0], 'ID' : listSpot[1]}

#Tous les spots sont numérotés et afficher à l'utilisateur pour son choix
for i in range(len(dictSpot)):
	print (str(i+1) + ') ' + dictSpot[str(i+1)]['name'].replace('_',' '))

ID = []

#C'est très la répetition de code mais j'ai la flemme de réfléchir à mieux
#Il serait beaucoup mieux de séparer le input pour la lisibilité mais ça va plus vite comme ça
ID.append(dictSpot[input("entrez le numéro correspondant au premier spot que vous voulez comparez\n")]['ID'])
ID.append(dictSpot[input("entrez le numéro correspondant au deuxième spot que vous voulez comparez\n")]['ID'])

jsonData1 = getResponse("https://services.surfline.com/kbyg/spots/forecasts/wave?spotId=" + ID[0] + "&days=1")
jsonData2 = getResponse("https://services.surfline.com/kbyg/spots/forecasts/wave?spotId=" + ID[1] + "&days=1")

i = 0

Hauteur1= []
Hauteur2= []

#toutes les hauteurs des vagues sont stocké dans leur listes correspondantes
for data in jsonData1["data"]["wave"]:
	#Les données ne sont updaté que toutes les 4 heures mais le site renvoit toutes les heures quand même donc le i%4 permet de réduire les infos qui se répetent
	if (i%4 == 0):
		Hauteur1.append(getHourFromTimestamp(data["timestamp"])+ "H " + str(data["swells"][0]["height"]))
	i += 1

i= 0

for data in jsonData2["data"]["wave"]:
	if (i%4 == 0):
		Hauteur2.append(data["swells"][0]["height"])
	i+=1

#Les espaces sont hardcodé pour que les textes soient bien aligné
print("Hauteur des vagues en mètre\n    Spot 1	Spot 2")
#Hauteur 1 et 2 devrait avoir la même taille
for i in range(len(Hauteur1)):
	print ( str(Hauteur1[i]) + "	" + str(Hauteur2[i]))

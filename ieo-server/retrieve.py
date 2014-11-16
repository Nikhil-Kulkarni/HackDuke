import json
import urllib2
import GraphLoader
import GraphLoader2

def getAddress(lat, long):
    data = json.load(urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?latlng=" +
                                     lat + "," + long + "&key=AIzaSyATwdAhys3Yde0-OA0vLabSkOqsM4KZJm8"))
    address = ""
    for d in data["results"]:
        if any("street_number" in s for s in d):
            address = address + d["short_name"]
        elif any("route" in s for s in d):
            address = address + d["short_name"]
        elif any("locality" in s for s in d):
            city = d["short_name"]
        elif any("postal_code" in s for s in d):
            zipcode = d["short_name"]

    return [ address, city, zipcode ]


def handleRetrieve(vars, response): #lat, long, allergy,, nutrition
    data = json.loads(vars["data"])
    addressInfo = getAddress(vars["lat"], vars["long"])
    allergies = []
    for key in data["allergies"]:
        if data["allergies"][key]:
            allergies.append(key + "-free")

    nutrition = []
    if data["heartdisease"] != "No":
        nutrition.append("low sodium")

    if data["alcoholtobacco"] != "No":
        nutrition.append("low cholesterol")

    GraphLoader.priceGraph(addressInfo[0], addressInfo[1], addressInfo[2], allergies, nutrition)
    GraphLoader2.priceNut(addressInfo[0], addressInfo[1], addressInfo[2], allergies, nutrition)

    return ["text/json", "0"]
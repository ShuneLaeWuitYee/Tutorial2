import urllib2, json, base64
accesstoken = 'AG3SCNP4WZQDCKL3KGNL'
#url='http://data.unistats.ac.uk/api/v4/KIS/Institution/10007772.json'
#url='http://data.unistats.ac.uk/api/v4/KIS/Institution/10003270.json'
url='http://data.unistats.ac.uk/api/v4/KIS/Institution/10007800.json'
#http://data.unistats.ac.uk/api/v4/KIS/Institutions.json
request=urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n',''))
response = urllib2.urlopen(request)
data=json.load(response)
print(data['Name'])
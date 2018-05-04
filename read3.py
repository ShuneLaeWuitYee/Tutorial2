import urllib2, json, base64
accesstoken = 'AG3SCNP4WZQDCKL3KGNL'
institution = '10007772'
course = 'U56119'
page = 0
url = 'http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json'.format(
	institution,
	course)
request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n',''))
response = urllib2.urlopen(request)
data = json.load(response)
dic={}
for d in data:
	if(d['Code']=='SALARY'):
		for i in d['Details']:
			if(i['Code']=='MED'):
				print("Sector Median salary for subject (6 months after graduation) .. ")
				print(i['Value'])
				#print(i['Code'],i['Value'])
			if(i['Code']=='LDMED'):
				print('Sector Median salary for subject (40 months after graduation) ..')
				print(i['Value'])
				#print(i['Code'],i['Value'])
		
#print json.dumps(data,indent=2)
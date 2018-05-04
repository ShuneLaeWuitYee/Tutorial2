import urllib2, json, base64
accesstoken = 'AG3SCNP4WZQDCKL3KGNL'
institution = '10007772'
page=4

for i in range(page+1):
	
	url = 'http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Courses.json?pageIndex={}'.format(
	institution,
	i)
	request = urllib2.Request(url)
	request.add_header(
		"Authorization",
		"Basic "+ base64.encodestring(accesstoken+":").replace('\n','')
		)
	response = urllib2.urlopen(request)
	data = json.load(response)
	for c in data:
		if(c["Title"]=='Computing'):
			print c["KisCourseId"], c["Title"]
		if(c["Title"]=='Software Engineering'):
			print c["KisCourseId"], c["Title"]
		if(c["Title"]=='Accounting'):
			print c["KisCourseId"], c["Title"]


 
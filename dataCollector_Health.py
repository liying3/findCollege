import urllib2
urlbase='http://www.collegefactual.com/majors/health-care-professions/rankings/top-ranked/'

response = urllib2.urlopen(urlbase)
html = response.read()
print html

req=urllib2.Request("http://www.collegedata.com/cs/data/college/college_pg03_tmpl.jhtml?schoolId=10")
response=urllib2.urlopen(req)
the_page=response.read()
f=open('RankHealth\school'+str(1)+'.html','w')

f.write(the_page)
f.close()
	
for i in range(2,57):
	print 'current getting '+str(i)+' of 3341'
	url=urlbase+'p'+str(i)+'.html'
	req=urllib2.Request(url)
	response = urllib2.urlopen(req)
	the_page = response.read()
#print the_page

	f=open('RankHealth\school'+str(i)+'.html','w')

	f.write(the_page)
	f.close()

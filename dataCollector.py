import urllib2
urlbase="http://www.collegedata.com/cs/data/college/college_pg02_tmpl.jhtml?schoolId="

for i in range(2887,3341):
	print 'current getting '+str(i)+' of 3341'
	url=urlbase+str(i)
	req=urllib2.Request(url)
	response = urllib2.urlopen(req)
	the_page = response.read()
#print the_page

	f=open('school\school'+str(i)+'.html','w')

	f.write(the_page)
	f.close()

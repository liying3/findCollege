from HTMLParser import HTMLParser
import re
FilterKeyWord=['span', 'script' ,'style' , 'li']

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.recording = 0
		self.data=''
		self.currentTag='';

	def handle_starttag(self, tag, attributes):
		self.currentTag=tag
		if tag != 'div':
			return
		if self.recording:
			self.recording += 1
			return
		for name, value in attributes:
			if name == 'class' and value == 'profiletabcont':
				print 'head find!!!'
				self.data=''
				break
		else:
			return
		self.recording = 1

	def handle_endtag(self, tag):
		self.currentTag=''
		#self.data+='\n'
		if (tag == 'th' or tag=='td') and self.recording:
			self.data+='\t'
		if tag == 'div' and self.recording:
			self.recording -= 1
			if self.recording==0:
				print 'end find!!!'
				#print self.data
		
	def handle_data(self, data):
		if self.recording and (not (self.currentTag in FilterKeyWord)):# and re.match(r"[^ \t\f\v]",data)!=None:
			#self.data+=self.currentTag
			self.data+=data
			#self.data+='\n'


for i in range(6,3341):
	print i
	f=open('Tuition\school'+str(i)+'.html','r')
	content=f.read()		
	parser = MyHTMLParser()
	parser.feed(content)
	#print parser.data
	output=open('infoRaw\school'+str(i)+'.txt','a')
	output.write(parser.data)
	output.close()
	f.close()
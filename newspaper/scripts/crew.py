#Vaughn Johnson Oct. 19 Create HTML Enquirer contact page
from numpy import arange

with open('crew.txt') as f:
    x = f.readlines()

contacts = []
i = 0
for line in x:
	if line == '\n':
		contacts.append("%s%s%s" %(x[i-3],x[i-2],x[i-1]))
	i+=1

contacts = [x.rsplit('\n',4) for x in contacts]
for i in range(0,19):
	contacts[i].remove('')

for i in contacts:
	if 'Artist' in i[1]:
		print '<!-- %s -->'%i[0]
		print '<div class="card">'
		print ''
		print '	<div class="thumbnail" ></div>'
		print ''
		print '	<div class="contact">'
		print '		<p><strong>%s</strong></p>'%i[0]
		print '		<p><a href="mailto:%s" target="_top">%s</a></p>'%(i[2],i[2])
		print '	</div>'
		print '</div>'
		print ''
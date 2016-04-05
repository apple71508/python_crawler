import tool_crawler_v2 as tool
import os

# Input should be like : http://www.xiumm.cc/photos/FeiLin-5110
# Original url : http://www.xiumm.cc/photos/FeiLin-5110.html to 
#	        	 http://www.xiumm.cc/photos/FeiLin-5110-11.html

url = input("Enter the url : ")
#mode = input("Type 0 to download, 1 to generate the html file of img links : ")
mode = 1

tool.url = url
tool.mode = mode

if int(mode) == 0:
	os.mkdir('./temp')

i = 1 # The page counter
while True:
	if i == 1:
		real_url = url + '.html' 
	else:
		real_url = url + '-' + str(i) + '.html'
	if int(tool.extract_img(real_url)) == 0:
		break
	i += 1

if int(mode) == 1:
	tool.genHtml()

print("done!")
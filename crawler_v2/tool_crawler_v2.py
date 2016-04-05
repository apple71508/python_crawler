import requests
from pyquery import PyQuery as pq

pic_count = 0
mode = 0
url = ''
list_img_src = []

def check_str(str_a, str_b):	# Search if str_a in str_b
	if str_a in str_b:
		return True
	else:
		return False

def extract_img(real_url):
	r = requests.get(real_url)
	if str(r.status_code) == '404':
		return 0
	s = pq(r.text)
	global pic_count
	global mode
	for img_tag in s('img'):
		if check_str( 'data', str( pq(img_tag).attr('src') ) ):
			if int(mode) == 0:
				url_img = pq(img_tag).attr('src') 
				r_img = requests.get(url_img)
				file_name = str(pic_count)
				f = open('./temp/' + file_name +'.jpg','wb')
				f.write(r_img.content)		
				f.close
				pic_count += 1
				print("{0:>2}.jpg -> {1} Bytes...done".format(file_name,r_img.headers['content-length']))
			elif int(mode) == 1:
				list_img_src.append( pq(img_tag).attr('src') )
				pic_count += 1
	return 1

def genHtml():
	global list_img_src
	global url
	f = open( url.split('/')[-1] + '.html', 'w')
	f.write('<html>\n')
	f.write('<body>\n')
	f.write('<a href=' + url + '.html><h3>Link</h3></a></br>\n')
	for src in list_img_src:
		f.write('<img src=' + src + ' >\n')
	f.write('</body>\n')
	f.write('</html>\n')
	f.close()

def get_max_page(): # Use internel to get max page number but slow
	count_page = 2
	while True:
		page_url = url + '-' + str(count_page) + '.html'
		temp_r = requests.get(page_url)
		if str(temp_r.status_code) == '404':
			break
		count_page += 1
	return count_page - 1

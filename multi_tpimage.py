import threading , requests , os
lock = threading.Lock()
url = raw_input("enter the url :") # ex : http://img.haokantu.com/TPimage/2010/18/####.jpg
os.mkdir('./tpimage_temp')
def dojob(*args):
	pic_count = int(args[0])
	global url
	while True:
		if pic_count < 10:
			temp_url = url + '000' + str(pic_count) + '.jpg'
		elif pic_count < 100:
			temp_url = url + '00' + str(pic_count) + '.jpg'
		else:
			temp_url = url + '0' + str(pic_count) + '.jpg'
		r = requests.get(temp_url)
		if int(r.headers['content-length']) < 5000:
			break
		file_name = str(pic_count)
		f = open('./tpimage_temp/'+file_name+'.jpg','wb')
		f.write(r.content)
		f.close
		pic_count += 3 
		lock.acquire()
		print("{0:>2}.jpg -> {1} Bytes...done".format(file_name,r.headers['content-length']))
		lock.release()

thd1 = threading.Thread(target=dojob,name='Thd1',args=(0,))
thd2 = threading.Thread(target=dojob,name='Thd2',args=(1,))
thd3 = threading.Thread(target=dojob,name='Thd3',args=(2,))

thd1.start()
thd2.start()
thd3.start()

while thd1.is_alive() or thd2.is_alive() or thd3.is_alive():
	pass

print "done!"  
os.system("PAUSE")
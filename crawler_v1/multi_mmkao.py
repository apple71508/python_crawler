import threading , requests , os , shutil
lock = threading.Lock()
url = input("enter the url :") 
# ex : http://img.mmkao.net/photo/ROSI/rosi982/##.jpg
num_pic = input("enter the number of images :")
if os.path.isdir('./ROSI_temp'):
	shutil.rmtree('./ROSI_temp')
	os.mkdir('./ROSI_temp')
else: 
	os.mkdir('./ROSI_temp')

def dojob(*args):
	pic_count = int(args[0])
	global url
	while True:
		if pic_count < 10:
			temp_url = url + '0' + str(pic_count) + '.jpg'
		elif pic_count < 100:
			temp_url = url + str(pic_count) + '.jpg'
		r = requests.get(temp_url)
		if pic_count > int(num_pic) + 1:
			break
		file_name = str(pic_count)
		f = open('./ROSI_temp/'+file_name+'.jpg','wb')
		f.write(r.content)
		f.close
		pic_count += 3
		lock.acquire()
		print("{0:>2}.jpg -> {1} Bytes...done".format(file_name,r.headers['content-length']))
		lock.release()

thd1 = threading.Thread(target=dojob,name='Thd1',args=(2,))
thd2 = threading.Thread(target=dojob,name='Thd2',args=(3,))
thd3 = threading.Thread(target=dojob,name='Thd3',args=(4,))

thd1.start()
thd2.start()
thd3.start()

while thd1.is_alive() or thd2.is_alive() or thd3.is_alive():
	pass

print ("done!")

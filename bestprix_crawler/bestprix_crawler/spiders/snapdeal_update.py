import scrapy
import MySQLdb
import sys
counter = 0
updated_list = []
none_count = 0
# url_list=set()
class snapdeal_update(scrapy.Spider):
	name = "snapdeal_update"
	start_urls = []
	db = MySQLdb.connect("localhost","root","root","bestprix_db" )
	cursor = db.cursor()
	sql = "SELECT url from web_app_snapdeal ORDER BY id LIMIT 10"
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			# print row[0]
			start_urls.append(row[0])
	except:
		print "Error: unable to fecth data"
	db.close()

	print "total:",len(start_urls)

	def db_queue(self, response):
		global counter
		global updated_list
		global none_count
		# //*[@id="soldOrDiscontPriceBox"]/div[2]/span/span
		price = response.xpath('//*[@class="payBlkBig"]/text()').extract_first()
		# price = response.xpath('//span[contains(@class, "payBlkBig")]/text()').extract()
		if price is not None:
			price = int(price.replace(',', ''))
			# url = response.url
			# db = MySQLdb.connect("localhost","root","root","bestprix_db" )
			# cursor = db.cursor()
			# sql = "UPDATE web_app_snapdeal SET price=%d WHERE url='%s'" % (price,url)
			# try:
			# 	cursor.execute(sql)
			# 	db.commit()
			counter += 1
			sys.stdout.write('\r')
			# the exact output you're looking for:
			sys.stdout.write("count:"+str(counter)+"\t")
			sys.stdout.flush()
			# print "count==>",counter
			# except Exception:
			# 	db.rollback()
			# db.close()
			updated_list.append({"price":price,"url":response.url})
		else:
			# print "price ==>",price,"\n",response.url
			none_count+=1

	def parse(self, response):
		if response.status is 200:
			if response.xpath('//*[@class="payBlkBig"]'):
				self.db_queue(response)
		else:
			print "ERROR ---->",response.url,"\nstatus---->",response.status

	def closed(self, reason):
		print "-"*50
		global updated_list
		global none_count
		t_len = len(updated_list)
		print "UPDATED LIST:",t_len,"\t|"
		print "-"*50
		print "None count:",none_count,'\t|'
		print "-"*50
		db = MySQLdb.connect("localhost","root","root","bestprix_db" )
		cursor = db.cursor()
		# print len(updated_list)

		for r in updated_list:
			t_len-=1
			sys.stdout.write('\r')
			# the exact output you're looking for:
			sys.stdout.write("Left:"+str(t_len)+" "*10)
			sys.stdout.flush()
			sql = "UPDATE web_app_snapdeal SET price=%d WHERE url='%s'" % (r['price'],r['url'])
			try:
				cursor.execute(sql)
			except Exception:
				print "Error: unable to update in database"
		db.commit()
		db.close()

		print "\n"
		print "UPDATED LIST:",t_len,"\t|"
		print "-"*50
		print "None count:",none_count,'\t|'
		print "-"*50
		print "\n"

import scrapy
import MySQLdb

url_list=set()
class flipkart(scrapy.Spider):
	name = "infibeam"
	start_urls = [
		'https://www.infibeam.com/',
	]
	allowed_domains = ["infibeam.com"]

	def db_ops(self, response):
		name = response.xpath('//*[@id="title-mob"]/h1/text()').extract_first()
		price = response.xpath('//*[@id="price-after-discount"]/span[2]/text()').extract_first()
		price = int(price.replace(',', ''))
		url = response.url
		db = MySQLdb.connect("localhost","root","root","bestprix_db" )
		cursor = db.cursor()
		sql = "INSERT INTO web_app_infibeam (id, name, url, price) VALUES (NULL, '%s', '%s', %d)" % (name,url,price)
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
		db.close()

	def parse(self, response):
		global url_list
		if response.xpath('//*[@id="price-after-discount"]/span[2]') and response.xpath('//*[@id="title-mob"]/h1'):
			self.db_ops(response)
		else:
			urls=response.xpath('//a/@href').extract()
			for href in urls:
				url=response.urljoin(href)
				if url not in url_list:
					url_list.add(url)
					yield scrapy.Request(url, callback=self.parse)
			# else:
			# 	pass

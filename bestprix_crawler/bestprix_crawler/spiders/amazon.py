import scrapy
from scrapy_splash import SplashRequest
import MySQLdb

url_list=set()
class flipkart(scrapy.Spider):
	name = "amazon"
	start_urls = [
		 'http://www.amazon.in/',
	]
	allowed_domains = ["www.amazon.in"]

	def start_requests(self):
		for url in self.start_urls:
			yield SplashRequest(url, self.parse,endpoint='render.html',args={'wait': 1},)

	def db_ops(self, response):
		name = response.xpath('//*[@id="productTitle"]/text()').extract_first().strip()
		price = response.xpath('//span[contains(@id, "priceblock_")]/text()').extract_first()
		try:
			price = int(float(price.replace(',', '').replace(' ','').replace('-','')))
		except Exception:
			return
		url = response.url
		db = MySQLdb.connect("localhost","root","root","bestprix_db" )
		cursor = db.cursor()
		sql = "INSERT INTO web_app_amazon (id, name, url, price) VALUES (NULL, '%s', '%s', %d)" % (name,url,price)
		try:
			cursor.execute(sql)
			db.commit()
		except Exception:
			db.rollback()
		db.close()


	def parse(self, response):
		if response.status is 200:
			if response.xpath('//*[@id="productTitle"]'):
				self.db_ops(response)
			else:
				urls=response.xpath('//a/@href').extract()
				for href in urls:
					url=response.urljoin(href)
					yield SplashRequest(url, self.parse,endpoint='render.html',args={'wait': 1},)
		else:
			pass

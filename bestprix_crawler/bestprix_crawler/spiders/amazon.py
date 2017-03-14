import scrapy
from scrapy_splash import SplashRequest
import MySQLdb

url_list=set()
class flipkart(scrapy.Spider):
	name = "amazon"
	start_urls = [
		 'http://www.amazon.in/',
		# 'http://www.amazon.in/OnePlus-3T-Gunmetal-6GB-64GB/dp/B01FM8M0XE/ref=br_asw_pdt-1?pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=0DW4QR2SCDGRXJ5BB8ZJ&pf_rd_t=36701&pf_rd_p=c80a0bb1-6a98-40cb-b035-91b6b9e0fbbf&pf_rd_i=desktop',
		# 'http://www.amazon.in/Exclusive-Dummy-ASIN197/dp/B01NCN4ICO/ref=br_asw_pdt-2?pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=0DW4QR2SCDGRXJ5BB8ZJ&pf_rd_t=36701&pf_rd_p=c80a0bb1-6a98-40cb-b035-91b6b9e0fbbf&pf_rd_i=desktop',
	]
	# with open('data/allurl_cat_test.txt', 'rb') as f:
	# 	for line in f:
	# 		start_urls.append(line)
	# 	f.close()

	allowed_domains = ["amazon.in"]
	def start_requests(self):
		for url in self.start_urls:
			yield SplashRequest(url, self.parse,endpoint='render.html',args={'wait': 0.5},)

	def db_ops(self, response):
		name = response.xpath('//*[@id="productTitle"]/text()').extract_first().strip()
		price = response.xpath('//span[contains(@id, "priceblock_")]/text()').extract_first()
		price = int(float(price.replace(',', '')))
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
					yield SplashRequest(url, self.parse,endpoint='render.html',args={'wait': 0.5},)
		else:
			pass

import scrapy
import MySQLdb

# url_list=set()
class snapdeal(scrapy.Spider):
	name = "snapdeal"
	start_urls = [
		'https://www.snapdeal.com/',
	]
	allowed_domains = ["www.snapdeal.com"]

	def db_ops(self, response):
		name = response.xpath('//*[@id="productOverview"]/div/div/div/div/div/h1/text()').extract_first().strip()
		price = response.xpath('//*[@id="buyPriceBox"]/div/div[1]/div/div/span/span/text()').extract_first()
		price = int(price.replace(',', ''))
		url = response.url
		db = MySQLdb.connect("localhost","root","root","bestprix_db" )
		cursor = db.cursor()
		sql = "INSERT INTO web_app_snapdeal (id, name, url, price) VALUES (NULL, '%s', '%s', %d)" % (name,url,price)
		try:
			cursor.execute(sql)
			db.commit()
		except Exception:
			db.rollback()
		db.close()

	def parse(self, response):
		# global url_list
		if response.status is 200:
			if response.xpath('//*[@id="productOverview"]/div/div/div/div/div/h1') and response.xpath('//*[@id="buyPriceBox"]/div/div/div/div/span/span'):
				self.db_ops(response)
			else:
				urls=response.xpath('//a/@href').extract()
				for href in urls:
					url=response.urljoin(href)
					yield scrapy.Request(url, callback=self.parse)
		else:
			pass

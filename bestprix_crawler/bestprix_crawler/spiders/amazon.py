import scrapy
from scrapy_splash import SplashRequest

url_list=set()
class flipkart(scrapy.Spider):
	name = "amazon"
	start_urls = [
		# 'http://www.amazon.in/',
		'http://www.amazon.in/gp/product/B01FM8M0XE/ref=s9_acss_bw_en_WLEV_d_1_1_w?pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-top-1&pf_rd_r=1EBBQRGCQD7E4J1DXWSM&pf_rd_r=1EBBQRGCQD7E4J1DXWSM&pf_rd_t=101&pf_rd_p=a4ac5afa-117c-4247-95ea-7b4b58e44b8b&pf_rd_p=a4ac5afa-117c-4247-95ea-7b4b58e44b8b&pf_rd_i=1389401031',
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
		if response.xpath('//*[@id="priceblock_ourprice"]'):
			price = response.xpath('//*[@id="buyPriceBox"]/div/div[1]/div/div/span/span/text()').extract_first()
		#elif response.xpathexi
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
		print response.url
		# if response.status is 200:
		# 	if response.xpath('//*[@id="productTitle"]'):
		# 		self.db_ops(response)
		# 	else:
		# 		urls=response.xpath('//a/@href').extract()
		# 		for href in urls:
		# 			url=response.urljoin(href)
		# 			yield SplashRequest(url, self.parse,endpoint='render.html',args={'wait': 0.5},)
		# else:
		# 	pass
		#

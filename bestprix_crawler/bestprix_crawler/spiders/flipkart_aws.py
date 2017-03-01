import scrapy
from scrapy_splash import SplashRequest

url_list=set()
class flipkart(scrapy.Spider):
	name = "flipkart_aws"
	start_urls = ['https://www.flipkart.com/redmi-note-4-gold-64-gb/p/itmeqg86fjyzkdq8?pid=MOBEQ98MNXHY4RU9&srno=b_1_1&otracker=browse&lid=LSTMOBEQ98MNXHY4RU9XEFSBA',]
	# with open('data/allurl_cat_test.txt', 'rb') as f:
	# 	for line in f:
	# 		start_urls.append(line)
	# 	f.close()

	allowed_domains = ["flipkart.com"]
	def start_requests(self):
		for url in self.start_urls:
			yield SplashRequest(url, self.parse,endpoint='render.html',args={'wait': 0.5},)

	def parse(self, response):
		if response.xpath('//*[@id="container"]/div/div/div/div/div/div/div/div/div/div/h1/text()'):
			product_name=response.xpath('//*[@id="container"]/div/div/div/div/div/div/div/div/div/div/h1/text()').extract()
			product_price=response.xpath('//*[@id="container"]/div/div/div/div/div/div/div/div/div/div/div/div/text()').extract()

		# response.body is a result of render.html call; it
		# contains HTML processed by a browser.
	# def parse(self, response):
	# 	print response.xpath('//*[@id="container"]/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[3]/div/div/div[1]').extract()
		# global url_list
		# urls=response.xpath('//a/@href').extract()
		# for href in urls:
		# 	url=response.urljoin(href)
		# 	if url not in url_list:
		# 		url_list.add(url)
		# 		with open('data/allurl_test.txt', 'ab') as f:
		# 			f.write(url+"\n")
		# 			f.close()
		# 		yield scrapy.Request(url, callback=self.parse)
		# 	else:
		# 		pass

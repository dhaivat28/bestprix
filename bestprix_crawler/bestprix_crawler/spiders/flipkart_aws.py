import scrapy
from scrapy_splash import SplashRequest

# url_list=set()
class flipkart(scrapy.Spider):
	name = "flipkart_aws"
	start_urls = [
		'https://www.flipkart.com/apple-iphone-6-space-grey-16-gb/p/itme8dvfeuxxbm4r',
	]
	allowed_domains = ["flipkart.com"]
	def start_requests(self):
		for url in self.start_urls:
			yield SplashRequest(url, self.parse,endpoint='render.html',args={'wait': 0.5},)

	def parse(self, response):
		print response.xpath('//*[@id="container"]/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[3]/div/div/div[1]').extract()
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

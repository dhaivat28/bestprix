import scrapy
from scrapy_splash import SplashRequest
url_list=[]
class flipkart(scrapy.Spider):
	name = "product_test"
	start_urls = [
		'https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree',
	]

	def start_requests(self):
		for url in self.start_urls:
			yield SplashRequest(url, self.parse,endpoint='render.html',args={'wait': 0.5},)

	def parse(self, response):
		global url_list
		urls=response.xpath('//*[@id="container"]/div/div/div/div/div/div/div/div/a/@href').extract()
		for href in urls:
			hurl=response.urljoin(href)
			if hurl not in url_list:
				url_list.append(hurl)
				with open('data/product_test.txt', 'ab') as f:
					f.write(hurl+"\n")
					f.close()

	# response.body is a result of render.html call; it
	# contains HTML processed by a browser.

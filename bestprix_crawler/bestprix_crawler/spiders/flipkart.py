import scrapy

url_list=[]
class flipkart(scrapy.Spider):
	name = "flipkart"
	start_urls = [
		'https://www.flipkart.com/',
	]
	allowed_domains = ["flipkart.com"]
	def parse(self, response):
		global url_list
		urls=response.xpath('//a/@href').extract()
		for href in urls:
			url=response.urljoin(href)
			if url not in url_list:
				url_list.append(url)
				with open('/home/sid/Development/allurl2.txt', 'ab') as f:
					f.write(url+"\n")
					f.close()
				yield scrapy.Request(url, callback=self.parse)
			else:
				pass

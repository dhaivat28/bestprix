import scrapy

url_list=set()
class flipkart(scrapy.Spider):
	name = "infibeam"
	start_urls = [
		'https://www.infibeam.com/unboxed-phones/apple-iphone-6-unboxed/P-mobi-80108009355-cat-z.html#variantId=P-mobi-4516313840',
	]
	allowed_domains = ["infibeam.com"]
	def db_ops(self, response):
		price = response.xpath('//*[@id="price-after-discount"]/span[2]/text()').extract_first()
	def parse(self, response):
		#global url_list
		#urls=response.xpath('//a/@href').extract()
		#for href in urls:
		#	url=response.urljoin(href)
		#	if url not in url_list:
		#		url_list.add(url)
		if response.xpath('//*[@id="price-after-discount"]/span[2]'):
			self.db_ops(response)
		#		yield scrapy.Request(url, callback=self.parse)
		#	else:
		#		pass

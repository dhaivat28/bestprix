from django.shortcuts import render
from django.http import HttpResponse
import time
import urllib
import base64
import hmac
import hashlib
import requests
import lxml.etree
import json

def amazon_signed_request(region, params, public_key, private_key, associate_tag=None):
	method = 'GET'
	host = 'webservices.amazon.' + region
	uri = '/onca/xml'
	params['Service'] = 'AWSECommerceService'
	params['AWSAccessKeyId'] = public_key
	params['Timestamp'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
	if associate_tag:
		params['AssociateTag'] = associate_tag
	canonicalized_query = [urllib.quote(param).replace('%7E', '~') + '=' + urllib.quote(params[param]).replace('%7E', '~')
	for param in sorted(params.keys())]
	canonicalized_query = '&'.join(canonicalized_query)
	string_to_sign = method + '\n' + host + '\n' + uri + '\n' + canonicalized_query;
	signature = base64.b64encode(hmac.new(key=private_key, msg=string_to_sign, digestmod=hashlib.sha256).digest())
	signature = urllib.quote(signature).replace('%7E', '~')
	return 'http://' + host + uri + '?' + canonicalized_query + '&Signature=' + signature

def index(request):
	return render(request, 'index.html')

def search(request):
	key = request.GET['q']
	if key.strip():
		#amzon block====================================================================================================>
		amazon_access_key = 'AKIAIBV3ZSCMXLX5DY6A'
		amazon_secret_key = '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'
		m_params={
			'Keywords':key,
			'Operation':'ItemSearch',
			'ResponseGroup':'Images,ItemAttributes,Offers',
			'SearchIndex':'All',
			'Service':'AWSECommerceService'
		}
		amazon_request_url = amazon_signed_request('in',m_params,amazon_access_key,amazon_secret_key,'bestprix09-21')
		print '\nBEGIN REQUEST====AMAZON=====>'
		print '\nRequest URL = ' + amazon_request_url
		amazon_r = requests.get(amazon_request_url)
		print '\nAMAZON===>Response code: %d\n' % amazon_r.status_code
		root = lxml.etree.fromstring(amazon_r.text.encode('utf-8'))
		items = root.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Items')
		item_set = items.findall('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Item')
		for item in item_set:
			for sub_item in item:
				title = sub_item.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Title')
				list_price = sub_item.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}ListPrice')
				if title is not None and list_price is not None:
					price = list_price.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}FormattedPrice')
					print price.text,"\t====>\t",title.text

		#flipkart block====================================================================================================>
		print "_____________________________________________________________________________________________________________"
		flipkart_aff_id='viraj2196'
		flipkart_token='c3636ff662bb4e6d9143a0b54df41c61'
		headers = {
		'Fk-Affiliate-Id': flipkart_aff_id,
		'Fk-Affiliate-Token' : flipkart_token,
		}
		flipkart_request_url='https://affiliate-api.flipkart.net/affiliate/search/json?query='+key+'&resultCount=10'
		print '\nBEGIN REQUEST====FLIPKART=====>'
		flipkart_r = requests.get(flipkart_request_url, headers=headers)
		print '\nRequest URL = ' + flipkart_request_url
		print '\nFLIPKART===>Response code: %d\n' % flipkart_r.status_code
		jsonResponse=json.loads(flipkart_r.text)
		# for p in jsonResponse["productInfoList"]:
		# 	print p
		# title = jsonResponse["productInfoList"][0]["productBaseInfo"]["productAttributes"]["title"]
		# print title
		# return render(request, 'search/index.html')
		for i in xrange(0,len(jsonResponse["productInfoList"])):
			print "INR",jsonResponse["productInfoList"][i]["productBaseInfo"]["productAttributes"]["sellingPrice"]["amount"],"\t====>\t",jsonResponse["productInfoList"][i]["productBaseInfo"]["productAttributes"]["title"]
		print "\n"
		context = {'key':key}
		return render(request, 'search/index.html',context)
		# return HttpResponse(flipkart_r.text,content_type="application/json")
	else:
		return HttpResponse("please enter something")

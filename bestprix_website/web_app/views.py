from django.shortcuts import render
from django.http import HttpResponse
import time
import urllib
import base64
import hmac
import hashlib
import requests
import lxml.etree

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
	key = request.GET['search_key']
	if key.strip():
		#amzon block
		amazon_access_key = 'AKIAIBV3ZSCMXLX5DY6A'
		amazon_secret_key = '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'
		m_params={
			'Keywords':key,
			'Operation':'ItemSearch',
			'ResponseGroup':'Images,ItemAttributes,Offers',
			'SearchIndex':'All',
			'Service':'AWSECommerceService'
		}
		request_url = amazon_signed_request('in',m_params,amazon_access_key,amazon_secret_key,'bestprix09-21')
		print '\nBEGIN REQUEST====AMAZON=====>'
		print 'Request URL = ' + request_url
		r = requests.get(request_url)
		print 'Response code: %d\n' % r.status_code
		root = lxml.etree.fromstring(r.text.encode('utf-8'))
		items = root.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Items')
		item_set = items.findall('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Item')
		for item in item_set:
			for sub_item in item:
				title = sub_item.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Title')
				list_price = sub_item.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}ListPrice')
				if title is not None and list_price is not None:
					price = list_price.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}FormattedPrice')
					print price.text,"\t====>\t",title.text

		#flipkart block
		return render(request, 'search/index.html')
	else:
		return HttpResponse("please enter something")

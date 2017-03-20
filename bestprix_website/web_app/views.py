from django.shortcuts import render
from django.http import HttpResponse
import time
import urllib
import base64
import hmac
import hashlib
import requests

def aws_signed_request(region, params, public_key, private_key, associate_tag=None):
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
		access_key = 'AKIAIBV3ZSCMXLX5DY6A'
		secret_key = '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'
		m_params={
			'Keywords':key,
			'Operation':'ItemSearch',
			'ResponseGroup':'Images,ItemAttributes,Offers',
			'SearchIndex':'All',
			'Service':'AWSECommerceService'
		}
		request_url = aws_signed_request('in',m_params,access_key,secret_key,'bestprix09-21')
		print '\nBEGIN REQUEST++++++++++++++++++++++++++++++++++++'
		print 'Request URL = ' + request_url
		r = requests.get(request_url)
		print 'Response code: %d\n' % r.status_code
		return HttpResponse(r.text,content_type='text/xml')
	else:
		return HttpResponse("please enter something")

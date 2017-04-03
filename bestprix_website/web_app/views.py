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
import MySQLdb

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

def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['pass']
		db = MySQLdb.connect("localhost","root","root","bestprix_db" )
		cursor = db.cursor()
		sql = "SELECT * FROM web_app_user_detail WHERE email_id='%s' AND password='%s'" % (email,password)
		flag = False
		try:
			cursor.execute(sql)
			results = cursor.fetchall()
			if results is not None:
				flag=True
		except Exception:
			print "Error"
		db.close()
		return HttpResponse(flag)
	else:
		return render(request, 'login/index.html')

def signup(request):
	if request.method == 'POST':
		fname = request.POST['fname']
		email = request.POST['email']
		password = request.POST['pass']
		sq = request.POST['sq']
		sa = request.POST['sa']
		db = MySQLdb.connect("localhost","root","root","bestprix_db" )
		cursor = db.cursor()
		sql = "INSERT INTO web_app_user_detail (id, email_id, name, password, s_q, s_a) VALUES (NULL, '%s', '%s', '%s', '%s', '%s')" % (email,fname,password,sq,sa)
		flag = False
		try:
			cursor.execute(sql)
			db.commit()
			flag = True
		except Exception:
			db.rollback()
		db.close()
		return HttpResponse(flag)
	else:
		return HttpResponse("error")

def search(request):
	key = request.GET['q']
	amazon_set=[]
	flipkart_set=[]
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
		try:
			amazon_r = requests.get(amazon_request_url)
			print '\nAMAZON===>Response code: %d\n' % amazon_r.status_code
		except Exception:
			print "\nStatus:Error sending request"
		try:
			if amazon_r.status_code is 200:
				root = lxml.etree.fromstring(amazon_r.text.encode('utf-8'))
				items = root.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Items')
				item_set = items.findall('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Item')
				for item in item_set:
					try:
						# for c in item :
						# 	for a in item.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}OfferSummary'):
						# 		print a
						asin = item.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}ASIN')
						product_url = item.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}DetailPageURL')
						img = item.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}LargeImage')
						offer_price = item.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}OfferSummary')
						LowestNewPrice = offer_price.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}LowestNewPrice')
						try:
							list_price = LowestNewPrice.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Amount')
						except Exception:
							list_price = None
						if img is not None:
							large_img_url = img.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}URL').text
						else:
							img_sets = item.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}ImageSets')
							img_set = img_sets.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}ImageSet')
							large = img_set.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}LargeImage')
							t_img = large.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}URL')
							# print
							# for img_set in img_sets:
							# 	for c in img_set:
							# 		for cc in c:
							# 			pass
							# 			# print cc
							large_img_url = t_img.text
						# print img
						for sub_item in item:
							title = sub_item.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Title')
							# list_price = sub_item.find('{http://webservices.amazon.com/AWSECommerceService/2011-08-01}ListPrice')
							if title is not None and list_price is not None:
								price = int(list_price.text)/100
								# print price,"\t====>\t",title.text
								amazon_set.append({'p_id':asin.text,'title':title.text,'price':price,'url':product_url.text,'img_url':large_img_url,'seller':'amazon'})
					except Exception:
						print "\nStatus: fetch Error"
				print "amazon product count:",len(amazon_set)
			else:
				print "invalid Response"
		except Exception:
			print "\nStatus:Error"
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
		print '\nRequest URL = ' + flipkart_request_url
		try:
			flipkart_r = requests.get(flipkart_request_url, headers=headers)
			print '\nFLIPKART===>Response code: %d\n' % flipkart_r.status_code
		except Exception:
			print "\nStatus:Error sending request"
		try:
			if flipkart_r.status_code is 200:
				jsonResponse=json.loads(flipkart_r.text)
				# for p in jsonResponse["productInfoList"]:
				# 	print p
				# title = jsonResponse["productInfoList"][0]["productBaseInfo"]["productAttributes"]["title"]
				# print title
				# return render(request, 'search/index.html')
				for i in xrange(0,len(jsonResponse["productInfoList"])):
					try:
						p_id = jsonResponse["productInfoList"][i]["productBaseInfo"]["productIdentifier"]["productId"]
						price = jsonResponse["productInfoList"][i]["productBaseInfo"]["productAttributes"]["sellingPrice"]["amount"]
						title = jsonResponse["productInfoList"][i]["productBaseInfo"]["productAttributes"]["title"]
						product_url = jsonResponse["productInfoList"][i]["productBaseInfo"]["productAttributes"]["productUrl"]
						try:
							img = jsonResponse["productInfoList"][i]["productBaseInfo"]["productAttributes"]["imageUrls"]["400x400"]
						except:
							t_img = jsonResponse["productInfoList"][i]["productBaseInfo"]["productAttributes"]["imageUrls"]
							keys = t_img.keys()
							img = t_img[keys[0]]
						#print title,"---->",img
						flipkart_set.append({'p_id':p_id,'title':str(title),'price':int(price),'url':product_url,'img_url':str(img),'seller':'flipkart'})
						# print "INR",jsonResponse["productInfoList"][i]["productBaseInfo"]["productAttributes"]["sellingPrice"]["amount"],"\t====>\t",jsonResponse["productInfoList"][i]["productBaseInfo"]["productAttributes"]["title"]
					except Exception:
						print "\nStatus:fetch Error in product-->",i
				print "flipkart product count:",len(flipkart_set)
				print "\n"
			else:
				print "invalid Response"
		except Exception:
			print "\nStatus:Error"

		product_set = amazon_set + flipkart_set
		# for i in range(len(product_set)):
		# 	print product_set[i]["price"]," => ",product_set[i]["title"]," => ",product_set[i]["seller"]
		sorted_product_set = sorted(product_set, key=lambda k: k['price'],reverse=True)
		# for i in range(len(sorted_product_set)):
		# 	print sorted_product_set[i]["price"]," => ",sorted_product_set[i]["title"]," => ",sorted_product_set[i]["seller"]
		# for p in sorted_product_set:
		# 	print p["price"],'===>',p["seller"]
		context = {'key':key,'amazon_set':amazon_set,'flipkart_set':flipkart_set}
		return render(request, 'search/index.html',context)
		# return HttpResponse(flipkart_r.text,content_type="application/json")
	else:
		return HttpResponse("please enter something")
def product(request):
	return render(request, 'product/index.html')

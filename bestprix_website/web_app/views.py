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
import api_functions as api

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
		amazon_set = api.amazon_callby_keyword(key)
		#flipkart block====================================================================================================>
		print "_____________________________________________________________________________________________________________"
		flipkart_set = api.flipkart_callby_keyword(key)
		product_set = amazon_set + flipkart_set
		# for i in range(len(product_set)):
		# 	print product_set[i]["price"]," => ",product_set[i]["title"]," => ",product_set[i]["seller"]
		sorted_product_set = sorted(product_set, key=lambda k: k['price'],reverse=True)
		# for i in range(len(sorted_product_set)):
		# 	print sorted_product_set[i]["price"]," => ",sorted_product_set[i]["title"]," => ",sorted_product_set[i]["seller"]
		# for p in sorted_product_set:
		# 	print p["price"],'===>',p["seller"]
		context = {'key':key,'product_set':sorted_product_set}
		return render(request, 'search/index.html',context)
		# return HttpResponse(flipkart_r.text,content_type="application/json")
	else:
		return HttpResponse("please enter something")

def product(request):
	if request.method == 'GET':
		p_id = request.GET['p_id']
		seller = request.GET['seller']
		print p_id,seller
	if seller == 'amazon':
		amazon = api.amazon_callby_id(p_id)
		print amazon['title']
		flipkart = api.flipkart_callby_keyword(amazon['title'])
		print flipkart
	return render(request, 'product/index.html')

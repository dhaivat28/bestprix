from django.shortcuts import render,redirect
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
from .models import user_detail,wishes

def index(request):
	return render(request, 'index.html')

def login(request):
	if request.method == 'POST':
		user = user_detail.objects.get(email_id=request.POST['email'])
		call_back = request.GET['next']
		# print call_back
		if user.password == request.POST['password']:
			request.session['member_id'] = user.email_id
			if call_back != "":
				import ast
				args = ast.literal_eval(call_back)
				print ">>",args
				url = args[0].strip()+"?next="+args[0].strip()+"&key="+args[1].strip()+"&p_id="+args[2].strip()+"&seller="+args[3].strip()
				return redirect(url)
			else:
				return redirect('/')
		else:
			return HttpResponse("Your username and password didn't match.")
	else:

		return render(request, 'login/index.html')

def signup(request):
	if request.method == 'POST':
		fname = request.POST['fname']
		email = request.POST['email']
		u_password = request.POST['password']
		sq = request.POST['sq']
		sa = request.POST['sa']
		user = user_detail(email_id=email,name=fname,password=u_password,s_q=sq,s_a=sa)
		user.save()
		request.session['member_id'] = email
		return HttpResponse("succsesfull")
	else:
		return HttpResponse("error")

def search(request):
	key = request.GET['q']
	amazon_set=[]
	flipkart_set=[]
	if key.strip():
		amazon_set = api.amazon_callby_keyword(key)
		#flipkart block====================================================================================================>
		flipkart_set = api.flipkart_callby_keyword(key)
		product_set = amazon_set + flipkart_set
		# for i in range(len(product_set)):
		# 	print product_set[i]["price"]," => ",product_set[i]["title"]," => ",product_set[i]["seller"]
		sorted_product_set = sorted(product_set, key=lambda k: k['title'])
		# for i in range(len(sorted_product_set)):
		# 	print sorted_product_set[i]["price"]," => ",sorted_product_set[i]["title"]," => ",sorted_product_set[i]["seller"]
		print "Final list:\n"
		for p in sorted_product_set:
			print p["price"],'\t====>\t',p["seller"],'\t===>\t',p["title"]
		print "\n"
		context = {'key':key,'product_set':sorted_product_set}
		return render(request, 'search/index.html',context)
		# return HttpResponse(flipkart_r.text,content_type="application/json")
	else:
		return HttpResponse("please enter something")

def product(request):
	if request.method == 'GET':
		p_id = request.GET['p_id']
		seller = request.GET['seller']
		key = request.GET['key']
		print '\n',p_id,seller,'\n'
		product = None
		match = None
		if seller == 'amazon':
			try:
				product = api.amazon_callby_id(p_id)
			except Exception:
				print "Status: Error in amazon API call"
			# print amazon['title']
			try:
				match = api.flipkart_callby_keyword(key)
			except Exception:
				print "Status: Error in flipkart API call"
			match = api.find_match(product,match)
			if match is not None:
				print "match:",match['match_score']
				print "\nproduct  ===> ",product['price'],product['title']
				print "match    ===> ",match['product']['price'],match['product']['title']
		elif seller == 'flipkart':
			try:
				product = api.flipkart_callby_id(p_id)
			except Exception:
				print "Status: Error in flipkart API call"
			# print flipkart['title']
			try:
				match = api.amazon_callby_keyword(key)
			except Exception:
				print "Status: Error in amazon API call"
			match = api.find_match(product,match)
			if match is not None:
				print "match:",match['match_score']
				print "\nproduct  ===> ",product['price'],product['title']
				print "match    ===> ",match['product']['price'],match['product']['title']

		context={'product':product,'match':match,'key':key}
		return render(request, 'product/index.html',context)
		# return HttpResponse('Error no match found')
	else:
		return HttpResponse('Error')

def wishlist(request):
	if request.method == 'GET':
		mp_id = request.GET['p_id']
		mseller = request.GET['seller']
		next_page = request.GET['next']
		key = request.GET['key']
		next_url = []
		next_url.append(next_page)
		next_url.append(key)
		next_url.append(mp_id)
		next_url.append(mseller)
		exist = False

		print '\n',mp_id,mseller,'\n'
		try:
			if request.session['member_id'] is not None:
				email = request.session['member_id']
				print "HERE"
				db = MySQLdb.connect("localhost","root","root","bestprix_db")
				cursor = db.cursor()
				try:
					sql = "SELECT * FROM web_app_wishes WHERE email_id='%s' and p_id='%s'" % (email,mp_id)
					cursor.execute(sql)
					results = cursor.fetchall()
					if len(results) == 0:
						sql = "INSERT INTO web_app_wishes (id,email_id, p_id, seller) VALUES (NULL, '%s', '%s', '%s')" % (email,mp_id,mseller)
						try:
							cursor.execute(sql)
							db.commit()

						except Exception as e:
							print "EROOR 2"
					else:
						return HttpResponse("already exist")
					db.close()
				except Exception:
					print "EROOR 1"

				return render(request,'wishlist/index.html')
		except Exception as e:
			print request.GET['next']
			context={'next':next_url}
			return render(request,'login/index.html',context)
	else:
		return HttpResponse("Error")

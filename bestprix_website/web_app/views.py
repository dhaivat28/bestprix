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
from .models import user_detail

def index(request):
	return render(request, 'index.html')

def login(request):
	if request.method == 'POST':
		user = user_detail.objects.get(email_id=request.POST['email'])
		if user.password == request.POST['password']:
			request.session['member_id'] = user.email_id
			return HttpResponse("logged in.")
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

		context={'product':product,'match':match}
		return render(request, 'product/index.html',context)
		# return HttpResponse('Error no match found')
	else:
		return HttpResponse('Error')

def wishlist(request):
	if request.method == 'GET':
		p_id = request.GET['p_id']
		seller = request.GET['seller']
		print '\n',p_id,seller,'\n'
		try:
			if request.session['member_id'] is not None:
				return render(request,'wishlist/index.html')
		except Exception as e:
			return render(request,'login/index.html')

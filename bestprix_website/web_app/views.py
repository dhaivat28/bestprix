from django.shortcuts import render
from django.http import HttpResponse
import sys, os, base64, datetime, hashlib, hmac
import requests
import urllib

def index(request):
	return render(request, 'index.html')

def search(request):
	access_key = 'AKIAIBV3ZSCMXLX5DY6A'
	secret_key = '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'

	return HttpResponse("hello")

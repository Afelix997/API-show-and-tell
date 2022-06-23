from urllib import response
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import requests as HTTP_Client
from requests_oauthlib import OAuth1
import pprint
import urllib3
import os
import random
pp = pprint.PrettyPrinter(indent=2, depth=1)
import json
from dotenv import load_dotenv


def index(request,image_id=105):
    
   
    http = urllib3.PoolManager()
    print(os.environ['apikey'])
    r = http.request('GET', f'https://api.harvardartmuseums.org/image/{image_id}',
        fields = {'apikey': os.environ['apikey'],})
    a= json.loads(r._body.decode("utf-8").replace("'",'"'))
    data= {"image":a['baseimageurl']}
    return render(request, "pages/index.html",data)


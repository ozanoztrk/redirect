# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 22:47:04 2023

@author: ozan
"""

import IP2Location, os, requests
from flask import Flask, redirect, render_template, request


LINK_TO_TURKISH_PAGE="https://mesc-is.org/exchange-rate/"
LINK_TO_ENGLISH_PAGE="https://mesc-is.org/6718-2/"
DATABASE_PATH='data/IP-COUNTRY-ISP-SAMPLE.BIN'

app = Flask(__name__)
database = IP2Location.IP2Location(DATABASE_PATH)

@app.route('/', methods=['GET'])
def redirect_page():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    
    print(ip)
    try:
        country_short=requests.get('https://api.country.is/'+str(ip)).json()['country']
        print('api.country.is')
    except:
        country_short=database.get_all(ip).country_short
        print('IP2Location')

    print('country:'+str(country_short))
    if country_short == 'TR' :
        ('TR')
        return redirect(LINK_TO_TURKISH_PAGE)
    else :
        return redirect(LINK_TO_ENGLISH_PAGE)

if __name__=="__main__":
    port =os.environ.get("PORT",5000)
    app.run(debug=False,host='0.0.0.0',port=port)
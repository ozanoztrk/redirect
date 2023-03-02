# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 22:47:04 2023

@author: ozan
"""

import IP2Location, os, requests
from flask import Flask, redirect, render_template, request


LINK_TO_TURKISH_PAGE="https://mesc-is.org/yerelkayit/"
LINK_TO_ENGLISH_PAGE="https://mesc-is.org/6718-2/"
DATABASE_PATH='data/IP-COUNTRY-ISP-SAMPLE.BIN'

app = Flask(__name__)
database = IP2Location.IP2Location(DATABASE_PATH)

@app.route('/', methods=['GET'])
def redirect_page():
    if 'X-Forwarded-For' in request.headers:
        proxy_data = request.headers['X-Forwarded-For']
        ip_list = proxy_data.split(',')
        ip = ip_list[0]  # first address in list is User IP
    else:
        ip = request.remote_addr  # For local development
        
    print(ip)
    
    try:
        print('trying to match from api.country.is')
        country_short=requests.get('https://api.country.is/'+str(ip)).json()['country']
        print('ip succesfully matched from api.country.is')
    except:
        print('trying to match from IP2Location')
        country_short=database.get_all(ip).country_short
        print('ip succesfully matched from IP2Location')

    print('country:'+str(country_short))
    if country_short in ['TR',('TR')]:
        return redirect(LINK_TO_TURKISH_PAGE)
    else:
        return redirect(LINK_TO_ENGLISH_PAGE)

if __name__=="__main__":
    port =os.environ.get("PORT",5000)
    app.run(debug=False,host='0.0.0.0',port=port)

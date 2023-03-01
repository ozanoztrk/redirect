# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 22:47:04 2023

@author: ozan
"""

import IP2Location, os
from flask import Flask, redirect, render_template, request

LINK_TO_TURKISH_PAGE="http://www.google.com"
LINK_TO_ENGLISH_PAGE="http://www.yahoo.com"
DATABASE_PATH='data/IP-COUNTRY-ISP-SAMPLE.BIN'

app = Flask(__name__)
database = IP2Location.IP2Location(DATABASE_PATH)
@app.route('/', methods=['GET'])
def main():
    global rec
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    rec = database.get_all(ip)
    print(rec.country_short)
    if rec.country_short == 'TR' :
        return redirect(LINK_TO_TURKISH_PAGE)
    else :
        return redirect(LINK_TO_ENGLISH_PAGE)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    #port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host='0.0.0.0', port=8000)
